# -*- coding: gbk -*-
from bs4 import BeautifulSoup
html = """<div data-v-a6e3291a="" class="recruit-list">
<a data-v-a6e3291a="" class="recruit-list-link">
<h4 data-v-a6e3291a="" class="recruit-title">PCG19-���ݴ����з�����ʦ�����ڣ�</h4>
<p data-v-a6e3291a="" class="recruit-tips">
                    <span data-v-a6e3291a="">PCG</span> |
                  <span data-v-a6e3291a="">����,�й�</span> |
                  <span data-v-a6e3291a="">����</span> |
                  <span data-v-a6e3291a="">��Ѷ��Ƶ</span> |
                   <span data-v-a6e3291a="">2019��10��03��</span></p>
                   <p data-v-a6e3291a="" class="recruit-text">�������ݴ���������з�������Http���ء�P2P���ء�����Э���Ż������ص����Ż��ȣ��������ݴ����������Ѷ��Ƶȫƽ̨��Ӧ������Լ�����������������PC���ֻ���Pad��TV��ƽ̨��Ѷ��Ƶȫƽ̨����������Ż���������Ѷ��Ƶȫƽ̨�����ʡ�ʵ��Ż���</p>
                   </a>
<div data-v-a6e3291a="" class="recruit-collection"><span data-v-a6e3291a="" class="icon-collection"></span>
<span data-v-a6e3291a="" class="collection-text">�ղ�</span></div>
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