# -*- coding: utf-8 -*-

from bottle import route, run, static_file, view, error, post, request
import yaml
from database import Valid, Text
from utils import encryptAES256, decryptAES256, encryptSHA256, dateLimit
import datetime

CONFIG = yaml.load(open('config.yaml','r'))

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=CONFIG['static_path'])

@error(404)
def error404(error):
    return 'Nothing here, sorry'

@route('/')
@route('/create')
@view('text_form')
def text_form():
    valids = {}
    for valid in Valid.select():
        valids[str(valid.id)] = valid.description
        
    return dict(valids=valids)

@post('/create')
def text_form_post():
    valid = request.forms.get('inputValid').encode('iso-8859-1').decode('utf-8')
    text = request.forms.get('inputText').encode('iso-8859-1').decode('utf-8')

    if valid and text:
        try:
            # encrypt text
            encrypted = encryptAES256(text)
            code = encrypted['key']+'+'+encrypted['iv']
            code_sha256 = encryptSHA256(code)
            # add to database
            get_valid = Valid.get(Valid.id == valid)
            created_text = Text(text=encrypted['text'], code=code_sha256,valid=get_valid)    
            created_text.save()
            #return url
            return {'Your link': '%s/get/%s' % (CONFIG['server_url'],code),}
        except:
            return {'error':'An error occured ...',}
    else:
        return {'error':'An error occured ...',}
    
    
@route('/get/<code>')
@view('get_text')
def get_text(code):
    try:
        # encrypt code
        code_sha256 = encryptSHA256(code)
        # get Text
        text = Text.get( Text.code == code_sha256)
        # decode text
        key = code[:code.find('+')]
        iv = code[code.find('+')+1:]
        text_decrypted = decryptAES256(text.text,key,iv)
        #date limit      
        date_limit = dateLimit(text.date_creation,text.valid.duration) 
        date_limit_str = datetime.datetime.strftime(date_limit, "%Y-%m-%d %Hh:%Mm:%Ss")
    
        #show template
        return dict(text_decrypted=text_decrypted,date_limit=date_limit_str)
    except:
        return 'Nothing here, sorry'
    
    
@route('/about')
@view('about')
def about():
    return dict()        

run(host='localhost', port=8080, debug=True)
