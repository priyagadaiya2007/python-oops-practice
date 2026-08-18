import numpy as np
class NumpyFeatureProcessor:
    def __init__(self, data):
        self.data = data
        self.array = None
        self.min_max_data = None
        self.standardized_data = None

    def validation_input(self):
        if not isinstance(self.data,list):
            raise TypeError("Input must be a list.")
        if len(self.data) == 0:
            raise ValueError("Input list cannot be empty.")
        if not all(isinstance(value, (int, float,np.number))and not isinstance(value, bool) for value in self.data):
            raise TypeError("Dataset contains non-numeric values.")

    def convert_to_numpy_array(self):
        self.array = np.array(self.data)

    def get_array_info(self):
        print("Numpy Array:")
        print(self.array)
        print("Data Type:", self.array.dtype)
        print("Dimensions:", self.array.ndim)
        print("Shape:", self.array.shape)
        print("Size:", self.array.size)

    def calculate_minimum(self):
        return np.min(self.array)

    def calculate_maximum(self):
        return np.max(self.array)

    def calculate_mean(self):
        return np.mean(self.array)

    def calculate_standard_deviation(self):
        return np.std(self.array)

    def min_max_scaling(self):
        minimum = np.min(self.array)
        maximum = np.max(self.array)
        if minimum == maximum:
            raise ValueError("Cannot scale data because all values are identical.")
        self.min_max_data = (self.array - minimum) / (maximum - minimum)
        return self.min_max_data
    
    def standardization(self):
        mean = np.mean(self.array)
        standard_deviation = np.std(self.array)
        if standard_deviation == 0:
            raise ValueError("Cannot standardize data because standard deviation is zero.")
        self.standardized_data = (self.array - mean) / standard_deviation
        return self.standardized_data

    def display_report(self):
        print("="*50)
        print("NUMPY FEATURE PROCESSING REPORT")
        print("="*50)
        print("\nOriginal Data:", self.data)
        print("\nNumpy Array Info:")
        print("\nMinimum:", self.calculate_minimum())
        print("Maximum:", self.calculate_maximum())
        print("Mean:", self.calculate_mean())
        print("Standard Deviation:", self.calculate_standard_deviation())
        print("\nMin-Max Scaled Data:", self.min_max_scaling())
        print("\nz-Score Standardized Data:", self.standardization())
        print(np.array(self.standardized_data))
        print("\n" + "="*50)

def main():
        data = [10, 20, 30, 40, 50]
        try:
            obj = NumpyFeatureProcessor(data)
            obj.validation_input()
            obj.convert_to_numpy_array()
            obj.display_report()
        except (TypeError, ValueError) as error:
            print("Error:", error)
if __name__ == "__main__":
    main()


        
            
            
