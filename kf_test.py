from filterpy.kalman import KalmanFilter
import numpy as np
f = KalmanFilter (dim_x=1, dim_z=1)
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