import math
import numpy 

times = [41777096]
dists = [249136211271011]
# times = [7, 15, 30]
# dists = [9, 40, 200]

ways = []
for i in range(len(times)):
    t = times[i]
    d = dists[i]

    u = ( t + math.sqrt(t**2 - (4*d)))  / 2
    l = ( t - math.sqrt(t**2 - (4*d)))  / 2

    # Coerce to appropriate integer
    if u.is_integer():
        u = int(u-1)
    else:
        u = math.floor(u)
    
    if l.is_integer():
        l = int(l+1)
    else:
        l = math.ceil(l)

    print(u, l)
    ways.append( int(u - l + 1) )

print(ways)
print(numpy.prod(ways))