"""
Write program to cut grades According to the following criteria
Grade   point range
0-49    F
50-59   D
60-69   C
70-79   B
80-100  A
With the following capabilities

The input will be a student's score in the range 0-100,
an integer number will enter in Until the number is 999
(* This value is not a score Do not need to be calculated)
into the program and therefore stop working
Count and display the total number of students.
Classified by grade, for example A has 2 people, B has 3 people etc.
Calculate and show the average grade of students in the whole class
(average score = total score / number of students)
Calculate and show GPA of all grade students (GPA = Total Grade / Number of Students)
If the first value is 999, do not show the Average Score and Average GPA.
"""
import numpy as np
import pandas as pd
# a = np.array(list(map(int, iter(input, '999'))))
a = np.array([60,74,88,65,42,81])
f = lambda x: ('F','D','C','B','A')[(80<=x)+(70<=x)+(60<=x)+(50<=x)]

d = pd.Series([f(n.item()) for n in a]).value_counts().sort_index()

print('Total Students by Grade: ', end='')
print(*[f'{i}={v}' for i,v in d.iteritems()],sep=',')
print('Average Score:', f'{a.mean():.2f}')

"""
60
74
88
65
42
81
999
"""










