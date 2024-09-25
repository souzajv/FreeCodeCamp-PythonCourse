import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("a lista tem que ter 9 números")

    arr = np.array(lst).reshape(3, 3)

    mean_axis1 = np.mean(arr, axis=0).tolist()
    mean_axis2 = np.mean(arr, axis=1).tolist()
    mean_flat = np.mean(arr).tolist()

    var_axis1 = np.var(arr, axis=0).tolist()
    var_axis2 = np.var(arr, axis=1).tolist()
    var_flat = np.var(arr).tolist()

    std_axis1 = np.std(arr, axis=0).tolist()
    std_axis2 = np.std(arr, axis=1).tolist()
    std_flat = np.std(arr).tolist()

    max_axis1 = np.max(arr, axis=0).tolist()
    max_axis2 = np.max(arr, axis=1).tolist()
    max_flat = np.max(arr).tolist()

    min_axis1 = np.min(arr, axis=0).tolist()
    min_axis2 = np.min(arr, axis=1).tolist()
    min_flat = np.min(arr).tolist()

    sum_axis1 = np.sum(arr, axis=0).tolist()
    sum_axis2 = np.sum(arr, axis=1).tolist()
    sum_flat = np.sum(arr).tolist()

    return {
        'mean': [mean_axis1, mean_axis2, mean_flat],
        'variance': [var_axis1, var_axis2, var_flat],
        'standard deviation': [std_axis1, std_axis2, std_flat],
        'max': [max_axis1, max_axis2, max_flat],
        'min': [min_axis1, min_axis2, min_flat],
        'sum': [sum_axis1, sum_axis2, sum_flat]
    }

print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))
