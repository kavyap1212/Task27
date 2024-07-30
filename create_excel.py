import pandas as pd

# Define the data
data = {
    'Test ID': [1, 2, 3, 4, 5],
    'Username': ['user1', 'user2', 'user3', 'user4', 'user5'],
    'Password': ['password1', 'password2', 'password3', 'password4', 'password5'],
    'Date': [''] * 5,  # Empty strings as placeholders
    'Time of Test': [''] * 5,  # Empty strings as placeholders
    'Name of Tester': ['Tester1', 'Tester2', 'Tester3', 'Tester4', 'Tester5'],
    'Test Result': [''] * 5  # Empty strings as placeholders
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to Excel
file_path = 'login_data.xlsx'
df.to_excel(file_path, index=False)

print(f"{file_path} created successfully.")