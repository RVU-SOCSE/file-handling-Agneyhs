Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>>  import pandas as pd
...  
SyntaxError: unexpected indent
>>> import pandas as pd
>>> df = pd.read_csv("C:/Users/Agney H S/Downloads/5prog_1experience.csv")
>>> mean_value = df['YearsExperience'].mean()
>>> median_value = df['YearsExperience'].median()
>>> mode_value = df['YearsExperience'].mode()[0]
>>> # In case of multiple modes, we take the first one
>>> min_value = df['YearsExperience'].min()
>>> max_value = df['YearsExperience'].max()
>>> variance_value = df['YearsExperience'].var()
>>> std_dev_value = df['YearsExperience'].std()
>>> print(f"Mean: {mean_value}")
Mean: 2.266666666666667
>>> print(f"Median: {median_value}")
Median: 2.2
>>> 
>>> print(f"Mode: {mode_value}")
Mode: 3.2
>>> print(f"Minimum: {min_value}")
Minimum: 1.1
>>> print(f"Maximum: {max_value}")
Maximum: 3.2
>>> print(f"Variance: {variance_value}")
Variance: 0.7050000000000001
>>> print(f"Standard Deviation: {std_dev_value}")
... Standard Deviation: 0.8396427811873333
SyntaxError: multiple statements found while compiling a single statement
>>> print(f"Standard Deviation: {std_dev_value}")
Standard Deviation: 0.8396427811873333
