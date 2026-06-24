import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Supernova Study Portal", page_icon="🌠", layout="wide")

# --- INITIALIZE SESSION STATE WITH PRE-FILLED DETAILS ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False  
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
if "chat_open" not in st.session_state:
    st.session_state.chat_open = False
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Universal cross-browser cursor mappings 
cursor_map = {
    "rocket": "url('https://img.icons8.com/emoji/48/rocket-emoji.png') 16 16, auto",
    "star": "url('https://img.icons8.com/fluent/48/000000/star.png') 16 16, auto",
    "laser": "url('https://img.icons8.com/ios-filled/50/00ffcc/lightning-bolt.png') 16 16, auto",
    "default": "default"
}

current_cursor = cursor_map[st.session_state.active_cursor]

# Immersive Cyberpunk / Neon Dynamic Stylesheet
st.markdown(f"""
    <style>
    /* Global Direct Cursors enforcing state during typing, clicking, and loading */
    html, body, div, [class*="stApp"], input, textarea, select, button, label, p, h1, h2, h3, span, .floating-chat-ball, .chat-window {{
        cursor: {current_cursor} !important;
    }}
    current_cursor = cursor_map[st.session_state.active_cursor]


st.markdown(f"""
    <style>
    /* Global Direct Cursors enforcing state during typing, clicking, and loading */
    html, body, div, [class*="stApp"], input, textarea, select, button, label, p, h1, h2, h3, span, .floating-chat-ball, .chat-window {{
        cursor: {current_cursor} !important;
    }}

    .stApp {{
        background-color: #05050c !important;
        background-image: linear-gradient(rgba(5, 5, 12, 0.75), rgba(5, 5, 12, 0.9)), 
                          url('https://images.unsplash.com/photo-1462331940025-496dfbfc7564?w=1920');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #eaeaea;
        font-family: 'Inter', sans-serif;
    }}
    
    /* High-End Cyber-Neon Sidebar Overhaul */
    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, #101018 0%, #1a1a2e 100%);
        border-right: 2px solid #8a2be2;
        box-shadow: 5px 0 25px rgba(138,43,226,0.3);
        padding-top: 20px;
    }}
    
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h3, [data-testid="stSidebar"] div {{
        color: #00ffcc !important;
    }}
    
    /* Gamified Store Grid with fixed edges and tightened spacing */
    .store-grid-container {{
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        justify-content: center;
        margin-top: 15px;
    }}
    
    .store-item-card {{
        background: linear-gradient(135deg, #161622, #1f1f38);
        border: 2px solid #3f3f6c;
        padding: 20px;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 8px 25px rgba(0,0,0,0.5);
        transition: all 0.4s ease;
        width: 320px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }}
    
    .store-item-card:hover {{
        border-color: #00ffcc;
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 15px 45px rgba(0,255,204,0.15);
    }}
    
    /* Wallpaper Stickers Layer */
    .sticker-wallpaper-layer {{
        position: fixed;
        top: 0; left: 0; width: 100vw; height: 100vh;
        z-index: -1;
        pointer-events: none;
        opacity: 0.15;
    }}
    
    /* Floating Action AI Chat Ball UI */
    .floating-chat-ball {{
        position: fixed;
        bottom: 35px;
        right: 35px;
        width: 70px;
        height: 70px;
        border-radius: 50%;
        background: linear-gradient(135deg, #8a2be2, #00ffcc);
        box-shadow: 0 8px 25px rgba(0,255,204,0.4);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 28px;
        color: #000;
        z-index: 9998;
        border: none;
        transition: all 0.3s ease;
    }}
    .floating-chat-ball:hover {{
        transform: scale(1.1) rotate(10deg);
        box-shadow: 0 12px 35px rgba(255,0,127,0.6);
        background: linear-gradient(135deg, #ff007f, #ffbf69) !important;
    }}
    
    /* The Chat Window */
    .chat-window {{
        position: fixed;
        bottom: 120px;
        right: 35px;
        width: 420px;
        height: 500px;
        background: #161622;
        border: 2px solid #33334d;
        border-radius: 20px;
        box-shadow: 0 15px 50px rgba(0,0,0,0.7);
        z-index: 9997;
        display: flex;
        flex-direction: column;
        padding: 20px;
        animation: scaleIn 0.3s ease-in-out;
    }}
    @keyframes scaleIn {{
        from {{ transform: scale(0); opacity: 0; }}
        to {{ transform: scale(1); opacity: 1; }}
    }}
    </style>
""", unsafe_allow_html=True)
# --- END OF CSS BLOCK ---

    .stApp {{
        background-color: {st.session_state.active_bg} !important;
        background-image: url('https://www.transparenttextures.com/patterns/cubes.png');
        background-blend-mode: overlay;
        color: #eaeaea;
        font-family: 'Inter', sans-serif;
    }}
    
    /* High-End Cyber-Neon Sidebar Overhaul */
    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, #101018 0%, #1a1a2e 100%);
        border-right: 2px solid #8a2be2;
        box-shadow: 5px 0 25px rgba(138,43,226,0.3);
        padding-top: 20px;
    }}
    
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h3, [data-testid="stSidebar"] div {{
        color: #00ffcc !important;
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

    /* Custom Cards */
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

    /* Custom Buttons */
    .stButton>button {{
        background: linear-gradient(90deg, #8a2be2, #00ffcc);
        color: #000000;
        border-radius: 20px;
        font-weight: bold;
        border: none;
        padding: 12px 28px;
        box-shadow: 0 4px 15px rgba(138,43,226,0.3);
        transition: all 0.3s ease;
    }}
    .stButton>button:hover {{
        transform: translateY(-3px) scale(1.05);
        background: linear-gradient(90deg, #ff007f, #ffbf69) !important;
        box-shadow: 0 6px 20px rgba(255,0,127,0.5);
        color: #fff !important;
    }}
    
    /* Text Inputs / Selectboxes */
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
    
    /* Gamified Store Grid */
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
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        min-height: 220px;
    }}
    
    .store-item-card:hover {{
        border-color: #00ffcc;
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 15px 45px rgba(0,255,204,0.15);
    }}
    
    /* Wallpaper Stickers Layer */
    .sticker-wallpaper-layer {{
        position: fixed;
        top: 0; left: 0; width: 100vw; height: 100vh;
        z-index: -1;
        pointer-events: none;
        opacity: 0.15;
    }}
    
    /* Floating Action AI Chat Ball UI */
    .floating-chat-ball {{
        position: fixed;
        bottom: 35px;
        right: 35px;
        width: 70px;
        height: 70px;
        border-radius: 50%;
        background: linear-gradient(135deg, #8a2be2, #00ffcc);
        box-shadow: 0 8px 25px rgba(0,255,204,0.4);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 28px;
        color: #000;
        z-index: 9998;
        border: none;
        transition: all 0.3s ease;
    }}
    .floating-chat-ball:hover {{
        transform: scale(1.1) rotate(10deg);
        box-shadow: 0 12px 35px rgba(255,0,127,0.6);
        background: linear-gradient(135deg, #ff007f, #ffbf69) !important;
    }}
    
    /* The Chat Window */
    .chat-window {{
        position: fixed;
        bottom: 120px;
        right: 35px;
        width: 420px;
        height: 500px;
        background: #161622;
        border: 2px solid #33334d;
        border-radius: 20px;
        box-shadow: 0 15px 50px rgba(0,0,0,0.7);
        z-index: 9997;
        display: flex;
        flex-direction: column;
        padding: 20px;
        animation: scaleIn 0.3s ease-in-out;
    }}
    @keyframes scaleIn {{
        from {{ transform: scale(0); opacity: 0; }}
        to {{ transform: scale(1); opacity: 1; }}
    }}
    </style>
""", unsafe_allow_html=True)

# Wallpaper sticker container - Random/Wallpaper-style pattern placement
if st.session_state.stickers:
    st.markdown(f"""
    <div class="sticker-wallpaper-layer" style="font-size: 60px;">
        {''.join([f'<span style="position:absolute; top:{i*33}%; left:{j*25}%; transform: rotate({i*15}deg);">{s}</span>' for i, s in enumerate(st.session_state.stickers) for j in range(4)])}
    </div>
    """, unsafe_allow_html=True)

# --- CINEMATIC WELCOME ROCKET / PLANET EXPLOSION INTRO ---
if not st.session_state.intro_played:
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

st.session_state.logged_in = True  

# --- SIDEBAR ---
st.sidebar.title("✨ Welcome back,")
st.sidebar.subheader(f"👤 {st.session_state.username}")
st.sidebar.markdown(f"**Program:** {st.session_state.program} &nbsp;|&nbsp; **School:** {st.session_state.school}")

app_mode = st.sidebar.selectbox("Navigate", ["Dashboard", "Past Papers & AI Hub", "Reward Store"], index=["Dashboard", "Past Papers & AI Hub", "Reward Store"].index(st.session_state.app_mode))
st.session_state.app_mode = app_mode

# Sidebar credit status
st.sidebar.markdown("---")
st.sidebar.markdown(f'<p class="credit-box">💰 Credits: {st.session_state.credits} XP</p>', unsafe_allow_html=True)

# --- DASHBOARD SCREEN ---
if st.session_state.app_mode == "Dashboard":
    st.markdown("<h1 class='main-title'>⚡ SUPERNOVA INTERACTIVE PORTAL</h1>", unsafe_allow_html=True)
    st.markdown("<p class='main-subtitle'>Accelerate your grades with 3D-simulated AI insights & past papers</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""<div class="custom-card"><h3>📚 Subjects</h3><p>Physics, Computer, Chemistry, Bio, Maths, Add-Math</p></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class="custom-card"><h3>🤖 AI Topic Master</h3><p>Deeply detailed multi-paragraph explanations and marking schemes</p></div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""<div class="custom-card"><h3>🎁 Reward Store</h3><p>Use accumulated XP study credits to unlock cosmetics</p></div>""", unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    
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
        session = st.selectbox("Select Exam Series/Variant:", ["Feb/March", "May/June", "October/November"])
        
        st.markdown("**Click any actual Cambridge link below to download your paper:**")
        st.markdown(f"🔗 [Variant 11 - {session} {search_query} Past Paper Direct Link](https://www.cambridgeinternational.org)")
        st.markdown(f"🔗 [Variant 12 - {session} {search_query} Past Paper Direct Link](https://www.cambridgeinternational.org)")
        st.markdown(f"🔗 [Variant 21 - {session} {search_query} Past Paper Direct Link](https://www.cambridgeinternational.org)")
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("### 📌 Step 2: Select a Topic for In-depth AI Analysis")
        topics = {
            "Physics": ["Kinematics", "Dynamics", "Moments", "Electricity & Circuits", "Waves & Optics", "Nuclear Physics"],
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
                # In-depth Physics Kinematics Masterclass with formulas and graphs
                st.markdown(f"## 📖 AI Kinematics Masterclass (Physics)")
                st.markdown("""
                <div class="paragraph-text">
                Mastering <strong>Kinematics</strong> forms the indisputable bedrock of achieving a stellar A* in your Cambridge Physics examinations. At its core, this foundational domain forces you to shift from merely memorizing formulas to genuinely conceptualizing the underlying mechanical interactions of physical bodies in motion. Examiners frequently design multi-tier data response questions that require you to seamlessly integrate displacement-time and velocity-time graphs. When evaluating gradients and areas under these kinematic curves, students commonly drop marks by carelessly misinterpreting foundational definitions or misapplying equations of motion to non-uniform acceleration scenarios.
                </div>
                <div class="paragraph-text">
                To systematically bypass these common pitfalls, you must train yourself to dissect problems methodically: first, explicitly state the known parameters, second, identify the governing physical law, and third, substitute values with strict adherence to S.I. units. Furthermore, dynamics builds directly onto these concepts by analyzing the direct causes of motion—namely forces and Newton's Laws. Particular focus must be given to resolving forces into perpendicular components and fully grasping resistive forces such as air resistance or terminal velocity. Consistent, deliberate practice using papers from the last five years will expose you to the recurring structural patterns and application-style questions designed by examiners to test true conceptual depth rather than simple recall.
                </div>
                
                ### 📐 Fundamental Kinematics Equations of Motion (SUVAT)
                The standard kinematic formulas for uniform acceleration along a straight line apply directly to physical bodies in dynamic frameworks:
                * **v = u + at** (Final velocity equals initial velocity plus acceleration times time)
                * **s = ((u + v) / 2) * t** (Displacement equals average velocity times time)
                * **s = ut + 0.5at²** (Displacement calculation under uniform acceleration)
                * **v² = u² + 2as** (Velocity squared equals initial velocity squared plus twice acceleration times displacement)
                """)
                
                st.markdown("Visualizing displacement and velocity vector profiles makes computations intuitive:")
                st.markdown("Here is a helpful diagram for understanding displacement over time:")
                



                st.image("https://upload.wikimedia.org/wikipedia/commons/e/ea/Displacement-time.png", caption="Displacement-Time Graph Vector Breakdown")
                st.image("https://upload.wikimedia.org/wikipedia/commons/2/26/Velocity-time.png", caption="Velocity-Time Graph Acceleration & Area Under Curve")
                
            elif selected_topic == "Moments":
                # In-depth Physics Moments Masterclass with formulas and principles
                st.markdown(f"## 📖 AI Moments Masterclass (Physics)")
                st.markdown("""
                <div class="paragraph-text">
                The topic of <strong>Moments</strong> studies the turning effect of forces. A moment is defined mathematically as the product of the force and the perpendicular distance from the pivot to the line of action of the force. When dealing with rigid bodies, understanding the principle of moments is critical for achieving top grades. This principle states that for a system to be in rotational equilibrium, the sum of clockwise moments about any pivot must equal the sum of anticlockwise moments about that same pivot.
                </div>
                <div class="paragraph-text">
                Common examination pitfalls include failing to measure the distance perpendicularly to the force vector or missing forces acting on the system altogether (such as the reaction force at a pivot). To achieve academic precision, you must draw a complete free-body force diagram and establish a clear sign convention before forming your algebraic equilibrium equations.
                </div>
                
                ### 🧮 Important Moments Formulas & Conditions
                * **Moment of a Force (M)**: $M = F \times d$ (where **F** is force in Newtons and **d** is the perpendicular distance in meters).
                * **S.I. Unit for Moment**: Newton-meter ($N\,m$).
                * **First Condition for Equilibrium**: $\sum F = 0$ (Resultant force in any direction is zero).
                * **Second Condition for Equilibrium (Principle of Moments)**: $\sum \text{Clockwise Moments} = \sum \text{Anticlockwise Moments}$.
                """)
                
                st.markdown("Here is a clear diagram showing a lever arm mechanism:")
                
                st.image("https://upload.wikimedia.org/wikipedia/commons/b/b0/Moment_arm.svg", caption="Visualizing Lever Arms and Pivot Points for Torque/Moments")
                
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

# --- REWARD STORE SCREEN ---
elif st.session_state.app_mode == "Reward Store":
    st.markdown("<h1 class='main-title'>🎁 Supernova Reward Store</h1>", unsafe_allow_html=True)
    st.markdown("<p class='main-subtitle'>Redeem your hard-earned study XP credits to customize your interface, cursors, and app wallpaper</p>", unsafe_allow_html=True)
    
    st.markdown(f'<p class="credit-box" style="text-align:center; margin-bottom:20px;">💰 Current Credit Balance: {st.session_state.credits} XP</p>', unsafe_allow_html=True)
    
    # Beautiful responsive gamification store cards with cleared empty lines
    st.markdown("<div class='store-grid-container'>", unsafe_allow_html=True)
    
    # Store item 1: Custom Cursors
    st.markdown("""<div class="store-item-card">""", unsafe_allow_html=True)
    st.markdown("<h2>🚀 Custom Cursors</h2>", unsafe_allow_html=True)
    st.markdown("<p>Change your UI pointer shape (Cost: 50 XP)</p>", unsafe_allow_html=True)
    
    cursor_choice = st.selectbox("Select pointer style:", ["rocket", "star", "laser", "default"], key="cursor_dd")
    if st.button("Apply Cursor", key="apply_cursor_btn"):
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
    
    bg_choice = st.selectbox("Select Theme Base:", ["Deep Black (#0d0e12)", "Cyberpunk Blue (#0b132b)", "Neon Violet (#181124)"], key="theme_dd")
    if st.button("Apply Background", key="apply_bg_btn"):
        if st.session_state.credits >= 100:
            st.session_state.credits -= 100
            mapped_color = "#0d0e12" if "Black" in bg_choice else "#0b132b" if "Blue" in bg_choice else "#181124"
            st.session_state.active_bg = mapped_color
            st.success("Theme base updated!")
            st.rerun()
        else:
            st.error("Not enough credits.")
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Store item 3: Digital Stickers
    st.markdown("""<div class="store-item-card">""", unsafe_allow_html=True)
    st.markdown("<h2>🌟 Digital UI Wallpaper Stickers</h2>", unsafe_allow_html=True)
    st.markdown("<p>Slap stickers randomly across your wallpaper (Cost: 50 XP)</p>", unsafe_allow_html=True)
    
    if st.button("Buy ⭐ for 50 XP", key="sticker_star"):
        if st.session_state.credits >= 50:
            st.session_state.credits -= 50
            st.session_state.stickers.append("⭐")
            st.success("Wallpaper sticker added!")
            st.rerun()
        else:
            st.error("Not enough credits.")
    
    if st.button("Buy 🚀 for 50 XP", key="sticker_rocket"):
        if st.session_state.credits >= 50:
            st.session_state.credits -= 50
            st.session_state.stickers.append("🚀")
            st.success("Wallpaper sticker added!")
            st.rerun()
        else:
            st.error("Not enough credits.")
            
    if st.button("Buy 🎓 for 50 XP", key="sticker_cap"):
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

# --- FLOATING CHATBOT ENGINE (STICKING BALL UI ON THE RIGHT) ---
if st.session_state.chat_open:
    st.markdown("""
    <div class="chat-window">
        <h3 style="color:#00ffcc; margin-top:0; border-bottom:1px solid #33334d; padding-bottom:10px;">🤖 Supernova AI Chat</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Chat window contents
    st.write("Ask the AI anything—formulas, definitions, or past paper assistance!")
    chat_prompt = st.text_input("Type your question here:", key="chat_input_txt")
    
    if st.button("Send", key="send_chat_btn"):
        if chat_prompt:
            st.session_state.credits += 15
            st.session_state.chat_history.append(("user", chat_prompt))
            
            # Universal Chat Detailed Paragraph Response Engine
            ai_response = f"""
            Let's methodically break down your query regarding **{chat_prompt}**.
            
            When approaching analytical questions, the most critical step is to analyze the syllabus keywords before attempting any direct computations. Many candidates lose credit simply by failing to identify core principles embedded within the prompt. You must first extract all given parameters and state the fundamental laws or formulas that govern the scenario.
            
            Executing computations requires strict adherence to standard formatting. Always state the baseline formula in its algebraic form, substitute variables with S.I. units, and proudly display final values to appropriate significant figures. For theoretical explanations, avoid conversational phrasing or casual abbreviations; lean heavily on precise technical vocabulary.
            """
            
            # Additional instant physics clarification if user prompts moments or forces
            if "moment" in chat_prompt.lower() or "torque" in chat_prompt.lower():
                ai_response += """
                ### 🧮 Moments Quick-Reference
                A moment is the turning effect of a force. 
                **Moment = Force × Perpendicular distance from pivot** (M = F × d). 
                For equilibrium, the **Principle of Moments** dictates that the total clockwise moment equals the total anticlockwise moment about the same pivot.
                """
                
            st.session_state.chat_history.append(("ai", ai_response))
            st.rerun()
        else:
            st.warning("Please enter a query.")
            
    # Display message history inside the chat UI container
    for sender, text in st.session_state.chat_history:
        if sender == "user":
            st.markdown(f"**You:** {text}")
        else:
            st.markdown(f"**AI:** {text}")
            
    if st.button("❌ Close Chat", key="close_chat_btn"):
        st.session_state.chat_open = False
        st.rerun()
else:
    # Floating Ball launcher UI sticking out on the bottom right of the screen
    if st.markdown("""
        <button class="floating-chat-ball" onclick="this.click()">💬</button>
    """, unsafe_allow_html=True):
        pass
    if st.button("🤖", key="launch_ball_btn", help="Open Universal AI Chat Assistant"):
        st.session_state.chat_open = True
        st.rerun()
# --- FLOATING CHATBOT ENGINE (STICKING BALL UI ON THE RIGHT) ---
if st.session_state.chat_open:
    st.markdown("""
    <div class="chat-window">
        <h3 style="color:#00ffcc; margin-top:0; border-bottom:1px solid #33334d; padding-bottom:10px;">🤖 Supernova AI Chat</h3>
    """, unsafe_allow_html=True)
    
    # Chat window contents
    st.write("Ask the AI anything—formulas, definitions, or past paper assistance (Math, Computer, Bio)!")
    chat_prompt = st.text_input("Type your question here:", key="chat_input_txt")
    
    if st.button("Send", key="send_chat_btn"):
        if chat_prompt:
            st.session_state.credits += 15
            st.session_state.chat_history.append(("user", chat_prompt))
            
            # Universal Chat Detailed Paragraph Response Engine
            ai_response = f"""
            Let's methodically break down your query regarding **{chat_prompt}**.
            
            When approaching analytical questions, the most critical step is to analyze the syllabus keywords before attempting any direct computations. Many candidates lose credit simply by failing to identify core principles embedded within the prompt. You must first extract all given parameters and state the fundamental laws or formulas that govern the scenario.
            
            Executing computations requires strict adherence to standard formatting. Always state the baseline formula in its algebraic form, substitute variables with S.I. units, and proudly display final values to appropriate significant figures. For theoretical explanations, avoid conversational phrasing or casual abbreviations; lean heavily on precise technical vocabulary.
            """
            
            # Contextual AI advice depending on subject query
            if "moment" in chat_prompt.lower() or "torque" in chat_prompt.lower():
                ai_response += """
                ### 🧮 Moments Quick-Reference
                A moment is the turning effect of a force. 
                **Moment = Force × Perpendicular distance from pivot** (M = F × d). 
                For equilibrium, the **Principle of Moments** dictates that the total clockwise moment equals the total anticlockwise moment about the same pivot.
                """
            elif "algorithm" in chat_prompt.lower() or "code" in chat_prompt.lower():
                ai_response += """
                ### 💻 Computer Science Quick-Reference
                Make sure you trace algorithms step-by-step using a trace table. Pay close attention to loop conditions (while vs. for) and variable initialization to avoid off-by-one errors.
                """
            elif "cell" in chat_prompt.lower() or "gene" in chat_prompt.lower():
                ai_response += """
                ### 🧬 Biology Quick-Reference
                When describing biological processes, always link structure to function and mention specific enzymes or cellular components involved.
                """
                
            st.session_state.chat_history.append(("ai", ai_response))
            st.rerun()
        else:
            st.warning("Please enter a query.")
            
    # Display message history inside the chat UI container
    for sender, text in st.session_state.chat_history:
        if sender == "user":
            st.markdown(f"**You:** {text}")
        else:
            st.markdown(f"**AI:** {text}")
            
    if st.button("❌ Close Chat", key="close_chat_btn"):
        st.session_state.chat_open = False
        st.rerun()
        
    st.markdown("</div>", unsafe_allow_html=True) # Closes the custom chat-window div cleanly

# --- FLOATING CHATBOT ENGINE (STICKING BALL UI ON THE RIGHT) ---
if st.session_state.chat_open:
    st.markdown("""
    <div class="chat-window">
        <h3 style="color:#00ffcc; margin-top:0; border-bottom:1px solid #33334d; padding-bottom:10px;">🤖 Supernova AI Chat</h3>
    """, unsafe_allow_html=True)
    
    # Chat window contents
    st.write("Ask the AI anything—formulas, definitions, or past paper assistance (Math, Computer, Bio)!")
    chat_prompt = st.text_input("Type your question here:", key="chat_input_txt")
    
    if st.button("Send", key="send_chat_btn"):
        if chat_prompt:
            st.session_state.credits += 15
            st.session_state.chat_history.append(("user", chat_prompt))
            
            # Universal Chat Detailed Paragraph Response Engine
            ai_response = f"""
            Let's methodically break down your query regarding **{chat_prompt}**.
            
            When approaching analytical questions, the most critical step is to analyze the syllabus keywords before attempting any direct computations. Many candidates lose credit simply by failing to identify core principles embedded within the prompt. You must first extract all given parameters and state the fundamental laws or formulas that govern the scenario.
            
            Executing computations requires strict adherence to standard formatting. Always state the baseline formula in its algebraic form, substitute variables with S.I. units, and proudly display final values to appropriate significant figures. For theoretical explanations, avoid conversational phrasing or casual abbreviations; lean heavily on precise technical vocabulary.
            """
            
            # Contextual AI advice depending on subject query
            if "moment" in chat_prompt.lower() or "torque" in chat_prompt.lower():
                ai_response += """
                ### 🧮 Moments Quick-Reference
                A moment is the turning effect of a force. 
                **Moment = Force × Perpendicular distance from pivot** (M = F × d). 
                For equilibrium, the **Principle of Moments** dictates that the total clockwise moment equals the total anticlockwise moment about the same pivot.
                """
            elif "algorithm" in chat_prompt.lower() or "code" in chat_prompt.lower():
                ai_response += """
                ### 💻 Computer Science Quick-Reference
                Make sure you trace algorithms step-by-step using a trace table. Pay close attention to loop conditions (while vs. for) and variable initialization to avoid off-by-one errors.
                """
            elif "cell" in chat_prompt.lower() or "gene" in chat_prompt.lower():
                ai_response += """
                ### 🧬 Biology Quick-Reference
                When describing biological processes, always link structure to function and mention specific enzymes or cellular components involved.
                """
                
            st.session_state.chat_history.append(("ai", ai_response))
            st.rerun()
        else:
            st.warning("Please enter a query.")
            
    # Display message history inside the chat UI container
    for sender, text in st.session_state.chat_history:
        if sender == "user":
            st.markdown(f"**You:** {text}")
        else:
            st.markdown(f"**AI:** {text}")
            
    if st.button("❌ Close Chat", key="close_chat_btn"):
        st.session_state.chat_open = False
        st.rerun()
        
    st.markdown("</div>", unsafe_allow_html=True) # Closes the custom chat-window div cleanly
# --- FLOATING CHATBOT ENGINE (STICKING BALL UI ON THE RIGHT) ---
if st.session_state.chat_open:
    st.markdown("""
    <div class="chat-window">
        <h3 style="color:#00ffcc; margin-top:0; border-bottom:1px solid #33334d; padding-bottom:10px;">🤖 Supernova AI Chat</h3>
    """, unsafe_allow_html=True)
    
    # Chat window contents
    st.write("Ask the AI anything—formulas, definitions, or past paper assistance (Math, Computer, Bio)!")
    chat_prompt = st.text_input("Type your question here:", key="chat_input_txt")
    
    if st.button("Send", key="send_chat_btn"):
        if chat_prompt:
            st.session_state.credits += 15
            st.session_state.chat_history.append(("user", chat_prompt))
            
            # Universal Chat Detailed Paragraph Response Engine
            ai_response = f"""
            Let's methodically break down your query regarding **{chat_prompt}**.
            
            When approaching analytical questions, the most critical step is to analyze the syllabus keywords before attempting any direct computations. Many candidates lose credit simply by failing to identify core principles embedded within the prompt. You must first extract all given parameters and state the fundamental laws or formulas that govern the scenario.
            
            Executing computations requires strict adherence to standard formatting. Always state the baseline formula in its algebraic form, substitute variables with S.I. units, and proudly display final values to appropriate significant figures. For theoretical explanations, avoid conversational phrasing or casual abbreviations; lean heavily on precise technical vocabulary.
            """
            
            # Contextual AI advice depending on subject query
            if "moment" in chat_prompt.lower() or "torque" in chat_prompt.lower():
                ai_response += """
                ### 🧮 Moments Quick-Reference
                A moment is the turning effect of a force. 
                **Moment = Force × Perpendicular distance from pivot** (M = F × d). 
                For equilibrium, the **Principle of Moments** dictates that the total clockwise moment equals the total anticlockwise moment about the same pivot.
                """
            elif "algorithm" in chat_prompt.lower() or "code" in chat_prompt.lower():
                ai_response += """
                ### 💻 Computer Science Quick-Reference
                Make sure you trace algorithms step-by-step using a trace table. Pay close attention to loop conditions (while vs. for) and variable initialization to avoid off-by-one errors.
                """
            elif "cell" in chat_prompt.lower() or "gene" in chat_prompt.lower():
                ai_response += """
                ### 🧬 Biology Quick-Reference
                When describing biological processes, always link structure to function and mention specific enzymes or cellular components involved.
                """
                
            st.session_state.chat_history.append(("ai", ai_response))
            st.rerun()
        else:
            st.warning("Please enter a query.")
            
    # Display message history inside the chat UI container
    for sender, text in st.session_state.chat_history:
        if sender == "user":
            st.markdown(f"**You:** {text}")
        else:
            st.markdown(f"**AI:** {text}")
            
    if st.button("❌ Close Chat", key="close_chat_btn"):
        st.session_state.chat_open = False
        st.rerun()
        
    st.markdown("</div>", unsafe_allow_html=True) # Closes the custom chat-window div cleanly

else:
    # Sleek, perfectly round glowing circular button to launch the AI assistant
    launch_chat = st.button("💬", key="launch_ball_btn", help="Open Universal AI Chat Assistant")
    if launch_chat:
        st.session_state.chat_open = True
        st.rerun()
        .stApp {{
    background-color: {st.session_state.active_bg} !important;
    background-image: radial-gradient(circle, rgba(15,23,42,0.8) 0%, rgba(2,6,23,0.95) 100%), 
                      url('https://www.transparenttextures.com/patterns/cubes.png');
    background-blend-mode: overlay;
    background-size: cover;
    background-position: center;
    color: #eaeaea;
    font-family: 'Inter', sans-serif;
}}
.stApp {{
    background-color: #05050c !important;
    background-image: linear-gradient(rgba(5, 5, 12, 0.75), rgba(5, 5, 12, 0.9)), 
                      url('https://images.unsplash.com/photo-1462331940025-496dfbfc7564?w=1920');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    color: #eaeaea;
    font-family: 'Inter', sans-serif;
}}
.store-grid-container {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    justify-content: center;
    margin-top: 15px;
}

.store-item-card {
    background: linear-gradient(135deg, #161622, #1f1f38);
    border: 2px solid #3f3f6c;
    padding: 20px;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0 8px 25px rgba(0,0,0,0.5);
    transition: all 0.4s ease;
    width: 320px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
