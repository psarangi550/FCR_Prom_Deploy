from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

api=Api(version='1.0', title='FCR Prometheus API ',description="Simulates FCR Prometheus API exposing metrics")
db=SQLAlchemy()