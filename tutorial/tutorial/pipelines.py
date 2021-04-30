# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter


# def dbHandle():
#     conn = pymysql.connect(
#         host="localhost",
#         user="root",
#         passwd="root",
#         charset="utf8",
#         use_unicode=False
#     )
#     return conn


class TutorialPipeline:
    def process_item(self, item, spider):
        print(111111111111)
        return item


class WallPaperPipeline:
    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost",
            user="root",
            passwd="root",
            charset="utf8",
            use_unicode=False
        )
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        self.cursor.execute("USE blog")
        text = item['text'].replace("′", "")
        print(text)
        # 插入数据库
        sql = """INSERT INTO quotes_to_scrape(author,text,tag) VALUES(%s,%s,%s)"""
        self.cursor.execute(sql,
                            (item['author'], text, ','.join(item['tag']))
                            )
        self.cursor.connection.commit()

        return item

    def close_spider(self, spider):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()
