import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Supernova Study Portal", page_icon="🌠", layout="wide")

# --- INITIALIZE SESSION STATE WITH PRE-FILLED DETAILS ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False  # Set to False briefly so intro runs
if "intro_played" not in st.session_state:
    st.session_state.intro_played = False
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

# Sticker wallpaper pattern generator
def get_sticker_wallpaper(stickers):
    if not stickers:
        return "none"
    # Create a repeating background pattern using the unlocked stickers
    sticker_svgs = "".join([f"<text y=\\'50%\\'> {s} </text>" for s in stickers])
    return f"radial-gradient(circle, rgba(138,43,226,0.1) 10%, transparent 10%), linear-gradient(45deg, #0d0e12 25%, transparent 25%)"

# Dynamic Wallpaper & Cursor injection
st.markdown(f"""
    <style>
    .stApp {{
        cursor: {cursor_map[st.session_state.active_cursor]};
        background-color: {st.session_state.active_bg} !important;
        background-image: url('https://www.transparenttextures.com/patterns/cubes.png');
        background-blend-mode: overlay;
    }}
    
    /* Global Dark Mode & Typography */
    .stApp {{
        color: #eaeaea;
        font-family: 'Inter', sans-serif;
    }}
    
    /* Main Headings */
    .main-title {{
        color: #00ffcc;
        font-weight: 800;
        text-align: center;
        font-size: 3.2em;
        text-shadow: 0px 0px 15px rgba(0,255,204,0.6);
        margin-bottom: 0.1em;
        animation: glow 2s ease-in-out infinite alternate;
    }}
    
    @keyframes glow {{
        from {{ text-shadow: 0 0 10px #00ffcc; }}
        to {{ text-shadow: 0 0 20px #8a2be2; }}
    }}
    
    .main-subtitle {{
        color: #a8b2c1;
        text-align: center;
        font-size: 1.4em;
        margin-bottom: 2em;
    }}

    /* Custom Cards (3D-like hover effects) */
    .custom-card {{
        background: linear-gradient(145deg, #181824, #101018);
        border: 1px solid #33334d;
        padding: 25px;
        border-radius: 16px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        margin-bottom: 15px;
    }}
    
    .custom-card:hover {{
        transform: translateY(-8px) scale(1.02);
        border-color: #00ffcc;
        box-shadow: 0 15px 40px rgba(0,255,204,0.2);
    }}

    /* Custom Buttons with Color-Changing Hover Effect */
    .stButton>button {{
        background: linear-gradient(90deg, #8a2be2, #00ffcc);
        color: #000000;
        border-radius: 20px;
        font-weight: bold;
        border: none;
        padding: 12px 28px;
        box-shadow: 0 4px 15px rgba(138,43,226,0.3);
        transition: all 0.3s ease;
        cursor: pointer !important;
    }}
    .stButton>button:hover {{
        transform: translateY(-3px) scale(1.05);
        background: linear-gradient(90deg, #ff007f, #ffbf69) !important;
        box-shadow: 0 6px 20px rgba(255,0,127,0.5);
        color: #fff !important;
    }}
    
    /* Text Inputs / Selectboxes Styling */
    .stTextInput>div>div>input, .stSelectbox>div>div>div {{
        background-color: #1e1e2a !important;
        color: #00ffcc !important;
        border: 1px solid #33334d !important;
        border-radius: 10px !important;
        font-size: 1.1em !important;
    }}

    /* Credit Box */
    .credit-box {{
        background: #1e1e2a;
        padding: 15px 22px;
        border-radius: 14px;
        border-left: 6px solid #00ffcc;
        font-weight: bold;
        color: #00ffcc;
        font-size: 1.2em;
        box-shadow: 0 4px 10px rgba(0,255,204,0.1);
    }}

    .paragraph-text {{
        font-size: 1.25rem; 
        line-height: 1.9; 
        color: #e2e8f0;
        background: #161622;
        padding: 20px;
        border-radius: 12px;
        border-left: 4px solid #8a2be2;
        margin-top: 15px;
        margin-bottom: 15px;
    }}
    
    /* Sleek Gamified Store Grid */
    .store-grid-container {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 25px;
        margin-top: 20px;
    }}
    
    .store-item-card {{
        background: linear-gradient(135deg, #161622, #1f1f38);
        border: 2px solid #3f3f6c;
        padding: 28px;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 10px 35px rgba(0,0,0,0.5);
        transition: all 0.4s ease;
    }}
    
    .store-item-card:hover {{
        border-color: #00ffcc;
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 15px 45px rgba(0,255,204,0.15);
    }}
    
    /* Wallpaper Stickers Layer */
    .sticker- wallpaper-layer {{
        position: fixed;
        top: 0; left: 0; width: 100vw; height: 100vh;
        z-index: -1;
        pointer-events: none;
        opacity: 0.15;
    }}
    </style>
""", unsafe_allow_html=True)

