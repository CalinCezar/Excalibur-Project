"""
IMORTANT:
-The student_visualization.py file used here is created when your run the student_data\student_visualization.ipynb 
-Make sure to set up your .env file with the OPENAI_API_KEY

"""



import streamlit as st
import openai
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    st.error("API key is missing!")
else:
    openai.api_key = OPENAI_API_KEY

df = pd.read_csv("student_data\preprocessed_students.csv")
df.columns = df.columns.str.strip()

st.title("Student Study Plan Generator")

st.subheader("Dataset")
st.dataframe(df)

student_id_input = st.text_input("Enter Student ID from the Dataset:")
student_id = student_id_input.strip().upper()

st.subheader("Enter Your Details")
user_data = {
    "studentid": st.text_input("Student ID"),
    "age": st.selectbox("Age", ['18-21', '22-25', '26-30', '31-35']),
    "gender": st.selectbox("Gender", ['Male', 'Female', 'Other']),
    "hs_type": st.selectbox("High School Type", ['State', 'Private', 'Other']),
    "scholarship": st.selectbox("Scholarship", ['None', '50%', '75%', '100%']),
    "work": st.selectbox("Do you work?", ['Yes', 'NoNO']),
    "activity": st.selectbox("Do you participate in activities?", ['Yes', 'No']),
    "partner": st.selectbox("Do you have a partner?", ['Yes', 'No']),
    "salary": st.selectbox("Salary Range", ['$135-200', '$201-270', '$271-340']),
    "transport": st.selectbox("Mode of Transport", ['Bus', 'Private car/taxi', 'Other']),
    "living": st.selectbox("Living Situation", ['Rental', 'With family', 'Dormitory', 'Other']),
    "mother_edu": st.selectbox("Mother's Education", ['Primary school', 'Secondary school', 'High school', 'University']),
    "father_edu": st.selectbox("Father's Education", ['Primary school', 'Secondary school', 'High school', 'University']),
    "#_siblings": st.number_input("Number of Siblings", min_value=0, max_value=10, value=0),
    "kids": st.selectbox("Do you have kids?", ['Yes', 'No']),
    "mother_job": st.selectbox("Mother's Job", ['Housewife', 'Retired', 'Private sector employee', 'Self-employment', 'Other']),
    "father_job": st.selectbox("Father's Job", ['Housewife', 'Retired', 'Private sector employee', 'Self-employment', 'Other']),
    "study_hrs": st.selectbox("Study Hours per Week", ['<5 hours', '6-10 hours', '11-15 hours', '16+ hours']),
    "read_freq": st.selectbox("Read Frequency", ['Never', 'Sometimes', 'Regularly']),
    "read_freq_sci": st.selectbox("Read Frequency (Science)", ['Never', 'Sometimes', 'Regularly']),
    "attend_dept": st.selectbox("Do you attend department lectures?", ['Yes', 'No']),
    "impact": st.selectbox("Impact on Learning", ['Positive', 'Negative', 'None']),
    "attend": st.selectbox("Attend lectures regularly?", ['Yes', 'No']),
    "prep_study": st.selectbox("Study Preparation Method", ['Closest date to the exam', 'Regularly during the semester']),
    "prep_exam": st.selectbox("Exam Preparation Method", ['Always', 'Sometimes', 'Never']),
    "notes": st.selectbox("Do you take notes?", ['Yes', 'No']),
    "listens": st.selectbox("Do you listen to lectures?", ['Yes', 'No']),
    "likes_discuss": st.selectbox("Do you like to discuss in class?", ['Yes', 'No']),
    "classroom": st.selectbox("Classroom Setting", ['Alone', 'With friends', 'Not applicable']),
    "cuml_gpa": st.selectbox("Cumulative GPA", ['<2.00', '2.00-2.49', '2.50-2.99', '3.00-3.49', '3.50+']),
    "exp_gpa": st.selectbox("Expected GPA", ['<2.00', '2.00-2.49', '2.50-2.99', '3.00-3.49', '3.50+']),
    "course_id": st.text_input("Course ID"),
    "grade": st.selectbox("Grade", ['1', '2', '3', '4', '5'])
}

if st.button("Generate Study Plan"):
    prompt = f"""
    Create a personalized study plan for the student with the following details:
    - Student ID: {user_data['studentid']}
    - Age: {user_data['age']}
    - Gender: {user_data['gender']}
    - High School Type: {user_data['hs_type']}
    - Scholarship: {user_data['scholarship']}
    - Work: {user_data['work']}
    - Activity: {user_data['activity']}
    - Partner: {user_data['partner']}
    - Salary: {user_data['salary']}
    - Transport: {user_data['transport']}
    - Living: {user_data['living']}
    - Mother's Education: {user_data['mother_edu']}
    - Father's Education: {user_data['father_edu']}
    - Number of Siblings: {user_data['#_siblings']}
    - Kids: {user_data['kids']}
    - Mother's Job: {user_data['mother_job']}
    - Father's Job: {user_data['father_job']}
    - Study Hours per Week: {user_data['study_hrs']}
    - Read Frequency: {user_data['read_freq']}
    - Read Frequency (Science): {user_data['read_freq_sci']}
    - Attend Department: {user_data['attend_dept']}
    - Impact: {user_data['impact']}
    - Attend: {user_data['attend']}
    - Exam Preparation: {user_data['prep_exam']}
    - Notes: {user_data['notes']}
    - Listens to Lectures: {user_data['listens']}
    - Likes Discussion: {user_data['likes_discuss']}
    - Classroom: {user_data['classroom']}
    - Cumulative GPA: {user_data['cuml_gpa']}
    - Expected GPA: {user_data['exp_gpa']}
    - Course ID: {user_data['course_id']}
    - Grade: {user_data['grade']}
    
    Suggest a personalized study routine, tips to improve their exam preparation, and resources for their weak areas.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300
    )

    study_plan = response['choices'][0]['message']['content'].strip()

    st.subheader("Personalized Study Plan:")
    st.write(study_plan)
