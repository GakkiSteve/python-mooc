class Student:
    def __init__(self):
        self.sname = ""
        self.mscore = 0
        self.cscore = 0
        self.escore = 0
        self.summ = 0
    
    def __lt__(self, other):
        return self.summ > other.summ
        
        
name = input().split(" ")
math = list(map(int,input().split()))
chinese = list(map(int,input().split()))
english = list(map(int,input().split()))
number = len(name)
ans = []
for i in range(number):
    tmp = Student()
    tmp.sname = name[i]
    tmp.mscore = math[i]
    tmp.cscore = chinese[i]
    tmp.escore = english[i]
    tmp.summ =  tmp.mscore + tmp.cscore + tmp.escore
    ans.append(tmp)
    
ans.sort()
print(ans[0].sname, ans[0].mscore, ans[0].cscore, ans[0].escore)