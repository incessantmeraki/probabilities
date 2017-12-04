import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

result = []
def throw_coin (number_of_samples, sample_size):
  for i in range(number_of_samples):
    trial = np.random.choice(['H','T'], size = sample_size)
    result.append(np.mean(trial == 'H'))
  return result

sample_sizes = np.arange(1,21,1)

trials = []
mean_of_sample_means = []
std_of_sample_means = []
for sample_size in sample_sizes:
  result = throw_coin(200,sample_size)
  trials.append(result)
  mean_of_sample_means.append(np.mean(result))
  std_of_sample_means.append(np.std(result))
  
# print(trials)
# print(mean_of_sample_means)
# print(std_of_sample_means)
  
# plt.hist(trials[0], alpha=0.3, label="100", bins=10)
# plt.hist(trials[1], alpha=0.5, label="1000", bins=10)
# plt.legend()

plt.title("Distribution for different sample sizes")
plt.plot(sample_sizes, std_of_sample_means, 'o-')
plt.xlabel("Sample size")
plt.ylabel("Probability")
# plt.title("Probability of Heads")
plt.show()
