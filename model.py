import streamlit as st

def model_load(conn, course_name, task_info, problem):
  course_name_like = '%'+course_name+'%'
  st.write('COURSE NAME LIKE: ', course_name_like)
  cursor = conn.cursor()
  cursor.execute('SELECT Model_Name FROM course_info WHERE Task = ? AND Course LIKE ? AND Question = ?', (task_info, course_name_like, problem))
  #result = [row[0] for row in cursor.fetchall()]
  result = cursor.fetchone()
  st.write('MODEL USED:',result[0])
  if result is None:
    result =('aesindo-bert-bilstm1_1.h5.',)
    
  return result[0]
