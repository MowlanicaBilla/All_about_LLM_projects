import streamlit as st

import os
import sqlite3

import google.generativeai as genai

# Configuring the API key
genai.configure(api_key = '')

# Function to load the Gemini AI model and provide SQL response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response =model.generate_content([prompt[0], question])
    return response.text


# Function to retrieve query from SQL database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()

    for row in rows:
        print(row)

    return rows


prompt = [
    """
    You are an expert in converting English question to SQL query. 
    The SQL database has the name STUDENT and has the following columns: NAME, CLASS, SECTION and MARKS
    \n \n for example, \n Example 1: How many entries of records are present?
    So the SQL command will be something like this - SELECT COUNT(*) FROM STUDENT;
    \n \n Example 2: Tell me all the students studying in Data Science class?
    \n The SQL command for the above question will be like this: 
    SELECT * FROM STUDENT WHERE CLASS = "Data Science"

    Also the SQL code should not have ``` in the beginning or end and provide SQL query in output
    """
]

# Streamlit page
st.set_page_config(page_title = "I can retrieve any SQL query")
st.header("Gemini App to retrieve any query")

question= st.text_input("Input: ", key="input")
submit = st.button("Ask the question")


# If submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    data = read_sql_query(response, "student.db")
    st.subheader("The response is:")
    for row in data:
        print(row)
        st.subheader(row)
