import filterpy.kalman

dim_x = 1
dim_z = 1
x = 1
dt = 0.35

def hx(x):
	return x

def fx(x, dt):
	return x


filter = UnscentedKalmanFilter(dim_x, dim_z, dt, hx, fx, points)