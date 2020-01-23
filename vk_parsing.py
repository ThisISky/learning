import requests
import csv

def take_1000_posts():
    token = "ca30fd14ca30fd14ca30fd1404ca5fbfa7cca30ca30fd14941848969e237b4b2cce9266"
    ver = 5.103
    domain = "dodosamara"
    offset = 0
    count = 100
    all_posts = []
    while offset < 1000:
        response = requests.get("https://api.vk.com/method/wall.get",
                                params={
                                    "access_token": token,
                                    "v": ver,
                                    "domain": domain,
                                    "count": count,
                                    "offset": offset
                                })

        data = response.json()["response"]["items"]
        offset += 100
        all_posts.extend(data)
    return all_posts

def file_writer(data):
    with open("dodosamara.csv", "w", encoding="utf-8", newline="") as file:
        a_pen = csv.writer(file, delimiter=";")
        a_pen.writerow(("likes", "body", "url"))
        for post in data:
            try:
                if post["attachments"][0]["type"]:
                    img_url = post["attachments"][0]["photo"]["sizes"][-1]["url"]
                else:
                    img_url = "pass"
            except:
                pass
            a_pen.writerow((post["likes"]["count"], post["text"], img_url))


file_writer(take_1000_posts())