import streamlit as st

# Αρχικοποίηση session_state για καταγραφή απαντήσεων και αποτελεσμάτων
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "user_answers" not in st.session_state:
    st.session_state.user_answers = []
if "scores" not in st.session_state:
    st.session_state.scores = {}

# Τίτλος και εισαγωγή ομάδας
st.title("📚 Κουίζ για την Παράκτια Διάβρωση")
team_name = st.text_input("🔹 Όνομα Ομάδας", placeholder="π.χ. Ομάδα Δελφίνια")

# Ερωτήσεις και απαντήσεις
questions = [
    {
        "question": "Ποια είναι η κύρια αιτία της παράκτιας διάβρωσης;",
        "type": "radio",
        "options": ["Ο άνεμος", "Τα κύματα", "Η βροχή", "Τα ποτάμια"],
        "answer": "Τα κύματα",
        "explanation": "Τα κύματα φθείρουν τις ακτές με την πάροδο του χρόνου, προκαλώντας διάβρωση."
    },
    {
        "question": "Ποιος τύπος ακτογραμμής είναι πιο ευάλωτος στη διάβρωση;",
        "type": "radio",
        "options": ["Βραχώδης ακτή", "Αμμώδης ακτή", "Ακτή με χορτάρι", "Ακτή με κύματα 90°"],
        "answer": "Αμμώδης ακτή",
        "explanation": "Η άμμος μετακινείται εύκολα από τα κύματα και τον άνεμο, προκαλώντας μεγαλύτερη διάβρωση."
    },
    {
        "question": "Ποια από τις παρακάτω επεμβάσεις μειώνει τη διάβρωση;",
        "type": "radio",
        "options": ["Καταστροφή της βλάστησης", "Κατασκευή κτιρίων στην παραλία", "Φύτευση φυτών", "Αφαίρεση άμμου"],
        "answer": "Φύτευση φυτών",
        "explanation": "Τα φυτά συγκρατούν το έδαφος και μειώνουν την ένταση των κυμάτων στην ακτή."
    },
    # Προσθέστε περισσότερες ερωτήσεις εδώ…
]

# Αν δεν έχει γίνει υποβολή, εμφάνιση ερωτήσεων
if not st.session_state.submitted:
    st.markdown("**Απαντήστε τις παρακάτω ερωτήσεις. Οι απαντήσεις καταγράφονται με την υποβολή στο τέλος.**")
    answers = []
    for i, q in enumerate(questions):
        st.markdown(f"**{i+1}. {q['question']}**")
        if q["type"] == "radio":
            user_input = st.radio(
                f"Ερώτηση {i+1}",
                q["options"],
                index=None,
                key=f"q_{i}"
            )
        answers.append(user_input)
    if st.button("✅ Υποβολή Απαντήσεων"):
        if not team_name.strip():
            st.warning("Παρακαλώ εισάγετε το όνομα της ομάδας πριν την υποβολή.")
        elif None in answers:
            st.warning("Παρακαλώ απαντήστε όλες τις ερωτήσεις πριν την υποβολή.")
        else:
            st.session_state.submitted = True
            st.session_state.user_answers = answers

# Μετά την υποβολή
if st.session_state.submitted:
    st.subheader(f"📊 Αποτελέσματα για την ομάδα: {team_name}")
    correct = 0
    for i, q in enumerate(questions):
        st.markdown(f"**{i+1}. {q['question']}**")
        st.markdown(f"Η απάντησή σας: **{st.session_state.user_answers[i]}**")
        if st.session_state.user_answers[i] == q["answer"]:
            st.success("✅ Σωστό!")
            correct += 1
        else:
            st.error(f"❌ Λάθος. Η σωστή απάντηση είναι: **{q['answer']}**")
        st.info(f"💡 {q['explanation']}")

    score = round((correct / len(questions)) * 100, 1)
    st.markdown(f"## 🎯 Συνολικό Σκορ: {correct}/{len(questions)} ({score}%)")

    # Καταγραφή σκορ ομάδας
    st.session_state.scores[team_name] = score

    # Εμφάνιση συγκεντρωτικών αποτελεσμάτων
    if len(st.session_state.scores) > 1:
        st.subheader("📋 Συγκεντρωτικά Αποτελέσματα Ομάδων")
        for name, sc in st.session_state.scores.items():
            st.markdown(f"**{name}**: {sc}%")



st.markdown("---")
st.caption("Δημιουργήθηκε για εκπαιδευτική χρήση από τον/την εκπαιδευτικό σας 👩‍🏫")
