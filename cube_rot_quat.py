import numpy as np
import matplotlib.pyplot as plt
import quaternion as quat
from my_figure import cube

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlim(0, 15)
ax.set_ylim(0, 15)
ax.set_zlim(0, 15)


theta = 30
for i in range(301):
    ax.clear()
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 15)
    ax.set_zlim(0, 15)

    cub = cube()
    x = cub[0]
    y = cub[1]
    z = cub[2]

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
