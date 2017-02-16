import pandas

#df1 = pandas.read_csv('supermarkets.csv')
# print(df1)

df2 = pandas.read_csv('supermarkets.json', error_bad_lines=False)
# df2.set_index('ID')
print(df2)

#df3 = pandas.read_csv('supermarkets.xlsx')
#print(df3)

# df4 = pandas.read_csv('supermarkets-commas.txt')
# print(df4)