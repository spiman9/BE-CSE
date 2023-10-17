'''
2GI20CS088
2GI20CS096
2GI20CS105
2GI20CS106
2GI20CS104
2GI20CS122
2GI20CS158
2GI20CS144
2GI20CS079
2GI20CS086
2GI20CS078
2GI20CS110
2GI20CS125
2GI20CS139
2GI20CS141
2GI20CS150
2gi20cs089
2gi20cs120
2gi20cs111
2gi20cs121
2GI20CS127
2GI20CS148
2GI20CS124
2GI20CS129
2GI20CS109
2GI20CS090
2GI20CS126
2GI20CS116
2GI20CS112
2GI20CS114
2GI20CS131
2GI20CS191
2GI20CS084
2GI29CS080
2GI20CS082
2GI30CS138
2gi20cs123
2gi20cs146
2gi20cs130
2gi20cs159
2GI20CS099
2GI20CS102
2GI20CS103
2GI20CS108
2GI20CS117
2GI20CS128
2GI20CS132
2GI20CS135
2GI20CS097
2GI20CS092
2GI20CS107
2GI20CS087
2GI20CS081
2GI20CS133
2GI20CS091
2GI20CS094
2GI20CS093
2GI20CS041
2GI20CS098
'''
l = list()
with open("./textUSN.txt" , 'r') as fd:
    lines = fd.readlines()
    
    for usn in lines:
        Slice = usn[7:10]
        l.append(int(Slice))
    l.sort()
    # print(l)

    

with open("./onlyUSN.txt" , 'w') as fd:
    for usn in l:
        banao = str(usn) +'\n'
        fd.write(banao)
    fd.write("Total : " + str(len(l)))


#check duplicates
def CheckDuplicates(l):
    for i in range(len(l)-1):
        if l[i] == l[i+1]:
            print("Duplicates")
            return
    print("No duplicates")


CheckDuplicates(l)