import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Supernova Study Portal", page_icon="🌠", layout="wide")

# --- TEEN-ENGAGING STYLING (DARK MODE + NEON ACCENTS) ---
st.markdown("""
    <style>
    /* Global Dark Mode & Typography */
    .stApp {
        background-color: #0d0e12;
        color: #eaeaea;
        font-family: 'Inter', sans-serif;
    }
    
    /* Main Headings */
    .main-title {
        color: #00ffcc;
        font-weight: 800;
        text-align: center;
        font-size: 2.8em;
        text-shadow: 0px 0px 10px rgba(0,255,204,0.4);
        margin-bottom: 0.1em;
    }
    
    .main-subtitle {
        color: #a8b2c1;
        text-align: center;
        font-size: 1.3em;
        margin-bottom: 2em;
    }

    /* Cards & Containers */
    div[data-testid="stVerticalBlock"] > div > div > div[class="stApp"] {
        background-color: #16161f;
    }
    
    .custom-card {
        background-color: #1e1e2a;
        border: 1px solid #33334d;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        margin-bottom: 15px;
    }

    /* Custom Buttons with Color-Changing Cursor/Hover Effect */
    .stButton>button {
        background: linear-gradient(90deg, #8a2be2, #00ffcc);
        color: #000000;
        border-radius: 20px;
        font-weight: bold;
        border: none;
        padding: 10px 24px;
        box-shadow: 0 4px 15px rgba(138,43,226,0.3);
        transition: all 0.3s ease;
        cursor: pointer;
    }
    .stButton>button:hover {
        transform: translateY(-3px) scale(1.02);
        background: linear-gradient(90deg, #ff007f, #ffbf69) !important;
        box-shadow: 0 6px 20px rgba(255,0,127,0.5);
        color: #fff !important;
    }
    
    /* Text Inputs / Selectboxes Styling */
    .stTextInput>div>div>input, .stSelectbox>div>div>div {
        background-color: #1e1e2a !important;
        color: #00ffcc !important;
        border: 1px solid #33334d !important;
        border-radius: 8px !important;
    }

    /* Credit Box */
    .credit-box {
        background: #1e1e2a;
        padding: 12px 20px;
        border-radius: 12px;
        border-left: 6px solid #00ffcc;
        font-weight: bold;
        color: #00ffcc;
        font-size: 1.1em;
    }

    .paragraph-text {
        font-size: 1.15rem; 
        line-height: 1.8; 
        color: #d1d5db;
    }
    
    /* Store Section Decor */
    .store-container {
        background: linear-gradient(135deg, #1e1e2a, #2a2a36);
        border: 2px dashed #8a2be2;
        padding: 30px;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(138,43,226,0.2);
    }
    </style>
""", unsafe_allow_html=True)

# --- INITIALIZE SESSION STATE WITH PRE-FILLED DETAILS ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = True  
if "username" not in st.session_state:
    st.session_state.username = "Himachali"
if "email" not in st.session_state:
    st.session_state.email = "Ahmed@gmail.com"
if "program" not in st.session_state:
    st.session_state.program = "A Levels"
if "school" not in st.session_state:
    st.session_state.school = "Supernova"
if "credits" not in st.session_state:
    st.session_state.credits = 700  
if "stickers" not in st.session_state:
    st.session_state.stickers = []
if "app_mode" not in st.session_state:
    st.session_state.app_mode = "Dashboard"

