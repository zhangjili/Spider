# -*- coding: gbk -*-
import csv
# with open('newfood.csv','r') as f:
#     # reader ��һ��������
#     reader = csv.reader(f)
#     for i in reader: #i ���б�
#         print(i)

# ����һ�ַ�ʽ�ֵ䷽ʽ
# with open('newfood.csv','r') as f:
#     # DictReader��ȡ��ʱ�򲻰�������
#     reader = csv.DictReader(f)
#     # print(reader)
#     for i in reader:
#         print({"name":i['name'],"sales":i['sales']})

# д��
# hreders = ['username','age','name']
# values = [
#     ('����',14,156),
#     ("����",18,170),
#     ("����",24,180)
# ]
# with open('11.csv','w',newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(hreders)
#     writer.writerows(values)

def write2():
    hreders = ['username', 'age']
    values = [
        {'username':'����','age':13},
        {'username': '����', 'age': 63}
    ]
    with open('12.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f,hreders)
        # д���ͷ����
        writer.writeheader()
        writer.writerows(values)
        
if __name__ == '__main__':
    write2()