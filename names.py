students = [
     {'first_name':  'Michael', 'last_name': 'Jordan'},
     {'first_name': 'John', 'last_name': 'Rosales'},
     {'first_name': 'Mark', 'last_name': 'Guillen'},
     {'first_name': 'KB', 'last_name': 'Tonel'}
 ]

def person_type(x):
    for student in x:
        print student['first_name'], student['last_name']


person_type(students)



users = {
 'Students': [
     {'first_name':  'Michael', 'last_name': 'Jordan'},
     {'first_name': 'John', 'last_name': 'Rosales'},
     {'first_name': 'Mark', 'last_name': 'Guillen'},
     {'first_name': 'KB', 'last_name': 'Tonel'}
  ],
 'Instructors': [
     {'first_name': 'Michael', 'last_name': 'Choi'},
     {'first_name': 'Martin', 'last_name': 'Puryear'}
  ]
 }
def studentTeacher(y):
    for i in users:
        counter = 0
        print i
        for person in users[i]:
            counter += 1
            first_name = person['first_name'].upper()
            last_name = person['last_name'].upper()
            length = len(first_name) + len(last_name)
            print "{} - {} {} - {}".format(counter, first_name, last_name, length)
                   



studentTeacher(users)

        


    

            
        
    