from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    result = []
    noticias = search_news({"title": {"$regex": title, "$options": "i"}})
    for nova in noticias:
        result.append((nova["title"], nova["url"]))

    return result


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
