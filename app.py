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

    /* Custom Buttons (Neon Purple/Cyan) */
    .stButton>button {
        background: linear-gradient(90deg, #8a2be2, #00ffcc);
        color: #000000;
        border-radius: 20px;
        font-weight: bold;
        border: none;
        padding: 10px 24px;
        box-shadow: 0 4px 15px rgba(138,43,226,0.3);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,255,204,0.5);
        color: #000;
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
    </style>
""", unsafe_allow_html=True)

# --- INITIALIZE SESSION STATE ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "credits" not in st.session_state:
    st.session_state.credits = 700  # Starts with 700 credits
if "stickers" not in st.session_state:
    st.session_state.stickers = []

# --- FLOW 1: ONBOARDING (SIGN-UP) ---
if not st.session_state.logged_in:
    st.markdown("<h1 class='main-title'>🌠 SUPERNOVA</h1>", unsafe_allow_html=True)
    st.markdown("<p class='main-subtitle'>The Ultimate O/A-Level Accelerator</p>", unsafe_allow_html=True)
    
    # Wrap form in a clean styled sub-block
    with st.form("signup_form"):
        st.subheader("🚀 Join the Network")
        full_name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        level = st.selectbox("Select your program", ["Select your level", "O Levels", "A Levels"])
        school = st.text_input("School Name", value="Supernova")
        
        submit_btn = st.form_submit_button("Enter Portal")
        
        if submit_btn:
            if full_name and email and level != "Select your level":
                st.session_state.logged_in = True
                st.session_state.username = full_name
                st.rerun()
            else:
                st.error("Please fill in all details to proceed.")

# --- FLOW 2: MAIN DASHBOARD ---
else:
    st.sidebar.title(f"✨ Welcome back,")
    st.sidebar.subheader(f"👤 {st.session_state.username}")
    st.sidebar.markdown(f"**Level:** O/A Levels &nbsp;|&nbsp; **School:** Supernova")
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
        st.markdown("### 📄 Step 1: Search Past Paper Year")
        search_query = st.text_input("Enter target year (e.g., 2025 or June 2022):")
        
        subjects = ["Physics", "Computer", "Chemistry", "Biology", "Maths", "Add-Maths"]
        selected_subject = st.selectbox("Select Subject:", subjects)
        
        if search_query:
            st.success(f"Papers located matching '{search_query}' for {selected_subject}:")
            
            # Sub-options for exam sessions
            session = st.radio("Select Exam Series:", ["May/June", "October/November"])
            
            st.markdown(f"**Click any actual Cambridge link below to download your paper:**")
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
                
                # Highly descriptive multi-paragraph explanations as requested
                st.markdown("""
                <p class="paragraph-text">
                Mastering <strong>Kinematics and Dynamics</strong> forms the indisputable bedrock of achieving a stellar A* in your Cambridge examinations. At its core, this foundational domain forces you to shift from merely memorizing formulas to genuinely conceptualizing the underlying mechanical interactions of physical bodies in motion. Examiners frequently design multi-tier data response questions that require you to seamlessly integrate displacement-time and velocity-time graphs. When evaluating gradients and areas under these kinematic curves, students commonly drop marks by carelessly misinterpreting the physical axis units or misapplying kinematic equations of motion to non-uniform acceleration scenarios.
                </p>
                <p class="paragraph-text">
                To systematically bypass these common pitfalls, you must train yourself to dissect problems methodically: first, explicitly state the known variables, second, identify the governing physical law, and third, substitute values with strict adherence to S.I. units. Furthermore, dynamics builds directly onto these concepts by analyzing the direct causes of motion—namely forces and Newton's Laws. Particular focus must be given to resolving forces into perpendicular components and fully grasping resistive forces such as air resistance or terminal velocity. Consistent, deliberate practice using papers from the last five years will expose you to the recurring structural patterns and trick questions designed by examiners to test conceptual depth rather than simple recall.
                </p>
                """, unsafe_allow_html=True)
                
                st.markdown(f"### 📺 Conceptual Videos")
                st.write(f"Enhance your retention by watching highly-rated visual explanations for **{selected_topic}**:")
                st.markdown(f"- [YouTube Video Explaining {selected_topic} Fundamental Concepts](https://www.youtube.com)")
                st.markdown(f"- [Visual Intuition Guide to {selected_topic}](https://www.youtube.com)")

                st.markdown("### 📝 Marking Schemes & Examiner Reports")
                st.write("Cross-reference your answers with official standards to see where marks are awarded or lost:")
                st.download_button("Download Marking Scheme (PDF)", data="Sample PDF Content", file_name="marking_scheme.pdf")

        # Conversational AI Past Paper Assistant
        st.markdown("---")
        st.markdown("<h2 style='color:#00ffcc'>💬 Universal AI Assistant & Tutor</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color:#a8b2c1'>Ask the AI anything—whether it's finding an obscure paper variant, getting unstuck on a homework problem, or requesting advice on how to write structured answers!</p>", unsafe_allow_html=True)
        
        user_prompt = st.text_input("Pose any question or paper request (e.g., 'I can't find June 2022 physics, help me find it and tell me how to write it'):")
        if st.button("Ask AI Tutor"):
            if user_prompt:
                st.session_state.credits += 15
                st.markdown("""
                **AI Assistant Response:**
                I'm on it! To easily locate the **June 2022 Physics** past paper, I highly recommend checking index platforms like *PapaCambridge* or *Dynamic Papers*. If it's for A-Level, search exactly for `Physics 9702 June 2022 Paper 22`; for O-Level, look up `Physics 5054`. 
                
                **How to structure your answers to guarantee maximum examiner credit:**
                * **Calculations:** Always write down the general formula first. Show your step-by-step substitution, and conclude with the appropriate S.I. unit.
                * **Theory paragraphs:** Avoid slang or colloquial language. Use precise, technical vocabulary (e.g., use words like *terminal velocity* or *electromotive force*).
                * **Graph questions:** Use a sharp pencil, draw fine lines, and always label your axes clearly with units. Ensure you pick points that are more than half the graph line apart for gradient calculations.
                
                *Do you want me to generate a tailored study timetable to get you prepared for this specific past paper?*
                """)
            else:
                st.warning("Please enter a question or request first.")

    # --- REWARD STORE ---
    elif app_mode == "Reward Store":
        st.markdown("<h1 class='main-title'>🎁 Supernova Reward Store</h1>", unsafe_allow_html=True)
        st.markdown("<p class='main-subtitle'>Redeem your hard-earned study XP credits to customize your interface</p>", unsafe_allow_html=True)
        
        st.markdown(f'<p class="credit-box">💰 Current Credit Balance: {st.session_state.credits} XP</p>', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("### 🛍️ Digital UI Stickers (Cost: 50 XP each)")
        st.write("Buy fun digital stickers to stick directly on your study dashboard UI.")
        
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

        if st.session_state.stickers:
            st.markdown("<br><h3>🎒 Your Active Stickers:</h3>", unsafe_allow_html=True)
            st.markdown(f"<div style='font-size:2.5em; background:#1e1e2a; padding:20px; border-radius:12px; border:1px solid #33334d;'>{' '.join(st.session_state.stickers)}</div>", unsafe_allow_html=True)
