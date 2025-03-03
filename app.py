import streamlit as st
import os

questions = [
    {
        "title": "Spidey Sense",
        "description": "There's something fishy about this image..?",
        "file": "./att/q3-forensics/sherlock.jpeg", 
        "sub_questions": [
            {"question": "Flag ", "answers": ["FLAG{Sh3rl0ck_H0lm3s_221B}"]}
        ]
    },
    {
        "title": "Web Shenanigans",
        "description": "I have hidden secrets on the website, try to find them...",
        "link": "https://gdg-worksop-web.vercel.app/",  # File in your project directory
        "sub_questions": [
            {"question": "Flag Inspect", "answers": ["FLAG{intr0_t0_insp3ct}"]},
            {"question": "Flag MD5", "answers": ["FLAG{Md5_15_n0t_s3cur3}"]},
            {"question": "What is the JWT token for admin on the server", "answers": ["eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiYWRtaW4ifQ.z-AQX6lhhej80JaC1hRx6mJZKklvu-CGPoIk2l-Hy6I"]}
        ]
    },
    {
        "title": "Reversing Reversal",
        "description": "I seem to have stumbled on the password checking system, can you decode it for me.",
        "file": "./att/q2-rev/Password.java", 
        "sub_questions": [
            {"question": "What is the length of the password?", "answers": ["16"]},
            {"question": "Flag what is the password?", "answers": ["FLAG{7036925814}"]}
        ]
    },
    {
        "title": "Interstellar Waves",
        "description": "beep boop beeeeep.",
        "file": "./att/q4-audio/galactus.wav", 
        "sub_questions": [
            {"question": "Encoded Audio 0.0", "answers": ["sp3ctral_an41lysis", "FLAG{sp3ctral_an41lysis}"]},
        ]
    },
    {
        "title": "The More you look the Less you see",
        "description": "FLAG{(35.9086,140.1836)(35.2500,136.7833)(33.5904,130.4017)(36.3222,139.0033)}",
        "sub_questions": [
            {"question": "Flag ", "answers": ["FLAG{RIFT}", "FLAG{rift}"]}
        ]
    }
]

# Initialize session state
if 'sub_flags' not in st.session_state:
    st.session_state.sub_flags = {
        i: [False] * len(questions[i]["sub_questions"]) for i in range(len(questions))
    }

# Create tabs for each question
tabs = st.tabs([f"Question {i+1}" for i in range(len(questions))])

for i, tab in enumerate(tabs):
    with tab:
        question_data = questions[i]
        
        # Display the title and description
        st.header(question_data["title"])
        st.write(question_data["description"])
        
        # Handle file downloads
        if "file" in question_data:
            file_path = question_data["file"]
            if os.path.exists(file_path):
                with open(file_path, "rb") as f:
                    st.download_button(
                        label="Download Attached File",
                        data=f,
                        file_name=file_path.split("/")[-1],
                        key=f"file_{i}"
                    )
            else:
                st.error("File not found!")
        
        # Handle links
        if "link" in question_data:
            st.markdown(f"**Attached link:** [Click here]({question_data['link']})")
                        
        # Display sub-questions/flags
        st.subheader("Flags:")
        for j, sub_question in enumerate(question_data["sub_questions"]):

            st.write(f"{sub_question['question']}")

            col1, col2 = st.columns([4, 1])
            
            with col1:
                # Text input for answer
                sub_user_answer = st.text_input(
                    "Enter flag:",
                    key=f"sub_input_{i}_{j}",
                    label_visibility="collapsed",
                    
                )
            
            with col2:
                # Submit button
                if st.button("Submit", key=f"sub_btn_{i}_{j}"):
                    if sub_user_answer.strip().lower() in [ans.lower() for ans in sub_question["answers"]]:
                        st.session_state.sub_flags[i][j] = True
                        st.toast("Correct!", icon='✅')
                    else:
                        st.session_state.sub_flags[i][j] = False
                        st.toast("Incorrect!", icon='❌')

# Run the app
if __name__ == "__main__":
    pass