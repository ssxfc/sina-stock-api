import logging

from sqlalchemy.orm import sessionmaker

from ..stocks import *
from ..dao.models import TRealStock, TTrans, TStock
from ..dao.conn import engine
from ..utils.excepts import CannotParsedException

logger = logging.getLogger(__name__)


def save_real_stock(code):
    try:
        stock = RealStock(code).parse()
        logger.info(f"saving {stock.data[stock.mode]['name']} k-line data...")
        obj = TRealStock(**stock.data[stock.mode])
        Session = sessionmaker(bind=engine)
        with Session() as session:
            session.add(obj)
            session.commit()
    except CannotParsedException as e:
        logger.error(e)


def save_trans(code):
    stock = Trans(code).parse()
    if len(stock.data[stock.mode]) == 0:
        logger.warning('empty trans were parsed, please check if the stock code exists or not!')
        return
    objs = [TTrans(**tran) for tran in stock.data[stock.mode]]
    Session = sessionmaker(bind=engine)
    with Session() as session:
        session.add_all(objs)
        session.commit()


def save_baseline(stock: TStock):
    r"""保存基线股票信息
    """
    Session = sessionmaker(bind=engine)
    with Session() as session:
        session.add(stock)
        session.commit()
