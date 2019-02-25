
#%%
import pandas as pd
import numpy as np


#%%
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)
school_d = school_data.rename(columns={'school_name' : 'School Name','type' : 'Type',
                                       'size' : 'Size','budget' : 'Budget'})
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])
school_d.head()


#%%
school_data_complete.head()


#%%
school = school_data_complete.rename(columns={'school_name' : 'School Name',
                                              'type' : 'Type','size' : 'Size','budget' : 'Budget',
                                              'student_name' : 'Student Name','gender' : 'Gender',
                                              'grade' : 'Grade','school_name' : 'School Name',
                                              'reading_score' : 'Reading_Score', 'math_score' : 'Math_Score'})


#%%
school.head()


#%%
print('District Summary')
Total_Schools = school["School Name"].unique()
Total_Schools = len(Total_Schools)
Total_Schools


#%%
Total_Students = school["Student Name"].nunique()
Total_Students


#%%
Total_Budget = school["Budget"].sum()
Total_Budget


#%%
Average_Math_Score = school["Math_Score"].mean()
Average_Math_Score


#%%
Average_Reading_Score = school["Reading_Score"].mean()
Average_Reading_Score


#%%
count_passing_math = school[school["Math_Score"] > 70].count()["School Name"]
count_passing_reading = school[school["Reading_Score"] > 70].count()["School Name"]
overall_passing_count = school[(school["Math_Score"] > 70) & (school["Reading_Score"] > 70)].count()["School Name"]
percent_passing_math = (count_passing_math / Total_Students) * 100
percent_passing_reading = (count_passing_reading / Total_Students) * 100
percent_passing_both = (overall_passing_count / Total_Students) * 100


#%%
percent_passing_both


#%%
count_passing_reading


#%%
District_Summary= pd.DataFrame({"Total Schools":[Total_Schools], "Total Students":[Total_Students],
                               "Total Budget":[Total_Budget], "Average Math Score":[Average_Math_Score],
                               "Average Reading Score":[Average_Reading_Score], "% Passing Math":percent_passing_math,
                               "% Passing Reading":percent_passing_reading, "Overall Passing Rate": percent_passing_both})


#%%
District_Summary = District_Summary[["Total Schools", "Total Students", "Total Budget", "Average Math Score",
                                     "Average Reading Score", "% Passing Math",
                                     "% Passing Reading", "Overall Passing Rate"]]
District_Summary


#%%
print('School Summary')
school_types = school_d.set_index(["School Name"])["Type"]
school_types
per_school_counts = school["School Name"].value_counts()
per_school_counts
per_school_budget = school.groupby(["School Name"]).mean()["Budget"]
per_school_budget
per_student_budget = per_school_budget/ per_school_counts
per_student_budget
avg_math_score = school.groupby(["School Name"]).mean()["Math_Score"]
avg_math_score
avg_reading_score = school.groupby(["School Name"]).mean()["Reading_Score"]
avg_reading_score
school_passing_math =  school[school["Math_Score"] > 70].groupby("School Name").count()["Student Name"]
school_passing_math
school_passing_reading =  school[school["Reading_Score"] > 70].groupby("School Name").count()["Student Name"]
school_passing_reading
percent_passing_math = school_passing_math / per_school_counts * 100
percent_passing_math
percent_passing_reading = school_passing_reading / per_school_counts * 100
percent_passing_reading
overall_passing_rate = (percent_passing_math + percent_passing_reading) / 2
overall_passing_rate


#%%
school_types = school_d.set_index(["School Name"])["Type"]
school_types


#%%
School_Summary = pd.DataFrame({"School Type":school_types, "Total Students":per_school_counts,
                                "Total School Budget":per_school_budget, "Per Student Budget":per_student_budget,
                                "Average Math Score":avg_math_score, "Average Reading Score":avg_reading_score,
                                "% Passing Math":percent_passing_math, "% Passing Reading":percent_passing_reading,
                                "Overall Passing rate":overall_passing_rate})                                        
    
    
School_Summary = School_Summary[["School Type","Total Students","Total School Budget","Per Student Budget",
                                  "Average Math Score","Average Reading Score","% Passing Math","% Passing Reading",
                                 "Overall Passing rate"]]
                             
    
School_Summary["Total School Budget"] = School_Summary["Total School Budget"].map("${:,.2f}".format)
School_Summary["Per Student Budget"] = School_Summary["Per Student Budget"].map("${:,.2f}".format)
School_Summary


#%%
print('Top Performing Schools (By Passing Rate)')
Top_School = School_Summary.sort_values(["Overall Passing rate"], ascending = False)
Top_School.head(8)


#%%
print('Bottom Performing Schools (By Passing Rate)')
Bottom_School = School_Summary.sort_values(["Overall Passing rate"], ascending = True)
Bottom_School.head(7)


#%%
print('Math Scores by Grade')
nineth_grade =  school[school["Grade"] == "9th"].groupby("School Name").mean()["Math_Score"]
tenth_grade =  school[school["Grade"] == "10th"].groupby("School Name").mean()["Math_Score"]
eleventh_grade=  school[school["Grade"] == "11th"].groupby("School Name").mean()["Math_Score"]
twelveth_grade =  school[school["Grade"] == "12th"].groupby("School Name").mean()["Math_Score"]
    
