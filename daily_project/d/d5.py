f = open('D:\\python_project\\file_process\\f_a_3.py', 'r',encoding='utf8')
data = eval(f.read())
print (data)
f.close()
# print (type(data))
# current_layer = data
# parent_layer = []
# # exit_flag = False
# while True:
#   for i in current_layer:
#     print(i)
#   choice = input(">>")
#   if choice in current_layer:
#     parent_layer.append(current_layer)
#     current_layer = current_layer[choice]
#   elif choice == 'b':
#     current_layer = parent_layer.pop()
#   elif choice == 'q': break
#   elif choice == 'i':
#     insert = input("输入你要添加的内容:")
#     current_layer.setdefault(insert, { })
#     with open('province.txt', 'w', encoding='utf8') as f_write:
#       f_write.write(str(data))
#       f_write.flush()
#   else:
#     print("查无此项")