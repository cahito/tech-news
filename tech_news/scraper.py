from parsel import Selector
import requests
import time


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
            url,
            headers={"user-agent": "Fake user-agent"},
            timeout=3,
        )
        time.sleep(1)
        if response.status_code != 200:
            raise Exception()
    except Exception:
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    news_urls = selector.css(
        ".entry-title a[rel*=bookmark]::attr(href)"
    ).getall()
    return news_urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    try:
        next_page_link = selector.css("div.nav-links a.next::attr(href)").get()
        if type(next_page_link) != str:
            raise Exception
    except Exception:
        return None
    else:
        return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    noticia = {}
    noticia["url"] = selector.css(
        "head link[rel*=canonical]::attr(href)"
    ).get()
    noticia["title"] = (
        selector.css("section h1.entry-title::text").get().strip()
    )
    noticia["timestamp"] = selector.css("section li.meta-date::text").get()
    noticia["writer"] = selector.css(
        "section li.meta-author a.url::text"
    ).get()
    comments = selector.css(".post-comments").re_first(r"\d+(?= comments)")
    noticia["comments_count"] = int(comments) if comments else 0
    topico = selector.css("div.entry-content p")[0].css("*::text").getall()
    noticia["summary"] = "".join(topico).strip()
    noticia["tags"] = selector.css(
        "section.post-tags [rel='tag']::text"
    ).getall()
    noticia["category"] = selector.css(
        "div.meta-category span.label::text"
    ).get()

    return noticia


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
