from collections import Counter
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
    find = find_news()
    find.sort(key=lambda x: (x["category"], x["title"]))
    array = []
    for news in find:
        array.append((news["category"]))
    popularity = Counter(array).most_common()
    order = [pair[0] for pair in popularity]
    return (order)[:5]
