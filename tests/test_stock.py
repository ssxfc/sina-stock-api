import unittest

from sqlalchemy.orm import sessionmaker

from stock.stocks import *
from stock.dao.models import TRealStock
from stock.dao.conn import engine

class TestStock(unittest.TestCase):
    def test_real_stock(self):
        s = RealStock('sh600250', 10)
        s.parse()
        logging.info(s.data['real'])
        obj = TRealStock(**s.data['real'])
        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(obj)
        session.commit()
        session.close()
        
    def test_div_time(self):
        s = DivTime('sh600250', 10)
        s.parse()
        logging.info(s)

    def test_trans(self):
        s = Trans('sh600250', 10)
        s.parse()
        logging.info(s)
