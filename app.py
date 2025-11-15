import streamlit as st
from src.detector import CrossModalDetector
from src.fact_checker import FactChecker  # <--- IMPORT NEW FILE

# Page Config
st.set_page_config(page_title="Fake News Guard", layout="wide")

# Initialize Models
@st.cache_resource
def load_models():
    return CrossModalDetector(), FactChecker()

detector, fact_checker = load_models()

st.title("🛡️ Ultimate Fake News Detector")
st.info("Feature 1: AI Consistency Check | Feature 2: Automated Fact-Checking")

# Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Upload News")
    headline = st.text_area("Headline", placeholder="e.g. 'Pope Francis wearing a puffer jacket'")
    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

    if uploaded_file:
        # Save temp image
        with open("temp.jpg", "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.image(uploaded_file, width=300)

with col2:
    st.subheader("2. Investigation Results")
    
    if uploaded_file and headline:
        # --- TAB INTERFACE ---
        tab1, tab2 = st.tabs(["🤖 AI Analysis", "🌍 Fact Check"])
        
        # FEATURE 1: AI Cross-Modal Check
        with tab1:
            if st.button("Run AI Detection"):
                with st.spinner("Analyzing image-text consistency..."):
                    score, label = detector.predict(headline, "temp.jpg")
                
                st.metric("Consistency Score", f"{score:.1f}%")
                if score < 40:
                    st.error(f"🚨 {label}")
                else:
                    st.success(f"✅ {label}")

        # FEATURE 2: Google Fact Check (NEW!)
        with tab2:
            if st.button("Run Fact Check"):
                with st.spinner("Searching global news sources..."):
                    verdict, sources = fact_checker.verify_news(headline)
                
                st.subheader(verdict)
                
                if sources:
                    st.write("---")
                    st.write("**Sources Found:**")
                    for s in sources:
                        # Add icons based on trust
                        icon = "✅" if s['is_trusted'] else "🔗"
                        if s['is_fact_check']: icon = "⚠️"
                        
                        st.markdown(f"{icon} [{s['title']}]({s['url']})")
                        st.caption(f"Source: {s['domain']}")
                else:
                    st.warning("No clear matches found on Google.")