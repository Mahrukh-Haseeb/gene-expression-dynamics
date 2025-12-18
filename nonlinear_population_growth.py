
#==============================Population Growth Model=======================================================

import numpy as np
import matplotlib.pyplot as plt


initial_population = 10
growth_rate = 0.3
carrying_capacity = 100
time_steps = 50


population = np.zeros(time_steps)
population[0] = initial_population
for t in range(1, time_steps):
    population[t] = population[t-1] + growth_rate * population[t-1] * (1 - population[t-1] / carrying_capacity)


plt.figure(figsize=(10, 6))
plt.plot(population, label='Population')
plt.xlabel('Time')
plt.ylabel('Population Size')
plt.title('Nonlinear Population Growth (Logistic Model)')
plt.axhline(y=carrying_capacity, color='r', linestyle='--', label='Carrying Capacity')
plt.legend()
plt.show()
