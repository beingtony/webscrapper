# utils.py
from difflib import get_close_matches
from CONSTANTS import COMPANIES, ROLES, YOE_RANGE

def correct_text(input_text, vocabulary):
    """
    Corrects user input string using a predefined vocabulary only.
    Uses fuzzy matching with get_close_matches.
    """
    matches = get_close_matches(input_text, vocabulary, n=1, cutoff=0.6)
    if matches:
        return matches[0]
    return input_text

def correct_query(company, role, experience):
    """
    Returns corrected company, role, and experience strings.
    Maps typos to known valid values from constants.py using predefined lists only.
    """
    corrected_company = correct_text(company, COMPANIES)
    corrected_role = correct_text(role, ROLES)
    corrected_experience = experience.strip()
    if corrected_experience not in YOE_RANGE:
        corrected_experience = "0"  
    return corrected_company, corrected_role, corrected_experience
