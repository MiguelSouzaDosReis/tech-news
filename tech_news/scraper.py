import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
        response.raise_for_status()
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    return selector.css("a.cs-overlay-link ::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    nextPage = selector.css("a.next.page-numbers ::attr(href)").get()
    return nextPage
    # while nextPage:
    #     print(selector.css("a.cs-overlay-link ::attr(href)").getall())
    #     return selector.css("a.cs-overlay-link ::attr(href)").getall()


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)
    url = selector.css("link[rel=canonical] ::attr(href)").get()
    title = selector.css("h1.entry-title ::text").get()
    timestamp = selector.css("li.meta-date ::text").get()
    writer = selector.css("a.url.fn.n ::text").get()
    summary = selector.css(
        "div.entry-content > p:nth-of-type(1) *::text"
    ).getall()
    count = 0
    category = selector.css("span.label ::text").get()
    comments_count = selector.css("article.comment-body ::text").get()
    tags = selector.css("a[rel=tag] ::text").getall()
    if tags is None:
        tags = []
    if comments_count:
        count += 1
    return {
        "url": url,
        "title": title.replace("\xa0", ""),
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": count,
        "summary": "".join(summary).replace("\xa0", "").strip(),
        "tags": tags,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
