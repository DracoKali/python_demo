name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def dictionary(var):
    dict(map(None, *[iter(var)] * 2))
    print var
    # a = iter(var)
    # dict(zip(a, a))

dictionary(name)



def addDictionary(var1, var2):
     newDIct = dict(zip(var1, var2))
     print newDIct


    
       

addDictionary(name, favorite_animal)

