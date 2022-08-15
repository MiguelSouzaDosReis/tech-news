from tech_news.database import find_news


# Requisito 10
def top_5_news():
    find = find_news()
    find.sort(reverse=True, key=lambda x: (x["comments_count"], x["title"]))
    array = []
    for news in find:
        array.append((news["title"], news["url"]))
    return (array)[:5]


# Requisito 11
def top_5_categories():
    ""
