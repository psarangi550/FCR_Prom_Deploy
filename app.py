
from flask import Flask
from extension import api,db
from resources import ns
# we need to import the APIManager class from flask_restless module 

#creeating the app  within the create_app()
def create_app():
    app=Flask(__name__)
    #setting the configgs for the SqlAlchemy DBs
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    api.init_app(app)
    api.add_namespace(ns)
    db.init_app(app)
    return app


if __name__=="__main__":
    app=create_app()
    app.run()