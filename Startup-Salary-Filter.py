import pandas as pd

# 1. Load data with the high-performance Arrow backend
# Ensure you have 'pyarrow' installed: pip install pyarrow
df = pd.read_csv('job_listings.csv', engine='pyarrow', dtype_backend='pyarrow')

# 2. The Filter Logic
# We use .loc for label-based boolean indexing
high_value_jobs = df.loc[
    (df['Job_Title'] == 'AI Engineer') & 
    (df['Location'] == 'Remote') & 
    (df['Salary_INR'] > 1200000)
]

# 3. View the top results
print(f"Found {len(high_value_jobs)} matching roles.")
print(high_value_jobs[['Company', 'Salary_INR']].head())

# 4. Export for your portfolio
high_value_jobs.to_csv('target_jobs.csv', index=False)