import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime, timedelta


def init_db(cred_path="serviceAccountKey.json"):
    """
    Initializes Firebase Firestore.
    Returns the Firestore client instance.
    """
    if not firebase_admin._apps:  # Prevent re-initialization error
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)
    db = firestore.client()
    return db


def get_cached_content(db, url_key):
    """
    Fetches cached content from Firestore using url_key.
    Checks if data is older than 30 days -> if expired, return None.
    Returns a tuple (raw_content, processed_content) if valid, else None.
    """
    doc_ref = db.collection("cached_content").document(url_key)
    doc = doc_ref.get()
    if doc.exists:
        data = doc.to_dict()
        processed_at = data.get("processed_at")

        if processed_at:
            # Firestore timestamps are in datetime format (UTC)
            if datetime.utcnow() - processed_at.replace(tzinfo=None) > timedelta(days=30):
                print("[⏰ Cache expired: older than 30 days]")
                return None  # Force re-scraping

        return data.get("raw_content"), data.get("processed_content")
    return None


def insert_cached_content(db, url_key, raw_content, processed_content):
    """
    Saves or updates content to Firestore under the url_key document.
    Updates processed_at timestamp.
    """
    doc_ref = db.collection("cached_content").document(url_key)
    doc_ref.set({
        "raw_content": raw_content,
        "processed_content": processed_content,
        "processed_at": datetime.utcnow()  # use system UTC for consistent checking
    })
    print("[💾 Saved/Updated in Firebase]")
