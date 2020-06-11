import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

N = 50 # Size of the unit cell
matrix = np.random.randint(2, size=(N, N))

def neighbours (ii,jj):
    global matrix
    l = len(matrix)
    count = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if not (i==0 and j==0):
                x = ii + i
                y = jj + j
                # Periodic boundary conditions:
                x = x - int(np.floor(x/l))*l
                y = y - int(np.floor(y/l))*l
                count = count + matrix[x][y]
    return count

def step(dummy):
    global matrix
    l = len(matrix)
    matrix2 = matrix.copy()
    for i in range(l):
        for j in range(l):
                nn = neighbours(i, j)
                alive = matrix[i][j]
                if not alive and nn==3: #reproduction
                    matrix2[i][j] = 1
                if alive and (nn<2 or nn>3): #under- or overpopulation
                    matrix2[i][j] = 0
    mat.set_data(matrix2)
    matrix = matrix2
    return matrix2


# set up animation
fig, ax = plt.subplots(figsize=(8,8))
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
mat = ax.matshow(matrix)
ani = animation.FuncAnimation(fig, step, interval=50, save_count=50)
plt.show()
