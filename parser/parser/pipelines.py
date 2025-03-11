import re
import psycopg
from scrapy import Spider
from parser.items import ArticleItem
from datetime import datetime

class StoringPipeline:

    def __init__(self) -> None:
        self.conn = psycopg.connect("host='db' dbname='postgres' user='postgres' password='postgres' port=5432")
        # self.conn.autocommit = True

    def process_item(self, item: ArticleItem, spider: Spider) -> ArticleItem:

        # TODO: create another class for clarifying data
        dt = datetime.fromisoformat(item['datetime'].replace("Z", "")) if item['datetime'] else None
        views = int(item['views']) if item['views'] else None
        with self.conn.cursor() as cursor:
            query = """
                INSERT INTO views_data (url, title, datetime, views) 
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (item['url'], item['title'], dt, views))
            self.conn.commit()
        return item
