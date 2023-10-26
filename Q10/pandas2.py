import pandas as pd

data = pd.DataFrame({
 'school_code': ['s001','s002','s003','s001','s002','s004'],
 'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
 'date_Of_Birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
 't_id':['t1', 't2', 't3', 't4', 't5', 't6']})

print("Default Index:")
print(data.head(10))

data1 = data.set_index('school_code')
print(data1)

data2 = data.set_index('t_id')
print(data2)
