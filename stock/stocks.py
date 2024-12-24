import re
import logging

from .base_stock import Stock

logging.basicConfig(level = logging.INFO, format='%(asctime)s - %(levelname)s - %(module)s - %(message)s')


class RealStock(Stock):
    """
    TODO: 可通过配置文件方式对这种硬编码进行优化.
    """
    def __init__(self, symbol):
        super(RealStock, self).__init__(symbol, num=1)
        self.mode = 'real'

    def parse_resp(self, resp):
        stock_dict = {}
        # 字符串截取
        resp = resp[resp.index("\"") + 1: len(resp) - 1]
        if resp.endswith(","):
            resp = resp[:-1]
        stock = resp.split(",")
        stock_dict["name"] = stock[0]
        stock_dict["open"] = stock[1]
        stock_dict["prevclose"] = stock[2]
        stock_dict["now"] = stock[3]
        stock_dict["high"] = stock[4]
        stock_dict["low"] = stock[5]
        stock_dict["buy"] = stock[6]
        stock_dict["sell"] = stock[7]
        stock_dict["volume"] = stock[8]
        stock_dict["turnover"] = stock[9]
        stock_dict["bid1_volume"] = stock[10]
        stock_dict["bid1"] = stock[11]
        stock_dict["bid2_volume"] = stock[12]
        stock_dict["bid2"] = stock[13]
        stock_dict["bid3_volume"] = stock[14]
        stock_dict["bid3"] = stock[15]
        stock_dict["bid4_volume"] = stock[16]
        stock_dict["bid4"] = stock[17]
        stock_dict["bid5_volume"] = stock[18]
        stock_dict["bid5"] = stock[19]
        stock_dict["ask1_volume"] = stock[20]
        stock_dict["ask1"] = stock[21]
        stock_dict["ask2_volume"] = stock[22]
        stock_dict["ask2"] = stock[23]
        stock_dict["ask3_volume"] = stock[24]
        stock_dict["ask3"] = stock[25]
        stock_dict["ask4_volume"] = stock[26]
        stock_dict["ask4"] = stock[27]
        stock_dict["ask5_volume"] = stock[28]
        stock_dict["ask5"] = stock[29]
        stock_dict["date"] = stock[30]
        stock_dict["time"] = stock[31]

        self.data = {
            'real': stock_dict
        }


class DivTime(Stock):
    def __init__(self, symbol, num=20):
        super(DivTime, self).__init__(symbol, num)
        self.mode = 'time'

    def parse_resp(self, resp):
        pattern = re.compile("\[.+\]", )
        time_divided = re.search(pattern, resp)
        time_divided = list(eval(time_divided.group(0)))

        self.data = {
            'time': time_divided
        }


class Trans(Stock):
    def __init__(self, symbol, num=20):
        super(Trans, self).__init__(symbol, num)
        self.mode = 'trans'
        self.nav = ['date', 'volume', 'price', 'buy']

    def parse_resp(self, resp):
        pattern = re.compile("\(.+\)")
        trans = re.findall(pattern, resp)
        trans = [tuple(eval(item)) for item in trans]
        trans = [{self.nav[i]: item[i] for i in range(len(item))} for item in trans]
        self.data = {
            self.mode: trans
        }
    
    def post_process(self):
        r"""将每笔交易内容都加上ref_id,也就是其所属的股票id信息
        """
        for tran in self.data[self.mode]:
            tran['ref_id'] = 1
            tran['buy'] = True if tran['buy'] == 'UP' else False
