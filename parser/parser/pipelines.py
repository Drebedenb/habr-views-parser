import re
import psycopg
from scrapy import Spider
from parser.items import ArticleItem
from datetime import datetime


class StoringPipeline:

    def open_spider(self, spider) -> None:
        self.conn = psycopg.connect("host='postgres-app' dbname='postgres' user='postgres' password='postgres' port=5432")
        self.buffer = []  # Temporary storage for batch insert
        self.batch_size = 100  # Insert after collecting this many items
        # self.conn.autocommit = True

    def process_item(self, item: ArticleItem, spider: Spider) -> ArticleItem:
        # TODO: create another class for clarifying data
        dt = datetime.fromisoformat(item['datetime'].replace("Z", "")) if item['datetime'] else None
        views = int(item['views']) if item['views'] else None

        self.buffer.append((item['url'], item['title'], dt, views))

        # If buffer reaches batch size, perform bulk insert
        if len(self.buffer) >= self.batch_size:
            self.flush()
        
        return item
    
    def flush(self):
        """Insert buffered data into the database in bulk."""
        if self.buffer:
            with self.conn.cursor() as cursor:
                query = """
                    INSERT INTO views_data (url, title, datetime, views) 
                    VALUES (%s, %s, %s, %s)
                """
                cursor.executemany(query, self.buffer)
                self.conn.commit()
            self.buffer.clear()

    def close_spider(self, spider: Spider):
        """Ensure remaining items are inserted when spider finishes."""
        self.flush()
        self.conn.close()
