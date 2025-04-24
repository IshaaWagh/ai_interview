# import streamlit as st
# import pandas as pd
# from ai_logic import get_feedback_for_display

# # Set page configuration
# st.set_page_config(
#     page_title="AI Mock Interview Feedback",
#     layout="wide",
#     initial_sidebar_state="collapsed"
# )

# # Custom CSS for better styling
# st.markdown("""
# <style>
#     .main-header {
#         color: #22c55e;
#         font-size: 32px;
#         font-weight: bold;
#     }
#     .sub-header {
#         font-size: 24px;
#         margin-bottom: 20px;
#     }
#     .rating-text {
#         font-size: 18px;
#         font-weight: bold;
#     }
#     .question-box {
#         background-color: #f3f4f6;
#         padding: 15px;
#         border-radius: 8px 8px 0 0;
#         margin-bottom: 0;
#         border: 1px solid #e5e7eb;
#     }
#     .answer-box {
#         background-color: #fee2e2;
#         padding: 15px;
#         border-left: 1px solid #e5e7eb;
#         border-right: 1px solid #e5e7eb;
#         margin-top: 0;
#         margin-bottom: 0;
#     }
#     .correct-answer-box {
#         background-color: #dcfce7;
#         padding: 15px;
#         border-left: 1px solid #e5e7eb;
#         border-right: 1px solid #e5e7eb;
#         margin-top: 0;
#         margin-bottom: 0;
#     }
#     .feedback-box {
#         background-color: #dbeafe;
#         padding: 15px;
#         border-radius: 0 0 8px 8px;
#         border: 1px solid #e5e7eb;
#         border-top: none;
#         margin-top: 0;
#         margin-bottom: 20px;
#     }
#     .rating-badge {
#         background-color: #fee2e2;
#         padding: 5px 10px;
#         border-radius: 5px;
#         font-weight: bold;
#         color: #ef4444;
#         float: right;
#     }
#     .overall-rating {
#         color: #3b82f6;
#         font-weight: bold;
#         font-size: 20px;
#     }
#     .bold-text {
#         font-weight: bold;
#     }
#     .home-button {
#         background-color: #4f46e5;
#         color: white;
#         padding: 10px 20px;
#         border-radius: 5px;
#         text-align: center;
#         text-decoration: none;
#         display: inline-block;
#         font-weight: bold;
#         margin-top: 20px;
#     }
# </style>
# """, unsafe_allow_html=True)

# # This would typically come from your recording and analysis system
# # Here we're just simulating the data
# # def load_interview_data():
# #     # In a real app, this would be loaded from a database or session state
# #     return {
# #         "overall_rating": 7,
# #         "questions": [
# #             {
# #                 "question": "Tell me about your experience with Python programming.",
# #                 "user_answer": "I've been coding in Python for about two years now. I mainly use it for data analysis.",
# #                 "correct_answer": "I have been using Python for [number] years and have built various projects, including [project 1 description]. I'm particularly familiar with [specific Python libraries/frameworks] and have experience with [specific Python patterns or techniques].",
# #                 "feedback": "This answer is very vague. Please provide concrete examples of projects or components you've built using Python. Mention specific libraries or frameworks you're familiar with, and highlight any challenges you faced and how you overcame them.",
# #                 "rating": 1
# #             },
# #             {
# #                 "question": "Describe a challenging project you worked on and how you solved the problems you encountered.",
# #                 "user_answer": "I worked on a data visualization dashboard that had to process large datasets in real-time. We used optimization techniques to improve performance by 40% and implemented data caching to reduce database load. I personally developed the backend API that served the processed data efficiently.",
# #                 "correct_answer": "I worked on [project description] that faced challenges including [specific issues]. To overcome these, I [specific actions taken] which resulted in [measurable outcomes]. Key learnings included [insights gained].",
# #                 "feedback": "Good detailed answer with specific project, challenges, solutions, and quantifiable results. You could strengthen it by mentioning specific technologies used and any team collaboration aspects of the project.",
# #                 "rating": 3
# #             },
# #             {
# #                 "question": "How do you handle tight deadlines and competing priorities?",
# #                 "user_answer": "I just try to work faster when deadlines are tight.",
# #                 "correct_answer": "I approach tight deadlines by first assessing all tasks and prioritizing based on urgency and impact. I communicate proactively with stakeholders about realistic timelines and potential tradeoffs. I use time management techniques like breaking down work into smaller tasks and focusing on high-value items first. If necessary, I identify opportunities to streamline processes or adjust scope while maintaining quality on critical components.",
# #                 "feedback": "This answer lacks depth and doesn't demonstrate effective prioritization skills. A stronger response would include specific strategies for prioritization, communication with stakeholders, and examples of how you've successfully managed tight deadlines in the past.",
# #                 "rating": 1
# #             },
# #             {
# #                 "question": "How do you stay updated with the latest technologies in your field?",
# #                 "user_answer": "I subscribe to several technical newsletters and follow key developers on social media. I also participate in monthly meetups and take online courses on platforms like Coursera and Udemy to build practical skills with new technologies. Recently, I completed a course on microservices architecture and applied it to a side project.",
# #                 "correct_answer": "I stay updated through a combination of methods: following industry publications, participating in professional communities, taking structured courses, working on side projects with new technologies, and attending relevant conferences or meetups. For example, I recently [specific example of learning and applying a new technology].",
# #                 "feedback": "Excellent answer that shows a proactive approach to continuous learning. You provided specific examples of learning methods and recent applications, which demonstrates genuine engagement with professional development.",
# #                 "rating": 3
# #             },
# #             {
# #                 "question": "Explain how you would design a scalable web application architecture.",
# #                 "user_answer": "I would use the cloud for scalability.",
# #                 "correct_answer": "I would design a scalable web architecture using a microservices approach with clear separation of concerns. The frontend would be a static site or SPA served via CDN. Backend services would be containerized, stateless, and deployed on Kubernetes for horizontal scaling. I'd implement caching layers, database sharding, and asynchronous processing for heavy tasks. For data storage, I'd choose appropriate databases based on access patterns. Monitoring and auto-scaling would be set up based on key performance metrics. This architecture provides flexibility to scale individual components as needed.",
# #                 "feedback": "This answer is extremely brief and vague. It shows minimal understanding of scalable architecture principles. You should discuss specific architectural patterns, technologies, and approaches like load balancing, caching strategies, database scaling, containerization, microservices, etc., with explanations of why and how you would implement them.",
# #                 "rating": 1
# #             }
# #         ]
# #     }

