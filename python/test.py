clothes = [['1','1'],['12','1'],['32','2']]
dic_clothes = {}
for name,typ in clothes:
    dic_clothes[typ] = dic_clothes.get(typ,name)

print(dic_clothes)