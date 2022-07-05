from flask import Flask,jsonify,request,make_response,send_file
from flask_cors import CORS
import json
import os
app=Flask(__name__)
CORS(app)

@app.route("/",methods=['GET'])
def helloWorld():
    return jsonify( {"data":"helloworld"})

@app.route("/download4",methods=['GET'])
def download4():
    return send_file(r'prog4.c')

@app.route("/download7",methods=['GET'])
def download7():
    return send_file(r'prog7.c')

@app.route("/download8",methods=['GET'])
def download8():
    return send_file(r'prog8.c')

@app.route("/download9",methods=['GET'])
def download9():
    return send_file(r'prog9.c')

@app.route("/download",methods=['GET'])
def download():
    return send_file(r'txt.t')

@app.route('/list',methods=['GET'])
def passport():
    dirlist=os.listdir('./models')
    modelsList=[]
    for x in dirlist:
        if x.endswith('.json'):
            modelsList.append(x.split('.')[0])
    return {"models":modelsList}

@app.route('/learning',methods=['POST'])
def learning():
    try:
        req=request.get_json()
        json_object = json.dumps(req, indent = 4)
        with open("./models/"+req["theater"]+".json", "w") as outfile:
            outfile.write(json_object)
        print(req)
        return { 'msg':"success"} 
    except :
        return {'err':"error occured"}

@app.route('/detection',methods=['POST'])
def detection():
    try:
        req=request.get_json()
        print(req['data'])
        tickets=req["data"].split('\n')
        print(tickets)
        # print(tickets)
        extraction=[]
        modelFile=open("./models/"+req["model"]+".json",'r')
        modelData=json.load(modelFile)
        model=modelData["model"]
        lineCount=len(model)
        k=0
        data={}
        while( k < len(tickets)):
            data={}
            for line in model:

                for attr in line:
                    i=attr['start']-1
                    j=attr['end']
                    data[attr['name']]=tickets[k][i:j].strip()
                k+=1
            extraction.append(data)
        return {"msg":"success","data":extraction}
    except :
        return {'err':"error occured"}

if(__name__=="__main__"):
    app.run(port="5050")