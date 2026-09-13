import pandas as pd


class PandasDataAnalyzer:

    def __init__(self, data):
        self.data = data
        self.df = None
        self.cleaned_df = None

    def create_dataframe(self):
        try:
            self.df = pd.DataFrame(
                self.data,
                columns=[
                    "Customer",
                    "Age",
                    "Income",
                    "Experience",
                    "Purchased"
                ]
            )
            return self.df
        except Exception as e:
            raise ValueError(f"Error creating DataFrame: {e}")

    def validate_input(self):
        if not isinstance(self.data, list):
            raise TypeError("Dataset must be a list.")

        if len(self.data) == 0:
            raise ValueError("Dataset cannot be empty.")

        required_columns = {
            "Customer",
            "Age",
            "Income",
            "Experience",
            "Purchased"
        }

        if self.df is None:
            self.create_dataframe()

        if set(self.df.columns) != required_columns:
            raise ValueError("Required columns are missing.")

        record_length = len(self.data[0])

        for record in self.data:
            if not isinstance(record, (list, tuple)):
                raise TypeError("Each record must be a list or tuple.")

            if len(record) != record_length:
                raise ValueError("All records must have consistent columns.")

        return True

    def get_dataset_info(self):
        print("\n--- DATASET INFORMATION ---")
        print("Rows:", self.df.shape[0])
        print("Columns:", self.df.shape[1])
        print("Column Names:", list(self.df.columns))
        print("Data Types:")
        print(self.df.dtypes)
        print("Shape:", self.df.shape)

    def find_missing_values(self):
        missing = self.df.isnull()
        print("\n--- MISSING VALUES ---")
        print(missing)
        return missing

    def count_missing_values(self):
        missing_count = self.df.isnull().sum()
        print("\nMissing values in each column:")
        print(missing_count)

        return missing_count

    def find_duplicates(self):
        duplicate_count = self.df.duplicated().sum()

        print("\n--- DUPLICATES ---")
        print("Duplicate Records:", duplicate_count)

        return duplicate_count

    def remove_duplicates(self):
        self.cleaned_df = self.df.drop_duplicates().copy()

        print("\n--- AFTER REMOVING DUPLICATES ---")
        print(self.cleaned_df)

        return self.cleaned_df

    def fill_missing_values(self):
        if self.cleaned_df is None:
            self.remove_duplicates()

        income_mean = self.cleaned_df["Income"].mean()

        self.cleaned_df["Income"] = self.cleaned_df["Income"].fillna(
            income_mean
        )

        print("\n--- AFTER FILLING MISSING INCOME ---")
        print(self.cleaned_df)

        return self.cleaned_df

    def filter_customers(self, min_income):
        if self.cleaned_df is None:
            self.fill_missing_values()

        filtered = self.cleaned_df[
            self.cleaned_df["Income"] >= min_income
        ]

        print(f"\n--- CUSTOMERS WITH INCOME >= {min_income} ---")
        print(filtered)

        return filtered

    def sort_by_income(self, ascending=True):
        if self.cleaned_df is None:
            self.fill_missing_values()

        sorted_df = self.cleaned_df.sort_values(
            by="Income",
            ascending=ascending
        )

        print("\n--- SORTED BY INCOME ---")
        print(sorted_df)

        return sorted_df

    def calculate_statistics(self):
        if self.cleaned_df is None:
            self.fill_missing_values()

        numerical_columns = [
            "Age",
            "Income",
            "Experience",
            "Purchased"
        ]

        statistics = self.cleaned_df[numerical_columns].agg(
            ["mean", "min", "max", "std"]
        )

        print("\n--- NUMERICAL STATISTICS ---")
        print(statistics)

        return statistics

    def analyze_features(self):
        if self.cleaned_df is None:
            self.fill_missing_values()

        features = [
            "Age",
            "Income",
            "Experience",
            "Purchased"
        ]

        print("\n--- FEATURE ANALYSIS ---")

        for feature in features:
            print(f"\n{feature}:")
            print("Mean:", self.cleaned_df[feature].mean())
            print("Minimum:", self.cleaned_df[feature].min())
            print("Maximum:", self.cleaned_df[feature].max())
            print("Standard Deviation:", self.cleaned_df[feature].std())

    def analyze_target(self):
        if self.cleaned_df is None:
            self.fill_missing_values()

        purchased_count = (
            self.cleaned_df["Purchased"] == 1
        ).sum()

        not_purchased_count = (
            self.cleaned_df["Purchased"] == 0
        ).sum()

        print("\n--- PURCHASE ANALYSIS ---")
        print("Purchased:", purchased_count)
        print("Not Purchased:", not_purchased_count)

        return purchased_count, not_purchased_count

    def perform_eda(self):
        if self.cleaned_df is None:
            self.fill_missing_values()

        customer_count = len(self.cleaned_df)
        average_age = self.cleaned_df["Age"].mean()
        average_income = self.cleaned_df["Income"].mean()
        highest_income = self.cleaned_df["Income"].max()
        average_experience = self.cleaned_df["Experience"].mean()
        number_of_purchasers = (
            self.cleaned_df["Purchased"] == 1
        ).sum()

        print("\n--- EDA REPORT ---")
        print("Customer Count:", customer_count)
        print("Average Age:", average_age)
        print("Average Income:", average_income)
        print("Highest Income:", highest_income)
        print("Average Experience:", average_experience)
        print("Number of Purchasers:", number_of_purchasers)

    def group_by_purchase_status(self):
        if self.cleaned_df is None:
            self.fill_missing_values()

        result = self.cleaned_df.groupby("Purchased").agg(
            Customer_Count=("Customer", "count"),
            Average_Age=("Age", "mean"),
            Average_Income=("Income", "mean"),
            Average_Experience=("Experience", "mean")
        )

        print("\n--- GROUP BY PURCHASE STATUS ---")
        print(result)

        return result

    def display_report(self):
        if self.cleaned_df is None:
            self.fill_missing_values()

        print("\n" + "=" * 50)
        print("CUSTOMER DATA ANALYSIS")
        print("=" * 50)

        print("Original Dataset Shape:", self.df.shape)

        missing_income = self.df["Income"].isnull().sum()
        duplicate_records = self.df.duplicated().sum()

        print("Missing Income Values:", missing_income)
        print("Duplicate Records:", duplicate_records)
        print("Rows After Cleaning:", len(self.cleaned_df))

        self.calculate_statistics()
        self.analyze_target()

        print("=" * 50)


def main():

    data = [
        ["C001", 25, 30000, 2, 0],
        ["C002", 30, 45000, 5, 1],
        ["C003", 35, None, 8, 1],
        ["C004", 40, 80000, 12, 1],
        ["C005", 45, 100000, 15, 0],
        ["C002", 30, 45000, 5, 1]
    ]

    analyzer = PandasDataAnalyzer(data)

    try:
        analyzer.create_dataframe()
        analyzer.validate_input()

        analyzer.get_dataset_info()

        analyzer.find_missing_values()
        analyzer.count_missing_values()

        analyzer.find_duplicates()
        analyzer.remove_duplicates()

        analyzer.fill_missing_values()

        analyzer.filter_customers(50000)

        analyzer.sort_by_income(ascending=True)
        analyzer.sort_by_income(ascending=False)

        analyzer.calculate_statistics()
        analyzer.analyze_features()
        analyzer.perform_eda()
        analyzer.analyze_target()

        analyzer.group_by_purchase_status()

        analyzer.display_report()

    except (TypeError, ValueError) as e:
        print("Error:", e)


if __name__ == "__main__":
    main()