# Wallpaper sticker container
if st.session_state.stickers:
    st.markdown(f"""
    <div class="sticker-wallpaper-layer" style="font-size: 50px;">
        {''.join([f'<span style="position:absolute; top:{i*25}%; left:{j*20}%;">{s}</span>' for i, s in enumerate(st.session_state.stickers) for j in range(5)])}
    </div>
    """, unsafe_allow_html=True)

# --- CINEMATIC INTRO ROCKET / PLANET EXPLOSION ANIMATION ---
if not st.session_state.intro_played:
    # Canvas animation via HTML/JS injection for 2-minute pitch impact
    st.markdown("""
        <div id="intro-container" style="position:fixed; top:0; left:0; width:100vw; height:100vh; background:#0d0e12; z-index:9999; display:flex; align-items:center; justify-content:center; flex-direction:column; animation: fadeOut 0.5s ease-in-out 3.5s forwards;">
            <div style="position:relative; width:300px; height:300px;">
                <div id="rocket" style="position:absolute; bottom:20px; left:20px; font-size:60px; animation: launch 2.2s cubic-bezier(0.25, 1, 0.5, 1) forwards;">🚀</div>
                <div id="planet" style="position:absolute; top:40px; right:40px; width:100px; height:100px; background:radial-gradient(circle at 30% 30%, #ff6b6b, #c9184a); border-radius:50%; box-shadow:0 0 20px #ff6b6b; animation: pulse 1.5s infinite alternate;"></div>
                <div id="explosion" style="position:absolute; top:20px; right:20px; width:140px; height:140px; border-radius:50%; background:radial-gradient(circle, #ffbf69 10%, #ff4757 50%, transparent 80%); transform:scale(0); animation: explode 0.8s ease-in-out 2.2s forwards;"></div>
            </div>
            <h1 id="supernova-text" style="color:#00ffcc; font-size:5em; font-weight:900; opacity:0; text-shadow:0 0 20px #00ffcc; animation: revealText 0.5s ease-in-out 2.5s forwards;">SUPERNOVA</h1>
        </div>
        
        <style>
        @keyframes launch {
            0% { bottom: 20px; left: 20px; transform: rotate(45deg) scale(0.8); }
            100% { bottom: 100px; right: 100px; transform: rotate(45deg) scale(0.8); }
        }
        @keyframes explode {
            0% { transform: scale(0); opacity: 1; }
            50% { transform: scale(1.8); opacity: 0.8; }
            100% { transform: scale(2.5); opacity: 0; }
        }
        @keyframes revealText {
            0% { opacity: 0; transform: translateY(20px); }
            100% { opacity: 1; transform: translateY(0); }
        }
        @keyframes pulse {
            0% { transform: scale(1); }
            100% { transform: scale(1.08); }
        }
        @keyframes fadeOut {
            0% { opacity: 1; visibility: visible; }
            99% { opacity: 0; visibility: visible; }
            100% { opacity: 0; visibility: hidden; z-index: -10; }
        }
        </style>
    """, unsafe_allow_html=True)
    st.session_state.intro_played = True

# --- FLOW: MAIN DASHBOARD ---
st.session_state.logged_in = True  

st.sidebar.title("✨ Welcome back,")
st.sidebar.subheader(f"👤 {st.session_state.username}")
st.sidebar.markdown(f"**Program:** {st.session_state.program} &nbsp;|&nbsp; **School:** {st.session_state.school}")

# Interactivity routing: sidebar handles the current screen explicitly
app_mode = st.sidebar.selectbox("Navigate", ["Dashboard", "Past Papers & AI Hub", "Reward Store"], index=["Dashboard", "Past Papers & AI Hub", "Reward Store"].index(st.session_state.app_mode))
st.session_state.app_mode = app_mode

# Sidebar persistent credit display
st.sidebar.markdown("---")
st.sidebar.markdown(f'<p class="credit-box">💰 Credits: {st.session_state.credits} XP</p>', unsafe_allow_html=True)

