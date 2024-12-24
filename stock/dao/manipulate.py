from sqlalchemy.orm import sessionmaker

from ..stocks import *
from ..dao.models import TRealStock, TTrans
from ..dao.conn import engine

def save_real_stock(code):
    stock = RealStock(code).parse()
    logging.info(stock.data[stock.mode])
    obj = TRealStock(**stock.data[stock.mode])
    Session = sessionmaker(bind=engine)
    with Session() as session:
        session.add(obj)
        session.commit()


def save_trans(code):
    stock = Trans(code).parse()
    logging.info(stock.data[stock.mode])
    objs = [TTrans(**tran) for tran in stock.data[stock.mode]]
    Session = sessionmaker(bind=engine)
    with Session() as session:
        session.add_all(objs)
        session.commit()
