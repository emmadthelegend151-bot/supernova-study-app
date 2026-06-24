import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Supernova Portal", page_icon="🌠", layout="wide")

# --- SESSION STATE ---
if "chat_open" not in st.session_state: st.session_state.chat_open = False
if "chat_history" not in st.session_state: st.session_state.chat_history = []
if "app_mode" not in st.session_state: st.session_state.app_mode = "Dashboard"

# --- NEON & DARK MODE STYLING ---
st.markdown("""
    <style>
    /* Global Page Styling */
    .stApp {
        background: radial-gradient(circle at center, #101025, #050505);
        color: #ffffff;
    }
    
    /* Neon Card Style */
    .neon-card {
        background: rgba(20, 20, 40, 0.7);
        border: 2px solid #00f2ff;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 0 15px #00f2ff;
        transition: 0.3s;
    }
    .neon-card:hover { transform: scale(1.02); box-shadow: 0 0 25px #00f2ff; }

    /* Fixed Floating Chat Window */
    .floating-chat {
        position: fixed;
        bottom: 30px;
        right: 30px;
        width: 350px;
        background: #1a1a2e;
        border: 2px solid #bc13fe;
        border-radius: 20px;
        padding: 20px;
        z-index: 9999;
        box-shadow: 0 0 30px #bc13fe;
    }
    </style>
""", unsafe_allow_html=True)

# --- AI BRAIN ---
def get_ai_response(query):
    q = query.lower()
    valid_subjects = ["physics", "math", "computer", "logic", "sudoku", "science", "moment"]
    
    if not any(sub in q for sub in valid_subjects):
        return "I am sorry, I can only assist with Physics, Math, or Computer Science topics. How else can I help with your studies?"
    
    if "moment" in q:
        return "A moment is the turning effect of a force ($M = F \\times d$). Ensure you're measuring the distance from the pivot!"
    elif "logic" in q or "sudoku" in q:
        return "For logic/Sudoku: Break the grid into 3x3 blocks and verify constraints. Always apply backtracking."
    
    return "That's an interesting question! Let's analyze the principles involved."

# --- NAVIGATION ---
st.title("🌠 Supernova Portal")

# Dashboard Content
if st.session_state.app_mode == "Dashboard":
    st.subheader("Your Dashboard")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="neon-card"><h3>📚 Curriculum</h3><p>Physics & Comp Sci Modules</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="neon-card"><h3>🛒 Reward Store</h3><p>Unlock new cursors & themes</p></div>', unsafe_allow_html=True)

# --- FLOATING CHAT LOGIC ---
if st.session_state.chat_open:
    st.markdown('<div class="floating-chat">', unsafe_allow_html=True)
    st.subheader("🤖 Supernova AI")
    
    # Close Button
    if st.button("✖ Close"):
        st.session_state.chat_open = False
        st.rerun()
    
    st.write("How may I help you?")
    
    # Chat Input
    user_q = st.text_input("Ask a question:", key="chat_in")
    if st.button("Send"):
        if user_q:
            resp = get_ai_response(user_q)
            st.session_state.chat_history.append(f"AI: {resp}")
            st.rerun()
            
    for msg in st.session_state.chat_history:
        st.write(msg)
        
    st.markdown('</div>', unsafe_allow_html=True)
else:
    # Button to Open
    if st.button("💬 Chat"):
        st.session_state.chat_open = True
        st.rerun()
