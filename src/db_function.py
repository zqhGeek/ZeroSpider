import pymysql


class DB():
    def __init__(self, host='localhost', port=3306, db='', user='root', password='123456', charset='utf8mb4'):
        # 建立连接
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password, charset=charset)
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        self.cur.execute('SHOW DATABASES')
        creat = True
        for database in self.cur:
            if str(database['Database']) == db:
                creat = False
        if creat:
            self.cur.execute('CREATE DATABASE ' + db)
        self.conn = pymysql.connect(host=host, port=port, db=db, user=user, password=password, charset=charset)
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        # 创建游标，操作设置为字典类型

    def __enter__(self):
        # 返回游标
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print("数据库错误")
            self.conn.rollback()
        # 提交数据库并执行
        print('提交数据库并执行')
        self.conn.commit()
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()
