# # # no.1
import spam
# # # spam.r1()


# # # no.2
# # from spam import r1
# # r1()


# no.3
from spam import r2
r2()


# no.3
# from spam import r3
spam.r3()
# print (spam.r3())
# print (a)



# no.4
# Python 会假设任何在函数内赋值的变量都是局部的。
Money = 2000
def AddMoney():
   # 想改正代码就取消以下注释:
   global Money
   Money = Money + 1
 
print (Money)
AddMoney()
print (Money)


