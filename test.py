import array
arr = []
inp = open ("processed.cleveland.data","r")
#read line into array
for line in inp.readlines():
    # add a new sublist
    items = line.split(',')
    temparr = []
    for i in items:
        try :
            temparr.append(float(i))
        except :
            temparr.append(i)
    arr.append(temparr)

print "RESULT: "
print arr