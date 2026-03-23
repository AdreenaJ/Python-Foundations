import numpy as np
import time

# 1. Generate 1,000 random marks (0-100)
grades = np.random.normal(70, 15, 1000)

start_time = time.time()

# 2. Vectorized Z-score calculation
mean = np.mean(grades)
std_dev = np.std(grades)
scores = (grades - mean) / std_dev

# 3. Scale to a 0-100 range (Optional Normalization)
normalized_grades = (scores * 10) + 75 

end_time = time.time()

print(f"Time taken: {end_time - start_time:.6f} seconds")
