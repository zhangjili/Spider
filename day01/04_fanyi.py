# coding=utf-8
import requests
import json
import sys

# query_string = sys.argv[1]

headers = {
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X)"
                  " AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"}

post_data = {
    "from":"zh",
    "to":"en",
    "query": "发森",
    "transtype":" enter",
    "simple_means_flag": "3",
    "token": "2a8f3292979ae4380da0ba7983116035"
}

post_url = "https://fanyi.baidu.com/v2transapi"

r = requests.post(post_url, data=post_data, headers=headers)
print(r.content.decode())
# dict_ret = json.loads(r.content.decode())
# ret = dict_ret["trans"][0]["dst"]
# print("result is :", ret)
