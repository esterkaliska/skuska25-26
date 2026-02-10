import math 
import os

class DataAnalysis:
    def __init__(self, file):
        folder = os.path.dirname(os.path.abspath(__file__))
        self.file = os.path.join(folder, file)
        self.data = []

    def load_data(self):
        try:
            with open (self.file, "r", encoding="utf-8") as file:
                for value in file:
                    value = value.strip()
                    if not value: continue
                    self.data.append(float(value))
                self.data.sort()
                return self.data 
        except FileNotFoundError: 
            print("Error! File was not found.")
            return None
        except ValueError: 
            print("Error! The values in the file are incorrect.")
            return None
        except Exception:
            print("Error!")
            return None

    def normal_distribution(self):
        n = len(self.data)
        if n == 0:
            return "No data."

        mean = sum(self.data) / n
        variance = sum((x - mean)**2 for x in self.data) / (n - 1)
        std_dev = math.sqrt(variance)

        max_difference = 0

        for i in range(n):
            z_score = (self.data[i] - mean) / std_dev
            theor_cdf = 0.5 * (1 + math.erf(z_score / math.sqrt(2)))
            
            emp_cdf_up = (i + 1) / n
            emp_cdf_down = i / n
            
            difference = max(abs(emp_cdf_up - theor_cdf), abs(emp_cdf_down - theor_cdf))
            
            if difference > max_difference:
                max_difference = difference

        print(f"Calculated D-statistic: {max_difference:.4f}")

        critical_value = 0.134
        if max_difference < critical_value:
            return "Result: Data follow a NORMAL distribution."
        else:
            return "Result: Data do NOT follow a normal distribution."

data = input("Input the name of your file (ex. data.txt): ")
function = DataAnalysis(data)
function.load_data()
result = function.normal_distribution()

print(result)
