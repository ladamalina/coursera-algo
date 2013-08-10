lb = -10000
rb = 10000

f = open('nums.txt', 'r')
lines = f.readlines()
f.close()
lines = [int(line) for line in lines]

rockstar_hash = {}
for line in lines:
    rockstar_hash[line] = 1

total = rb - lb
itotal = 1.0 / float(total)
    
result = 0
for summa in range(lb, rb):
    temp_dict = rockstar_hash.copy()
    for line in rockstar_hash:
        if (line in temp_dict) and (summa-line in temp_dict):
            if summa != line*2:
                result += 1
                del temp_dict[line]
                del temp_dict[summa-line]
    print str((summa - lb)*100*itotal) + "% (" + str(result) + " results)"
  
print "Finally:"          
print result
