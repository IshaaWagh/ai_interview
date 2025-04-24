import google.generativeai as genai
import mysql.connector
import json
import os
from dotenv import load_dotenv
import io
import re



# Load API Key from .env
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini AI
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro-002")

# Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ishaa123@",
    database="ai_mock_interview"
)
cursor = db.cursor()

# Gemini Setup


# ✅ Function 1: Generate and store feedback for all 5 questions
def generate_feedback_for_interview(user_id, position):
    conn=db
    cursor=conn.cursor(dictionary=True)
    
    cursor.execute("""
        SELECT * FROM interview_feedback
        WHERE user_id = %s AND position = %s AND rating IS NULL
        ORDER BY question_id ASC
    """, (user_id, position))
    rows = cursor.fetchall()

    total_rating = 0

    for row in rows:
        question = row["question"]
        user_answer = row["user_answer"]
        qid = row["question_id"]

        # Prompt to Gemini
        prompt = f"""Evaluate the following interview answer:
Question: {question}
Answer: {user_answer}

Give the following:
1. Feedback on the answer (1-2 sentences)
2. A better corrected version of the answer
3. Rate the answer out of 3 (just the number)

Return the result in this format:
Feedback: <your feedback>
Correct Answer: <your version>
Rating: <1-3 number only>
"""

        response = model.generate_content(prompt)
        content = response.text.strip()

        try:
            feedback = content.split("Feedback:")[1].split("Correct Answer:")[0].strip()
            correct_answer = content.split("Correct Answer:")[1].split("Rating:")[0].strip()
            rating = int(content.split("Rating:")[1].strip())
        except Exception as e:
            print("Error parsing feedback:", e)
            feedback, correct_answer, rating = "N/A", "N/A", 0

        total_rating += rating

        # Update DB row
        cursor.execute("""
            UPDATE interview_feedback
            SET feedback=%s, correct_answer=%s, rating=%s
            WHERE user_id=%s AND position=%s AND question_id=%s
        """, (feedback, correct_answer, rating, user_id, position, qid))

    # Final update: Overall rating out of 10
    overall = round((total_rating / 15) * 10)

    cursor.execute("""
        UPDATE interview_feedback
        SET overall_rating=%s
        WHERE user_id=%s AND position=%s AND overall_rating IS NULL
    """, (overall, user_id, position))

    db.commit()


# ✅ Function 2: Get all feedback info to display in feedback page
def get_feedback_for_display(user_id, position):
    conn=db
    cursor=conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT question, user_answer, correct_answer, feedback, rating, overall_rating
        FROM interview_feedback
        WHERE user_id = %s AND position = %s
        ORDER BY question_id ASC
        LIMIT 5
    """, (user_id, position))
    return cursor.fetchall()


# Generate AI Interview Questions (Using Gemini)
def generate_interview_questions(position, skills, experience):
    prompt = f"""
    Generate 5 technical interview questions(questions that are actually asked during interviews) for a {position} with expertise in {skills} 
    and {experience} years of experience. Just return plain questions line by line without numbering or bullet points.
    """
    model = genai.GenerativeModel("gemini-1.5-pro-002")
    response = model.generate_content(prompt)

    if response.text:
        lines = response.text.strip().split("\n")
        questions = [line.strip("0123456789. ").strip() for line in lines if line.strip()]
        return questions
    return []
def store_answers_in_db(user_id, question_id, question, user_answer,position):
    cursor = db.cursor()

    
    cursor.execute("""
        INSERT INTO interview_feedback(user_id, question_id, question, user_answer,position) 
        VALUES (%s, %s, %s,%s,%s)
    """, (user_id, question_id, question,user_answer,position))

    db.commit()
    cursor.close()
def get_all_answered_questions(user_id, position):
    query = """
        SELECT question_id, question, user_answer
        FROM interview_feedback
        WHERE user_id = %s AND position = %s AND user_answer IS NOT NULL
        ORDER BY question_id
    """
    cursor = db.cursor(dictionary=True)
    cursor.execute(query, (user_id, position))
    results = cursor.fetchall()
    cursor.close()

    # Return as list of (question, answer)
    return [(row['question'], row['user_answer']) for row in results]
   


