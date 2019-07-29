# import json

# data={
# 	'a':'1','b':'2','c':'3'
# }

# we=json.dumps(data)
# # print (we)
# # print (data)
# # print (type(we))
# # print (type(data))

# print (repr(data))
# print (we)





# #如果你要处理的是文件而不是字符串，你可以使用 json.dump() 和 json.load() 来编码和解码JSON数据。例如：

# # 写入 JSON 数据
# with open('data.json', 'w') as f:
#     json.dump(data, f)
 
# # 读取数据
# with open('data.json', 'r') as f:
#     data = json.load(f)



import json
dic1 = {'type':'dic1','username':'sunchengquan','age':25}
json_dic1 = json.dumps(dic1)
print(json_dic1)
json_dic2 = json.dumps(dic1,sort_keys=False,indent =4,separators=(',', ': '),ensure_ascii=True )
json_dic2 = json.dumps(dic1,indent =4)
print(json_dic2)