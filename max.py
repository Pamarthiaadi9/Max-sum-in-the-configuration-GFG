def max_sum(a, n):
    # Calculate the initial sum and initialize the result
    current_sum = sum(i * a[i] for i in range(n))
    max_sum = current_sum
    
    # Initialize the sum of array elements
    array_sum = sum(a)
    
    # Iterate through each rotation
    for i in range(1, n):
        current_sum += array_sum - n * a[n - i]
        max_sum = max(max_sum, current_sum)
    
    return max_sum
