import flask
from flask import request
import requests
import rsa as rsa
import uuid as uuid

class user(object):
    def __init__(self,name):
        self.name=name
        (self.SK, self.PK) = rsa.newkeys(512)
        self.ID=uuid.uuid4()

class vote(object):
    def __init__(self, voter:user, candidate:int):
        self.voter=voter
        self.candidate=candidate
        self.ID=uuid.uuid4()
        self.signature=rsa.encrypt(str(self.ID).encode('utf-8'), voter.SK)

def submit_vote(new_vote:vote):
    #提交选票
    pass

