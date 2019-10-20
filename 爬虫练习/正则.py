#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
# string = '''
#     abcd
#     abcd
# '''
# # 相当于
# # 1. 编译正则表达式
# # (.*)      贪婪匹配，尽可能多匹配直到无法匹配
# # (.*?)     非贪婪匹配，只要匹配到就返回
# #  . 符号默认不包含换行符，DOTALL模式表示让 . 符号匹配任何字符包括换行符
# # re.DOTALL == re.S == re.RegexFlag.DOTALL == re.RegexFlag.S
# pattern = re.compile(r'a(.*)d',re.RegexFlag.S)
#
# # 2. 提取数据
# result = pattern.findall(string)
# print(result)
#
#
# string = '''
#     abcD
#     abcD
# '''
# # 相当于
# # 1. 编译正则表达式
# # (.*)      贪婪匹配，尽可能多匹配直到无法匹配
# # (.*?)     非贪婪匹配，只要匹配到就返回
# #  . 符号默认不包含换行符，DOTALL模式表示让 . 符号匹配任何字符包括换行符
# # re.DOTALL == re.S == re.RegexFlag.DOTALL == re.RegexFlag.S
# # 忽略大小写
# # re.IGNORECASE == re.I == re.RegexFlag.IGNORECASE == re.RegexFlag.I
# # 忽略大小写并且支持 DOTALL模式 使用 |
# pattern = re.compile(r'a(.*)d',re.RegexFlag.IGNORECASE | re.DOTALL)
#
# # 2. 提取数据
# result = pattern.findall(string)
# print(result)



# string = "123abc123"
# # match 开头匹配，只匹配一次
# pattern = re.compile('\d+')
# # result = pattern.match(string)
#
# # search 全局匹配，只匹配一次
# # result = pattern.search(string)
#
# '''
# findall 优点：使用简单，缺点：必须把所有数据搜索返回再返回
# finditer 优点：找到就返回，可以边找边返回
# 如果数据量小 使用 findall
#
# 如果数据量大 使用 finditer
#
# '''
# # findall 匹配所有符号条件的数据，返回是 结果列表
# # result = pattern.findall(string)
#
# # finditer 迭代对象，迭代 Match 对象
# results = pattern.finditer(string)
# for result in results:
#     print(result)
#
# print(results)
#
# import re
# string = "a;dj jkl,jj; j;sd"
# # split 分组
# pattern = re.compile(r'[; ,]+')
# result = pattern.split(string)
# print(result)
#
# # sub 交换
# string = "hello world;sjd;ssdjkls;sdjk;crise lyj"
# # 带 空格的词组替换成 #
# pattern = re.compile(r'(\w+) (\w+)')
#
# # 把 空格的词组 进行交换
# result = pattern.sub(r"\2 \1",string)
#
# print(result)


string = '<input type="submit" id="su" value="百度一下" class="bg s_btn">'

pattern = re.compile(r'<input type="submit" id="(.*?)" value="(.*?)" class="bg s_btn">')

result = pattern.findall(string)
print(result)
