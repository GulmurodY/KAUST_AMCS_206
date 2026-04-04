import numpy as np
import matplotlib.pyplot as plt
import os


n = 10   # number of lamps
lamps = np.array([  # x, y positions of lamps and height above floor
    [ 4.1, 20.4, 4  ],
    [14.1, 21.3, 3.5],
    [22.6, 17.1, 6  ],
    [ 5.5, 12.3, 4.0],
    [12.2,  9.7, 4.0],
    [15.3, 13.8, 6  ],
    [21.3, 10.5, 5.5],
    [ 3.9,  3.3, 5.0],
    [13.1,  4.3, 5.0],
    [20.3,  4.2, 4.5],
])

N = 25     # grid size
m = N * N  # number of pixels

# If we number the pixels lexicographically in columns starting from the
# bottom left cell going upwards in every column, then the x and y
# coordinates of pixel number k (1-indexed) will be:
# (note that x-axis corresponds to j index, and the y-axis is i index)
# x = floor((k-1) / N) + 0.5
# y = mod(k-1, N) + 0.5

k = np.arange(1, m + 1)
px = np.floor((k - 1) / N) + 0.5
py = ((k - 1) % N) + 0.5

A = np.zeros((m, n))

for j in range(n):
    dx = px - lamps[j, 0]
    dy = py - lamps[j, 1]
    dz = lamps[j, 2]         
    d_sq = dx**2 + dy**2 + dz**2
    A[:, j] = 1.0 / d_sq


target = np.ones(m)

Q, R = np.linalg.qr(A, mode='reduced')
p_opt = np.linalg.solve(R, Q.T @ target)

l_opt = A @ p_opt
RMS = np.linalg.norm(l_opt - target) / np.sqrt(m)

for i in range(n):
    print(f"Lamp {i+1}: power = {p_opt[i]}")
print(f"\nRMS error: {RMS:.6f}")

L = l_opt.reshape(N, N, order='F') 

plt.figure(figsize=(8, 7))
plt.imshow(L, origin='lower', extent=[0, 25, 0, 25], cmap='hot')
plt.colorbar(label='Illumination level')
plt.scatter(lamps[:, 0], lamps[:, 1], c='blue', s=50, zorder=5)
for i in range(n):
    plt.annotate(f'{i+1} ({lamps[i,2]}m)',
                 (lamps[i,0], lamps[i,1]), color='white', fontweight='bold')
plt.title(f'Optimized Illumination\nRMS = {RMS}')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plot_dir = os.path.join(os.path.dirname(__file__), 'plots')
plot_path = os.path.join(plot_dir, f'prob33.png')
plt.savefig(plot_path, dpi=200, bbox_inches='tight')
plt.show()

"""
output:
Lamp 1: power = 15.236535802965893
Lamp 2: power = 8.211418810166986
Lamp 3: power = 30.91273147036235
Lamp 4: power = 7.748793414469892
Lamp 5: power = 0.8667427693315101
Lamp 6: power = 2.2158990322106815
Lamp 7: power = 2.2111536907406815
Lamp 8: power = 21.374854370592864
Lamp 9: power = 9.458061471794759
Lamp 10: power = 15.341937827396489

RMS error: 0.140390
"""