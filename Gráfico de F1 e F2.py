import pandas as pd
import matplotlib.pyplot as plt

# Load the data from CSV (replace 'your_file.csv' with the actual file path)
df = pd.read_csv('quadro.csv')

# Clean the data (replace NaNs and ensure F1 and F2 are numeric)
df['F1'] = pd.to_numeric(df['F1'], errors='coerce')
df['F2'] = pd.to_numeric(df['F2'], errors='coerce')

# Filter out rows without necessary F1/F2 values
df = df.dropna(subset=['F1', 'F2'])

# Split data by languages (adjust according to your actual dataset)
df_finnish = df.iloc[:4]  # Assuming the first 5 rows are Finnish vowels
df_dutch = df.iloc[4:]    # The remaining rows are Dutch vowels

# Plot settings
plt.figure(figsize=(10, 6))

# Plot Finnish vowels
plt.scatter(df_finnish['F2'], df_finnish['F1'], color='blue', label='PB')
for i, vowel in enumerate(df_finnish['Vogal']):
    plt.text(df_finnish['F2'].iloc[i], df_finnish['F1'].iloc[i], vowel, fontsize=12, color='blue', fontfamily='Arial')

# Plot Dutch vowels
plt.scatter(df_dutch['F2'], df_dutch['F1'], color='red', label='Espanhol')
for i, vowel in enumerate(df_dutch['Vogal']):
    plt.text(df_dutch['F2'].iloc[i], df_dutch['F1'].iloc[i], vowel, fontsize=12, color='red', fontfamily='Arial')

# Invert the F1 axis to reflect vowel height
plt.gca().invert_yaxis()
plt.ylim(900, 300)  # Define limits for F1 from 0 to 500 (inverted)

# Axis labels and title
plt.xlabel('F2 (anterioridade)', fontsize=12)
plt.ylabel('F1 (altura)', fontsize=12)
plt.title('Vowel Chart', fontsize=14)
plt.legend()

# Display the plot
plt.grid(True)
plt.show()
