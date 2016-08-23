#Dominique Paster
#Manipulate List based on input 
'''
input
12
insert 0 5
insert 1 10
insert 0 6
print 
remove 6
append 9
append 1
sort 
print
pop
reverse
print

output
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''
import sys

L = []
for command in sys.stdin:
    commandParts = command.split()
    if commandParts[0] == "insert":
        L.insert(int(commandParts[1]),int(commandParts[2]))
    elif commandParts[0] == "reverse":
        L.reverse()
    elif commandParts[0] == "pop":
        L.pop()
    elif commandParts[0] == "print":
        length = len(L)
        sys.stdout.write("[")
        for item in L:
            length -=1
            if length >0:
                sys.stdout.write(str(item)+", ")
            else:
                sys.stdout.write(str(item))       
        sys.stdout.write("]\n")     
    elif commandParts[0] =="sort":
        L.sort()
    elif commandParts[0] == "remove":
        L.remove(int(commandParts[1]))
    elif commandParts[0] == "append":
        L.append(int(commandParts[1]))
    elif int(command)>0:
        continue
    else:
        sys.stdout.write("Invalid Command")

