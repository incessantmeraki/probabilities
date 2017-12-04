import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

result = []
def throw_coin (number_of_samples, sample_sizes):
  for i in range(number_of_samples):
    trial = np.random.choice(['H','T'], size = sample_sizes)
    result.append(np.mean(trial == 'H'))
  return result

sample_sizes = np.arange(1,1001,1)

probabilities = throw_coin(20,10)
print(probabilities)
  
# plt.plot(trials, probabilities, 'o-')
# plt.xlabel("Number of trials")
# plt.ylabel("Probability")
# plt.title("Probability of Heads")
# plt.show()
