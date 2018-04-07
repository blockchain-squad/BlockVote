import flask
from flask import request,Flask
import requests

app=Flask(__name__)

ip_list=[]

@app.route('/register',methods=['GET'])
def register():
    #注册接口，将发送请求的矿机ip保存至listip_,并将这个ip广播至所有矿机
    pass

@app.route('/get_ip_list',methods=['GET'])
def get_ip_list():
    #获得IP列表接口函数，将ip列表打包进response
    pass

