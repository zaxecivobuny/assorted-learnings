import random

def simulateDraw(red_marbles,white_marbles,string_size):
    white_count = 0
    total_marbles = red_marbles + white_marbles

    while total_marbles > 0:

        drawn_marble = random.randint(1,total_marbles)
        if drawn_marble < red_marbles:
            red_marbles -= 1
            white_count = 0
        else:
            white_marbles -= 1
            white_count += 1
            if white_count >= string_size:
                return True
            elif white_marbles == 0:
                return False

        total_marbles = red_marbles + white_marbles

    return False

numberOfRuns = 10*1000
numberOfSuccesses = 0

red_marbles = 200
white_marbles = 165
string_size = 7

for i in xrange(numberOfRuns):
    if simulateDraw(red_marbles,white_marbles,string_size):
        numberOfSuccesses += 1

print "You tried a case with", white_marbles, "white marbles and", red_marbles, "red marbles, seeking a string of", string_size, "white marbles."
print "There were", numberOfSuccesses, "successes in", numberOfRuns, "runs for a chance of", (1.0*numberOfSuccesses)/(1.0*numberOfRuns)
