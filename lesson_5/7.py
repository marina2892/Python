import json

dict_pr = {}
dict_ub = {}
sum = 0
cnt = 0
f_o = open("file7.txt","r",encoding = "utf-8")
with f_o:
    for str in f_o:
        list = str.split()
        pr = float(list[2]) - float(list[3])
        fl = 0
        if pr < 0:
            ub = abs(pr)
            dict_ub.update({list[0]:ub})
            fl = 1
        if fl == 0:
            cnt = cnt + 1
            dict_pr.update({list[0]:pr})
            sum = sum + pr
avg = sum / cnt
list_result = [dict_pr,{"average_profit":avg},dict_ub]

f_o = open("file.json","w")
with f_o:
    json.dump(list_result, f_o)