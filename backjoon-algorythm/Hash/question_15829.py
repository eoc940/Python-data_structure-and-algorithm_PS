# Hashing

import sys

n = int(sys.stdin.readline())
alpha = sys.stdin.readline()
hashing = dict()
result = 0
mod = 1234567891

for i in range(26) :
    hashing[chr(97+i)] = i+1

for j in range(n) :
    result += hashing.get(alpha[j])*(31**j)

print(result%mod)