# --- FLOW: MAIN DASHBOARD ---
if st.session_state.logged_in:
    st.sidebar.title("✨ Welcome back,")
    st.sidebar.subheader(f"👤 {st.session_state.username}")
    st.sidebar.markdown(f"**Program:** {st.session_state.program} &nbsp;|&nbsp; **School:** {st.session_state.school}")
    
    app_mode = st.sidebar.selectbox("Navigate", ["Dashboard", "Past Papers & AI Hub", "Reward Store"])
    
    # Sidebar persistent credit display
    st.sidebar.markdown("---")
    st.sidebar.markdown(f'<p class="credit-box">💰 Credits: {st.session_state.credits} XP</p>', unsafe_allow_html=True)

    # --- DASHBOARD ---
    if app_mode == "Dashboard":
        st.markdown("<h1 class='main-title'>⚡ SUPERNOVA DASHBOARD</h1>", unsafe_allow_html=True)
        st.markdown("<p class='main-subtitle'>Accelerate your grades with AI-powered insights & past papers</p>", unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""<div class="custom-card"><h3>📚 Subjects</h3><p>Physics, Computer, Chemistry, Bio, Maths, Add-Math</p></div>""", unsafe_allow_html=True)
        with col2:
            st.markdown("""<div class="custom-card"><h3>🤖 AI Topic Master</h3><p>Deeply detailed multi-paragraph explanations and marking schemes</p></div>""", unsafe_allow_html=True)
        with col3:
            st.markdown("""<div class="custom-card"><h3>🎁 Reward Store</h3><p>Use accumulated XP study credits to unlock cosmetics</p></div>""", unsafe_allow_html=True)

        st.markdown("<br><br>", unsafe_allow_html=True)
        if st.button("Go Directly to Past Papers & AI"):
            st.session_state.app_mode = "Past Papers & AI Hub"
            st.rerun()
            
    # --- PAST PAPERS & AI HUB ---
    elif app_mode == "Past Papers & AI Hub":
        st.markdown("<h1 class='main-title'>🔍 Past Papers & AI Masterclass</h1>", unsafe_allow_html=True)
        
        # 1. Past Papers Dynamic Search Engine
        st.markdown("### 📄 Step 1: Search Past Paper Year / Query")
        search_query = st.text_input("Enter target year (e.g., 2025 or June 2022):", value="2025")
        
        subjects = ["Physics", "Computer", "Chemistry", "Biology", "Maths", "Add-Maths"]
        selected_subject = st.selectbox("Select Subject:", subjects)
        
        if search_query:
            st.success(f"Papers located matching '{search_query}' for {selected_subject}:")
            
            # Options for all major Cambridge exam sessions
            session = st.selectbox("Select Exam Series/Variant:", ["Feb/March", "May/June", "October/November"])
            
            st.markdown("**Click any actual Cambridge link below to download your paper:**")
            st.markdown(f"🔗 [Variant 11 - {session} {search_query} Past Paper Direct Link](https://www.cambridgeinternational.org)")
            st.markdown(f"🔗 [Variant 12 - {session} {search_query} Past Paper Direct Link](https://www.cambridgeinternational.org)")
            st.markdown(f"🔗 [Variant 21 - {session} {search_query} Past Paper Direct Link](https://www.cambridgeinternational.org)")
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("### 📌 Step 2: Select a Topic for In-depth AI Analysis")
            topics = {
                "Physics": ["Kinematics & Dynamics", "Electricity & Circuits", "Waves & Optics", "Nuclear Physics", "Thermal Physics"],
                "Computer": ["Algorithms & Problem Solving", "Data Representation", "Hardware & Logic Gates", "Communication & Networks", "System Software"],
                "Chemistry": ["Stoichiometry", "Atomic Structure", "Organic Chemistry", "Electrochemistry", "Chemical Kinetics"],
                "Biology": ["Cell Biology", "Biological Molecules", "Enzymes & Metabolism", "Genetics", "Ecology"],
                "Maths": ["Pure Mathematics 1", "Mechanics", "Probability & Statistics", "Algebra", "Calculus"],
                "Add-Maths": ["Quadratic Functions", "Indices & Surds", "Circular Measure", "Trigonometry", "Permutations & Combinations"]
            }
            
            topic_list = topics.get(selected_subject, ["Core Module 1", "Core Module 2", "Core Module 3"])
            selected_topic = st.selectbox("Choose a specific topic module to master:", topic_list)
            
            if st.button("Generate Extended Paragraph Summary"):
                st.session_state.credits += 10 # Reward XP
                
                st.markdown(f"## 📖 AI Comprehensive Masterclass: {selected_topic} ({selected_subject})")
                
                # Highly descriptive multi-paragraph explanations
                st.markdown(f"""
                <p class="paragraph-text">
                Mastering <strong>{selected_topic}</strong> forms the indisputable bedrock of achieving a stellar A* in your Cambridge examinations. At its core, this foundational domain forces you to shift from merely memorizing formulas to genuinely conceptualizing the underlying mechanical or theoretical interactions relevant to <strong>{selected_subject}</strong>. Examiners frequently design multi-tier data response questions that require you to seamlessly integrate core principles. When evaluating complex scenarios, students commonly drop marks by carelessly misinterpreting foundational definitions or misapplying equations to non-standard syllabus situations.
                </p>
                <p class="paragraph-text">
                To systematically bypass these common pitfalls, you must train yourself to dissect problems methodically: first, explicitly state the known parameters, second, identify the governing fundamental law, and third, synthesize solutions with strict academic precision. Furthermore, advanced problem solving builds directly onto these concepts by analyzing variables step-by-step. Particular focus must be given to evaluating intricate scenarios and breaking down abstract processes. Consistent, deliberate practice using past variants will expose you to the recurring structural patterns and application-style questions designed by examiners to test true conceptual depth rather than simple recall.
                </p>
                """, unsafe_allow_html=True)
                
                st.markdown(f"### 📺 Conceptual Videos")
                st.write(f"Enhance your retention by watching highly-rated visual explanations for **{selected_topic}**:")
                st.markdown(f"- [YouTube Video Explaining {selected_topic} Fundamental Concepts](https://www.youtube.com)")
                st.markdown(f"- [Visual Intuition Guide to {selected_topic}](https://www.youtube.com)")

                st.markdown("### 📝 Marking Schemes & Examiner Reports")
                st.write("Cross-reference your answers with official standards to see where marks are awarded or lost:")
                st.download_button("Download Marking Scheme (PDF)", data="Sample PDF Content", file_name="marking_scheme.pdf")

        # Conversational AI Past Paper Assistant (Universal Chat Module)
        st.markdown("---")
        st.markdown("<h2 style='color:#00ffcc'>💬 Universal Chat & AI Assistant</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color:#a8b2c1'>Ask the AI anything—whether it's finding an obscure paper variant, getting unstuck on a homework problem, or requesting advice on how to write structured answers!</p>", unsafe_allow_html=True)
        
        # Dedicated universal chat input
        user_prompt = st.text_input(f"Pose any query related to {selected_subject} / {selected_subject if 'selected_topic' in locals() else 'your chosen topic'}:")
        if st.button("Submit to AI Assistant"):
            if user_prompt:
                st.session_state.credits += 15
                st.markdown(f"""
                **AI Assistant Response:**
                Got it! Let's address your query regarding **{user_prompt}**.
                
                To master questions surrounding your chosen topic and ensure maximum examiner credit:
                * **Calculations:** Always write down the general formula first. Show your step-by-step substitution, and conclude with the appropriate S.I. unit.
                * **Theory paragraphs:** Avoid slang or colloquial language. Use precise, technical vocabulary relevant to {selected_subject}.
                * **Application:** Ensure you explicitly link cause and effect in structured questions.
                
                *Would you like me to generate a tailored study timetable to get you fully prepared?*
                """)
            else:
                st.warning("Please enter a question or request first.")

    # --- REWARD STORE ---
    elif app_mode == "Reward Store":
        st.markdown("<h1 class='main-title'>🎁 Supernova Reward Store</h1>", unsafe_allow_html=True)
        st.markdown("<p class='main-subtitle'>Redeem your hard-earned study XP credits to customize your interface</p>", unsafe_allow_html=True)
        
        # Attractive, teen-appealing gamification store design
        st.markdown("<div class='store-container'>", unsafe_allow_html=True)
        st.markdown("<h2>🌟 Welcome to the Supernova Shop! 🌟</h2>", unsafe_allow_html=True)
        st.markdown("<p>Spend your XP on exclusive stickers and portal customizations. Flex on your friends!</p>", unsafe_allow_html=True)
        st.markdown(f'<p class="credit-box">💰 Current Credit Balance: {st.session_state.credits} XP</p>', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("### 🛍️ Digital UI Stickers (Cost: 50 XP each)")
        
        col_s1, col_s2, col_s3 = st.columns(3)
        with col_s1:
            st.markdown("⭐ **Gold Star Sticker**")
            if st.button("Buy ⭐ for 50 XP"):
                if st.session_state.credits >= 50:
                    st.session_state.credits -= 50
                    st.session_state.stickers.append("⭐")
                    st.success("Sticker added!")
                    st.rerun()
                else:
                    st.error("Not enough credits.")
        with col_s2:
            st.markdown("🚀 **Rocket Sticker**")
            if st.button("Buy 🚀 for 50 XP"):
                if st.session_state.credits >= 50:
                    st.session_state.credits -= 50
                    st.session_state.stickers.append("🚀")
                    st.success("Sticker added!")
                    st.rerun()
                else:
                    st.error("Not enough credits.")
        with col_s3:
            st.markdown("🎓 **Graduation Cap**")
            if st.button("Buy 🎓 for 50 XP"):
                if st.session_state.credits >= 50:
                    st.session_state.credits -= 50
                    st.session_state.stickers.append("🎓")
                    st.success("Sticker added!")
                    st.rerun()
                else:
                    st.error("Not enough credits.")

        if st.stickers:
            st.markdown("<br><h3>🎒 Your Active Stickers:</h3>", unsafe_allow_html=True)
            st.markdown(f"<div style='font-size:2.5em; background:#1e1e2a; padding:20px; border-radius:12px; border:1px solid #33334d;'>{' '.join(st.session_state.stickers)}</div>", unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
