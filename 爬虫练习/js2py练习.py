# -*- coding: utf-8 -*-
import js2py

js = """
function escramble_758(){
var a,b,c
a='+1 '
b='84-'
a+='425-'
b+='7450'
c='9'
document.write(a+c+b)
}
escramble_758()
""".replace("document.write", "return ")
result = js2py.eval_js(js)

# 第二种:执行js库或代码多,函数多的时候
with open('./get_key.js') as fp:
    js = fp.read()
    # ctx2 = execjs.compile(js)
    context = js2py.EvalJs()
    context.execute(js)
    vl5x = context.getKey(cookie)