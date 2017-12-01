from filterpy.kalman import ExtendedKalmanFilter
import numpy as np
f = ExtendedKalmanFilter (dim_x=1, dim_z=1)
z = None
def hj():
	j = 1
	return j
def hx():
	x = 1
	return x




f.x = np.array([[2.]])       # initial state (location and velocity)

f.F = np.array([[1.]])    # state transition matrix

f.H = np.array([[1.]])    # Measurement function
f.P *= 1000.                 # covariance matrix
f.R = 5                      # state uncertainty
f.Q = 0 # process uncertainty





while True:
    f.predict()
    i = input('input:')
    f.update(i)

    # do something with the output
    x = f.x
    print x