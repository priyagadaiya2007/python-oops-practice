from typing import List, Any
class StatisticalAnalyzer:
    def __init__(self, numbers: 
                 List[Any]):
        self.numbers = numbers

    def validate_input(self) -> None:
        if not isinstance(self.numbers, list):
            raise TypeError("Input must be a list of numerical values.")
        if len(self.numbers) == 0:
            raise ValueError("Input list must not be empty.")

        for i, val in enumerate(self.numbers):
            if isinstance(val, bool) or not isinstance(val, (int, float)):
                raise TypeError("Input must contain only numerical values.")

    def calculate_mean(self) -> float:
        n = len(self.numbers)
        total = 0.0
        for val in self.numbers:
            total += float(val)
        return total / n

    def calculate_median(self) -> float:
        sorted_vals = sorted(self.numbers)
        n = len(sorted_vals)
        mid = n // 2
        if n % 2 == 1:
            return float(sorted_vals[mid])
        else:
            return (float(sorted_vals[mid - 1]) + float(sorted_vals[mid])) / 2.0

    def calculate_mode(self):
        freq = {}
        for val in self.numbers:
            freq[val] = freq.get(val, 0) + 1

        max_count = max(freq.values())
        if max_count == 1:
            return "No unique mode"

        modes = [val for val, cnt in freq.items() if cnt == max_count]
        if len(modes) == 1:
            return modes[0]
        return sorted(modes)

    def find_minimum(self) -> float:
        return min(self.numbers)

    def find_maximum(self) -> float:
        return max(self.numbers)

    def count_unique_values(self) -> int:
        return len(set(self.numbers))

    # Bonus methods
    def calculate_range(self) -> float:
        return self.find_maximum() - self.find_minimum()

    def calculate_variance(self) -> float:
        # population variance
        mean = self.calculate_mean()
        n = len(self.numbers)
        s = 0.0
        for x in self.numbers:
            diff = float(x) - mean
            s += diff * diff
        return s / n

    def display_result(self) -> None:
        mean = self.calculate_mean()
        median = self.calculate_median()
        mode = self.calculate_mode()
        minimum = self.find_minimum()
        maximum = self.find_maximum()
        unique_count = self.count_unique_values()

        print("================================")
        print("\n       STATISTICAL REPORT\n")
        print("================================\n")
        print(f"Original Data : {self.numbers}\n")
        print(f"Mean          : {mean:.2f}\n")
        print(f"Median        : {median}\n")
        # Mode formatting
        if isinstance(mode, list):
            print(f"Mode          : {mode}\n")
        else:
            print(f"Mode          : {mode}\n")

        print(f"Minimum       : {minimum}\n")
        print(f"Maximum       : {maximum}\n")
        print(f"Unique Values : {unique_count}\n")
        # Bonus outputs
        try:
            r = self.calculate_range()
            v = self.calculate_variance()
            print(f"Range         : {r}\n")
            print(f"Variance      : {v:.4f}\n")
        except Exception:
            pass

        print("================================")


def main() -> None:
    numbers = [10, 20, 20, 30, 40, 50]
    analyzer = StatisticalAnalyzer(numbers)
    try:
        analyzer.validate_input()
        analyzer.display_result()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
