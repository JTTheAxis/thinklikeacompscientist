eng2sp={"one":"uno", "two":"dos"}
for k in eng2sp.keys():   # The order of the k's is not defined
   print("Got key", k, "which maps to value", eng2sp[k])

ks = list(eng2sp.keys())
#print(ks)

for (k,v) in eng2sp.items():
   print("Got",k,"that maps to",v)
   
matrix = [[0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0],
          [0, 2, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 3, 0]]

alreadyknown = {0: 0, 1: 1}

def fib(n):
   if n not in alreadyknown:
      new_value = fib(n-1) + fib(n-2)
      alreadyknown[n] = new_value
   return alreadyknown[n]

print(fib(1000))