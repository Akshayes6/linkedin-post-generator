# LinkedIn Post Generator 🚀

An AI-powered tool to generate LinkedIn posts using LLaMA 3.3 (via Groq) with few-shot learning from real LinkedIn post examples.

## Features
- Generate posts by topic, length, and language
- Supports English and Hinglish
- Few-shot prompting from real LinkedIn examples
- Simple Streamlit UI

## Project Structure
```
├── main.py            # Streamlit app
├── postgen.py         # Post generation logic
├── few_shot.py        # Few-shot example selector
├── llm_helper.py      # LLM setup (Groq)
├── preprocessed.py    # Data preprocessing
├── requirements.txt   # Dependencies
└── data/
    ├── raw_posts.json
    └── processed_posts.json
```

## Setup

1. Clone the repo
   ```bash
   git clone https://github.com/Akshayes6/linkedin-post-generator.git
   cd linkedin-post-generator
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file and add your Groq API key:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. Preprocess posts (first time only)
   ```bash
   python preprocessed.py
   ```

5. Run the app
   ```bash
   streamlit run main.py
   ```

## How It Works
1. Raw LinkedIn posts are preprocessed to extract tags, language, and line count
2. Posts are categorized as Short / Medium / Long
3. When generating, similar posts are fetched as few-shot examples
4. LLaMA 3.3 generates a new post matching your selected topic, length, and language

## Tech Stack
- [Streamlit](https://streamlit.io/) - UI
- [LangChain](https://langchain.com/) - LLM framework
- [Groq](https://groq.com/) - LLM API (LLaMA 3.3 70B)
- [Pandas](https://pandas.pydata.org/) - Data handling
