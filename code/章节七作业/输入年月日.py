from datetime import *
d=input()
d1=datetime.strptime(d[:4]+'/1/1','%Y/%m/%d')
d2=datetime.strptime(d,'%Y/%m/%d')
print((d2-d1).days+1)