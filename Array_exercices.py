import numpy as np

arr = np.random.randint(0, 11, size=100)
print("input array: ", arr)
max_value = arr.max()
min_value = arr.min()
arr.sort()
sum = 0
for i in arr:
    sum += i
avr_value = sum / arr.shape[0]
median_value = arr[arr.shape[0]//2]
print("Minimal value: %.0f, maximal value: %.0f, average value: %.2f, median value: %.0f" % (min_value, max_value,
                                                                                            avr_value, median_value))
