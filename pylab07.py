Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import pandas as pd
data = { 'Name': ['Alice', 'Bob', 'Charlie', 'David'],
         'Age': [25, 30, 35, 40],
         'Salary': [50000, 60000, 70000, 80000] }
df = pd.DataFrame(data)
print("DataFrame from Scratch:")
DataFrame from Scratch:
print(df)
      Name  Age  Salary
0    Alice   25   50000
1      Bob   30   60000
2  Charlie   35   70000
3    David   40   80000
df['Bonus'] = df['Salary'] * 0.10
print("\nDataFrame after adding 'Bonus' column:")

DataFrame after adding 'Bonus' column:
DataFrame after adding 'Bonus' column:
    
SyntaxError: invalid syntax
print(df)
      Name  Age  Salary   Bonus
0    Alice   25   50000  5000.0
1      Bob   30   60000  6000.0
2  Charlie   35   70000  7000.0
3    David   40   80000  8000.0
import pandas as pd
df = pd.read_csv("C:/Users/Agney H S/Downloads/7prog_6Mcd_null_values.csv")

print("First 6 rows of the DataFrame:")
First 6 rows of the DataFrame:
print(df.head(6))
   Year  McDonalds_Revenue_$Billion  Growth_rate_percent   Q1   Q2   Q3   Q4
0  1999                        13.3                  NaN  NaN  NaN  NaN  NaN
1  2000                        14.2                  7.0  NaN  NaN  NaN  NaN
2  2001                        14.9                  4.0  NaN  NaN  NaN  NaN
3  2002                        15.4                  4.0  NaN  NaN  NaN  3.0
4  2003                        17.1                 11.0  3.8  4.3  4.5  4.6
5  2004                        18.6                  8.0  4.4  4.7  4.9  4.5
print("\nColumn names and data types:")

Column names and data types:
print(df.info())
<class 'pandas.DataFrame'>
RangeIndex: 24 entries, 0 to 23
Data columns (total 7 columns):
 #   Column                      Non-Null Count  Dtype  
---  ------                      --------------  -----  
 0   Year                        24 non-null     int64  
 1   McDonalds_Revenue_$Billion  24 non-null     float64
 2   Growth_rate_percent         23 non-null     float64
 3   Q1                          20 non-null     float64
 4   Q2                          20 non-null     float64
 5   Q3                          20 non-null     float64
 6   Q4                          21 non-null     float64
dtypes: float64(6), int64(1)
memory usage: 1.4 KB
None
import pandas as pd
df = pd.read_csv(r"C:/Users/Agney H S/Downloads/7prog_6Mcd_null_values.csv")
print("Original DataFrame:")
Original DataFrame:
df
    Year  McDonalds_Revenue_$Billion  Growth_rate_percent   Q1   Q2   Q3   Q4
0   1999                        13.3                  NaN  NaN  NaN  NaN  NaN
1   2000                        14.2                  7.0  NaN  NaN  NaN  NaN
2   2001                        14.9                  4.0  NaN  NaN  NaN  NaN
3   2002                        15.4                  4.0  NaN  NaN  NaN  3.0
4   2003                        17.1                 11.0  3.8  4.3  4.5  4.6
5   2004                        18.6                  8.0  4.4  4.7  4.9  4.5
6   2005                        19.1                  3.0  4.8  5.1  5.3  3.9
7   2006                        20.9                  9.0  4.9  5.4  5.5  5.1
8   2007                        22.8                  9.0  5.3  5.8  5.9  5.8
9   2008                        23.5                  3.0  5.6  6.1  6.3  5.6
10  2009                        22.7                 -3.0  5.1  5.6  6.0  6.0
11  2010                        24.1                  6.0  5.6  5.9  6.3  6.2
12  2011                        27.0                 12.0  6.1  6.9  7.2  6.8
13  2012                        27.6                  2.0  6.5  6.9  7.2  7.0
14  2013                        28.1                  2.0  6.6  7.1  7.3  7.1
15  2014                        27.4                 -2.0  6.7  7.2  7.0  6.6
16  2015                        25.4                 -7.0  6.0  6.5  6.6  6.3
17  2016                        24.6                 -3.0  5.9  6.3  6.4  6.0
18  2017                        22.8                 -7.0  5.7  6.0  5.8  5.3
19  2018                        21.3                 -7.0  5.1  5.4  5.4  5.4
20  2019                        21.4                  1.0  5.0  5.3  5.6  5.4
21  2020                        19.2                -10.0  4.7  3.8  5.4  5.3
22  2021                        23.2                 21.0  5.1  5.9  6.2  6.0
23  2022                        23.2                  0.0  5.7  5.7  5.9  5.9
print("\nMissing values in the DataFrame:")

