#Dominique Paster
#Create and hash tuple
'''Tuples are immutable so they are great when values cannot be changed
They can also be hashed'''

import sys

tuples = int(sys.stdin.readline())
t = ()
num = sys.stdin.readline().split()
for x in range(0,tuples):
    t = t + (int(num[x]),)
sys.stdout.write(str(hash(t)))