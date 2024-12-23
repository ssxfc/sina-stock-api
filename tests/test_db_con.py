import unittest
import mysql.connector


class TestDBCon(unittest.TestCase):
    def test_db_con(self):
        config = {
            'user': 'root',
            'password': '123456',
            'host': 'localhost',
            'database': 'stock'
        }
        cnx = mysql.connector.connect(**config)
        
        # 创建一个游标对象
        cursor = cnx.cursor()
        
        # 执行一个查询
        query = ("SELECT * FROM t_person")
        cursor.execute(query)
        
        # 获取查询结果
        for (column1, column2, column3) in cursor:
            print("{}, {}, {}".format(column1, column2, column3))
        
        # 关闭游标和连接
        cursor.close()
        cnx.close()
