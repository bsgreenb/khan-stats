from math import sqrt

def get_mean(num_arr):
    total = 0
    for num in num_arr:
        total += num
    
    return total / len(num_arr)

def get_variance(num_arr):
    mean = get_mean(num_arr)

    sum_squares = 0
    for num in num_arr:
        sum_squares += (num - mean) ** 2

    return sum_squares / len(num_arr)

def sample_variance(num_arr):
    mean = get_mean(num_arr)

    sum_squares = 0
    for num in num_arr:
        sum_squares += (num - mean) ** 2

    return sum_squares / (len(num_arr) - 1)

# Implemented as numpy.std
def stddev(num_arr):
    variance = get_variance(num_arr)

    return sqrt(variance)

def sample_stddev(num_arr):
    variance = sample_variance(num_arr)

    return sqrt(variance)

def z_score(mean, std, amount):
    mean_distance = amount - mean

    return mean_distance / std

print(z_score(81, 6.3, 65))
print(z_score(81, 6.3, 83))
print(z_score(81, 6.3, 93))
print(z_score(81, 6.3, 100))