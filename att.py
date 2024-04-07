import streamlit as st
import pandas as pd
import base64

# Function to create a download link for a DataFrame
def create_download_link(df, filename):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    return f'<a href="data:file/csv;base64,{b64}" download="{filename}">Download CSV file</a>'

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

# Add a button to export the attendance data to a CSV file
if st.button('Export to CSV'):
    download_link = create_download_link(all_attendance_df, 'attendance.csv')
    st.markdown(download_link, unsafe_allow_html=True)
