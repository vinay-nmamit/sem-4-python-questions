import pandas as pd

student_data1 = pd.DataFrame({
    'student_id' : ['s1','s2','s3','s4','s5'],
    'name' : ['vinay','kumar','shishir','yashraj','vedant'],
    'marks' : [200,199,198,198,200]
})
student_data2 = pd.DataFrame({
    'student_id' : ['s6','s7','s6','s9','s10'],
    'name' : ['vinay','kumar','shishir','yashraj','vedant'],
    'marks' : [200,199,198,198,200]
})
exam_data = pd.DataFrame({
    'student_id' : ['s1','s2','s3','s4','s5','s6','s7','s8','s9','s10'],
    'exam_id' : [23,82,12,56,67,113,51,5,10,79]
})
print("Original DataFrames:")
print(student_data1)
print(student_data2)
print(exam_data)

result_data = pd.concat([student_data1, student_data2])
print(result_data)

final_merged_data = pd.merge(result_data, exam_data, on='student_id')
print(final_merged_data)
