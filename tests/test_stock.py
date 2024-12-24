import unittest

from stock.stocks import *
from stock.dao.manipulate import save_real_stock, save_trans

class TestStock(unittest.TestCase):
    def test_real_stock(self):
        save_real_stock('sh600250')
        
    def test_div_time(self):
        r"""10:29:59的这个最后一笔交易作为10:30这个分时的最终价格
        """
        s = DivTime('sh600250').parse()
        logging.info(s)

    def test_trans(self):
        r"""10:29:00 ~ 10:29:59 之间的交易作为10:30这个分时的成交明细
        这一分钟的交易量由成交明细累加而来，而非由div_time中的信息得来
        """
        # s = Trans('sh600250').parse()
        # logging.info(s)
        save_trans('sh60250')

    def test_trans_press(self):
        s = Trans('sh600250').parse()
        logging.info(s)

    def test_div_time_press(self):
        for i in range(1000):
            s = DivTime('sh600250').parse()
            logging.info(s)
