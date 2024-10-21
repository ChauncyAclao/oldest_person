#input name age
#validate name age
#store in array
#input another entry?
#find oldest person

#input name age

#validate name
while True:
    try:
        while True:
            name = input("Name: ")

            if len(name) >1:
             break

#validate age
        while True:
            age = int(input("age "))

            if age > 0 :
                break
    except:
        print("try again")


