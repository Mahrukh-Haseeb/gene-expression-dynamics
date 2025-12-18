
#======================Stochastic Gene Expression===================
import numpy as np
import matplotlib.pyplot as plt


num_cells = 10
time_steps = 100
prob_transcription = 0.1  


protein_levels = np.zeros((num_cells, time_steps))
for cell in range(num_cells):
    for t in range(1, time_steps):
        if np.random.rand() < prob_transcription:
            protein_levels[cell, t] = protein_levels[cell, t-1] + 1
        else:
            protein_levels[cell, t] = protein_levels[cell, t-1]


plt.figure(figsize=(10, 6))
for i in range(num_cells):
    plt.plot(protein_levels[i], label=f'Cell {i+1}')
plt.xlabel('Time')
plt.ylabel('Protein Level')
plt.title('Stochastic Gene Expression in 10 Cells')
plt.legend()
plt.show()
