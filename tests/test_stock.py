import unittest

import schedule

from stock.stocks import *

class TestStock(unittest.TestCase):
    def test_real_stock(self):
        s = RealStock('sh600250', 10)
        s.parse()
        logging.info(s)
        
    def test_div_time(self):
        s = DivTime('sh600250', 10)
        s.parse()
        logging.info(s)

    def test_trans(self):
        s = Trans('sh600250', 10)
        s.parse()
        logging.info(s)
