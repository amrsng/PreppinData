# Preppin Data 2023 Week 22
# https://preppindata.blogspot.com/2023/05/2023-week-22-student-attendance-vs-test.html

# get data
import pandas as pd
from tabulate import tabulate

xls = pd.ExcelFile("D:/Python/PreppinData/2023/2023W22/Student Attendance vs Scores.xlsx")

# list sheets
print(xls.sheet_names)

# make dataframes
attendance = pd.read_excel(xls, sheet_name="Attendance Figures")
scores = pd.read_excel(xls, sheet_name="Student Test Scores", skiprows=1)

# check tables
print(tabulate(attendance.head(), headers="keys", tablefmt="pretty"))
print("\n")
print(tabulate(scores.head(), headers="keys", tablefmt="pretty"))

# join together
df = attendance.merge(scores, how="inner", on="student_name")
print("\n")
print(tabulate(df.head(), headers="keys", tablefmt="pretty"))

# identify spelling mistakes
print("\n")
print(df["subject"].unique())

# correct spelling mistakes
spelling = {"Math": "Maths", "Engish": "English", "Sciece": "Science"}
df.replace({"subject": spelling}, inplace=True)
print("\n")
print(tabulate(df.head(), headers="keys", tablefmt="pretty"))

# round test scores to nearest whole number
df["test_score"] = round(df["test_score"], 0).astype(int)
print("\n")
print(tabulate(df.head(), headers="keys", tablefmt="pretty"))

# If any student has an attendance percentage less than 70%, flag it as "Low Attendance" in a new column
# "attendance flag". Conversely, if above 90%, flag as “high attendance”. And anything else as “Medium”.


def attendance(x):
    if x["attendance_percentage"] < 0.7:
        return "Low Attendance"
    elif x["attendance_percentage"] > 0.9:
        return "High Attendance"
    else:
        return "Medium Attendance"


df["attendance_flag"] = df.apply(lambda x: attendance(x), axis=1)
print("\n")
print(tabulate(df.head(), headers="keys", tablefmt="pretty"))


# output
df.to_csv("D:/Python/PreppinData/2023/2023W22/2023W22_output.csv", index=False)