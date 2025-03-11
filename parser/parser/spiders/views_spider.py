from pathlib import Path
from typing import Generator
import scrapy
from scrapy.http.response import Response

from ..items import ArticleItem


class ViewsSpider(scrapy.Spider):
    name: str = "views"
    start_id: int = 663000  
    num_articles: int = 14
    start_urls: list[str] = [f"https://habr.com/ru/articles/{662928 + i}" for i in range(num_articles)]
    
    def parse(self, response: Response) -> Generator[ArticleItem, None, None]:
        yield ArticleItem(
            url=response.url,
            title=response.css("meta[property='og:title']::attr(content)").get(),
            datetime=response.css("meta[property='aiturec:datetime']::attr(content)").get(),
            views=response.css("span.tm-icon-counter__value::attr(title)").get(),
        )
