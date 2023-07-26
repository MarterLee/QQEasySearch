import sqlite3
import os
import csv
import pandas as pd

class DataLoader:
    def __int__(self):
        self.path = os.getcwd()
        self.connection = sqlite3.connect(self.path + '\db.db') # 建立并链接数据库
        self.cmd_ptr = self.connection.cursor() #命令指针
        self.data_port = None
    def initDataBase(self,tabel_name,tabel_keys):
        self.tabel_name = tabel_name
        tabel_sql = 'create table if not exists '+tabel_name+' ('+ ','.join(tabel_keys)+')' #拼接sql
        self.cmd_ptr.execute(tabel_sql) # 创建表
        self.connection.commit() # 提交表
    def loadData(self,file,method="pandas"):
        self.load_method = method
        with open(file,"r") as csvfile:
            if method=="sqlite":
                csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的文件
                header = next(csv_reader)        # 读取第一行每一列的标题
                for i,row in enumerate(csv_reader): #按行读取数据。
                    data = self.transData(row)
                    # 写入数据 index,merchant_id,item_name,category_name,sub_category_name,embedding_vector
                    self.cmd_ptr.execute('insert into ' + self.tabel_name + ' values(?,?,?,?,?,?)', (i, *data))
                    # 写入数据 index,merchant_id,item_name,category_name,sub_category_name,embedding_vector
                    self.connection.commit()
                    self.data_port=(self.cmd_ptr,self.connection)
            elif method== "pandas":
                pd_data = pd.read_csv(r'C:\Users\lenovo\Desktop\parttest.csv', sep=',', header='infer')
                row_num,col_num = pd_data.shape
                pd_data.insert(col_num, 'embedding_vector', None)
                pd_data.insert(0, 'index', 0)
                for i in range(row_num):
                    embedding_vector = self.data2Vec(pd_data[i][2])
                    pd_data[i][0]=i+1
                    pd_data[i][col_num+1] = embedding_vector
                self.data_port = pd_data
    # 对召回数据进行准备，转换为可以写入数据库的格式
    def transData(self,row):
        pass
    # 将item_name 通过 text2vec 工具进行生成embedding_vector
    def data2Vec(self,text):
        pass
    def search(self):
        pass