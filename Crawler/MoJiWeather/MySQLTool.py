# -*- coding:UTF-8 -*-

# author:wanghc
# datetime:2021/12/20 21:55
# software: PyCharm

"""
文件说明：
    mysql工具类
"""
import pymysql
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s:%(message)s')
mysql_host = 'localhost'
mysql_db = 'crawler'
mysql_user = 'root'
mysql_pwd = '123456'
mysql_table = 'xh_weather_info'


class MySQL:
    def __init__(self):
        # MySQL
        self.MYSQL_HOST = mysql_host
        self.MYSQL_DB = mysql_db
        self.MYSQ_USER = mysql_user
        self.MYSQL_PWD = mysql_pwd
        self.connect = pymysql.connect(
            host=self.MYSQL_HOST,
            db=self.MYSQL_DB,
            port=3306,
            user=self.MYSQ_USER,
            passwd=self.MYSQL_PWD,
            charset='utf8',
            use_unicode=False
        )
        self.cursor = self.connect.cursor()

    def insert_weatherinfo(self, weather_info):
        """
        将天气数据插入mysql
        :param weather_info: 天气数据
        :return:
        """
        sql = "insert into {}(`quality`, `temperature`, `weather`,`humidity`,`wind_direction`,`crawler_time`) VALUES (%s, %s, %s,%s,%s,%s)".format(mysql_table)
        try:
            self.cursor.execute(sql, (weather_info['quality'], weather_info['temperature'], weather_info['weather'], weather_info['humidity'], weather_info['wind_direction'],weather_info['crawler_time']))
            self.connect.commit()
            logging.info('天气数据插入成功')
        except Exception as e:
            logging.error('天气数据插入失败', exc_info=True)
        finally:
            self.cursor.close()
            self.connect.close()
