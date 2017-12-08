# x = [4, 6, 1, 3, 5, 7, 25]
# x1 = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]



def draw_Star(var):
    for i in var:
        if isinstance(i, int):
            print (i * '*')
        elif isinstance(i, str):
            string = len(i)
            i = i[0].lower()
            print i * string

                    


draw_Star([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
)