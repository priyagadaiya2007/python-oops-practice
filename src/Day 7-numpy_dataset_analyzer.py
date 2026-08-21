import numpy as np

class NumpyDatasetAnalyzer:
    def __init__(self, data):
        self.data = data
        self.array = None

    def validate_input(self):
        if not isinstance(self.data,list):
            raise TypeError("Dataset must be a list.")
        if len(self.data) == 0:
            raise ValueError("Dataset cannot be empty.")
        if not all(isinstance(row, list) for row in self.data):
            raise TypeError("Each row must be a list.")
        column_count = len(self.data[0])
        if column_count == 0:
            raise ValueError("Rows cannot be empty.")
        
        for row in self.data:
            if len(row) != column_count:
                raise ValueError("All rows must contain the same number of columns.")
        for value  in row:
            if not isinstance(value, (int, float)):
                raise TypeError("Dataset contain non-numeric values.")

    def convert_to_numpy_array(self):
        self.array = np.array(self.data)

    def get_dataset_info(self):
        if self.array is None:
            raise ValueError("Dataset must be converted to Numpy array first.")
        rows, columns = self.array.shape 
        print("\n----Dataset Information----")
        print("Rows :", rows)
        print("Columns :", columns)
        print("Dimension :", self.array.ndim)
        print("Size :", self.array.size)
        print("Data Type :", self.array.dtype)

    def get_column(self, column_index):
        if self.array is None:
            raise ValueError("Dataset must be converted to Numpy array first.")
        return self.array[:, column_index]

    def get_row(self, row_index):
        if self.array is None:
            raise ValueError("Dataset must be converted to Numpy array first.")
        return self.array[row_index, :]

    def calculate_column_mean(self):
        return np.mean(self.array, axis=0)

    def calculate_column_minimum(self):
        return np.min(self.array, axis=0)
    
    def calculate_column_maximum(self):
        return np.max(self.array, axis=0)
    
    def calculate_column_std(self):
        return np.std(self.array, axis=0)
    
    def scale_features(self):
        minimum = np.min(self.array, axis=0)
        maximum = np.max(self.array, axis=0)
        range_values = maximum - minimum
        range_values = np.where(range_values == 0, 1, range_values)
        scaled = (self.array - minimum) / range_values
        return scaled

    def features_summary(self):
        mean = self.calculate_column_mean()
        minimum = self.calculate_column_minimum()
        maximum = self.calculate_column_maximum()
        std = self.calculate_column_std()

        print("\n----Features Summary----")
        for i in range(self.array.shape[1]):
            print(f"\nFeature {i+1}")
            print("Mean", mean[i])
            print("Minimum", minimum[i])
            print("Maximum", maximum[i])
            print("Standard Deviation:", std[i])

    def display_report(self):
        print("\n ----Numpy Dataset Analysis----")
        self.get_dataset_info()

        print("\n---First Column---")
        print(self.get_column(0))

        print("\n---First Row---")
        print(self.get_row(0))

        print("\n----Column Means----")
        print(self.calculate_column_mean())

        print("\n----Column Minimum----")
        print(self.calculate_column_minimum())

        print("\n----Column Maximum----")
        print(self.calculate_column_maximum())

        print("\n----Column Standard Deviation----")
        print(self.calculate_column_std())
        print("\n----Scaled Features----")
        print(self.scale_features())
        print(self.features_summary())

def main():
    data = [
        [25, 30000, 2],
        [30, 45000, 5],
        [35, 60000, 8],
        [40, 80000, 12],
        [45, 100000, 15],
    ]
    try:
        analyzer = NumpyDatasetAnalyzer(data)
        analyzer.validate_input()
        analyzer.convert_to_numpy_array()
        analyzer.display_report()
    except(TypeError, ValueError)as error:
        print("Error:", error)

if __name__ == "__main__":
    main()

