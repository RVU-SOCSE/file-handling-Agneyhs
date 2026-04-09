Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
df = pd.read_csv("C:/Users/Agney H S/Downloads/5prog_1experience.csv")
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    df = pd.read_csv("C:/Users/Agney H S/Downloads/5prog_1experience.csv")
NameError: name 'pd' is not defined. Did you mean: 'id'?
df = pd.read_csv('C:/Users/Agney H S/Downloads/5prog_1experience.csv')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    df = pd.read_csv('C:/Users/Agney H S/Downloads/5prog_1experience.csv')
NameError: name 'pd' is not defined. Did you mean: 'id'?
import pandas as pd
df = pd.read_csv('C:/Users/Agney H S/Downloads/5prog_1experience.csv')
description = df.describe()
quantiles = df['YearsExperience'].quantile([0.25, 0.5, 0.75])
 skewness = df['YearsExperience'].skew()
 
SyntaxError: unexpected indent
>>> skewness = df['YearsExperience'].skew()
>>> kurtosis = df['YearsExperience'].kurt()
>>> value_counts = df['YearsExperience'].value_counts()
>>> print("Statistical Summary:\n", description)
Statistical Summary:
        YearsExperience
count         9.000000
mean          2.266667
std           0.839643
min           1.100000
25%           1.500000
50%           2.200000
75%           3.000000
max           3.200000
>>> print("\nQuantiles:\n", quantiles)

Quantiles:
 0.25    1.5
0.50    2.2
0.75    3.0
Name: YearsExperience, dtype: float64
>>> print("\nSkewness:", skewness)

Skewness: -0.18643041769017651
>>> print("Kurtosis:", kurtosis)
Kurtosis: -1.8530398729583881
>>> print("\nValue Counts:\n", value_counts)

Value Counts:
 YearsExperience
3.2    2
1.1    1
1.3    1
1.5    1
2.0    1
2.2    1
2.9    1
3.0    1
Name: count, dtype: int64
