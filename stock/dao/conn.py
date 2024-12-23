from sqlalchemy import create_engine


# 例如，连接到SQLite数据库
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/stock')
