import numpy as np

class fib:
    def __init__(self, maximum, devid, final):
        self.maximum = maximum
        self.devid = devid
        self.final = final

    def generate_array(self):
        # Local list to avoid global variable issues
        sequence = [0, 1]
        for i in range(2, self.final):
            sequence.append(sequence[i-1] + sequence[i-2])
        return np.array(sequence)

    def get_filtered_fibs(self):
        # 1. Generate the full array first
        fibnumb = self.generate_array()
        
        # 2. Find numbers smaller than maximum AND divisible by devid
        # We can use a boolean mask for a "Pythonic" and efficient way
        mask = (fibnumb < self.maximum) & (fibnumb % self.devid == 0)
        fib_fin = fibnumb[mask]
        
        return fib_fin

# --- Usage ---
# Example: Max value 1000, Divisible by 2 (even), up to the 20th Fibonacci number
f = fib(maximum=np.inf, devid=7, final=100)
results = f.get_filtered_fibs()

print(f"The Fibonacci numbers smaller than {f.maximum} and divisible by {f.devid} are:")
print(results)