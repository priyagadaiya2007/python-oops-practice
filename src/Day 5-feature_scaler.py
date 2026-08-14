class FeatureScaler:
    def __init__(self, data):
        self.data = data
        self.scaled_data = []

    def validate_input(self):
        if not isinstance(self.data, list):
            raise ValueError("Input must be a list.")

        if len(self.data) == 0:
            raise ValueError("Input list cannot be empty.")

        for value in self.data:
            if value is None or not isinstance(value, (int, float)):
                raise ValueError("Dataset contains invalid values.")

        return True

    def find_minimum(self):
        return min(self.data)

    def find_maximum(self):
        return max(self.data)

    def scale_data(self):
        minimum = self.find_minimum()
        maximum = self.find_maximum()

        if minimum == maximum:
            raise ValueError(
                "Cannot scale data because all values are identical."
            )

        self.scaled_data = [
            (value - minimum) / (maximum - minimum)
            for value in self.data
        ]

        return self.scaled_data

    def display_report(self):
        minimum = self.find_minimum()
        maximum = self.find_maximum()

        self.scale_data()

        print("=" * 40)
        print("FEATURE SCALING REPORT")
        print("=" * 40)

        print()
        print("Original Data :", self.data)
        print()
        print("Minimum       :", minimum)
        print("Maximum       :", maximum)
        print()
        print("Scaled Data   :", self.scaled_data)
        print()
        print("=" * 40)


def main():
    data = [10, 20, 30, 40, 50]

    try:
        obj = FeatureScaler(data)

        obj.validate_input()
        obj.display_report()

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()