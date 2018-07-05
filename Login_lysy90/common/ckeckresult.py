#coding:utf-8

class CkeckResult():
    def __init__(self):
        pass
    def ckeckresult(self,expected,result):
        flag = None
        if expected == result:
           flag = True
           print("测试登录成功")
           return flag
        else:
            flag = False
            print("测试登录失败")
            return flag
