from tech_news.database import find_news


# Requisito 10
def top_5_news():
    result = []
    noticias = find_news()
    noticias_pop = sorted(
        noticias, key=lambda order: (-order["comments_count"], order["title"])
    )
    for x in range(5):
        try:
            result.append((noticias_pop[x]["title"], noticias_pop[x]["url"]))
        except IndexError:
            pass
    
    return result


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
