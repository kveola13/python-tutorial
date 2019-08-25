import requests


def getMovieTitles(substr):
    url = "https://jsonmock.hackerrank.com/api/movies/search/?Title=" + substr
    titles = []
    page_total = requests.get(url).json()["total_pages"]
    print(page_total)
    for pages in range(1, page_total + 1, 1):
        url_plus_request = url + "&page=" + str(pages)
        if url_plus_request:
            page_title = requests.get(url_plus_request).json()["data"]
            for info in page_title:
                titles.append(info["Title"])
    titles.sort()
    return titles


if __name__ == '__main__':
    title = "Spiderman"
    for value in getMovieTitles(title):
        print(value)
