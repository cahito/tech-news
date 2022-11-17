from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    result = []
    noticias_por_titulo = search_news(
        {"title": {"$regex": title, "$options": "i"}}
    )
    for nova in noticias_por_titulo:
        result.append((nova["title"], nova["url"]))

    return result


# Requisito 7
def search_by_date(date):
    result = []
    try:
        data_formatada = datetime.strptime(date, "%Y-%m-%d").strftime(
            "%d/%m/%Y"
        )
        noticias_por_data = search_news({"timestamp": data_formatada})
        for cada in noticias_por_data:
            result.append((cada["title"], cada["url"]))
        return result
    except ValueError:
        raise (ValueError("Data inválida"))


# Requisito 8
def search_by_tag(tag):
    result = []
    noticias_por_titulo = search_news(
        {"tags": {"$regex": tag, "$options": "i"}}
    )
    for nova in noticias_por_titulo:
        result.append((nova["title"], nova["url"]))

    return result


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
