#coding:utf-8
import xlrd
import xlwt
from xlutils.copy import copy
import os

class FileMetod():
    def __init__(self):
        self.readfilepath = 'E:\Login\\testdata\\testdata.xlsx'
        self.writefilepath = 'E:\Login\\report\\result.xlsx'
#读文件
    def openfile(self,file):
        try:
            data = xlrd.open_workbook(file)
            print(self.readfilepath+"文件成功打开")
            return data
        except Exception as e:
            print(e)
            print("打开文件失败")

#读数据
    def readfile(self,colnameindex = 0,by_index=0):
        open = self.openfile(self.readfilepath)
        rtable = open.sheets()[by_index]   #by_index表的索引
        nrows = rtable.nrows         #行数
        ncols = rtable.ncols         #列数
        list = []
        # colnames = rtable.row_values(colnameindex)   #某行数据
        for rownum in range(0,nrows):

            row = rtable.row_values(rownum)
            if row:
                app = []
                for i in range(0,ncols):
                # for i in range(len(colnames)):
                    app.append(row[i])
                list.append(app)
        return list
#写数据
    def writefile(self,username,password,excepted,result,flag):
        if os.path.exists(self.writefilepath):
            pass
        else:
            workbook = xlwt.Workbook()
            row0 = [u'用户名',u'密码', u'预期结果', u'实际结果', u'测试是否通过']
            wtable1 = workbook.add_sheet(u"测试成功")
            for i in range(0, len(row0)):
                wtable1.write(0, i, row0[i])
            wtable2 = workbook.add_sheet(u"测试失败")
            for i in range(0, len(row0)):
                wtable2.write(0, i, row0[i])
            workbook.save(self.writefilepath)

        openfile = self.openfile(self.writefilepath) # 用wlrd提供的方法读取一个excel文件


        if flag==True:
            rows = openfile.sheets()[0].nrows  # 用wlrd提供的方法获得现在已有的行数
            excel = copy(openfile)  # 用xlutils提供的copy方法将xlrd的对象转化为xlwt的对象
            table = excel.get_sheet(0)
        else:
            rows = openfile.sheets()[1].nrows  # 用wlrd提供的方法获得现在已有的行数
            excel = copy(openfile)  # 用xlutils提供的copy方法将xlrd的对象转化为xlwt的对象
            table = excel.get_sheet(1)
        row = rows
        table.write(row, 0, str(username))  # xlwt对象的写方法，参数分别是行、列、值
        table.write(row, 1, str(password))
        table.write(row, 2, str(excepted))
        table.write(row, 3, str(result))
        table.write(row, 4, str(flag))
        row += 1
        excel.save(self.writefilepath)  # xlwt对象的保存方法，这时便覆盖掉了原来的ex
