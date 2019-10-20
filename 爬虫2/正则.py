import  re
s = "this is a number 234-235-22-4223"
r= re.match(r'(.+)(\d+-\d+-\d+-\d+)',s)
print(r.groups())

s1 = "this is a number 234-235-22-4223"
r1= re.match(r'(.+?)(\d+-\d+-\d+-\d+)',s1)
print(r1.groups())

a=[1,2]
b=["aa","bb"]
c= zip(a,b)
for value in c:
    index,title=value
    print(index,title)
    
a,b = ('hello',"world")
print(a)
print(b)

print('\n'.join([''.join([('love'[(x-y) % len('love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30,30)]) for y in range(30, -30, -1)]))
for i in range(30,-30,-1):
    print(i)

import time

words =input('Please input the words you want to say!:')

for item in words.split():
    print('\n'.join([''.join([('love'[(x - y) % len('love')] if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (
                x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))
    time.sleep(1.5);