import pandas as pd 
data = { 
    "Name": ["Anu", "Ravi", "Kiran", "Sita", "Rahul"], 
    "Age": [22, 25, 21, 24, 27], 
    "City": ["Rajahmundry", "Hyderabad", "Chennai", "Rajahmundry", "Hyderabad"], 
    "Salary": [25000, 45000, 30000, 35000, 55000], 
    "Department": ["IT", "HR", "IT", "Finance", "IT"]
    } 
df = pd.DataFrame(data) 

print(df)

#filtering data
   #Salary greater than 30000

result= df[df["Salary"]>30000]
print(result)

    #multiple conditions
    #And
result=df[(df["Salary"]>30000)&(df["Department"]=="IT")]
print(result)
    #or
result=df[(df["City"]=="Hyderabad")| (df["City"]=="Rajahmundry")]
print(result)

#Filter Using  isin()
result=df[df["City"].isin(["Hyderabad","Chennai"])]
print(result)

#sorting data
   #ascending order
df.sort_values("Salary")

 #dscending order
result=df.sort_values("Salary",ascending=True)
print(result)
#sort multiple column
result=df.sort_values( ["Department","Salary"], ascending=[True,False])
print(result)
#creating new column
df["Bonus"]=df["Salary"]*0.10
print(df)
#calculate total salary
df["TotalSalary"]=df["Salary"]+df["Bonus"]
print(df)
# Conditional Column with  np.where()
import numpy as np
df["Level"]=np.where(df["Salary"]>=40000,"Senior","junior")
print(df)
#groupby()
result=df.groupby("Department")["Salary"].mean()
print(result)
#groupby with aggression functions
result=df.groupby("Department")["Salary"].agg(["count","sum","mean","min","max"])
print(result)
#groupby with city
result=df.groupby("City")["Salary"].mean()
print(result)
#groupby with multiple column
result=df.groupby(["City","Department"])["Salary"].mean()
print(result)
#value_counts()
print(df["Department"].value_counts())
#city-wise value_count()
print(df["City"].value_counts())
#missing value
data={
    "Name":["Anu","Ravi","Kiran","Sita"],
    "Age":[24,None,21,20],
    "Salary":[25000,45000,None,35000]
    }
df=pd.DataFrame(data)
print(df)
#find missing value
print(df.isnull())
#count missing value
print(df.isnull().sum())
#fill age with average age 
df["Age"]=df["Age"].fillna(df["Age"].mean())
print(df)
#fill salary with 0
df["Salary"]=df["Salary"].fillna(0)
print(df)
#remaving missing row
df.dropna()
print(df)
#remove duplicate data
df.drop_duplicates(subset=["Name"])
print(df)
#rename column
df.rename( columns={ "Salary": "MonthlySalary", "Age": "EmployeeAge" }, inplace=True )
print(df) 
#loc[]
print(df.loc[0]) 
#Select specific columns: 
print(df.loc[:, ["Name", "MonthlySalary"]]) 
# Filter rows:
result = df.loc[df["MonthlySalary"] > 30000] 
print(result) 

#iloc[]
print(df.iloc[0])

#First 3 rows: 
print(df.iloc[0:3]) 

#First 3 rows and first 2 columns: 
print(df.iloc[0:3, 0:2])

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