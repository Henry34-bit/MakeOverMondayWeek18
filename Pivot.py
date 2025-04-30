import pandas as pd

# Load the original file
input_path = r'C:\Users\hmeehan\Desktop\Trump Approval Ratings - Response.csv'
df = pd.read_csv(input_path)

# Convert to long format
long_df = df.melt(
    id_vars=["Demographic"],
    var_name="Response Type",
    value_name="Percentage"
)

# Save the result to a new CSV
output_path = r'C:\Users\hmeehan\Desktop\Trump Approval Ratings - Long Format.csv'
long_df.to_csv(output_path, index=False)

print(f"Long-format CSV saved to: {output_path}")

