# -*- coding: gbk -*-
from bs4 import BeautifulSoup
html = """<div data-v-a6e3291a="" class="recruit-list">
<a data-v-a6e3291a="" class="recruit-list-link">
<h4 data-v-a6e3291a="" class="recruit-title">PCG19-数据传输研发工程师（深圳）</h4>
<p data-v-a6e3291a="" class="recruit-tips">
                    <span data-v-a6e3291a="">PCG</span> |
                  <span data-v-a6e3291a="">深圳,中国</span> |
                  <span data-v-a6e3291a="">技术</span> |
                  <span data-v-a6e3291a="">腾讯视频</span> |
                   <span data-v-a6e3291a="">2019年10月03日</span></p>
                   <p data-v-a6e3291a="" class="recruit-text">负责数据传输组件的研发，包括Http下载、P2P下载、传输协议优化、下载调度优化等；负责数据传输组件在腾讯视频全平台的应用落地以及相关问题跟进，包括PC、手机、Pad、TV等平台；讯视频全平台下载体验的优化；负责腾讯视频全平台带宽节省率的优化；</p>
                   </a>
<div data-v-a6e3291a="" class="recruit-collection"><span data-v-a6e3291a="" class="icon-collection"></span>
<span data-v-a6e3291a="" class="collection-text">收藏</span></div>
</div>"""
soup = BeautifulSoup(html,'lxml')
spans = soup.find_all('span')
# for i in trs:
#     print(trs)
# trs = soup.find_all('span',limit=2)[1]
# print(trs)
# print(spans)
for span in spans:
    sp = list(span.stripped_strings)
    print(sp)
# span = soup.select("span")
# for i in span:
#     print(i.string)
# print(span)