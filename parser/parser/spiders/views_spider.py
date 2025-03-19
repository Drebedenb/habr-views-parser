from typing import Generator
import scrapy
from scrapy.http.response import Response

from ..items import ArticleItem

class ViewsSpider(scrapy.Spider):
    name: str = "views"
    num_articles: int = 1000
    start_urls: list[str] = [f"https://habr.com/ru/articles/{890000 + i}" for i in range(num_articles)]
    
    def parse(self, response: Response) -> Generator[ArticleItem, None, None]:
        yield ArticleItem(
            url=response.url,
            title=response.css("meta[property='og:title']::attr(content)").get(),
            datetime=response.css("meta[property='aiturec:datetime']::attr(content)").get(),
            views=response.css("span.tm-icon-counter__value::attr(title)").get(),
        )
