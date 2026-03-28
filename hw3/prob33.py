import numpy as np

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
