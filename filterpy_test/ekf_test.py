from filterpy.kalman import ExtendedKalmanFilter
import numpy as np
f = ExtendedKalmanFilter (dim_x=1, dim_z=1)
z = None
def hj(j):
	j = np.array([[0.]])
	return j
def hx(x):
	x = np.array([[0.]])
	return x




f.x = np.array([[-50.]])       # initial state (location and velocity)

f.F = np.array([[1.]])    # state transition matrix
#f.B = np.array([[1.]])
#f.K = 0.5
f.H = np.array([[1.]])    # Measurement function
f.P *= 10.                 # covariance matrix
f.R = 10                      # state uncertainty
f.Q = 3 # process uncertainty





while True:
    f.predict()
    i = input('input:')
    f.update(i, hj, hx)

    # do something with the output
    x = f.x
    print x