# # def display_feedback_page():
# #     # Load interview data
# #     interview_data = load_interview_data()
# user_id = st.session_state["user_id"] 
# position = st.session_state["position"]
#     # Display feedback header
# st.markdown("<div class='main-header'>Congratulation!</div>", unsafe_allow_html=True)
# st.markdown("<div class='sub-header'>Here is your interview feedback</div>", unsafe_allow_html=True)
   
#     # Display overall rating
# st.markdown(f"<div class='rating-text'>Your overall interview rating: <span class='overall-rating'>{interview_data['overall_rating']}/10</span></div>", unsafe_allow_html=True)
# st.markdown("<div class='rating-text'>Find below interview questions with correct answer, your answer and feedback for improvement</div>", unsafe_allow_html=True)
   
#     # Display each question with feedback
# for i, q_data in enumerate(interview_data['questions']):
#     st.markdown(f"""
#         <div class='question-box'>
#             <span>{q_data['question']}</span>
#             <span class='rating-badge'>Rating: {q_data['rating']}</span>
#         </div>
#         """, unsafe_allow_html=True)
       
#     st.markdown(f"""
#         <div class='answer-box'>
#             <span class='bold-text'>Your Answer:</span> {q_data['user_answer']}
#         </div>
#         """, unsafe_allow_html=True)
       
#     st.markdown(f"""
#         <div class='correct-answer-box'>
#             <span class='bold-text'>Correct Answer:</span> {q_data['correct_answer']}
#         </div>
#         """, unsafe_allow_html=True)
       
#     st.markdown(f"""
#         <div class='feedback-box'>
#             <span class='bold-text'>Feedback:</span> {q_data['feedback']}
#         </div>
#         """, unsafe_allow_html=True)
   
#     # Create download button for results
#     results_df = pd.DataFrame({
#         'Question': [q['question'] for q in interview_data['questions']],
#         'Your Answer': [q['user_answer'] for q in interview_data['questions']],
#         'Rating': [q['rating'] for q in interview_data['questions']],
#         'Feedback': [q['feedback'] for q in interview_data['questions']]
#     })
   
#     csv = results_df.to_csv(index=False)
#     st.download_button(
#         label="Download Feedback Results",
#         data=csv,
#         file_name="interview_feedback.csv",
#         mime="text/csv",
#     )
   
#     # Home button
#     st.markdown("""
#     <style>
#         div.stButton > button.go-home {
#             background-color: #004aad;
#             color: white;
#             border: none;
#             border-radius: 10px;
#             font-size: 18px;
#             font-family: 'Segoe UI', sans-serif;
#             font-weight: 600;
#             padding: 10px 24px;
#             transition: background-color 0.3s ease;
#         }
#         div.stButton > button.go-home:hover {
#             background-color: #003080;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Streamlit button with the custom class
#     if st.button("Go Home", key="home_btn"):
#         st.switch_page("pages/dashboard.py")
   
#     # Add footer
#     st.markdown("---")
#     st.markdown("AI Mock Interview Feedback System | Created with Streamlit")

# # Run the feedback page
# display_feedback_page()

import streamlit as st
import pandas as pd
from ai_logic import get_feedback_for_display

