from flask_restx import Resource, Namespace
from flask import jsonify,request
import time
import datetime
from datetime import datetime, timedelta
from json import dumps
import random

# here the NameSpace will act like the blueprint in flask

ns = Namespace("api")


def generate_instant_metrics():
    data = {
        "payload": {
            "status": "success",
            "data": {
                "resultType": "matrix",
                "result": [
                    {
                        "metric": {
                            "name": "host_box_Databus_status",
                            "device_name": "fcrvirt427e8",
                        },
                        "values": [[x for x in range(0, 10)]],
                    }
                ],
            },
        },
        "_msgid": "b5bcaec7930b8fa2",
        "startTime": (datetime.now()-timedelta(seconds=30)).strftime("%Y:%m:%D %H:%m:%S"),
        "endTime": datetime.now().strftime("%Y:%m:%D %H:%m:%S"),
        "query": "pipeline_pipeline_preprocessor_exec_avg",
        "statusCode": 200,
        "headers": {
            "content-type": "application/json",
            "date": datetime.isoformat(datetime.now()),
            "content-length": "63",
            "connection": "close",
            "x-node-red-request-node": "cf15688a",
        },
        "responseUrl": "http://prometheus:9090/api/v1/query_range?query=pipeline_pipeline_preprocessor_exec_avg{device_name=%22fcrvirt427e8%22}&start=1686031854.809&end=1686031884.809&step=45",
        "redirectList": [],
        "retry": 0,
    }
    return data


@ns.route("/promapi")
class Home(Resource):
    def get(self):
        data = generate_instant_metrics()
        args=request.values
        data["args"]=args
        return jsonify(data)

