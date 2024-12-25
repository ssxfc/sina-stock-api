import time
import unittest
import logging

from stock.utils.code import preprecess
from stock.stocks import *
from stock.dao.manipulate import save_real_stock, save_trans, save_baseline
from stock.dao.models import TStock

logger = logging.getLogger(__name__)

class TestStock(unittest.TestCase):
    def test_save_real_stock(self):
        s = RealStock('510020').parse()
        logging.info(s)
        
    def test_div_time(self):
        r"""10:29:59的这个最后一笔交易作为10:30这个分时的最终价格
        """
        s = DivTime('510020').parse()
        logging.info(s)

    def test_save_trans(self):
        r"""10:29:00 ~ 10:29:59 之间的交易作为10:30这个分时的成交明细
        这一分钟的交易量由成交明细累加而来，而非由div_time中的信息得来
        """
        save_trans('510020')

    def test_trans_press(self):
        s = Trans('510020').parse()
        logging.info(s)

    def test_div_time_press(self):
        s = DivTime('510020').parse()
        logging.info(s)

    def test_add_baseline_stock(self):
        f = r"D:\py\engineering\sina-stock-api\resources\stock.txt"
        stock_list = []
        with open(f, 'r') as ff:
            stocks = ff.readlines()
            for i in stocks:
                try:
                    stock = i.replace("\n", "").replace("\r", "")
                    stock = RealStock(preprecess(stock)).parse()
                    x = {"name": stock.data[stock.mode]['name'],
                        "code": i.replace("\n", "").replace("\r", "")}
                    s = TStock(**x)
                    save_baseline(s)
                    time.sleep(0.5)
                    logger.info(i)
                    stock_list.append(i)
                except:
                    logger.error(f"存储失败：{i}")
        with open(r'D:\py\engineering\sina-stock-api\resources\new_stock.txt','w') as fff:
            for xx in stock_list:
                fff.write(xx)
