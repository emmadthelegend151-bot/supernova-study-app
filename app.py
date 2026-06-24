import streamlit as st

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="Supernova Portal", page_icon="🌠", layout="wide")

# --- 2. SESSION STATE (The Memory) ---
if "app_mode" not in st.session_state: st.session_state.app_mode = "Dashboard"
if "chat_open" not in st.session_state: st.session_state.chat_open = False
if "credits" not in st.session_state: st.session_state.credits = 700

# --- 3. CSS (The Styling) ---
st.markdown("""
    <style>
    /* Fixed Chat Window */
    .chat-container {
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 350px;
        height: 500px;
        background: #161622;
        border: 2px solid #8a2be2;
        border-radius: 20px;
        padding: 20px;
        z-index: 9999;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    /* Dashboard Cards */
    .card {
        background: #1c1c2e;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #33334d;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# --- 4. FUNCTIONS (The Brain) ---
def get_ai_tutor_response(query):
    q = query.lower()
    
    # SUBJECT VALIDATOR
    valid_subjects = ["physics", "computer", "math", "logic", "sudoku", "science"]
    if not any(sub in q for sub in valid_subjects):
        return "I am sorry, I do not understand. I am specialized in Physics, Math, and Computer Science. Please ask a question related to these subjects!"
    
    # TEACHING LOGIC
    if "moment" in q:
        return "A moment is the turning effect of a force. Formula: $M = F \\times d$. Remember to use the perpendicular distance from the pivot."
    elif "sudoku" in q or "logic" in q:
        return "To solve Sudoku or logic problems, always define your constraints first. Break the problem into small, solvable steps using boolean logic."
    
    return "That's a great question! Let's break it down by identifying the core principle first."

# --- 5. UI LAYOUT ---

# Header
st.title("🌠 Supernova Study Portal")

# Sidebar
st.sidebar.header("Navigation")
if st.sidebar.button("Dashboard"): st.session_state.app_mode = "Dashboard"; st.rerun()
if st.sidebar.button("Reward Store"): st.session_state.app_mode = "Store"; st.rerun()

# --- MAIN NAVIGATION AREA ---
if st.session_state.app_mode == "Dashboard":
    st.subheader("Welcome to the Hub!")
    st.write("This app is designed to help you master your curriculum.")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="card"><h3>AI Hub</h3><p>Get topic explanations.</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card"><h3>Store</h3><p>Spend your XP.</p></div>', unsafe_allow_html=True)

elif st.session_state.app_mode == "Store":
    st.subheader("Reward Store")
    st.write(f"You have {st.session_state.credits} Credits.")

# --- 6. FLOATING CHAT UI ---
if st.session_state.chat_open:
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    st.subheader("🤖 Supernova AI")
    
    # Close button that actually works
    if st.button("❌ Close Chat"):
        st.session_state.chat_open = False
        st.rerun()
        
    user_q = st.text_input("Ask a question:", key="chat_input")
    if st.button("Send"):
        if user_q:
            st.write(get_ai_tutor_response(user_q))
            
    st.markdown('</div>', unsafe_allow_html=True)
else:
    # Button to open the chat
    if st.button("💬 Open AI Chat"):
        st.session_state.chat_open = True
        st.rerun()
