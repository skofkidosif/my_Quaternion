import matplotlib.pyplot as plt
from def_mat_rotation import draw_new
from my_figure import cube

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlim(0, 15)
ax.set_ylim(0, 15)
ax.set_zlim(0, 15)

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
        r = draw_new(0, 90 * i / 10, 0, x[j], y[j], z[j])
        ax.plot3D(r[0], r[1], r[2])
    plt.pause(0.01)

plt.show()

