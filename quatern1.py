import numpy as np
import quaternion as quat
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlim(0, 15)
ax.set_ylim(0, 15)
ax.set_zlim(0, 15)

theta = 30
for i in range(111):
    q1 = np.quaternion(np.cos(np.pi * theta / 360 * i / 10), np.sin(np.pi * theta / 360 * i / 10), 0,
                       np.sin(np.pi * theta / 360 * i / 10))
    q2 = q1.inverse()

    x1 = np.array([0, 1])
    y1 = np.array([0, 5])
    z1 = np.array([0, 10])

    vec_start = np.array([x1[0], y1[0], z1[0]])
    vec_end = np.array([x1[1], y1[1], z1[1]])

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
    ax.plot3D(x1, y1, z1)
    plt.pause(0.01)

plt.show()
