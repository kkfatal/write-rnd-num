import numpy as np

n=0
while 1:
	s = np.random.normal(0, 5, 10000000)
	np.save(str(n)+".npy",s)
	n=n+1

print("End")
