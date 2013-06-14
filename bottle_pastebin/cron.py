#-*- coding: utf-8
from database import Text
from utils import dateLimit
import datetime


def delete_expired_pastes():
    """ method to delete expired pastes, return number of deleted """
    deleted = 0
    for text in Text.select():      
        limit = dateLimit(text.date_creation, text.valid.duration)        
        # if limit attempt,remove text
        if(datetime.datetime.now()>limit):
            text.delete_instance()
            deleted+=1
        
    return deleted


if __name__ == '__main__':   
    """ run cron """
    delete_expired_pastes()