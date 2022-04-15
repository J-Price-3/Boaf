import matplotlib.pyplot as plt

positionHistory = open("positions.txt", "r")
velocityHistory = open("velocities.txt", "r")

positions = positionHistory.readlines()
c = 0
for p in positions:
    p = p.strip("\n").strip('(').strip(')').split(", ")
    p = [float(p[0]), float(p[1])]
    positions[c] = p
    c += 1

velocities = velocityHistory.readlines()
c = 0
for p in velocities:
    p = p.strip("\n").strip('(').strip(')').split(", ")
    p = (float(p[0]), float(p[1]))
    velocities[c] = p
    c += 1

pX = []
pY = []
for p in positions:
    pX.append(p[0])
    pY.append(p[1])

vX = []
vY = []
for v in velocities:
    vX.append(v[0])
    vY.append(v[1])

plt.plot(pX, pY, marker='o')
plt.title("Positions")
plt.show()

plt.plot(vX, vY, marker='o')
plt.title("Velocities")
plt.show()