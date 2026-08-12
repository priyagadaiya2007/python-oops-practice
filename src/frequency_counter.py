class FrequencyCounter:
    def __init__(self, numbers):
        self.numbers = numbers

    def validate_input(self):
        if not isinstance(self.numbers, list):
            raise TypeError("Input must be a list.")

        if len(self.numbers) == 0:
            raise ValueError("Input list cannot be empty.")

    def count_frequency(self):
        frequency = {}

        for value in self.numbers:
            if value in frequency:
                frequency[value] += 1
            else:
                frequency[value] = 1

        return frequency

    def display_result(self):
        result = self.count_frequency()

        print("Input List :", self.numbers)
        print("Frequency  :", result)


def main():
    try:
        numbers = [1, 2, 2, 3, 1, 5, 4, 2, 5, 5]

        obj = FrequencyCounter(numbers)

        obj.validate_input()

        obj.display_result()

    except Exception as e:
        print("Error -", e)


if __name__ == "__main__":
    main()
