#Modify your code so that it normalizes the output for 
#the function sense. This means that the entries in q 
#should sum to one.


p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q=[]
    total = 0
    for i in range(len(p)):
        hit = (Z == world[i])
        unnormalized_probability = p[i] * (hit * pHit + (1-hit) * pMiss)
        total += unnormalized_probability
        q.append(unnormalized_probability)
    for i in range(len(q)):
        q[i]/=float(total)
    return q
print sense(p,Z)
