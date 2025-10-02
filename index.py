import streamlit as st
from url import get_urls
from content_preprocess import extract_relevant_sentences
from crypto import encrypt_aes_cbc
from db import init_db, get_cached_content, insert_cached_content
import trafilatura
from utils import correct_query


def extract_with_trafilatura(url):
    downloaded = trafilatura.fetch_url(url)
    if downloaded:
        return trafilatura.extract(downloaded)
    return None

def extract_content(url):
    text = extract_with_trafilatura(url)
    return text if text else None

# Streamlit UI
st.title("Job Info Extractor 🔍")

company = st.text_input("Enter Company Name", "")
role = st.text_input("Enter Job Role", "")
experience = st.text_input("Enter Years of Experience", "")

if st.button("Search"):
    if company and role:
        company, role, experience = correct_query(company, role, experience)
        query = f"{company} {role} for {experience} years experience"
        st.write(f"🔎 Searching for: {query}")

        # Initialize Firebase
        db = init_db("serviceAccountKey.json")
        urls = get_urls(query, max_results=5)

        for u in urls:
            st.write(f"🔗 URL: {u}")
            url_key = encrypt_aes_cbc(u)

            cached_content = get_cached_content(db, url_key)
            if cached_content:
                st.info("💾 Fetched from Firebase")
                raw_content, processed_content = cached_content
                relevant_info = processed_content.split("\n")
            else:
                content = extract_content(u)
                if content:
                    relevant_info = extract_relevant_sentences(content)
                    insert_cached_content(db, url_key, content, "\n".join(relevant_info))
                else:
                    relevant_info = []

            if relevant_info:
                st.subheader("📌 Relevant Extracted Sentences:")
                for line in relevant_info:
                    st.write("-", line)
            else:
                st.warning("⚠️ No relevant content found")
