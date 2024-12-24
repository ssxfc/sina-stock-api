from apscheduler.schedulers.background import BlockingScheduler

from apscheduler.executors.pool import ThreadPoolExecutor

from .dao.conn import engine
from .stocks import *
from .dao.models import TRealStock


def task():
    executor = ThreadPoolExecutor(20) # 最多20个线程同时执行
    # 创建定时任务的调度器对象
    scheduler = BlockingScheduler(executors={'default': executor})
    # 定义定时任务
    def job(param1, param2):
        print(param1)
        print(param2)
        print('Hello, world')

    # 向调度器中添加定时任务
    scheduler.add_job(job, 'interval', seconds=5, args=['Hello', 'world'])
    # 启动定时任务调度器工作
    # BlockingScheduler:发生阻塞
    scheduler.start()


if __name__ == '__main__':
    # 执行task
    task()
