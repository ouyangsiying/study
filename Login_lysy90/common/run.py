#coding:utf-8

from common import filemethod
from common import networkrequest
from common import ckeckresult
import json

#运行入口
class Run():
    def __init__(self):
        self.fileread = filemethod.FileMetod()
        self.log = networkrequest.NetworkRequest()
        self.check = ckeckresult.CkeckResult()

    def run(self):
        list = self.fileread.readfile()
        for item in list:
            username = item[0]
            password = item[1]
            expected = item[2]
            if isinstance(item[0],float):
                username = int(item[0])
            if isinstance(item[1], float):
                password = int(item[1])
            loginResult = self.log.login(username,password)
            loginResult = json.loads(loginResult)["errno"]
            flag= self.check.ckeckresult(expected,loginResult)
            self.fileread.writefile(username,password,expected,loginResult,flag)
