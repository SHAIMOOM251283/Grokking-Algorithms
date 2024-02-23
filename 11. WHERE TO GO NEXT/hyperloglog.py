import math
import hashlib

class HyperLogLog:
    def __init__(self, num_buckets):
        self.num_buckets = num_buckets
        self.registers = [0] * num_buckets

    def add(self, element):
        hash_value = hashlib.md5(str(element).encode()).digest()
        hash_int = int.from_bytes(hash_value, byteorder='big')
        bucket = hash_int % self.num_buckets
        trailing_zeros = self._count_trailing_zeros(hash_int >> (self.num_buckets.bit_length() - 1))
        self.registers[bucket] = max(self.registers[bucket], trailing_zeros)

    def count(self):
        alpha = self._calculate_alpha(self.num_buckets)
        estimate = alpha * (self.num_buckets ** 2) / sum(2 ** (-register) for register in self.registers)
        if estimate <= 2.5 * self.num_buckets:
            # Small range correction
            zeros = self.registers.count(0)
            if zeros != 0:
                corrected_estimate = self.num_buckets * math.log(self.num_buckets / zeros)
            else:
                corrected_estimate = estimate
        elif estimate <= (1 / 30) * (2 ** 32):
            # No correction needed
            corrected_estimate = estimate
        else:
            # Large range correction
            corrected_estimate = - (2 ** 32) * math.log(1 - (estimate / (2 ** 32)))
        return int(corrected_estimate)

    def _count_trailing_zeros(self, num):
        count = 0
        while num & 1 == 0:
            count += 1
            num >>= 1
        return count

    def _calculate_alpha(self, num_buckets):
        if num_buckets == 16:
            return 0.673
        elif num_buckets == 32:
            return 0.697
        elif num_buckets == 64:
            return 0.709
        else:
            return 0.7213 / (1 + 1.079 / num_buckets)

# Example usage:
hll = HyperLogLog(16)
elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for element in elements:
    hll.add(element)

print("Estimated count:", hll.count())
