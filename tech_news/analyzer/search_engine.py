from tech_news.database import search_news
import time


# Requisito 6
def search_by_title(title):
    array = []
    for news in search_news({"title": {"$regex": f"{title.lower()}"}}):
        array.append((news["title"], news["url"]))
    return array


# Requisito 7
def search_by_date(date):
    dateSplit = date.split("-")
    year = dateSplit[0]
    mouth = dateSplit[1]
    day = dateSplit[2]
    NewDate = f"{day}/{mouth}/{year}"
    try:
        time.strptime(date, "%Y-%m-%d")
        array = []
        for news in search_news({"timestamp": {"$regex": f"{NewDate}"}}):
            array.append((news["title"], news["url"]))
        return array
    except(ValueError):
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    array = []
    for news in search_news({"tags": {"$regex": f"{tag}", "$options": "i"}}):
        array.append((news["title"], news["url"]))
    return array


# Requisito 9
def search_by_category(category):
    array = []
    c = category
    for news in search_news({"category": {"$regex": f"{c}", "$options": "i"}}):
        array.append((news["title"], news["url"]))
    return array
