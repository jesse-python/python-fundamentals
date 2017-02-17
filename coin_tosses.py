import random

heads = 0
tails = 0

for i  in range(0,5000):
    random_num = random.random()
    random_int = round(random_num)
    if random_int == 1:
        curr_face = "heads"
        heads += 1
    elif random_int == 0:
        curr_face = "tails"
        tails += 1
    print "Attempt #%s: Throwing a coin...It's a %s! ... Got %s head(s) so far and %s tail(s) so far" % (i, curr_face, heads, tails)
