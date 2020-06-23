import requests
import random
import time
import json
import math
from flask import Flask,render_template
class data:
    url='https://leetcode.com/api/problems/algorithms/'
    def __init__(self):
        req=requests.get(self.url)
        result=req.json()
        self.objects=[]
        for x in result['stat_status_pairs']:
            self.objects.append(questionObject(x))
    
    def generateRequest(self):
        random.seed(int(time.time()))
        returnObject=[]
        for i in range(5):
            v=math.floor(random.random()*len(self.objects))
            returnObject.append(self.objects[v])
        return returnObject

class questionObject:
    link=""
    title=""
    difficulty=""
    questionId=""
    def __init__(self,obj):
        self.link="https://leetcode.com/problems/"+str(obj['stat']['question__title_slug'])
        self.title=str(obj['stat']['question__title'])
        self.difficulty=obj['difficulty']['level']
        self.questionId=obj['stat']['frontend_question_id']
        self.paidOnly=obj['paid_only']
    def printObject(self):
        print(self.title)
        print(self.link)
        print(str(self.questionId)+"   " +str(self.difficulty))
        print(self.paidOnly)        

app = Flask(__name__)
mainObject=data()
@app.route('/')
def runService():
    returnObject=mainObject.generateRequest()
    return render_template('index.html',result=returnObject)
    
@app.route('/update',methods=["POST"])
def updateQuestions():
    return runService()

