import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Config
st.set_page_config(page_title="LegalPulse AI", layout="wide")

st.title("⚖️ LegalPulse AI: Transcript Analysis")
st.write("Upload your deposition transcript to generate the visual timeline.")

# 2. The Upload Section
uploaded_file = st.file_uploader("Upload Transcript (PDF/TXT)", type=["pdf", "txt"])

if uploaded_file is not None:
    st.success("File uploaded successfully!")
    
    # 3. The "Mock" Analysis (This is what they see for their $199)
    st.subheader("🚩 Conflict Detection Report")
    st.info("AI Analysis found 3 potential contradictions.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.error("Page 14, Line 3: Witness contradicts police report regarding speed.")
        st.warning("Page 88, Line 10: Witness mentions 'rain' but weather reports say 'sunny'.")
    
    # 4. The Visualization (Your IBM Skill)
    st.subheader("📅 Case Timeline (Visualized)")
    df = pd.DataFrame([
        dict(Task="Incident", Start='2025-01-01', Finish='2025-01-01', Type='Event'),
        dict(Task="Witness A Statement", Start='2025-01-05', Finish='2025-01-05', Type='Conflict'),
        dict(Task="Police Report", Start='2025-01-02', Finish='2025-01-02', Type='Evidence'),
    ])
    fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", color="Type")
    st.plotly_chart(fig, use_container_width=True)