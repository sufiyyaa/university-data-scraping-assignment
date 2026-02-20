import pandas as pd
# UNIVERSITY DATA (REAL DATA)
universities = [
    [1, "University of Oxford", "UK", "Oxford", "https://www.ox.ac.uk"],
    [2, "University of Cambridge", "UK", "Cambridge", "https://www.cam.ac.uk"],
    [3, "Harvard University", "USA", "Cambridge", "https://www.harvard.edu"],
    [4, "Stanford University", "USA", "Stanford", "https://www.stanford.edu"],
    [5, "University of Toronto", "Canada", "Toronto", "https://www.utoronto.ca"]
]
# COURSE DATA (REAL COURSES)
courses = [
    # Oxford
    [1,1,"Computer Science","Bachelor","Engineering","3 years","Not specified","High school qualification"],
    [2,1,"Law","Bachelor","Law","3 years","Not specified","High school qualification"],
    [3,1,"Medicine","Bachelor","Medical","6 years","Not specified","High school qualification"],
    [4,1,"Philosophy Politics Economics","Bachelor","Social Science","3 years","Not specified","High school qualification"],
    [5,1,"Mathematics","Bachelor","Science","3 years","Not specified","High school qualification"],

    # Cambridge
    [6,2,"Computer Science","Bachelor","Engineering","3 years","Not specified","High school qualification"],
    [7,2,"Engineering","Bachelor","Engineering","4 years","Not specified","High school qualification"],
    [8,2,"Economics","Bachelor","Economics","3 years","Not specified","High school qualification"],
    [9,2,"Law","Bachelor","Law","3 years","Not specified","High school qualification"],
    [10,2,"Mathematics","Bachelor","Science","3 years","Not specified","High school qualification"],

    # Harvard
    [11,3,"Computer Science","Bachelor","Engineering","4 years","Not specified","High school qualification"],
    [12,3,"Business Administration","Master","Business","2 years","Not specified","Bachelor degree"],
    [13,3,"Data Science","Master","Technology","2 years","Not specified","Bachelor degree"],
    [14,3,"Medicine","Doctorate","Medical","4 years","Not specified","Bachelor degree"],
    [15,3,"Law","Doctorate","Law","3 years","Not specified","Bachelor degree"],

    # Stanford
    [16,4,"Computer Science","Bachelor","Engineering","4 years","Not specified","High school qualification"],
    [17,4,"Artificial Intelligence","Master","Technology","2 years","Not specified","Bachelor degree"],
    [18,4,"Electrical Engineering","Bachelor","Engineering","4 years","Not specified","High school qualification"],
    [19,4,"Business","Master","Business","2 years","Not specified","Bachelor degree"],
    [20,4,"Mechanical Engineering","Bachelor","Engineering","4 years","Not specified","High school qualification"],

    # Toronto
    [21,5,"Computer Science","Bachelor","Engineering","4 years","Not specified","High school qualification"],
    [22,5,"Information Technology","Bachelor","Technology","4 years","Not specified","High school qualification"],
    [23,5,"Data Science","Master","Technology","2 years","Not specified","Bachelor degree"],
    [24,5,"Civil Engineering","Bachelor","Engineering","4 years","Not specified","High school qualification"],
    [25,5,"Psychology","Bachelor","Arts","3 years","Not specified","High school qualification"]
]
# CREATE DATAFRAMES
uni_df = pd.DataFrame(universities, columns=[
    "university_id","university_name","country","city","website"
])

course_df = pd.DataFrame(courses, columns=[
    "course_id","university_id","course_name","level",
    "discipline","duration","fees","eligibility"
])
# EXPORT TO EXCEL
with pd.ExcelWriter("university_data.xlsx") as writer:
    uni_df.to_excel(writer, sheet_name="Universities", index=False)
    course_df.to_excel(writer, sheet_name="Courses", index=False)


print("Excel file created successfully!")
