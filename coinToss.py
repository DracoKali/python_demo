
import random

def CointToss(TimesTossed):
    head_count = 0
    tail_count = 0
    attempts = 0
    result = ''
    result_complete = ""
    for x in range(0, TimesTossed):
      coin = random.randrange(1, 4)
      if coin <= 2 and coin >= 1:
        head_count += 1  
        result = 'head'
      elif coin <= 4 and coin >= 3:
        tail_count += 1 
        result = 'tail' 
        if  (head_count or tail_count) + 1:
         attempts += 1

    print "Attempts #", attempts, ": Throwing a coin... it's a", result, "! Got", head_count, "head(s) so far", tail_count, "tail(s) so far" 

CointToss(5)






    # import math
    # x = .23945593
    # x_rounded = int(math.floor(x)) 
    # y = .798839238
    # y_rounded = int(math.ceil(y))
    # print x_rounded, y_rounded