# Imports dictionaries stored in a  different file that contain the text part of the final comments.
import csv
from comments import achievementDict as achievementDict, attentionDict as attentionDict, attendanceDict as attendanceDict, homeworkDict as homeworkDict, gradeDict as gradeDict, traitsDict as traitsDict, course_description as course_description


# Defines variables
def define_data(line):  
    name, achievement, attention, attendance, homework, exam_grade, traits, course, extra = line
    return name, achievement, attention, attendance, homework, exam_grade, traits, course, extra

# Auto grader that takes in all the score for each category for a student and compute a letter grade
def find_grade(achievement, attention, attendance, homework):
  scoreavg = (int(achievement) + int(attention) + int(attendance) + int(homework))/4
  if scoreavg >= 4:
    grade = 'A'
  elif scoreavg >= 3.5:
    grade = 'A-'
  elif scoreavg >= 3:
    grade = 'B'
  else:
    grade = 'C'
  return grade

# Opens the csv file to read it, closes it once done
with open('data.csv') as data:
    # Defines two variabes - data holds the information in the file after reading it, header stores the first line.
    data, header = csv.reader(data), next(data) 
    # Iterates through the lines in the csv file.
    for line in data: 
        # Calls the function to define the variables.
        name, achievement, attention, attendance, homework, exam_grade, traits, course, extra = define_data(line)
        grade = find_grade(achievement, attention, attendance, homework)
        with open(f"{name}.txt", "w") as writef:
          # write into txt file.
          writef.write(course_description[course])
          writef.write('\n')
          writef.write(f"{name} {achievementDict[int(achievement)]} {attentionDict[int(attention)]} {attendanceDict[int(attendance)]} {homeworkDict[int(homework)]} The grade you earned on the previous exam was {exam_grade}, keep going! {extra} {gradeDict[grade]} ")
          if ' ' in traits:
            traits = traits.split(', ')
            for trait in traits:
              writef.write(f"{traitsDict[trait]} ")
          else:
            writef.write(traitsDict[trait])
