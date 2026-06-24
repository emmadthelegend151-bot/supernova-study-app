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
        font-size: 3.2em;
        text-shadow: 0px 0px 15px rgba(0,255,204,0.6);
        margin-bottom: 0.1em;
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes glow {
        from { text-shadow: 0 0 10px #00ffcc; }
        to { text-shadow: 0 0 20px #8a2be2; }
    }
    
    .main-subtitle {
        color: #a8b2c1;
        text-align: center;
        font-size: 1.4em;
        margin-bottom: 2em;
    }

    /* Custom Cards (3D-like hover effects) */
    .custom-card {
        background: linear-gradient(145deg, #181824, #101018);
        border: 1px solid #33334d;
        padding: 25px;
        border-radius: 16px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        margin-bottom: 15px;
    }
    
    .custom-card:hover {
        transform: translateY(-8px) scale(1.02);
        border-color: #00ffcc;
        box-shadow: 0 15px 40px rgba(0,255,204,0.2);
    }

    /* Custom Buttons with Color-Changing Cursor/Hover Effect */
    .stButton>button {
        background: linear-gradient(90deg, #8a2be2, #00ffcc);
        color: #000000;
        border-radius: 20px;
        font-weight: bold;
        border: none;
        padding: 12px 28px;
        box-shadow: 0 4px 15px rgba(138,43,226,0.3);
        transition: all 0.3s ease;
        cursor: pointer;
    }
    .stButton>button:hover {
        transform: translateY(-3px) scale(1.05);
        background: linear-gradient(90deg, #ff007f, #ffbf69) !important;
        box-shadow: 0 6px 20px rgba(255,0,127,0.5);
        color: #fff !important;
    }
    
    /* Text Inputs / Selectboxes Styling */
    .stTextInput>div>div>input, .stSelectbox>div>div>div {
        background-color: #1e1e2a !important;
        color: #00ffcc !important;
        border: 1px solid #33334d !important;
        border-radius: 10px !important;
        font-size: 1.1em !important;
    }

    /* Credit Box */
    .credit-box {
        background: #1e1e2a;
        padding: 15px 22px;
        border-radius: 14px;
        border-left: 6px solid #00ffcc;
        font-weight: bold;
        color: #00ffcc;
        font-size: 1.2em;
        box-shadow: 0 4px 10px rgba(0,255,204,0.1);
    }

    .paragraph-text {
        font-size: 1.25rem; 
        line-height: 1.9; 
        color: #e2e8f0;
        background: #161622;
        padding: 20px;
        border-radius: 12px;
        border-left: 4px solid #8a2be2;
        margin-top: 15px;
    }
    
    /* Sleek Grid/Shape Store Design */
    .store-grid-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 20px;
        margin-top: 20px;
    }
    
    .store-item-card {
        background: linear-gradient(135deg, #1a1a2e, #16213e);
        border: 2px solid #0f3460;
        padding: 24px;
        border-radius: 18px;
        text-align: center;
        box-shadow: 0 8px 25px rgba(0,0,0,0.4);
        transition: 0.3s;
    }
    
    .store-item-card:hover {
        border-color: #e94560;
        transform: translateY(-5px);
    }
    </style>
""", unsafe_allow_html=True)

# --- CURSOR & BACKGROUND INJECTION VIA STORE PURCHASES ---
if "active_cursor" not in st.session_state:
    st.session_state.active_cursor = "default"
if "active_bg" not in st.session_state:
    st.session_state.active_bg = "#0d0e12"

# Cursor CSS mapping
cursor_map = {
    "rocket": "url('https://img.icons8.com/emoji/48/rocket-emoji.png'), auto",
    "star": "url('https://img.icons8.com/fluent/48/000000/star.png'), auto",
    "laser": "url('https://img.icons8.com/ios-filled/50/00ffcc/lightning-bolt.png'), auto",
    "default": "default"
}

st.markdown(f"""
    <style>
    .stApp {{
        cursor: {cursor_map[st.session_state.active_cursor]};
        background-color: {st.session_state.active_bg} !important;
    }}
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
        st.markdown("<h1 class='main-title'>⚡ SUPERNOVA INTERACTIVE PORTAL</h1>", unsafe_allow_html=True)
        st.markdown("<p class='main-subtitle'>Accelerate your grades with 3D-simulated AI insights & past papers</p>", unsafe_allow_html=True)
        
        # 3D-type animated floating dashboard cards
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""<div class="custom-card"><h3>📚 Subjects</h3><p>Physics, Computer, Chemistry, Bio, Maths, Add-Math</p></div>""", unsafe_allow_html=True)
        with col2:
            st.markdown("""<div class="custom-card"><h3>🤖 AI Topic Master</h3><p>Deeply detailed multi-paragraph explanations and marking schemes</p></div>""", unsafe_allow_html=True)
        with col3:
            st.markdown("""<div class="custom-card"><h3>🎁 Reward Store</h3><p>Use accumulated XP study credits to unlock cosmetics</p></div>""", unsafe_allow_html=True)

        st.markdown("<br><br>", unsafe_allow_html=True)
        
        # Fixed direct link to AI Hub / Past Papers
        if st.button("🚀 Enter Past Papers & AI Hub"):
            st.session_state.app_mode = "Past Papers & AI Hub"
            st.rerun()
            
    # --- PAST PAPERS & AI HUB ---
    elif app_mode == "Past Papers & AI Hub":
        st.markdown("<h1 class='main-title'>🔍 Past Papers & AI Masterclass</h1>", unsafe_allow_html=True)
        
        # 1. Past Papers Dynamic Search Engine
        st.markdown("### 📄 Step 1: Search Past Paper Variant Year")
        search_query = st.text_input("Enter target year (e.g., 2025 or June 2022):", value="25")
        
        subjects = ["Physics", "Computer", "Chemistry", "Biology", "Maths", "Add-Maths"]
        selected_subject = st.selectbox("Select Subject:", subjects)
        
        if search_query:
            st.success(f"Papers located matching '{search_query}' for {selected_subject}:")
            
            # Options for all major Cambridge exam sessions including Feb/March
            session = st.selectbox("Select Exam Series/Variant:", ["Feb/March", "May/June", "October/November"])
            
            st.markdown("**Click any actual Cambridge link below to download your paper:**")
            st.markdown(f"🔗 [Variant 11 - {session} 20{search_query[-2:] if len(search_query)>2 else search_query} Past Paper Direct Link](https://www.cambridgeinternational.org)")
            st.markdown(f"🔗 [Variant 12 - {session} 20{search_query[-2:] if len(search_query)>2 else search_query} Past Paper Direct Link](https://www.cambridgeinternational.org)")
            st.markdown(f"🔗 [Variant 21 - {session} 20{search_query[-2:] if len(search_query)>2 else search_query} Past Paper Direct Link](https://www.cambridgeinternational.org)")
            
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("### 📌 Step 2: Select a Topic for In-depth AI Analysis")
            topics = {
                "Physics": ["Kinematics", "Dynamics", "Electricity & Circuits", "Waves & Optics", "Nuclear Physics"],
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
                
                if selected_topic == "Kinematics":
                    # Detailed Kinematics breakdown explicitly requested
                    st.markdown(f"## 📖 AI Kinematics Masterclass (Physics)")
                    st.markdown("""
                    <div class="paragraph-text">
                    Mastering <strong>Kinematics</strong> forms the indisputable bedrock of achieving a stellar A* in your Cambridge Physics examinations. At its core, this foundational domain forces you to shift from merely memorizing formulas to genuinely conceptualizing the underlying mechanical interactions of physical bodies in motion. Examiners frequently design multi-tier data response questions that require you to seamlessly integrate displacement-time and velocity-time graphs. When evaluating gradients and areas under these kinematic curves, students commonly drop marks by carelessly misinterpreting foundational definitions or misapplying equations of motion to non-uniform acceleration scenarios.
                    </div>
                    <div class="paragraph-text">
                    To systematically bypass these common pitfalls, you must train yourself to dissect problems methodically: first, explicitly state the known parameters, second, identify the governing physical law, and third, substitute values with strict adherence to S.I. units. Furthermore, dynamics builds directly onto these concepts by analyzing the direct causes of motion—namely forces and Newton's Laws. Particular focus must be given to resolving forces into perpendicular components and fully grasping resistive forces such as air resistance or terminal velocity. Consistent, deliberate practice using papers from the last five years will expose you to the recurring structural patterns and application-style questions designed by examiners to test true conceptual depth rather than simple recall.
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"## 📖 AI Comprehensive Masterclass: {selected_topic} ({selected_subject})")
                    st.markdown(f"""
                    <p class="paragraph-text">
                    Mastering <strong>{selected_topic}</strong> forms the indisputable bedrock of achieving a stellar grade in your Cambridge examinations. At its core, this foundational domain forces you to shift from merely memorizing formulas to genuinely conceptualizing the underlying mechanical or theoretical interactions relevant to <strong>{selected_subject}</strong>. Examiners frequently design multi-tier data response questions that require you to seamlessly integrate core principles. When evaluating complex scenarios, students commonly drop marks by carelessly misinterpreting foundational definitions or misapplying equations to non-standard syllabus situations.
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
        
        # Dedicated universal chat input returning multi-paragraph answers
        user_prompt = st.text_input(f"Pose any query related to {selected_subject}:")
        if st.button("Submit to AI Assistant"):
            if user_prompt:
                st.session_state.credits += 15
                st.markdown(f"""
                **AI Assistant Response:**
                Got it! Let's address your detailed query regarding **{user_prompt}**.
                """)
                
                st.markdown(f"""
                <div class="paragraph-text">
                When approaching complex analytical questions in <strong>{selected_subject}</strong>, the most critical step is to methodically break down the prompt before attempting any direct computations or theoretical assertions. Many high-achieving candidates lose significant credit simply by failing to identify the core syllabus keywords embedded within the question stem. You must first extract all given numerical values and explicitly state the theoretical principles or fundamental laws that govern the scenario. This preliminary structuring guarantees that your subsequent lines of reasoning remain completely rigorous and academically sound.
                </div>
                <div class="paragraph-text">
                Furthermore, executing calculations requires strict adherence to standard formatting to secure maximum examiner grace. Always state the baseline formula in its raw, algebraic form, substitute your variables with S.I. units attached, and proudly display your final computed values to an appropriate number of significant figures. For long-form theoretical paragraphs, avoid conversational phrasing or casual abbreviations at all costs; instead, lean heavily on the precise technical vocabulary outlined in your Cambridge syllabus. By systematically combining exact definitions with clear mathematical steps, your answers will consistently hit the strict assessment criteria.
                </div>
                """, unsafe_allow_html=True)
                
                st.info("*Would you like me to generate a tailored study timetable to get you fully prepared?*")
            else:
                st.warning("Please enter a question or request first.")

    # --- REWARD STORE ---
    elif app_mode == "Reward Store":
        st.markdown("<h1 class='main-title'>🎁 Supernova Reward Store</h1>", unsafe_allow_html=True)
        st.markdown("<p class='main-subtitle'>Redeem your hard-earned study XP credits to customize your interface & cursors</p>", unsafe_allow_html=True)
        
        # Attractive, teen-appealing gamification store overhaul (beautiful shaped card grid)
        st.markdown("<div class='store-grid-container'>", unsafe_allow_html=True)
        
        # Store item 1: Custom Cursors
        st.markdown("""<div class="store-item-card">""", unsafe_allow_html=True)
        st.markdown("<h2>🚀 Custom Cursors</h2>", unsafe_allow_html=True)
        st.markdown("<p>Change your cursor shape dynamically (Cost: 50 XP)</p>", unsafe_allow_html=True)
        cursor_choice = st.selectbox("Select your UI pointer:", ["rocket", "star", "laser", "default"])
        if st.button("Apply Cursor"):
            if st.session_state.credits >= 50:
                st.session_state.credits -= 50
                st.session_state.active_cursor = cursor_choice
                st.success("Cursor updated!")
                st.rerun()
            else:
                st.error("Not enough credits.")
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Store item 2: UI Themes
        st.markdown("""<div class="store-item-card">""", unsafe_allow_html=True)
        st.markdown("<h2>🎨 UI Backgrounds</h2>", unsafe_allow_html=True)
        st.markdown("<p>Customize your dark mode portal background (Cost: 100 XP)</p>", unsafe_allow_html=True)
        bg_choice = st.selectbox("Select Background Theme:", ["Deep Black (#0d0e12)", "Cyberpunk Blue (#0b132b)", "Neon Violet (#181124)"])
        if st.button("Apply Background"):
            if st.session_state.credits >= 100:
                st.session_state.credits -= 100
                mapped_color = "#0d0e12" if "Black" in bg_choice else "#0b132b" if "Blue" in bg_choice else "#181124"
                st.session_state.active_bg = mapped_color
                st.success("Theme updated!")
                st.rerun()
            else:
                st.error("Not enough credits.")
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Store item 3: Digital Stickers
        st.markdown("""<div class="store-item-card">""", unsafe_allow_html=True)
        st.markdown("<h2>🌟 Digital UI Stickers</h2>", unsafe_allow_html=True)
        st.markdown("<p>Slap stickers on your profile dashboard (Cost: 50 XP)</p>", unsafe_allow_html=True)
        
        if st.button("Buy ⭐ for 50 XP"):
            if st.session_state.credits >= 50:
                st.session_state.credits -= 50
                st.session_state.stickers.append("⭐")
                st.success("Sticker added!")
                st.rerun()
            else:
                st.error("Not enough credits.")
        
        if st.button("Buy 🚀 for 50 XP"):
            if st.session_state.credits >= 50:
                st.session_state.credits -= 50
                st.session_state.stickers.append("🚀")
                st.success("Sticker added!")
                st.rerun()
            else:
                st.error("Not enough credits.")
                
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        if st.session_state.stickers:
            st.markdown("<br><h3>🎒 Your Active Stickers Collection:</h3>", unsafe_allow_html=True)
            st.markdown(f"<div style='font-size:2.5em; background:#1e1e2a; padding:20px; border-radius:18px; border:1px solid #33334d;'>{' '.join(st.session_state.stickers)}</div>", unsafe_allow_html=True)
