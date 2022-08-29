import numpy as np
import matplotlib.pyplot as plt
from plane_rotation import draw_new
import quaternion as quat

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlim(0, 15)
ax.set_ylim(0, 15)
ax.set_zlim(0, 15)

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
theta = 30
for i in range(301):
    ax.clear()
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 15)
    ax.set_zlim(0, 15)
    x = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12]
    y = [y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12]
    z = [z1, z2, z3, z4, z5, z6, z7, z8, z9, z10, z11, z12]

    for j in range(12):
        q1 = np.quaternion(np.cos(np.pi * theta / 360 * i / 10), np.sin(np.pi * theta / 360 * i / 10), 0,
                           np.sin(np.pi * theta / 360 * i / 10))
        q2 = q1.inverse()


        vec_start = np.array([x[j][0], y[j][0], z[j][0]])
        vec_end = np.array([x[j][1], y[j][1], z[j][1]])

        a_qt_start = quat.from_vector_part(vec_start, vector_axis=-1)
        a_qt_end = quat.from_vector_part(vec_end, vector_axis=-1)

        q_start_new = q1 * a_qt_start * q2
        q_end_new = q1 * a_qt_end * q2

        vec_start_new = quat.as_vector_part(q_start_new)
        vec_end_new = quat.as_vector_part(q_end_new)

        x_new = np.array([vec_start_new[0], vec_end_new[0]])
        y_new = np.array([vec_start_new[1], vec_end_new[1]])
        z_new = np.array([vec_start_new[2], vec_end_new[2]])

        ax.plot3D(x_new, y_new, z_new)
    plt.pause(0.01)
plt.show()
