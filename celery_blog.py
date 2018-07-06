from celery import Celery
import requests

app = Celery('celery_blog',
             # backend='redis://localhost',
             broker='redis://localhost')


@app.task
def fetch_url(url):
    resp = requests.get(url)
    write_result(resp.status_code)


def func(urls):
    for url in urls:
        fetch_url.delay(url)


def write_result(res):
    with open('res.txt', mode='a') as f:
        f.write(str(res) + '\n')


if __name__ == "__main__":
    # func(["http://google.com", "https://amazon.com", "https://facebook.com", "https://twitter.com", "https://alexa.com"])
    func(["http://google.com", "http://google.co.uk"])
