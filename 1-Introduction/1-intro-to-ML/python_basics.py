# Exercise adapted from Microsoft Learn:
#https://learn.microsoft.com/en-us/training/modules/explore-analyze-data-with-python/3-exercise-explore-data


#python list structure
data = [50,50,47,97,49,3,53,42,26,74,82,62,37,15,70,27,36,35,48,52,63,64]
# print(data)     [50, 50, 47, 97, 49, 3, 53, 42, 26, 74, 82, 62, 37, 15, 70, 27, 36, 35, 48, 52, 63, 64]


# need NumPy to perform mathematical operations (provides mathematical functions)

import numpy as np   

# NumPy array structure
grades = np.array(data)
#print(grades)           # [50 50 47 97 49  3 53 42 26 74 82 62 37 15 70 27 36 35 48 52 63 64]

#print(grades.shape)     # (22,) 1D array with 22 elements

#print(grades[0])    # 50

#print(grades.mean())   # 49.18181818181818



# Define an array of study hours
study_hours = [10.0,11.5,9.0,16.0,9.25,1.0,11.5,9.0,8.5,14.5,15.5,
               13.75,9.0,8.0,15.5,8.0,9.0,6.0,10.0,12.0,12.5,12.0]

# Create a 2D array 
student_data = np.array([study_hours, grades])
#print(student_data)

#print(student_data.shape)  #(2, 22) 2D array with 22 columns and 2 rows

#print(student_data[0][0])  


# avg_study = student_data[0].mean()
# avg_grade = student_data[1].mean()

# print('Average study hours: {:.2f}\nAverage grade: {:.2f}'.format(avg_study, avg_grade))  # avg hours: 10.52 avg grade: 49.18


# pandas library for data analysis and manipulation
import pandas as pd

df_students = pd.DataFrame({'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic', 'Jimmie', 
                                     'Rhonda', 'Giovanni', 'Francesca', 'Rajab', 'Naiyana', 'Kian', 'Jenny',
                                     'Jakeem','Helena','Ismat','Anila','Skye','Daniel','Aisha'],
                            'StudyHours':student_data[0],
                            'Grade':student_data[1]})

#print(df_students)


# loc to retrieve data for a specific index value
#print(df_students.loc[5])

# for a range of index values
#print(df_students.loc[0:5])


# iloc to retrieve data for a specific index position
#print(df_students.iloc[0:5]) 

#print(df_students.iloc[0,[1,2]])

#print(df_students.loc[0,'Grade'])


# print(df_students.loc[df_students['Name']=='Aisha']) # *
# print(df_students[df_students['Name']=='Aisha'])  # *
# print(df_students.query('Name=="Aisha"'))    # * all three lines provide same output, for good measure use query()


df_students = pd.read_csv('1-Introduction/1-intro-to-ML/grades.csv',delimiter=',',header='infer')
#print(df_students.head())

#print(df_students.isnull())     #isnull to identify null values

print(df_students.isnull().sum())


#axis= 0 operate down on each column
#axis= 1 operate across on each row
print(df_students[df_students.isnull().any(axis=1)]) # to filter only rows where any column has a null value NaN (not a number)


# fillna to replace the missing value with the mean study hours
df_students.StudyHours = df_students.StudyHours.fillna(df_students.StudyHours.mean()) 
print(df_students)

# dropna to remove rows with missing values
df_students = df_students.dropna(axis=0, how='any') 
print(df_students)


# mean study hours and grades
mean_study = df_students['StudyHours'].mean()
mean_grade = df_students.Grade.mean()

print('Average weekly study hours: {:.2f}\nAverage grade: {:.2f}'.format(mean_study, mean_grade))

# students that studies more than mean
print(df_students[df_students.StudyHours > mean_study])
# their mean grade
print(df_students[df_students.StudyHours > mean_study].Grade.mean())


# creating Pandas Series to indicate a student passed or failed
passes  = pd.Series(df_students['Grade'] >= 60)
df_students = pd.concat([df_students, passes.rename("Pass")], axis=1)

print(df_students)

# groupby to count the number of students that passed and failed
print(df_students.groupby(df_students.Pass).Name.count())

# finding mean study time and grade for the groups of students who passed and failed the course
print(df_students.groupby(df_students.Pass)[['StudyHours', 'Grade']].mean())


# Creating a DataFrame with the data sorted by Grade (descending)
df_students = df_students.sort_values('Grade', ascending=False)
print(df_students)