# Math score by grade in table form
Math_score_by_grade_dataframe = pd.DataFrame({"9th":nineth_grade, "10th":tenth_grade,
                                              "11th":eleventh_grade,"12th":twelveth_grade})            
#grade_Wise_Math_Score= math_score_by_grade_dataframe[["9th", "10th", "11th", "12th"]]
#grade_Wise_Math_Score.index.name = None
#grade_Wise_Math_Score
Math_score_by_grade_dataframe


#%%
print('Reading Scores by Grade')
nineth_grade =  school[school["Grade"] == "9th"].groupby("School Name").mean()["Reading_Score"]
tenth_grade =  school[school["Grade"] == "10th"].groupby("School Name").mean()["Reading_Score"]
eleventh_grade=  school[school["Grade"] == "11th"].groupby("School Name").mean()["Reading_Score"]
twelveth_grade =  school[school["Grade"] == "12th"].groupby("School Name").mean()["Reading_Score"]
    
# Reading score by grade in table form
Reading_score_by_grade_dataframe = pd.DataFrame({"9th":nineth_grade, "10th":tenth_grade,
                                              "11th":eleventh_grade,"12th":twelveth_grade})            
#grade_Wise_Reading_Score= math_score_by_grade_dataframe[["9th", "10th", "11th", "12th"]]
#grade_Wise_Reading_Score.index.name = None
#grade_Wise_Reading_Score
Reading_score_by_grade_dataframe


#%%
print('Scores by School Spending')
spending_bins = [0, 585, 615, 645, 675]
spending_ranges = ["<585", "585-615", "615-645", "645-675"]
School_wise_Summary["Spending Ranges (Per Student)"] = pd.cut(per_student_budget, spending_bins, labels = spending_ranges)
    
spending_passing_math =  School_wise_Summary.groupby(["Spending Ranges (Per Student)"]).mean()['% Passing Math']
spending_passing_reading =  School_wise_Summary.groupby(["Spending Ranges (Per Student)"]).mean()['% Passing Reading']
spending_math_score = School_wise_Summary.groupby(["Spending Ranges (Per Student)"]).mean()['Average Math Score']
Spending_reading_score = School_wise_Summary.groupby(["Spending Ranges (Per Student)"]).mean()['Average Reading Score']
overall_passing_rate =  (spending_math_score + Spending_reading_score) / 2
Spending_Score = pd.DataFrame({"Average Math Score":spending_math_score, "Average Reading Score":Spending_reading_score,
                                "% Passing Math":spending_passing_math,"% Passing Reading":spending_passing_reading,
                                "Overall Passing Rate":overall_passing_rate})
Spending_Score = Spending_Score[["Average Math Score", "Average Reading Score",
                                   "% Passing Math","% Passing Reading","Overall Passing Rate"]]
Spending_Score


#%%
print('Scores by School Size')
size_bins = [0, 1000, 2000, 5000]
size_ranges = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]
School_Summary["School Size"] = pd.cut(School_Summary["Total Students"], size_bins, labels = size_ranges)

avg_reading_score = School_Summary.groupby(["School Size"]).mean()['Average Reading Score']
percent_passing_reading =  School_Summary.groupby(["School Size"]).mean()['% Passing Reading']
overall_passing_rate = School_Summary.groupby(["School Size"]).mean()['Overall Passing rate']
avg_math_score = School_Summary.groupby(["School Size"]).mean()['Average Math Score']
percent_passing_math =  School_Summary.groupby(["School Size"]).mean()['% Passing Math']
Size_Score_School = pd.DataFrame({"Average Math Score":avg_math_score, "Average Reading Score":avg_reading_score,
                                    "% Passing Math":percent_passing_math,"% Passing Reading":percent_passing_reading,
                                    "Overall Passing rate":overall_passing_rate})   
Size_Score_School = Size_Score_School[["Average Math Score", "Average Reading Score",
                                       "% Passing Math","% Passing Reading","Overall Passing rate"]]

# Display the data frame
Size_Score_School


#%%
print('Scores by School Type')
reading_percent_passing =  School_Summary.groupby(["School Type"]).mean()['% Passing Reading']
rate_overall_passing = School_Summary.groupby(["School Type"]).mean()['Overall Passing rate']
score_avg_math = School_Summary.groupby(["School Type"]).mean()['Average Math Score']
score_avg_reading = School_Summary.groupby(["School Type"]).mean()['Average Reading Score']
math_percent_passing =  School_Summary.groupby(["School Type"]).mean()['% Passing Math']
Type_Score_School = pd.DataFrame({"Average Math Score":score_avg_math, "Average Reading Score":score_avg_reading,
                                    "% Passing Math":math_percent_passing,
                                    "% Passing Reading":reading_percent_passing,
                                    "Overall Passing rate":rate_overall_passing})            
Type_Score_School = Type_Score_School[["Average Math Score", "Average Reading Score",
                                        "% Passing Math","% Passing Reading","Overall Passing rate"]]
Type_Score_School


#%%



#%%



