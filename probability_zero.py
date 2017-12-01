import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def throw_coin (size = 10):
  return np.random.choice(['H','T'], size = size)



trials = [10, 30, 50, 70, 100, 130, 170, 200, 500, 1000, 2000, 5000, 10000]
trials = sorted(trials)

probabilities = []
for trial in trials:
  result = throw_coin(trial)
  # print('Total no of heads', np.sum(result=='H'))
  # print('probability of head', np.mean(result=='H'))
  probabilities.append(np.mean(result=='H'))
  
plt.plot(trials, probabilities, 'o-')
plt.xlabel("Number of trials")
plt.ylabel("Probability")
plt.title("Probability of Heads")
plt.show()