# --- DASHBOARD SCREEN ---
if st.session_state.app_mode == "Dashboard":
    st.markdown("<h1 class='main-title'>⚡ SUPERNOVA INTERACTIVE PORTAL</h1>", unsafe_allow_html=True)
    st.markdown("<p class='main-subtitle'>Accelerate your grades with 3D-simulated AI insights & past papers</p>", unsafe_allow_html=True)
    
    # Animated floating dashboard cards
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""<div class="custom-card"><h3>📚 Subjects</h3><p>Physics, Computer, Chemistry, Bio, Maths, Add-Math</p></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class="custom-card"><h3>🤖 AI Topic Master</h3><p>Deeply detailed multi-paragraph explanations and marking schemes</p></div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""<div class="custom-card"><h3>🎁 Reward Store</h3><p>Use accumulated XP study credits to unlock cosmetics</p></div>""", unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Smooth routing button
    if st.button("🚀 Enter Past Papers & AI Hub"):
        st.session_state.app_mode = "Past Papers & AI Hub"
        st.rerun()
        
# --- PAST PAPERS & AI HUB SCREEN ---
elif st.session_state.app_mode == "Past Papers & AI Hub":
    st.markdown("<h1 class='main-title'>🔍 Past Papers & AI Masterclass</h1>", unsafe_allow_html=True)
    
    st.markdown("### 📄 Step 1: Search Past Paper Variant Year")
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
            st.session_state.credits += 10 
            
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
                # Strategic Diagram for Learners
                st.markdown("Visualizing displacement and velocity graphs helps simplify calculations:")
                st.image("https://upload.wikimedia.org/wikipedia/commons/e/ea/Displacement-time.png", caption="Displacement-Time Graph Vector Breakdown")
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
    
    user_prompt = st.text_input(f"Pose any query related to {selected_subject}:")
    if st.button("Submit to AI Assistant"):
        if user_prompt:
            st.session_state.credits += 15
            st.markdown(f"""
            **AI Assistant Response:**
            Got it! Let's address your detailed query regarding **{user_prompt}**.
            """)
            # Multi-paragraph rich explanation as requested by student
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

# --- REWARD STORE SCREEN (HIGH-END NEON / SHAPED GRID) ---
elif st.session_state.app_mode == "Reward Store":
    st.markdown("<h1 class='main-title'>🎁 Supernova Reward Store</h1>", unsafe_allow_html=True)
    st.markdown("<p class='main-subtitle'>Redeem your hard-earned study XP credits to customize your interface, cursors, and app wallpaper</p>", unsafe_allow_html=True)
    
    st.markdown(f'<p class="credit-box" style="text-align:center; margin-bottom:20px;">💰 Current Credit Balance: {st.session_state.credits} XP</p>', unsafe_allow_html=True)
    
    # Beautiful responsive gamification store cards
    st.markdown("<div class='store-grid-container'>", unsafe_allow_html=True)
    
    # Store item 1: Custom Cursors
    st.markdown("""<div class="store-item-card">""", unsafe_allow_html=True)
    st.markdown("<h2>🚀 Custom Cursors</h2>", unsafe_allow_html=True)
    st.markdown("<p>Change your UI pointer shape (Cost: 50 XP)</p>", unsafe_allow_html=True)
    cursor_choice = st.selectbox("Select pointer style:", ["rocket", "star", "laser", "default"])
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
    st.markdown("<p>Customize your dark mode portal base (Cost: 100 XP)</p>", unsafe_allow_html=True)
    bg_choice = st.selectbox("Select Theme Base:", ["Deep Black (#0d0e12)", "Cyberpunk Blue (#0b132b)", "Neon Violet (#181124)"])
    if st.button("Apply Background"):
        if st.session_state.credits >= 100:
            st.session_state.credits -= 100
            mapped_color = "#0d0e12" if "Black" in bg_choice else "#0b132b" if "Blue" in bg_choice else "#181124"
            st.session_state.active_bg = mapped_color
            st.success("Theme base updated!")
            st.rerun()
        else:
            st.error("Not enough credits.")
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Store item 3: Digital Stickers (Spawned to wallpaper)
    st.markdown("""<div class="store-item-card">""", unsafe_allow_html=True)
    st.markdown("<h2>🌟 Digital UI Wallpaper Stickers</h2>", unsafe_allow_html=True)
    st.markdown("<p>Slap stickers randomly across your wallpaper (Cost: 50 XP)</p>", unsafe_allow_html=True)
    
    if st.button("Buy ⭐ for 50 XP"):
        if st.session_state.credits >= 50:
            st.session_state.credits -= 50
            st.session_state.stickers.append("⭐")
            st.success("Wallpaper sticker added!")
            st.rerun()
        else:
            st.error("Not enough credits.")
    
    if st.button("Buy 🚀 for 50 XP"):
        if st.session_state.credits >= 50:
            st.session_state.credits -= 50
            st.session_state.stickers.append("🚀")
            st.success("Wallpaper sticker added!")
            st.rerun()
        else:
            st.error("Not enough credits.")
            
    if st.button("Buy 🎓 for 50 XP"):
        if st.session_state.credits >= 50:
            st.session_state.credits -= 50
            st.session_state.stickers.append("🎓")
            st.success("Wallpaper sticker added!")
            st.rerun()
        else:
            st.error("Not enough credits.")
            
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    if st.session_state.stickers:
        st.markdown("<br><h3>🎒 Your Active Wallpaper Stickers:</h3>", unsafe_allow_html=True)
        st.markdown(f"<div style='font-size:2.5em; background:#1e1e2a; padding:20px; border-radius:18px; border:1px solid #33334d; text-align:center;'>{' '.join(st.session_state.stickers)}</div>", unsafe_allow_html=True)
