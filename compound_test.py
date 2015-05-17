# In Futurama, Fry has a bank account with a balance of .93 cents in the year 2000. 
# In the year 3000 he had 4.3 billon due to compound interest.
# What was the interest rate on the account?

initial = .93

interest = .02228 / 12

months = 12000

current = initial

for i in xrange(months):
    current *= (1 + interest)

print current / 1000000000