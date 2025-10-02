Job Info Extractor Project

A Python-based web scraping and search tool that extracts relevant interview and job-related information from websites based on company name, job role, and years of experience. The project uses Firebase Firestore for caching, AES-CBC encryption for unique keys, and Streamlit for a user-friendly UI.

Features

Accepts Company Name, Job Role, and Years of Experience as input.

Uses web scraping (via Trafilatura) to extract relevant content from top search URLs.

Stores scraped content in Firebase Firestore with caching to avoid duplicate scraping.

Automatically updates cached content if older than 30 days.

Corrects minor typos in user inputs using predefined company and role dictionaries.

Preprocesses content with sentence tokenization, stopword removal, and lemmatization.

Displays relevant extracted sentences in a clean Streamlit interface.

Folder Structure
webscraper_project/
│
├── db.py                  # Firebase DB interactions
├── fetch.py               # Main scraper logic (can be modularized)
├── content_preprocess.py  # Preprocessing extracted text
├── crypto.py              # AES-CBC encryption for URL keys
├── utils.py               # Typo correction and input validation
├── constants.py           # Predefined company and job role lists
├── index.py               # Streamlit app
├── requirements.txt       # All required packages
├── serviceAccountKey.json # Firebase service account key
└── README.md

Installation

Clone the repository:

git clone https://github.com/yourusername/webscraper_project.git
cd webscraper_project


Install Python 3.9+ and pip packages:

pip install -r requirements.txt

requirements.txt
streamlit
trafilatura
firebase-admin
pycryptodome
nltk
pyspellchecker


Note: pyspellchecker is optional if you want to remove it and rely only on predefined dictionaries.

Firebase Setup

Create a Firebase project: https://console.firebase.google.com/

Enable Cloud Firestore.

Create a service account and download serviceAccountKey.json.

Place the file in your project root directory.

Usage
Run Streamlit UI
streamlit run index.py


Enter Company Name, Job Role, and Years of Experience.

Click Search.

View relevant extracted sentences from top URLs.

Scraper & DB Workflow

Generate AES-CBC hash key from the URL.

Check if URL content exists in Firebase.

If yes and content is < 30 days old, fetch from Firebase.

If not, scrape content, preprocess, and save in Firebase.

Preprocess content:

Clean text, remove URLs and special characters.

Tokenize sentences.

Remove stopwords and lemmatize.

Keep only meaningful sentences (≥ 30 characters).

Display relevant sentences in the UI.

Input Correction Logic

Uses predefined dictionaries in constants.py for companies and roles.

Applies fuzzy matching (difflib.get_close_matches) to correct typos.

Experience validated against 0–20 years range.

Optional Enhancements

Add dropdowns in Streamlit for company and role to eliminate typos.

Integrate LLM or semantic similarity to rank most relevant sentences.

Add proxy support to avoid being blocked by frequent scraping.

Deploy app on Streamlit Cloud or Heroku for web access.
