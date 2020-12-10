import numpy as np

arr = np.random.randint(0, 11, size=100)
print("input array: ", arr)
max_value = arr.max()
min_value = arr.min()
arr.sort()
middle_value = 0
sum = 0
for i in arr:
    sum += i
middle_value = sum/arr.shape[0]
median_value = arr[arr.shape[0]//2]
print("Minimal value: %.0f, maximal value: %.0f, middle value: %.2f, median value: %.0f" % (min_value, max_value,
                                                                                            middle_value, median_value))
