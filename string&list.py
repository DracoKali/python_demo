
import operator
words = "It's thanksgiving day. It's my birthday,too!"
for x in words.split():
 print  words.split()[2]


import operator
words = "It's thanksgiving day. It's my birthday,too!"
print words.replace("day", "month")


x = [2,54,-2,7,12,98]
print max(x)
print min(x)

x = ["hello",2,54,-2,7,12,98,"world"];
print x[0], x[7]
new_x = [x[0], x[7]]
print (new_x)



x = [19,2,54,-2,7,12,98,32,10,-3,6]
x == x.sort()
def split_list(a_list, number_of_splits):
    step = len(a_list) / number_of_splits + (1 if len(a_list) % number_of_splits else 0)
    return [a_list[i*step:(i+1)*step] for i in range(number_of_splits)] 
    print split_list(x, 2)







