import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file into a pandas dataframe
df = pd.read_excel('feedback.xlsx', sheet_name='Sheet6')

# Access the data in the dataframe
print("The data is : ------------")
print(df)

# Select the column and store it in a list
x = df['Name'].tolist()
y = df['Rating'].tolist()
print(x)
print(y)

# df.plot(x='Name', y='Score', kind='line')
# # plt.hist(df['Rating'], bins=15)

# # Add labels and a title
# plt.xlabel('Name of Resource Person')
# plt.ylabel('Rating')
# plt.title('Plot of Name and Rating')

# # Display the plot
# plt.show()
