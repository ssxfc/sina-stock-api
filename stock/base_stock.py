import time
import json
import logging

import requests
from abc import abstractmethod

from . import constants
from .utils.code import preprecess

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.ERROR)


class Stock:
    r"""新浪股票数据接口.
    """
    def __init__(self, symbol, num):
        preprocessed_symbol = preprecess(symbol)
        self.urls = {
            'real': f"https://hq.sinajs.cn/rn={int(time.time() * 1000)}&list={preprocessed_symbol}",
            'time': f"https://vip.stock.finance.sina.com.cn/quotes_service/view/vML_DataList.php? \
                asc=j&symbol={preprocessed_symbol}&num={num}", 
            'trans': f"https://vip.stock.finance.sina.com.cn/quotes_service/view/CN_TransListV2.php? \
                symbol={preprocessed_symbol}&num={num}"
        }
        self.mode = None
        self.code = preprocessed_symbol

    def _get_headers(self):
        return {
            "Accept-Encoding": "gzip, deflate, sdch",
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/54.0.2840.100 \
                Safari/537.36"
            ),
            'Referer': 'http://finance.sina.com.cn/'
        }
    
    def _determine_url(self):
        assert self.mode in self.urls, f'class:Stock子类的mode属性只能属于real,time,trans三者之一'
        return self.urls[self.mode]

    def request(self):
        proxy = {"http": None, "https": None}
        try:
            resp = requests.session().get(self._determine_url(), headers=self._get_headers(), proxies=proxy)
            return resp.text
        except Exception as e:
            logger.error(f'{constants.NET_REQUEST_ERROR}: {e}')

    def parse(self):
        resp = self.request()
        self.parse_resp(resp)
        self.post_process()
        return self

    @abstractmethod
    def parse_resp(self, resp):
        pass
        # raise NotImplementedError("parse_resp() method not implemented for class:Stock")

    @abstractmethod
    def post_process(self):
        r"""后置处理方法，具体由子类来实现
        """
        pass

    def __str__(self):
        return json.dumps(self.data, indent=2)
