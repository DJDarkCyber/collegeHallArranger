import pandas as pd
import numpy as np

def arrangeRollNo(halls):
    halls = int(halls)
    f = open("data/rolls.txt", "r")
    cont = f.read().split(",")
    rolls = []
    for stuff in cont:
        stuff = stuff.replace("\n", "").replace(" ", "").replace("\t", "")
        rolls.append(stuff)
    print(rolls)
    rollsNos = pd.Series(rolls)
    unqvals = rollsNos.str.slice(stop=-3).astype(np.int64).unique()
    unqvals = unqvals.astype(str)
    arrgRolls = []
    for i in range(len(unqvals)):
        arrgRolls.append(rollsNos[rollsNos.str.slice(stop=-3) == unqvals[i]].to_list())
    print(arrgRolls)
    arrngedRollNo = []
    count = len(rollsNos)


    cur1 = 0
    cur2 = 1
    while count!=0:
        if len(arrgRolls[cur1]) != 0:
            arrngedRollNo.append(arrgRolls[cur1][0])
            arrgRolls[cur1].pop(0)
            count -= 1
        else:
            cur1 += 2
            if cur1 >= len(arrgRolls):
                print(len(arrgRolls))
                break
        if len(arrgRolls[cur2]) != 0:
            arrngedRollNo.append(arrgRolls[cur2][0])
            arrgRolls[cur2].pop(0)
            count -= 2
        else:
            cur2 += 2
            if cur2 >= len(arrgRolls):
                break

    for i in range(len(arrgRolls)):
        for j in range(len(arrgRolls[i])):
            arrngedRollNo.append(np.nan)
            arrngedRollNo.append(arrgRolls[i][j])
    print(arrngedRollNo)
    nd = len(arrngedRollNo)/halls
    if nd > float(int(nd)):
        seat = int(nd) + 1
    else:
        seat = int(nd)
    
    data = {
        "Seats": [x+1 for x in range(seat)]
    }
    
    for i in range(halls):
        data["Hall_" + str(i+1)] = np.nan
    halldf = pd.DataFrame(data)
    s = 0
    for i in range(halls):
        try:
            for sts in range(seat):
                halldf["Hall_" + str(i+1)][sts] = arrngedRollNo[s]
                s += 1
        except IndexError:
            pass

    print(halldf)
    halldf.to_excel("data/hall.xlsx", index=False)

    halldict = halldf.to_dict()
    del halldict['Seats']
    totalHalls = []
    totalRolls = []
    for stuff, lol in halldict.items():
        totalHalls.append(stuff)
        morevals = []
        for nks, vals in lol.items():
            morevals.append(vals)
        totalRolls.append(morevals)

    return totalHalls, totalRolls, len(halldict)