from flask_restx import Resource,Namespace
import time
from datetime import datetime,date
from json import dumps
# here the NameSpace will act like the blueprint in flask 

ns=Namespace("api")


data={
	"payload": {
		"status": "success",
		"data": {
			"resultType": "matrix",
			"result": []
		}
	},
	"_msgid": "b5bcaec7930b8fa2",
	"startTime": time.strftime("%Y:%m:%D %H:%m:%S",time.localtime(time.time()-30)),
	"endTime": time.strftime("%Y:%m:%D %H:%m:%S",time.localtime(time.time())),
	"query": "pipeline_pipeline_preprocessor_exec_avg",
	"statusCode": 200,
	"headers": {
		"content-type": "application/json",
		"date": datetime.isoformat(datetime.now()),
		"content-length": "63",
		"connection": "close",
		"x-node-red-request-node": "cf15688a"
	},
	"responseUrl": "http://prometheus:9090/api/v1/query_range?query=pipeline_pipeline_preprocessor_exec_avg{device_name=%22fcrvirt427e8%22}&start=1686031854.809&end=1686031884.809&step=45",
	"redirectList": [],
	"retry": 0
}

@ns.route("/promapi")
class Home(Resource):
    
    def get(self):
        return {"data":data}