N = int(input())

planet = []
for i in range(N):
    planet.append( (i,)+ tuple( map(int,input().split())) )
# Tree.sort(key = lambda x:x[0])
# print(planet)

px = [item[:] for item in planet]
px.sort(key=lambda x:x[1])

py = [item[:] for item in planet]
py.sort(key=lambda x:x[2])

pz = [item[:] for item in planet]
pz.sort(key=lambda x:x[3])

edges = []
# edge = ( distance, node1, node2 )
for i in range(len(px)-1):
    edge = ( abs(px[i+1][1] - px[i][1]) , px[i][0] , px[i+1][0]  )  
    edges.append( edge )
    
for i in range(len(py)-1):
    edge = ( abs(py[i+1][2] - py[i][2]) , py[i][0] , py[i+1][0]  )  
    edges.append( edge )
    
for i in range(len(pz)-1):
    edge = ( abs(pz[i+1][3] - pz[i][3]) , pz[i][0] , pz[i+1][0]  )  
    edges.append( edge )

edges.sort(key=lambda x:x[0])

parent = [i for i in range(N)]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

answer= 0 
for w, s, e in edges:
    sRoot = find(s)
    eRoot = find(e)
    if sRoot != eRoot:
        if sRoot > eRoot:
            parent[sRoot] = eRoot
        else:
            parent[eRoot] = sRoot
        answer += w

print(answer)