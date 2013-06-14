# -*- coding : utf-8 -*-
import peewee
import yaml
import datetime

CONFIG = yaml.load(open('config.yaml','r'))
DATABASE_CONNECTION = peewee.PostgresqlDatabase(
                                database=CONFIG['db_name'], 
                                user=CONFIG['db_user'],
                                password=CONFIG['db_password'], 
                                host=CONFIG['db_host'],
                                port=CONFIG['db_port']
                    )

DATABASE_CONNECTION.get_conn().set_client_encoding('UTF8')

class BaseModel(peewee.Model):
    """ Base model """
    class Meta:
        database = DATABASE_CONNECTION

class Valid(BaseModel):
    """ Valid model """
    description = peewee.CharField(max_length=256,null=False)
    duration = peewee.BigIntegerField() #in milliseconds
    
class Text(BaseModel):
    """ Text model """
    text = peewee.CharField(max_length=256, null=False)
    code = peewee.CharField(max_length=256,null=False, unique=True)
    date_creation = peewee.DateTimeField(default=datetime.datetime.now, null=False)
    valid = peewee.ForeignKeyField(Valid, related_name='texts', null=False)


if __name__ == '__main__':    
    # Create tables    
    for model in (Valid,Text):
        try:
            model.create_table()
            
            if model is Valid:
                oneday = Valid(description="One day", duration=86400000)
                oneweek = Valid(description="One week", duration=604800000)
                onemonth = Valid(description="One month", duration=2628000000)
                oneday.save()
                oneweek.save()
                onemonth.save()
        except Exception as e:
            print("Error during the database creation")
            print(e)