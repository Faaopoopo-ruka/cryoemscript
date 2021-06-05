#Author：Alex.Zhang
import execjs

query = 'Hello spider'
with open('baidutrans.js', 'r', encoding='utf-8') as f:
    ctx = execjs.compile(f.read())
sign = ctx.call('e', query)
print(sign)
