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
    result = []
    noticias = find_news()
    categorias = [nova["category"] for nova in noticias]
    contagem = {}

    for categoria in categorias:
        if categoria in contagem:
            contagem[categoria] += 1
        else:
            contagem[categoria] = 1
    categorias_pop = sorted(
        contagem, key=lambda order: (-contagem.get(order), order)
    )
    result = categorias_pop[:5]

    return result
