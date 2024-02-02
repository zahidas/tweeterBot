#coding:utf-8

# import library
import numpy as np, re, datetime, os, sys, glob
from datetime import datetime as dt
import twitter

# class
class TwitterUtil:
    # Variable initial settings
    def __init__(self, id=None, text="", post_time="00:00:00", pos_tim_rad=False, t_range=0):
        # Variable initial settings
        self.api_key, self.api_secret = "api_key", "api_secret_key"
        self.token, self.token_secret = "access_token", "access_token_secret"
        self.api=twitter.Api(consumer_key=self.api_key, consumer_secret=self.api_secret, \
                                access_token_key=self.token, access_token_secret=self.token_secret)
        # Argument setting
        self.id = id
        self.text = text
        self.post_time = dt.strptime(post_time, '%H:%M:%S')
        self.post_time_random = pos_tim_rad
        self.time_range = t_range
        # Read-set API & token
        self.read_key_token()
        self.set_key_token()
    
    # Read API key and access token
    def read_key_token(self):
        # API_Key
        f = open('./config/API_Key', 'r')
        datalist = f.readlines()
        f.close()
        self.api_key = datalist[0].split()[1]
        self.api_secret = datalist[1].split()[1]
        # Access_Token
        f = open('./config/Access_Token', 'r')
        datalist = f.readlines()
        f.close()
        self.token = datalist[0].split()[1]
        self.token_secret = datalist[1].split()[1]
    
    # Set API key and access token
    def set_key_token(self):
        self.api=twitter.Api(consumer_key=self.api_key, consumer_secret=self.api_secret, \
                                access_token_key=self.token, access_token_secret=self.token_secret)
    
    # Post a message to twitter
    def post(self):
        self.api.PostUpdate(self.text)
        print("post: "+self.text)