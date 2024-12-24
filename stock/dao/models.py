# 导入必要的模块
from sqlalchemy import Column, Integer, \
    String, Boolean, Float, \
    Date, Time
from sqlalchemy.orm import declarative_base

from .conn import engine
 
# 创建一个基类，用于定义数据模型的基本结构
Base = declarative_base()


class TStock(Base):
    # 定义表名
    __tablename__ = 't_stock'
 
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    code = Column(String(100))
    is_good = Column(Boolean)


class TRealStock(Base):
    __tablename__ = 't_real_stock'
    
    id = Column(Integer, primary_key=True)
    ref_id = Column(Integer)

    name = Column(String(100))
    open = Column(Float)
    prevclose = Column(Float)
    now = Column(Float)
    high = Column(Float)
    low = Column(Float)
    buy = Column(Float)
    sell = Column(Float)
    volume = Column(Integer)
    turnover = Column(Float)
    bid1_volume = Column(Integer)
    bid1 = Column(Float)
    bid2_volume = Column(Integer)
    bid2 = Column(Float)
    bid3_volume = Column(Integer)
    bid3 = Column(Float)
    bid4_volume = Column(Integer)
    bid4 = Column(Float)
    bid5_volume = Column(Integer)
    bid5 = Column(Float)
    ask1_volume = Column(Integer)
    ask1 = Column(Float)
    ask2_volume = Column(Integer)
    ask2 = Column(Float)
    ask3_volume = Column(Integer)
    ask3 = Column(Float)
    ask4_volume = Column(Integer)
    ask4 = Column(Float)
    ask5_volume = Column(Integer)
    ask5 = Column(Float)
    date = Column(Date)
    time = Column(Time)

    
class TTrans(Base):
    __tablename__ = 't_trans'
    
    id = Column(Integer, primary_key=True)
    ref_id = Column(Integer)

    volume = Column(Integer)
    price = Column(Float)
    # 当前批次的交易类型，True:买盘；False:卖盘
    buy = Column(Boolean)
    date = Column(Time)


Base.metadata.create_all(engine)