Missing values in the DataFrame:
print(df.isnull().sum())
Year                          0
McDonalds_Revenue_$Billion    0
Growth_rate_percent           1
Q1                            4
Q2                            4
Q3                            4
Q4                            3
dtype: int64
df['Q1'].fillna(df['Q1'].mean(), inplace=True)

Warning (from warnings module):
  File "<pyshell#23>", line 1
ChainedAssignmentError: A value is being set on a copy of a DataFrame or Series through chained assignment using an inplace method.
Such inplace method never works to update the original DataFrame or Series, because the intermediate object on which we are setting values always behaves as a copy (due to Copy-on-Write).

For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' instead, to perform the operation inplace on the original object, or try to avoid an inplace operation using 'df[col] = df[col].method(value)'.

See the documentation for a more detailed explanation: https://pandas.pydata.org/pandas-docs/stable/user_guide/copy_on_write.html
0     5.43
1     5.43
2     5.43
3     5.43
4     3.80
5     4.40
6     4.80
7     4.90
8     5.30
9     5.60
10    5.10
11    5.60
12    6.10
13    6.50
14    6.60
15    6.70
16    6.00
17    5.90
18    5.70
19    5.10
20    5.00
21    4.70
22    5.10
23    5.70
Name: Q1, dtype: float64
>>> print("\nDataFrame after filling missing values in 'Q1'
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print('\nDataFrame after filling missing values in 'Q1')
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print("\nDataFrame after filling missing values in 'Q1' column:")
...       

DataFrame after filling missing values in 'Q1' column:
>>> df
...       
    Year  McDonalds_Revenue_$Billion  Growth_rate_percent   Q1   Q2   Q3   Q4
0   1999                        13.3                  NaN  NaN  NaN  NaN  NaN
1   2000                        14.2                  7.0  NaN  NaN  NaN  NaN
2   2001                        14.9                  4.0  NaN  NaN  NaN  NaN
3   2002                        15.4                  4.0  NaN  NaN  NaN  3.0
4   2003                        17.1                 11.0  3.8  4.3  4.5  4.6
5   2004                        18.6                  8.0  4.4  4.7  4.9  4.5
6   2005                        19.1                  3.0  4.8  5.1  5.3  3.9
7   2006                        20.9                  9.0  4.9  5.4  5.5  5.1
8   2007                        22.8                  9.0  5.3  5.8  5.9  5.8
9   2008                        23.5                  3.0  5.6  6.1  6.3  5.6
10  2009                        22.7                 -3.0  5.1  5.6  6.0  6.0
11  2010                        24.1                  6.0  5.6  5.9  6.3  6.2
12  2011                        27.0                 12.0  6.1  6.9  7.2  6.8
13  2012                        27.6                  2.0  6.5  6.9  7.2  7.0
14  2013                        28.1                  2.0  6.6  7.1  7.3  7.1
15  2014                        27.4                 -2.0  6.7  7.2  7.0  6.6
16  2015                        25.4                 -7.0  6.0  6.5  6.6  6.3
17  2016                        24.6                 -3.0  5.9  6.3  6.4  6.0
18  2017                        22.8                 -7.0  5.7  6.0  5.8  5.3
19  2018                        21.3                 -7.0  5.1  5.4  5.4  5.4
20  2019                        21.4                  1.0  5.0  5.3  5.6  5.4
21  2020                        19.2                -10.0  4.7  3.8  5.4  5.3
22  2021                        23.2                 21.0  5.1  5.9  6.2  6.0
23  2022                        23.2                  0.0  5.7  5.7  5.9  5.9
