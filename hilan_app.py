import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="HILAN – Human-in-the-Loop AI Network", layout="centered")

# --- Title ---
st.title("🤖 HILAN – Human-in-the-Loop AI")
st.caption("AI answers you can trust – because humans verify them.")

# --- Tabs for User and Validator ---
tab1, tab2 = st.tabs(["User", "Validator"])

# -----------------------------
# USER SIDE
# -----------------------------
with tab1:
    st.header("Ask a Question")
    question = st.text_area("Type your question here:")

    if st.button("Generate AI Draft"):
        # Fake AI Draft (for prototype – replace with OpenAI later)
        ai_answer = "AI Draft: Artificial Intelligence is the simulation of human intelligence by machines."
        st.subheader("AI Draft Answer")
        st.info(ai_answer)

        if st.button("Send for Human Verification"):
            st.success("✅ Your answer has been sent to validators. Please check back soon.")

# -----------------------------
# VALIDATOR SIDE
# -----------------------------
with tab2:
    st.header("Validator Dashboard")

    # Example pending task
    pending_task = {
        "question": "What is AI?",
        "ai_answer": "AI Draft: Artificial Intelligence is the simulation of human intelligence by machines."
    }

    st.subheader("Pending Review Task")
    st.write("**Question:**", pending_task["question"])
    st.write("**AI Draft Answer:**", pending_task["ai_answer"])

    action = st.radio("Choose action:", ["Approve", "Edit", "Reject"], key="validator_action")

    edit_answer = ""
    if action == "Edit":
        edit_answer = st.text_area("Edit the AI answer:")

    if st.button("Submit Review"):
        if action == "Approve":
            st.success("✅ Approved. Human-Verified Answer saved.")
        elif action == "Edit":
            st.success(f"✏️ Edited Answer saved: {edit_answer}")
        else:
            st.error("❌ Rejected. This AI answer was not valid.")

    st.write("---")
    st.subheader("Earnings")
    st.metric("Tasks Completed", 5)
    st.metric("Balance", "€2.50")
