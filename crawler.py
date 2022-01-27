# 抓取ptt電影版的網頁原始碼（HTML）
import bs4
import urllib.request as req
url = "https://www.ptt.cc/bbs/movie/index.html"
# 建立一個request物件，附加Request Headers 的資訊
# 這可以使我們的發送要求更像人類
request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
})
# 利用上方request物件去做連線
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

# 解析原始碼，取得每篇文章的標題
root = bs4.BeautifulSoup(data, "html.parser")
titles = root.find_all("div", class_="title")
for title in titles:
    if title.a != None:
        print(title.a.string)
