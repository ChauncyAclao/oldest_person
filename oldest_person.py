#input name age
#validate name age
#store in array
#input another entry?
#find oldest person

entries = []

#iput another entry
while True:
#input name age
#validate name 
    name = input("Name: ")
    if not len(name) > 1:
        print("Try again")
        continue

#validate age
    age = input("age: ")
    if not (age.isdigit() and int(age) >= 1):
        print("Try again")
        continue
    
    entries.append({
        "name" : name,
        "age" : int(age)
    })

#for input another entry
    new_entry = input("Give another entry? (yes or no) ")
    if new_entry == "no":
        break

print(entries)
print()

if entries:
   oldest = max(entry['age'] for entry in entries)
print(oldest)


