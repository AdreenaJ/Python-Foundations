import pandas as pd
import random

# Data options
titles = ['AI Engineer', 'Data Scientist', 'Full Stack Developer', 'Backend Engineer', 'Prompt Engineer']
locations = ['Remote', 'Bangalore', 'Hyderabad', 'Pune', 'Mumbai', 'Delhi']
companies = ['TechNova', 'AI-Flow', 'CloudScale', 'DeepSolutions', 'DataLogic']

data = {
    'Company': [random.choice(companies) for _ in range(5000)],
    'Job_Title': [random.choice(titles) for _ in range(5000)],
    'Location': [random.choice(locations) for _ in range(5000)],
    'Salary_INR': [random.randint(600000, 2500000) for _ in range(5000)]
}

df = pd.DataFrame(data)
df.to_csv('job_listings.csv', index=False)
print("✅ Success! 'job_listings.csv' created with 5,000 entries.")