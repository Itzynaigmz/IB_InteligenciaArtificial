name = input("Enter your name: ")
lastname = input("Enter your lastname: ")
name1 = "Ana"
name2 = "John"
name3 = "Doe"

if name == name1 or name2 or name3:
    print("*my    *")
    print("*is   *")
    print("*",name,"*")
    print("*",lastname,"*")
    print("*******")
else:
    print("*******")
    print("*Hi    *")
    print("*my    *")
    print("*is   *")
    print("*",name,"*")
    print("*",lastname,"*")
    print("*******")


list = []
list.append(lastname)
list.append(name)
print(list)

