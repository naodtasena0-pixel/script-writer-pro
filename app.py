import streamlit as st
import google.generativeai as genai

# Page Setup
st.set_page_config(page_title="ScriptPro AI", page_icon="🎬")
st.title("🎬 ScriptPro AI: Faceless Script Genius")

# Sidebar for Setup
st.sidebar.header("Configuration")
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    # Set up the AI
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    # User Inputs
    niche = st.selectbox("Select Your Niche", ["Horror/Creepy", "Motivation/Hustle", "Science/What If"])
    topic = st.text_input("What is the video about?", placeholder="e.g. The mystery of the abandoned asylum")

    if st.button("Generate My Viral Script"):
        if topic:
            with st.spinner("Writing your script..."):
                # The Master Prompt
                prompt = f"Write a 1000-word YouTube script for a {niche} channel about {topic}. Include a strong 5-second hook, visual cues in [brackets] for the editor, and punchy, engaging pacing."
                response = model.generate_content(prompt)
                st.subheader("Your Generated Script:")
                st.write(response.text)
        else:
            st.error("Please enter a topic first!")
else:
    st.info("👈 Please enter your Gemini API Key in the sidebar to unlock the tool.")

# Subscription Link
st.sidebar.markdown("---")
st.sidebar.subheader("Pro Version")
st.sidebar.write("Get unlimited scripts and high-retention templates.")
st.sidebar.link_button("🚀 Upgrade to Pro", "https://your-lemon-squeezy-link-later.com")
