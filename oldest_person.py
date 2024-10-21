#input name age
#validate name age
#store in array
#input another entry?
#find oldest person

#iput another entry
while True:
    #input name age
    #validate name
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

#for another entry
    except:
        print("Invalid Retry")

    new_entry = input("Give another entry? (yes or no) ")
    if new_entry == "no":
            break


        
        
