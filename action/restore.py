import requests

def get_url_restore(url):
    urls = url.split("://")
    schema = "http"
    if len(urls) < 2:
        urls = schema + urls
    else:
        urls[0] = schema
    url = "://".join(urls)
    return handle_response(url)


def handle_response(url):
    r = requests.get(url)
    history = r.history
    if history:
        res = history[0]
        jrs = res.headers
        return jrs.get("location")
    else:
        raise Exception("URL Invalid")
