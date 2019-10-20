# -*- coding: gbk -*-
import json

persons = [
    {
        'username': '张三',
        'age': 18,
        'country': 'chian'
    },
    {
        'username': 'hello',
        'age': 34,
        'country': 'china'
    }
    # 把python对象转为json字符串
]
# json_str = json.dumps(persons)
# # # print(type(json_str))
# # # print(json_str)
# # with open('person.json', 'w') as f:
# #     #     f.write(json_str)
# #     # dump可以直接存到文件中ensure_ascii=False中文就不会被转为Unicode编码的类型了
# #     json.dump(persons, f,ensure_ascii=False)

# json_str ='[{"username": "张三", "age": 18, "country": "chian"}, {"username": "hello", "age": 34, "country": "china"}]'
# p = json.loads(json_str)
# for i in p:
#     print(i)
with open('person.json','r') as fp:
    p = json.load(fp)
    for i in p:
        print(i)
