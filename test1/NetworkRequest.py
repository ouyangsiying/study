# coding:utf-8
import requests
import json
import hashlib

class NetworkRequest():
    def __init__(self):
        self.baseUrl = 'http://vip.lysy90store.xyz/'
        self.requests = requests.Session()
        self.laravel_session = ''
        self.cookies = {}
        self.headers = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}
        self.token = ''

    def getNowToken(self):
        return self.token

    def gettoken(self):
        req = self.get("/api/token")
        token = json.loads(req.content)["result"]["_token"]
        self.laravel_session = req.cookies['laravel_session']
        self.cookies = {'laravel_session': self.laravel_session}
        return token

    def get(self,url,params={}):
        req = requests.get(self.baseUrl+url,params=params,headers = self.headers,cookies = self.cookies)
        return req

    def post(self,url,params={}):
        req = requests.post(self.baseUrl+url,params=params,headers = self.headers,cookies = self.cookies)
        return req

    def post2(self, url, params={},m=""):
        headers = {'Accept': 'application/json', 'Content-Type': m}
        req = requests.post(self.baseUrl + url, data=params, headers=headers, cookies=self.cookies)
        return req

    def delete(self,url,params={}):
        req = requests.delete(self.baseUrl+url,params=params,headers = self.headers,cookies = self.cookies)
        return req

    def put(self,url,params={}):
        req = requests.put(self.baseUrl+url,params=params,headers = self.headers,cookies = self.cookies)
        return req

#登录
    def login(self,username,password):
        token = self.gettoken()
        
        self.token = token
        username = str(username)
        password = str(password)
        param = {}
        param["_token"] = token
        param["user_name"] = username
        pasw = password.encode('utf-8')                                 #在python3中必须先转码再加密
        hashPwd = hashlib.sha1(pasw).hexdigest()
        past = (hashPwd+self.gettoken()).encode('utf-8')
        haspassword = hashlib.sha1(past).hexdigest()
        param["password"] = str(haspassword)
        req = self.post("/auth/login",param)
        print("用户名",username,"密码：",password,"登录结果：",req.content)
        return req.content

#退出
    def logout(self):
        self.post("/auth/logout", {})

