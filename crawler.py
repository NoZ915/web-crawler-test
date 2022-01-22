# 抓取ptt電影版的網頁原始碼（HTML）
import urllib.request as req
url = "https://www.ptt.cc/bbs/movie/index.html"
# 建立一個Request物件，附加Request Headers 的資訊
# 這可以使我們的發送要求更像人類
request=req.Request(url, headers={
  "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
})
with req.urlopen(request) as response:
  data=response.read().decode("utf-8")
print(data)