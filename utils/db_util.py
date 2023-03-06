import pymysql

from apitestframework import setting
from apitestframework.utils.file_load import load_yaml_file


class DB:

    def __init__(self,project_name):
        self.dbinfo = load_yaml_file(setting.DIR_NAME + '/configs/db.yml').get(project_name)
        self.connection = pymysql.connect(
            host=self.dbinfo['host'],
            port=self.dbinfo['port'],
            user=self.dbinfo['user'],
            password=self.dbinfo['password'],
            db='',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)


    def select(self,sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()  #得到所有的查询结果
        cursor.close()
        return data

    def update(self,sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.connection.commit() #提交
        cursor.close()

    def close(self):
        self.connection.close()

if __name__ == '__main__':
    db = DB('mxtshop')
    print(db.select("select uname,nickname from mtxshop_member.es_member where uname='shamo';"))
