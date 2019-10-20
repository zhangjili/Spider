# encoding=utf-8
import re
import itchat
itchat.login()
#爬取自己好友相关信息， 返回一个json文件
friends = itchat.get_friends(update=True)[0:]
siglist = []
for i in friends:
    signature = i["Signature"].strip().replace("span","").replace("class","").replace("emoji","")
    rep = re.compile("1f\d+\w*|[<>/=]")
    signature = rep.sub("", signature)
    siglist.append(signature)
text = "".join(siglist)
import jieba
wordlist = jieba.cut(text, cut_all=True)
word_space_split = " ".join(wordlist)
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image as Image
coloring = np.array(Image.open("兔子.jpg"))
my_wordcloud = WordCloud(background_color="white", max_words=2000,
                         mask=coloring, max_font_size=60, random_state=42, scale=2,
                         font_path="D:\\迅雷下载\\2-1Q22FT622\\罗西钢笔行楷.ttf").generate(word_space_split)

image_colors = ImageColorGenerator(coloring)
plt.imshow(my_wordcloud.recolor(color_func=image_colors))
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()