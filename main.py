import sys
import schedule
from datetime import datetime
from jd_spider_requests import JdSeckill
from multiprocessing import Process

def job():
    dt = datetime.now().strftime("%Y-%m-%d") + " 09:59:59.500"
    jdSeckill = JdSeckill(buy_time = dt)
    jdSeckill.seckill_by_proc_pool()

if __name__ == '__main__':
    a = """

       oooo oooooooooo.            .oooooooo.                     oooo         o8o  oooo  oooo  
       `888 `888'   `Y8b          d8P'    `Y8                     `888         `"'  `888  `888  
        888  888      888         Y88bo.       .ooooo.   .ooooo.   888  oooo  oooo   888   888  
        888  888      888          `"Y8888o.  d88' `88b d88' `"Y8  888 .8P'   `888   888   888  
        888  888      888 8888888      `"Y88b 888ooo888 888        888888.     888   888   888  
        888  888     d88'         oo     .d8P 888    .o 888   .o8  888 `88b.   888   888   888  
    .o. 88P o888bood8P'           8""88888P'  `Y8bod8P' `Y8bod8P' o888o o888o o888o o888o o888o 
    `Y888P                                                                                                                                                  
                                               
    """
    print(a)

    schedule.every().day.at("11:59:30").do(job)

    while True:
        schedule.run_pending()