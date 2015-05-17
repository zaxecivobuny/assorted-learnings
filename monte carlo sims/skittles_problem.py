import random

def get_skittle_pack(n):
    skittles = ["R", "P", "Y", "G", "V", "B"]
    #r:red:cherry
    #p:pink:strawberry
    #y:yellow:lemon
    #g:green:lime
    #v:violet:grape
    #b:blue:raspberry

    pack = []
    for i in xrange(n):
        pack.append(skittles[int(random.random() * 6)])

    return pack

def three_pairs(pack):
    temp_pack = sorted(pack[:])
    if (temp_pack[0] == temp_pack[1]) and (temp_pack[2] == temp_pack[3]) and (temp_pack[4] == temp_pack[5]) and not temp_pack[0] == temp_pack[2] and not temp_pack[2] == temp_pack[4]:
        return True
    else:
        return False

monte_carlo = 1000000

hits = 0

for i in xrange(monte_carlo):
    try_pack = get_skittle_pack(6)
    if three_pairs(try_pack):
        hits += 1

print hits, "hits in ", monte_carlo, "tries"
print "%s/%s" %(hits, monte_carlo)