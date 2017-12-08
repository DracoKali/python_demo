
L1 = (1, 'List', 2, 'is', 3, 'a', 4, 'compound', 5, 'data type', 6, 'in', 7, 'Python')


new_string = ""

output = ""

total = 0

for value in L1:
        if isinstance(value, int) or isinstance(value, float):
            total += value
            if output == "string":
                output = "The val you entered is mixed"
        else:
            output = "The value is a number"
            if isinstance(value, str):
                new_string = new_string + value
            else:
                if output == "number":
                    output = "mixed"
            if output == "It is a mixed string":
                output = output + value
print total
print "new_string" + new_string
print "output" + output

            




         