# Set page configuration
st.set_page_config(
    page_title="AI Mock Interview Feedback",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        color: #22c55e;
        font-size: 32px;
        font-weight: bold;
    }
    .sub-header {
        font-size: 24px;
        margin-bottom: 20px;
    }
    .rating-text {
        font-size: 18px;
        font-weight: bold;
    }
    .question-box {
        background-color: #f3f4f6;
        padding: 15px;
        border-radius: 8px 8px 0 0;
        margin-bottom: 0;
        border: 1px solid #e5e7eb;
    }
    .answer-box {
        background-color: #fee2e2;
        padding: 15px;
        border-left: 1px solid #e5e7eb;
        border-right: 1px solid #e5e7eb;
        margin-top: 0;
        margin-bottom: 0;
    }
    .correct-answer-box {
        background-color: #dcfce7;
        padding: 15px;
        border-left: 1px solid #e5e7eb;
        border-right: 1px solid #e5e7eb;
        margin-top: 0;
        margin-bottom: 0;
    }
    .feedback-box {
        background-color: #dbeafe;
        padding: 15px;
        border-radius: 0 0 8px 8px;
        border: 1px solid #e5e7eb;
        border-top: none;
        margin-top: 0;
        margin-bottom: 20px;
    }
    .rating-badge {
        background-color: #fee2e2;
        padding: 5px 10px;
        border-radius: 5px;
        font-weight: bold;
        color: #ef4444;
        float: right;
    }
    .overall-rating {
        color: #3b82f6;
        font-weight: bold;
        font-size: 20px;
    }
    .bold-text {
        font-weight: bold;
    }
    div.stButton > button.go-home {
        background-color: #004aad;
        color: white;
        border: none;
        border-radius: 10px;
        font-size: 18px;
        font-family: 'Segoe UI', sans-serif;
        font-weight: 600;
        padding: 10px 24px;
        transition: background-color 0.3s ease;
    }
    div.stButton > button.go-home:hover {
        background-color: #003080;
    }
</style>
""", unsafe_allow_html=True)

# Logout button
if st.button("Logout"):
    st.session_state.clear()
    st.experimental_rerun()

# Require login and position selection
if "user_id" not in st.session_state or "position" not in st.session_state:
    st.error("Please complete a mock interview or log in first.")
    st.stop()

user_id = st.session_state["user_id"]
position = st.session_state["position"]

# Fetch real feedback data
interview_data = get_feedback_for_display(user_id, position)
if not interview_data:
    st.warning("No feedback found. Please complete a mock interview first.")
    st.stop()

# Extract overall rating (same for all rows)
overall_rating = interview_data[0]["overall_rating"]

# Display headers
st.markdown("<div class='main-header'>Congratulation!</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-header'>Here is your interview feedback</div>", unsafe_allow_html=True)

# Display overall rating
st.markdown(
    f"<div class='rating-text'>Your overall interview rating: "
    f"<span class='overall-rating'>{overall_rating}/10</span></div>",
    unsafe_allow_html=True
)
st.markdown("<div class='rating-text'>Find below interview questions with correct answer, your answer and feedback for improvement</div>", unsafe_allow_html=True)

# Loop through each feedback row
for idx, row in enumerate(interview_data, start=1):
    st.markdown(f"""
    <div class='question-box'>
        <span>{row['question']}</span>
        <span class='rating-badge'>Rating: {row['rating']}/3</span>
    </div>
    """, unsafe_allow_html=True)
    st.markdown(f"""
    <div class='answer-box'>
        <span class='bold-text'>Your Answer:</span> {row['user_answer']}
    </div>
    """, unsafe_allow_html=True)
    st.markdown(f"""
    <div class='correct-answer-box'>
        <span class='bold-text'>Correct Answer:</span> {row['correct_answer']}
    </div>
    """, unsafe_allow_html=True)
    st.markdown(f"""
    <div class='feedback-box'>
        <span class='bold-text'>Feedback:</span> {row['feedback']}
    </div>
    """, unsafe_allow_html=True)

# Prepare DataFrame for download
results_df = pd.DataFrame({
    'Question': [r['question'] for r in interview_data],
    'Your Answer': [r['user_answer'] for r in interview_data],
    'Correct Answer': [r['correct_answer'] for r in interview_data],
    'Feedback': [r['feedback'] for r in interview_data],
    'Rating': [r['rating'] for r in interview_data]
})
csv = results_df.to_csv(index=False)

# Download button
st.download_button(
    label="Download Feedback Results",
    data=csv,
    file_name="interview_feedback.csv",
    mime="text/csv",
)

# Go Home button
if st.button("Go Home", key="home_btn", args=None):
    st.switch_page("pages/dashboard.py")

# Footer
st.markdown("---")
st.markdown("AI Mock Interview Feedback System | Created with Streamlit")