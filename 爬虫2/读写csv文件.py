# -*- coding: gbk -*-
import csv
# with open('newfood.csv','r') as f:
#     # reader 是一个迭代器
#     reader = csv.reader(f)
#     for i in reader: #i 是列表
#         print(i)

# 另外一种方式字典方式
# with open('newfood.csv','r') as f:
#     # DictReader读取的时候不包含标题
#     reader = csv.DictReader(f)
#     # print(reader)
#     for i in reader:
#         print({"name":i['name'],"sales":i['sales']})

# 写入
# hreders = ['username','age','name']
# values = [
#     ('张三',14,156),
#     ("李四",18,170),
#     ("王五",24,180)
# ]
# with open('11.csv','w',newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(hreders)
#     writer.writerows(values)

def write2():
    hreders = ['username', 'age']
    values = [
        {'username':'张三','age':13},
        {'username': '根根', 'age': 63}
    ]
    with open('12.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f,hreders)
        # 写入表头数据
        writer.writeheader()
        writer.writerows(values)
        
if __name__ == '__main__':
    write2()