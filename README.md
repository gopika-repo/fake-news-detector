# 🛡️ Ultimate Fake News Detector

This project is a multi-layered detection tool that fights misinformation using a powerful hybrid approach. It combines AI-driven content analysis with real-world fact-checking to identify fake news that simpler detectors would miss.

This application is deployed live on Streamlit Community Cloud.
**[>> Visit the Live App <<](https://fake-news-detector-tzvykj7gd4dz6y4jf6uqdt.streamlit.app)**

---

## 🚀 Key Features

This project uses a "Swiss Cheese Model" of security, where one feature catches the failures of the other.

### 1. 🤖 AI Analysis (Cross-Modal Consistency)
* **What it does:** Uses **OpenAI's CLIP** model to analyze the *semantic consistency* between a news headline (text) and its accompanying image.
* **Answers:** "Does this image *actually match* what the headline is claiming?"
* **Catches:** "Cheapfakes" or "Out-of-Context" media (e.g., a real photo from 2010 used for a fake story today).

### 2. 🌍 Automated Fact-Checking (Web Verification)
* **What it does:** Uses the **DuckDuckGo Search** to scan the live internet for the user's headline.
* **Answers:** "Has a trusted, real-world source (like Reuters, BBC, or Snopes) already confirmed or debunked this story?"
* **Catches:** Sophisticated fakes where the image *does* match the text, but the story *itself* is a lie (like the "AI Pope" example).

---

## 💡 How It Works: The "Pope Test"

This project's advanced logic is best demonstrated by the famous "AI Pope Puffer Jacket" fake.

1.  **The Test:**
    * **Image:** The AI-generated photo of the Pope in a white puffer jacket.
    * **Headline:** "Pope Francis wears luxury puffer jacket."
2.  **The Results:**
    * **Feature 1 (AI):** Returns **✅ High Consistency (e.g., 74%)**. Why? Because the image *does* show a Pope in a puffer jacket. The AI is fooled because the lie is consistent.
    * **Feature 2 (Fact-Check):** Returns **🚨 CAUTION!** Why? Because it finds real-world articles from Snopes and BBC that have already debunked this image as AI-generated.

This proves that *both* features are necessary to build a robust detector.

---

## 🛠️ Tech Stack

This project combines deep learning, web scraping, and a web UI into a single application.

| Category | Technology | Purpose |
| :--- | :--- | :--- |
| **Language** | Python 3.9+ | Core logic |
| **Web App** | Streamlit | Building the interactive frontend |
| **AI Model** | PyTorch & Hugging Face `transformers` | To run the pre-trained `openai/clip-vit-base-patch32` model |
| **Fact-Check** | `duckduckgo-search` | To perform real-time, un-blocked web searches |
| **Image Handling** | `Pillow (PIL)` | To load and process user-uploaded images |
| **Styling** | `TOML` | For custom themeing (e.g., the pink background) |

---

## 💻 How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/gopika-repo/fake-news-detector.git](https://github.com/gopika-repo/fake-news-detector.git)
    cd fake-news-detector
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/Scripts/activate
    ```

3.  **Install all required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

The app will automatically open in your browser.
