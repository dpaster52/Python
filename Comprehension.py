#Dominique Paster
#List Comprehension Practice

import sys

X = int(sys.stdin.readline())
Y = int(sys.stdin.readline())
Z = int(sys.stdin.readline())
N = int(sys.stdin.readline())
listComprehension = [[x,y,z] for x in range(X+1) for y in range(Y+1) for z in range(Z+1) if x+y+z != N]
sys.stdout.write(str(listComprehension))