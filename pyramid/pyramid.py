
def decrypt_action(action):
    return [int(s) for s in action.split() if s.isdigit()]


index=0
m=0
n=0
p = 0
tab=[]
action_map = []
f = open("input.txt", "r")
for x in f:
    line = x.replace("\n", "")
    #print(line)
    if index == 0:
        param = line.split(" ")
        m = param[0]
        n = param[1]
        p = param[2]

    if index != 0 and line[0].isnumeric():
        pile= line.split(" ")
        index_line=int(pile[0])
        tab.append(pile[1:len(pile)])

    if index != 0 and not line[0].isnumeric():
        if line.startswith('L'):
            action_map.append([0, decrypt_action(line)])
        else:
            action_map.append([1, decrypt_action(line)])

        print(line)
    print("action_map", action_map)

    index += 1

print("tab", tab)
print("action_map", action_map)
f.close()


for action in action_map:
    print("action1", action[1])
    quantity_stack = int(action[1][0])
    from_stack = int(action[1][1]) - 1
    to_stack = int(action[1][2]) - 1
    if action[0] == 0:
        print("o", quantity_stack, from_stack, to_stack)
        for q in range(quantity_stack):
            temp_pierre = "_"
            if tab[from_stack].__len__() != 0:
                temp_pierre = tab[from_stack].pop(tab[from_stack].__len__()-1)
                tab[to_stack].append(temp_pierre)
    else:
        print("O", quantity_stack, from_stack, to_stack)
        temp_pierre=[]
        for q in range(quantity_stack):
            toremove=tab[from_stack].pop()
            print("toremove", toremove)
            temp_pierre.insert(0, toremove)
        #temp_pierre = tab[from_stack][tab[from_stack].__len__()-q+1:tab[from_stack].__len__()]
        for a in temp_pierre:
            tab[to_stack].append(a)

    print("tab", tab)


print("tab final", tab)
final=""
for t in tab:
    if t.__len__() != 0:
        final += (t[t.__len__()-1])
print("final", final)