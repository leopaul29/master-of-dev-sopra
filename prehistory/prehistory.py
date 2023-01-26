w = 0
h = 0
i = 0
tab = []
f = open("input.txt", "r")
for x in f:
    line = x.replace("\n", "")
    if i == 0:
        size = line.split(" ")
        r = int(size[0])
        c = int(size[1])

    if i != 0 and line != "":
        print("line", line)
        row=[]
        for s in line:
            row.append(s)
        tab.append(row)

    i += 1
f.close()
print(tab)
rindex = int(r/2)
cindex = int(c/2)
print(rindex, cindex)
print(tab[rindex][cindex])