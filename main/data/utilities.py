import json
import os
from flask import current_app as app
from main.data.models import db

class DataManager():

    @staticmethod
    def initDB():
        app.logger.info('DB URI: %s',app.config['SQLALCHEMY_DATABASE_URI'])
        app.logger.info('Create DB')
        
        _localfile = os.path.join(os.getcwd(), 'data.sqlite')
        if os.path.exists(_localfile):
            os.remove(_localfile)
        db.create_all()
        db.session.commit()
