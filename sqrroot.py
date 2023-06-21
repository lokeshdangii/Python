m=36
e=0.001

g1 = 9
cv = m/g1
g2 = (g1+cv)/2

while (g1-g2 <= e):
	g2 = (g1+cv)/2
	g1 = g2

print(g2)

