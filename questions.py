def load_question(conn, course_name, task_info, question_number):
  cursor = conn.cursor()
  question_num = str(task_info)+"_"+str(question_number)
  cursor.execute('SELECT Question FROM course_info WHERE Course = ? AND question_id = ?', (course_name, question_num))
  result = [row[0] for row in cursor.fetchall()]
  if result[0] is None:
    result[0]='Tidak ada pertanyaan.'
  return result[0]
