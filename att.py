import streamlit as st
import pandas as pd

# List of all students
all_students = ['Sakshi', 'Bhavin', 'Prasad', 'Nairutya']

# Set the title of the app
st.title('Attendance Tracker')

# Initialize session state for attendance if it doesn't exist
if 'attendance' not in st.session_state:
    st.session_state['attendance'] = {}

# Create a form to capture user input
with st.form(key='attendance_form'):
    st.subheader('Mark Attendance')
    name = st.selectbox('Select Student', all_students)
    status = st.selectbox('Select Status', ['Present', 'Absent'])
    submit_button = st.form_submit_button(label='Mark Attendance')

# If the form is submitted, add the name and status to the attendance dictionary
if submit_button:
    st.session_state.attendance[name] = status
    st.success(f'Attendance marked for {name} as {status}')

# Display the overall attendance
st.subheader('Overall Attendance')
# Create a dictionary with all students and their status. If a student's attendance has not been marked, set their status to 'Not Marked'
all_attendance = {student: st.session_state.attendance.get(student, 'Not Marked') for student in all_students}
all_attendance_df = pd.DataFrame(list(all_attendance.items()), columns=['Name', 'Status'])
st.table(all_attendance_df)