# coding=utf-8
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
    "Cookie": "anonymid=k0hyz431-7bnj7b; depovince=BJ; _r01_=1; JSESSIONID=abcxYogd1OjytaetKiQ0w; "
              "ick_login=715a9ea4-96f4-4b76-9862-397d49967fa2; _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; "
              "ick=2dffc3ed-791f-49c7-b27c-e2417105ad9c; t=9476a1d7701098c29c6908356f1060a27; "
              "societyguester=9476a1d7701098c29c6908356f1060a27; id=972239077; xnsid=d5dbcbe7; "
              "XNESSESSIONID=e8676b4c6511; ver=7.0; loginfrom=null; "
              "jebe_key=92a1837e-61df-4569-a719-deae45111647%7C553a534b8be4669a3c8d8683c978bc9a%7C1568370123116%7C1"
              "%7C1568370125260; jebe_key=92a1837e-61df-4569-a719-deae45111647%7C553a534b8be4669a3c8d8683c978bc9a"
              "%7C1568370123116%7C1%7C1568370125263; wp_fold=0; jebecookies=d7c675ab-1abd-4166-acbe-c9b16f1f84df||||| "
}

r = requests.get("http://www.renren.com/972239077/profile", headers=headers)

# 保存页面
with open("人人网2.html", "w", encoding="utf-8") as f:
    f.write(r.content.decode())
