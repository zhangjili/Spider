# -*- coding: gbk -*-
import json

persons = [
    {
        'username': '����',
        'age': 18,
        'country': 'chian'
    },
    {
        'username': 'hello',
        'age': 34,
        'country': 'china'
    }
    # ��python����תΪjson�ַ���
]
# json_str = json.dumps(persons)
# # # print(type(json_str))
# # # print(json_str)
# # with open('person.json', 'w') as f:
# #     #     f.write(json_str)
# #     # dump����ֱ�Ӵ浽�ļ���ensure_ascii=False���ľͲ��ᱻתΪUnicode�����������
# #     json.dump(persons, f,ensure_ascii=False)

# json_str ='[{"username": "����", "age": 18, "country": "chian"}, {"username": "hello", "age": 34, "country": "china"}]'
# p = json.loads(json_str)
# for i in p:
#     print(i)
with open('person.json','r') as fp:
    p = json.load(fp)
    for i in p:
        print(i)
