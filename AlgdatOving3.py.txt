toppnode=Node()
for (ord, pos) in ordliste
    temp = toppnode
    for n in ord
        if !od[n] in temp.barn
            temp.barn[n] = Node()
        temp = temp.barn[n]
        if n==(ord.len -1)
            temp.posi.append(pos)
return toppnode


