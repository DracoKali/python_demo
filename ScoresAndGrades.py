
import random
def scores_grades(TestScore):
    score = random.randrange(60, 100)
    if (score <= 69 and score >= 60):
        print 'Score:', score, '; Your score is D'
    elif (score <= 79 and score >= 70):
        print 'Score:', score, '; Your Score is C'
    elif (score <= 89 and score >= 80):
        print 'Score:', score, '; Your Score is B'
    elif(score <= 100 and score >= 90):
        print 'Score:', score ,'; Your Score is A'  
    else:
        print "You failed"
        print "End of the program.  Bye!"
    

scores_grades(90)