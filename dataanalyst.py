import pandas as pd
data = { 
    "Employee": ["A", "B", "C", "D", "E", "F"], 
    "Department": ["IT", "HR", "IT", "Sales", "HR", "IT"], 
    "Salary": [40000, 30000, 50000, 35000, 32000, 60000], 
    "Experience": [2, 1, 4, 3, 2, 6] 
    } 
df = pd.DataFrame(data)
print(df) 

#Employees earning above ₹40,000 
result=df[df["Salary"] > 40000]
print(result)

#Average salary 
result=df["Salary"].mean()
print(result)

#Highest salary 
result=df["Salary"].max()
print(result)

#Employee with highest salary
result= df.loc[df["Salary"].idxmax()]
print(result)

#Average salary by department
result=df.groupby("Department")["Salary"].mean() 
print(result)

#number of employee by department
result=df["Department"].value_counts()
print(result)

#Employees with more than 3 years experience 
result=df[df["Experience"] > 3]
print(result)  

# Add annual salary 
result=df["AnnualSalary"] = df["Salary"] * 12 
print(result)