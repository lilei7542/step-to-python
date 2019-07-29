shaoguan = {'仁化', '始兴', '乐昌', '南雄'}
jiangmeng = {'开平', '蓬江', '台山', '鹤山', '恩平'}
guangdong_province = {'韶关':shaoguan, '江门':jiangmeng}
nanchang = {'东湖', '西湖', '新建', '安义', '进贤'}
jingdezhen = {'昌江', '珠山', '乐平', '浮梁'}
jiangxi_province = {'南昌': nanchang, '景德镇': jingdezhen}
provinces = {'广东': guangdong_province, '江西': jiangxi_province} 
# print (shaoguan)
# print (provinces)


# current_layer = data
current_layer = provinces
parent_layer = []
# exit_flag = False
while True:
  for i in current_layer:
    print(i)
  choice = input(">>")
  if choice in current_layer:
    parent_layer.append(current_layer)
    current_layer = current_layer[choice]
  elif choice == 'b':
    current_layer = parent_layer.pop()
  elif choice == 'q': break
  elif choice == 'i':
    insert = input("输入你要添加的内容:")
    current_layer.setdefault(insert, { })
    with open('province.txt', 'w', encoding='utf8') as f_write:
      f_write.write(str(data))
      f_write.flush()
  else:
    print("查无此项")