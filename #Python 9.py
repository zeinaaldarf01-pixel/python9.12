#Python 9.12
i = 1
while i <= 10:
 print(i)
 i += 1
 #task 2
 i = 10
while i >= 0:
 print(i)
i -= 1  
print("Blast off!")
#task3
password = input("Enter password: ")
while password != "python123":
 print("Wrong password, try again.")
 password = input("Enter password: ")
print("Access granted")