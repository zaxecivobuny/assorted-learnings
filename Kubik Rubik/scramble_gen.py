import random

cube_number = 9

number_of_turns = 10

layers = cube_number / 2

print layers

turns = []

def gimmeturn(layers):
    facemap = {0:'F', 1:'B', 2:'U', 3:'D', 4:'L', 5:'R'}
    degreemap = {0:'', 1:'2', 2:"'"}
    layermap = {0:''}
    for i in xrange(1, layers):
        layermap[i] = str(i+1)

    rand_face = facemap[int(random.random() * 6)]
    rand_degree = degreemap[int(random.random() * 3)]
    rand_layer = layermap[int(random.random() * layers)]

    return "%s%s%s" % (rand_layer, rand_face, rand_degree)

#turn1 = "%s%s" % (facemap[int(random.random() * rando)], degreemap[int(random.random() * 3)]) 

#turns.append()

310 337 8911

print random.random()

for i in xrange(number_of_turns):
    turns



print turns