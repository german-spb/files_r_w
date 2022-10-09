dic = {}
with open('1.txt', 'r', encoding='utf8') as file:
    res_1 = file.readlines()
    t_1 = len(res_1)
with open('2.txt', 'r', encoding='utf8') as file:
    res_2 = file.readlines()
    t_2 = len(res_2)
with open('3.txt', 'r', encoding='utf8') as file:
    res_3 = file.readlines()
    t_3 = len(res_3)
dic.update({t_1: res_1, t_2: res_2, t_3: res_3})
dic = dict(sorted(dic.items(), key=lambda x: x[0]))
with open('result.txt', 'w', encoding='utf8') as file:
    for keys, values in dic.items():
        new_str = ''.join(values).strip(' \n')
        if keys == t_1:
            name_txt = '1.txt'
        if keys == t_2:
            name_txt = '2.txt'
        if keys == t_3:
            name_txt = '3.txt'
        file.write(name_txt + '\n' + str(keys) + '\n' + new_str + '\n')
