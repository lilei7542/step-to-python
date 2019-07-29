month=int(input("say something "))
year = int(input("输入一个年份: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} 是闰年".format(year))   # 整百年能被400整除的是闰年
       else:
           print("{0} 不是闰年".format(year))
   else:
       print("{0} 是闰年".format(year))       # 非整百年能被4整除的为闰年
else:
   print("{0} 不是闰年".format(year))



print("{0} is a month".format(month))



{0}  要跟 format 搭配更妙哦


print("{0} is a friday".format(5), "{0} is sunday".format(7))

print("{0} is a friday,{0} is sunday".format(5).format(7)) # see what ? hahaha

