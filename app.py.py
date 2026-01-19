
import streamlit as st
import pandas as pd
import plotly.express as px
import google.generativeai as genai

# This adds the logo to the top of your sidebar
st.sidebar.image("logo.png", use_container_width=True)

# 1. SETUP: Securely get your API Key from Streamlit Secrets
try:
    # This pulls the key from the "Secrets" dashboard we will set up next
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except Exception:
    st.error("Missing Gemini API Key. Please add it to your Streamlit Secrets.")

st.set_page_config(page_title="LegalPulse AI", layout="wide")

# --- SIDEBAR DISCLAIMER ---
with st.sidebar:
    st.title("⚖️ LegalPulse Guard")
    st.info("""
    **Professional Disclosure:**
    This tool uses AI to assist in identifying patterns and contradictions. 
    It is a **supplement** to, not a replacement for, human legal review.
    """)
    
    st.warning("""
    **User Responsibility:**
    In accordance with Model Rule 1.1, attorneys must independently 
    verify all AI-generated citations and factual claims before 
    use in any legal proceeding.
    """)
    
    st.markdown("---")
    st.caption("🔒 Data is processed via secure, encrypted API and is not used for model training.")

st.title("⚖️ LegalPulse AI: Transcript Analysis")
st.markdown("---")

# 2. FILE UPLOAD: Accept legal transcripts (PDF or Text)
uploaded_file = st.file_uploader("Upload Deposition Transcript (PDF or TXT)", type=["pdf", "txt"])

if uploaded_file:
    st.success("File uploaded successfully!")
    
    # AI analysis button
    if st.button("🔍 Generate AI Contradiction Report"):
        with st.spinner("Gemini is analyzing the testimony..."):
            try:
                # Initialize the Gemini model
                # CHANGE THIS LINE
                model = genai.GenerativeModel('gemini-2.5-flash')  # Use the current 2026 model
                
                # Convert file to text for the AI
                content = uploaded_file.read().decode("utf-8") if uploaded_file.type == "text/plain" else "Processing PDF..."
                
                # The AI Prompt for legal analysis
                prompt = f"Analyze this legal transcript and identify the top 3 contradictions. Format as a bulleted list: \n\n {content[:5000]}"
                
                response = model.generate_content(prompt)
                
                st.subheader("🚩 Found Contradictions")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"AI Analysis failed: {e}")

    # 3. VISUALIZATION: Case Timeline
    st.subheader("📅 Case Timeline")
    df = pd.DataFrame([
        dict(Event="Initial Statement", Start='2023-01-01', End='2023-01-02', Type="Testimony"),
        dict(Event="Accident Date", Start='2023-02-15', End='2023-02-16', Type="Fact"),
        dict(Event="Contradiction Found", Start='2023-03-10', End='2023-03-12', Type="Alert")
    ])
    fig = px.timeline(df, x_start="Start", x_end="End", y="Event", color="Type")
    st.plotly_chart(fig, use_container_width=True)



