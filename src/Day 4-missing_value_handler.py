class MissingValueHandler:
    def __init__(self, data):
        self.data = data
        self.cleaned_data = None

    def validate_input(self):
        if not isinstance(self.data, list):
            raise TypeError("Input must be a list.")

        if len(self.data) == 0:
            raise ValueError("Input list cannot be empty.")

        for value in self.data:
            if value is not None and not isinstance(value, (int, float)):
                raise ValueError("Dataset contains invalid values.")

        return True

    def find_missing_indexes(self):
        return [index for index, value in enumerate(self.data)
                if value is None]

    def count_missing_values(self):
        return sum(1 for value in self.data if value is None)

    def calculate_mean(self):
        available_values = [
            value for value in self.data
            if value is not None
        ]

        if len(available_values) == 0:
            raise ValueError(
                "No valid values exist to calculate the mean."
            )

        total = 0

        for value in available_values:
            total += value

        mean = total / len(available_values)

        return mean

    def fill_missing_values(self):
        mean = self.calculate_mean()

        self.cleaned_data = []

        for value in self.data:
            if value is None:
                self.cleaned_data.append(mean)
            else:
                self.cleaned_data.append(value)

        return self.cleaned_data

    def display_report(self):
        missing_indexes = self.find_missing_indexes()
        missing_count = self.count_missing_values()
        mean = self.calculate_mean()
        cleaned_data = self.fill_missing_values()

        print("=" * 40)
        print("       MISSING VALUE REPORT")
        print("=" * 40)

        print("\nOriginal Data:")
        print(self.data)

        print("\nTotal Values       :", len(self.data))
        print("Missing Values     :", missing_count)
        print("Missing Indexes    :", missing_indexes)

        available_values = len(self.data) - missing_count
        print("Available Values   :", available_values)

        print("Mean               :", mean)

        print("\nCleaned Data:")
        print(cleaned_data)

        print("\n" + "=" * 40)


def main():
    data = [25, 30, None, 40, None, 35, 28]

    try:
        obj = MissingValueHandler(data)

        obj.validate_input()
        obj.display_report()

    except (TypeError, ValueError) as error:
        print("Error:", error)


if __name__ == "__main__":
    main()


            

