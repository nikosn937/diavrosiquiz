import streamlit as st

# Αρχικοποίηση μεταβλητών κατάστασης
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = []

if 'submitted' not in st.session_state:
    st.session_state.submitted = False

st.title("🌊 Κουίζ για την Παράκτια Διάβρωση")
st.markdown("**Απάντησε σε όλες τις ερωτήσεις και πάτα 'Υποβολή' στο τέλος για να δεις το σκορ και τις απαντήσεις.**")

# Λίστα ερωτήσεων
quiz = [
    {
        "question": "Τι είναι η παράκτια διάβρωση;",
        "type": "radio",
        "options": [
            "Η δημιουργία νέων ακτών",
            "Η καταστροφή της ακτής λόγω φυσικών φαινομένων",
            "Η κ


st.markdown("---")
st.caption("Δημιουργήθηκε για εκπαιδευτική χρήση από τον/την εκπαιδευτικό σας 👩‍🏫")
