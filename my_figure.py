import numpy as np
import matplotlib.pyplot as plt

# fig = plt.figure()
# ax = plt.axes(projection='3d')
# ax.set_xlim(0, 15)
# ax.set_ylim(0, 15)
# ax.set_zlim(0, 15)

def cube():
    x1 = np.array([0, 0])
    y1 = np.array([0, 10])
    z1 = np.array([0, 0])
    x2 = np.array([0, 0])
    y2 = np.array([0, 0])
    z2 = np.array([0, 10])
    x3 = np.array([0, 10])
    y3 = np.array([0, 0])
    z3 = np.array([0, 0])
    x4 = np.array([10, 10])
    y4 = np.array([0, 10])
    z4 = np.array([0, 0])
    x5 = np.array([0, 0])
    y5 = np.array([10, 10])
    z5 = np.array([0, 10])
    x6 = np.array([10, 10])
    y6 = np.array([0, 10])
    z6 = np.array([10, 10])
    x7 = np.array([0, 10])
    y7 = np.array([10, 10])
    z7 = np.array([0, 0])
    x8 = np.array([10, 10])
    y8 = np.array([0, 0])
    z8 = np.array([10, 0])
    x9 = np.array([10, 10])
    y9 = np.array([10, 10])
    z9 = np.array([10, 0])
    x10 = np.array([0, 10])
    y10 = np.array([10, 10])
    z10 = np.array([10, 10])
    x11 = np.array([0, 0])
    y11 = np.array([0, 10])
    z11 = np.array([10, 10])
    x12 = np.array([0, 10])
    y12 = np.array([0, 0])
    z12 = np.array([10, 10])

    x = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12]
    y = [y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12]
    z = [z1, z2, z3, z4, z5, z6, z7, z8, z9, z10, z11, z12]

    a = (x,y,z)
    return a

# cub = cube()
#
# x=cub[0]
# y=cub[1]
# z=cub[2]
#
# for i in range(12):
#     ax.plot3D(x[i], y[i], z[i])
#
# plt.show()


