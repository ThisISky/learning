import requests  # Можно использовать для отправки всех видов HTTP-запросов.
from bs4 import BeautifulSoup as bs  # Модуль для парсинга

headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
     Chrome/79.0.3945.117 Safari/537.36"
}

url = "https://samara.hh.ru/search/vacancy?search_period=3&clusters\
        =true&area=78&text=Python&enable_snippets=true"


def hh_parse(url, headers):
    jobs = []
    session = requests.Session()
    request = session.get(url, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, "html.parser")
        divs = soup.find_all("div", attrs={"data-qa": "vacancy-serp__vacancy"})
        for div in divs:
            title = div.find("a", attrs={"data-qa": "vacancy-serp__vacancy-title"}).text
            href = div.find("a", attrs={"data-qa": "vacancy-serp__vacancy-title"})["href"]
            company = div.find("a", attrs={"data-qa": "vacancy-serp__vacancy-employer"}).text
            text1 = div.find("div", attrs={"data-qa": "vacancy-serp__vacancy_snippet_responsibility"}).text
            text2 = div.find("div", attrs={"data-qa": "vacancy-serp__vacancy_snippet_requirement"}).text
            content = text1 + " " + text2
            jobs.append({
                "title": title,
                "href": href,
                "company": company,
                "content": content
            })
        print(jobs)
    else:
        print("Error")


hh_parse(url, headers)