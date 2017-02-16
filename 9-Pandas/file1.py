import pandas

df1 = pandas.DataFrame([[2, 4, 6], [10, 20, 30]])

print(df1)

df2 = pandas.DataFrame([[2, 4, 6], [10, 20, 30]], columns=["Price", "Age", "Value"])

print(df2)

df3 = pandas.DataFrame([[2, 4, 6], [10, 20, 30]], columns=["Price", "Age", "Value"],
                       index=["First", "Sedond"])

print(df3)
