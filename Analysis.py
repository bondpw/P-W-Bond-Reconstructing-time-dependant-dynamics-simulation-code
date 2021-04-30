import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "cursive"

xData = np.load("xData.npy",allow_pickle = True)
pData = np.load("pData.npy", allow_pickle = True)
timeData = np.load("timedata.npy", allow_pickle = True)

plt.plot(timeData, xData, label = "x(t)")
plt.xlabel("Time/s")
plt.ylabel("Component Position")
plt.rcParams.update({'font.size': 22})
plt.show()

plt.plot(timeData, pData, label = "p(t)")
plt.xlabel("Time/s")
plt.ylabel("Component Position")

plt.show()