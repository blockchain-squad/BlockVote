import flask
from flask import request,Flask
import requests
import rsa as rsa
import uuid as uuid
import time as time
import hashlib as hasher
from Client import user,vote

app=Flask(__name__)

DIFFICULTY=6
vote_buffer=[]#选票缓冲区
ip_list=[]#在线矿机列表


class block(object):
    def __init__(self,index:int,pre_block_hash:str):
        self.data=[]
        self.index=index
        self.id=uuid.uuid4()
        self.time_stamp=time.ctime(time.time())
        self.nonce=0
        self.__hasher=hasher.sha256()
        self.pre_block_hash=pre_block_hash
        self.__hasher.update((str(self.time_stamp)+str(self.index)+str(self.pre_block_hash)).encode('utf-8'))
        self.hash=self.__hasher.hexdigest()

class chain(object):
    def __init__(self):
        self.data=[]
        self.size=0

def verify_vote(new_vote:vote):
    #选票验证函数，验证签名
    pass

def verify_block(new_block:block):
    #区块验证函数：验证PoW以及每一张选票的签名

    pass

def verify_chain(new_chain:chain):
    #链验证函数：1、创世区块是否相同。2、区块是否首尾相连。3、每个区块是否合法
    pass

@app.route('/broadcast/vote',methods=['POST'])
def vote_broadcast_listener(new_vote:vote):
    #交易监听函数

    # 收听广播，接收待验证的选票：

    # if 验证通过：

    # else：

    # return

    pass

@app.route('/broadcast/block',methods=['POST'])
def block_broadcast_listener(new_block:block):
    #区块监听函数

    #收听广播，接收待验证的区块：


    #调用区块验证函数：


    #if 验证通过：


    #else：


    #return

    pass

def mining():
    #挖矿函数
    #循环挖矿，如果符合PoW要求跳出循环

    #广播这个区块

    #添加一个空白块
    pass

def agreement_sender(target_address):
    # 共识函数，如果收到的区块index远大于当前链的长度，则调用该函数，向target矿机发送共识请求

    # 向target发送共识请求

    # 接收target的response，并从response中提取链的信息

    # 验证新链是否合法

    # if合法，用新链替代自己的链

    # else拒绝

    pass

@app.route('/agreement',methods=['GET'])
def agreement_listener():
    #监听共识请求，将本机区块链打包进response
    pass

@app.route('/broadcast/ip',methods=['POST'])
def register_broadcast_listener(new_ip):
    #上线矿机ip监听函数，收到Server的POST请求之后将POST中的新上线矿机ip保存至ip_list
    pass

def register():
    #将本机在Server上进行注册
    pass

if __name__=='__main__':
    #main
    pass