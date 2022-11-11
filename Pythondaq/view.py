import matplotlib.pyplot as plt
from diode_experiment import DiodeExperiment

Experiment_1 = DiodeExperiment()
measurement_1 = Experiment_1.scan(0,1023,3)
print(len(measurement_1[0]))
print(len(measurement_1[1]))
print(len(measurement_1[2]))
print(len(measurement_1[3]))
print(len(measurement_1[4]))
print(len(measurement_1[5]))

#plot the graph
plt.errorbar(x=measurement_1[0],y=measurement_1[1], xerr = measurement_1[3], yerr = measurement_1[4],fmt = "o")
plt.xlabel("U(V)")
plt.ylabel("I(A)")
plt.show()
