import streamlit as st
from model import predict_mood

st.set_page_config(page_title="MindEase - Mental Health Companion", layout="wide")

# Custom CSS for smooth UI
st.markdown("""
    <style>
    body {
        background-color: #f5f7fa;
    }
    .main {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
    }
    </style>
""", unsafe_allow_html=True)

st.image("images/banner.jpg", use_container_width=True)

st.title("🧠 MindEase - AI Mental Health Companion")

st.sidebar.title("🌿 About")
st.sidebar.write("""
This AI chatbot detects student mood using Machine Learning 
and provides empathetic responses and relaxation tips.
""")

user_input = st.text_area("💬 How are you feeling today?")

if st.button("Analyze My Mood"):
    if user_input.strip() != "":
        mood = predict_mood(user_input)

        if mood == "positive":
            st.success("😊 You seem positive and confident!")
            st.write("✨ Keep doing what makes you happy!")

        elif mood == "negative":
            st.error("😔 You seem stressed or upset.")

            st.image("images/relax.jpg", use_container_width=True)

            st.markdown("### 🌿 Let's Try a 30-Second Breathing Exercise")
            st.write("Inhale for 4 seconds...")
            st.write("Hold for 4 seconds...")
            st.write("Exhale for 4 seconds...")

            st.markdown("### 💙 Remember:")
            st.write("This feeling is temporary. You are stronger than you think.")

            st.image("images/hope.jpg", width=250)

            st.markdown("### ✨ Small Self-Care Tips:")
            st.write("- Drink some water")
            st.write("- Step outside for fresh air")
            st.write("- Talk to a trusted friend")

        else:
            st.info("😐 You seem neutral.")
            st.write("🌸 Try listening to calm music or take a short walk.")

    else:
        st.warning("Please enter something first.")
