from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '17515793'
API_KEY = 'hsyLsFTFMEQc5qr1hCQwpWp9'
SECRET_KEY = 'xBYMn3FdZzrI6bh8Brywel955MYRmFiT'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)  # 创建连接
fp = open("测试2.png", "rb").read()  # 打开并读取文件内容
# res=client.basicGeneral(fp)#普通
res = client.webImage(fp)  # 高精度
# print(res)

# 将所有的文字都合并到一起
strx = ""
for tex in res["words_result"]:  # 遍历结果
    strx += tex["words"]  # 每一行
print(strx)  # 输出内容
