import requests as r
from bs4 import BeautifulSoup


dcard_url_2="https://www.dcard.tw/_api/forums/makeup/posts?popular=false"
res1 = r.get(dcard_url_2)
d_jsons = res1.json()
for y in d_jsons :
    article = "https://www.dcard.tw/f/makeup/p/{}"
    article_links = article.format(y['id'])
    print(article_links)
    print(y['title'])
    
no30_arc = d_jsons[29]['id']
print(no30_arc)

turning_pg = "https://www.dcard.tw/_api/forums/makeup/posts?popular=false&before={}"
nxt_pg = turning_pg.format(no30_arc)
print(nxt_pg) # nxt_pg is url



while True :
    turning_pg = "https://www.dcard.tw/_api/forums/makeup/posts?popular=false&before={}"
    nxt_pg = turning_pg.format(no30_arc)
    print(nxt_pg) # nxt_pg is url
    resource = r.get(nxt_pg)
    print(resource)
    try:
        dp_jsons = resource.json()
    except:
        print('[Error] %s, retrying'%nxt_pg)
        continue

    for x in dp_jsons :
        article = "https://www.dcard.tw/f/makeup/p/{}"
        article_links = article.format(x['id'])
        print(article_links)
        print(x['title'])

        no30_arc = dp_jsons[29]['id']
