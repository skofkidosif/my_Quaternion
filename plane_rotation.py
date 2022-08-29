import numpy as np
import quaternion
import matplotlib.pyplot as plt



# x1 = np.array([0, 0])
# y1 = np.array([0, 10])
# z1 = np.array([0, 0])




def mat_x(alpha):
    m_x = np.matrix([[1, 0, 0], [0, np.cos(alpha), -np.sin(alpha)], [0, np.sin(alpha), np.cos(alpha)]])
    return m_x


def mat_y(alpha):
    m_y = np.matrix([[np.cos(alpha), 0, np.sin(alpha)], [0, 1, 0], [-np.sin(alpha), 0, np.cos(alpha)]])
    return m_y


def mat_z(alpha):
    m_z = np.matrix([[np.cos(alpha), -np.sin(alpha), 0], [np.sin(alpha), np.cos(alpha), 0], [0, 0, 1]])
    return m_z

def draw_new(angle_x,angle_y,angle_z,a,b,c):
    def vec_col(x, y, z):
        p_start = (x[0], y[0], z[0])
        p_end = (x[1], y[1], z[1])
        p_start_arr = np.asarray(p_start)
        p_end_arr = np.asarray(p_end)
        p_start_arr_t = np.array([p_start_arr]).T
        p_end_arr_t = np.array([p_end_arr]).T
        A = (p_start_arr_t, p_end_arr_t)
        return (A)
    phi_x = angle_x * np.pi / 180
    phi_y = angle_y * np.pi / 180
    phi_z = angle_z * np.pi / 180
    p_start_arr_t_new = mat_x(phi_x) * mat_y(phi_y)*mat_z(phi_z)*vec_col(a,b,c)[0]
    p_start_arr_new = np.ravel(p_start_arr_t_new.T)
    p_end_arr_t_new = mat_x(phi_x) * mat_y(phi_y)*mat_z(phi_z)*vec_col(a,b,c)[1]
    p_end_arr_new = np.ravel(p_end_arr_t_new.T)


    x_new = np.array([p_start_arr_new[0], p_end_arr_new[0]])
    y_new = np.array([p_start_arr_new[1], p_end_arr_new[1]])
    z_new = np.array([p_start_arr_new[2], p_end_arr_new[2]])
    B=(x_new,y_new,z_new)
    return (B)



#draw_new(90,0,0,x1,y1,z1)