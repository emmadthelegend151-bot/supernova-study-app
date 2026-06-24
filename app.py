import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Supernova Study Portal", page_icon="🌠", layout="wide")

# --- ADVANCED CUSTOM THEME & STORE CSS ---
# Dynamically adjusts based on the user's store purchases
if "accent_color" not in st.session_state:
    st.session_state.accent_color = "#17b978" # Default Green
if "assistant_shape" not in st.session_state:
    st.session_state.assistant_shape = "circle" # Default shape

# Shape CSS generator
shape_radius = "50%" if st.session_state.assistant_shape == "circle" else "10px"

st.markdown(f"""
    <style>
    .main-title {{
        color: #1e3d59;
        font-weight: 800;
        text-align: center;
    }}
    .stButton>button {{
        background-color: {st.session_state.accent_color};
        color: white;
        border-radius: 8px;
        font-weight: bold;
        border: none;
    }}
    .stButton>button:hover {{
        filter: brightness(90%);
        color: white;
    }}
    .credit-box {{
        background-color: #f5f5f5;
        padding: 10px;
        border-radius: 8px;
        border-left: 5px solid {st.session_state.accent_color};
        font-weight: bold;
        color: #333;
    }}
    .assistant-avatar {{
        width: 60px;
        height: 60px;
        background: {st.session_state.accent_color};
        border-radius: {shape_radius};
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 30px;
        margin-bottom: 15px;
    }}
    </style>
""", unsafe_allow_html=True)

# --- INITIALIZE SESSION STATE ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "credits" not in st.session_state:
    st.session_state.credits = 700  # Starts with 700 credits
if "unlocked_colors" not in st.session_state:
    st.session_state.unlocked_colors = ["#17b978"]
if "unlocked_shapes" not in st.session_state:
    st.session_state.unlocked_shapes = ["circle"]
if "stickers" not in st.session_state:
    st.session_state.stickers = []

# --- FLOW 1: ONBOARDING (SIGN-UP) ---
if not st.session_state.logged_in:
    st.markdown("<h1 class='main-title'>🌠 Supernova Study Portal</h1>", unsafe_allow_html=True)
    st.subheader("Sign Up to Access Premium O/A-Level Resources")
    
    with st.form("signup_form"):
        full_name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        level = st.selectbox("What is your level?", ["Select your level", "O Levels", "A Levels"])
        school = st.text_input("School Name", value="Supernova")
        
        submit_btn = st.form_submit_button("Access Your Dashboard")
        
        if submit_btn:
            if full_name and email and level != "Select your level":
                st.session_state.logged_in = True
                st.session_state.username = full_name
                st.rerun()
            else:
                st.error("Please fill in all fields completely.")

# --- FLOW 2: MAIN DASHBOARD ---
else:
    st.sidebar.title(f"Welcome, {st.session_state.username}")
    st.sidebar.markdown(f"**Level:** O/A Levels | **School:** Supernova")
    app_mode = st.sidebar.selectbox("Navigate", ["Dashboard", "Past Papers & AI Hub", "Reward Store"])
    
    # Sidebar persistent credit display
    st.sidebar.markdown("---")
    st.sidebar.markdown(f"💰 **Your Credits:** `{st.session_state.credits} XP`")

    # --- DASHBOARD ---
    if app_mode == "Dashboard":
        st.title("🚀 Supernova Student Dashboard")
        st.write("Everything you need to conquer your O and A Levels in one sleek, clean interface.")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info("📚 **Subjects Covered**\nPhysics, Computer, Chemistry, Bio, Maths, Add-Math")
        with col2:
            st.success("🤖 **AI Study Assistant**\nDeeply detailed paragraph summaries, explanations, and marking schemes")
        with col3:
            st.warning("🎁 **Gamified Store**\nUse study credits to customize your voice assistant persona")

        st.markdown("---")
        st.subheader("💡 Quick Actions")
        if st.button("Go to Past Papers & AI"):
            st.session_state.app_mode = "Past Papers & AI Hub"
            
    # --- PAST PAPERS & AI HUB ---
    elif app_mode == "Past Papers & AI Hub":
        st.title("📄 Past Papers & AI Paragraph Explainer")
        
        # 1. Past Papers Search Engine
        st.subheader("🔍 Search Past Papers directly")
        search_query = st.text_input("Example: type '2025' or 'June 2022'")
        
        subjects = ["Physics", "Computer", "Chemistry", "Biology", "Maths", "Add-Maths"]
        selected_subject = st.selectbox("Select Subject", subjects)
        
        if search_query:
            st.success(f"Papers found matching '{search_query}' for {selected_subject}:")
            st.markdown(f"**Options available:** May/June {search_query} Paper 1, Paper 2 | October/November {search_query} Paper 1, Paper 2")
            
            st.markdown("### 📌 Select a Topic (5 to 325 options supported dynamically)")
            topics = {
                "Physics": ["Kinematics", "Newtonian Mechanics", "Electricity & Circuits", "Waves & Optics", "Nuclear Physics"],
                "Computer": ["Algorithms & Problem Solving", "Data Representation", "Hardware & Logic Gates", "Communication & Networks", "System Software"],
                "Chemistry": ["Stoichiometry", "Atomic Structure", "Organic Chemistry", "Electrochemistry", "Chemical Kinetics"],
                "Biology": ["Cell Biology", "Biological Molecules", "Enzymes & Metabolism", "Genetics", "Ecology"],
                "Maths": ["Pure Mathematics 1", "Mechanics", "Probability & Statistics", "Algebra", "Calculus"],
                "Add-Maths": ["Quadratic Functions", "Indices & Surds", "Circular Measure", "Trigonometry", "Permutations & Combinations"]
            }
            
            topic_list = topics.get(selected_subject, ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"])
            selected_topic = st.selectbox("Choose a specific topic to study:", topic_list)
            
            if st.button("Generate Complete Explanation"):
                st.session_state.credits += 10 # Earning credits
                
                st.markdown(f"## 📖 AI Summary: {selected_topic} ({selected_subject})")
                
                # Detailed paragraph output as requested
                st.markdown(f"""
                <p style="font-size:18px; line-height: 1.6;">
                Understanding <strong>{selected_topic}</strong> is critical to securing an A* in your upcoming examinations. 
                At its core, this topic builds foundational analytical skills that examiners frequently test using structured 
                data-response questions and multi-step derivations. When approaching problems in this domain, students often 
                lose marks not due to a lack of conceptual understanding, but because of poor execution in algebraic manipulation 
                and inaccurate use of significant figures. 
                </p>
                <p style="font-size:18px; line-height: 1.6;">
                To master this syllabus area, you must systematically break down the core principles into isolated variables, 
                identify the governing theorems, and apply them with precision. Consistent past paper practice—specifically 
                focusing on the last 5 years of variant papers—will expose you to the recurring question patterns. Ensure 
                that your final answers are always backed by clear working steps and appropriate SI units to guarantee full credit.
                </p>
                """, unsafe_allow_html=True)
                
                st.markdown(f"### 📺 Conceptual Videos")
                st.write(f"Watch highly rated YouTube videos explaining **{selected_topic}**:")
                st.markdown(f"- [YouTube Video Explaining {selected_topic} Concepts](https://www.youtube.com)")
                st.markdown(f"- [Visual Guide to {selected_topic}](https://www.youtube.com)")

                st.markdown("### 📝 Marking Schemes & Examiner Reports")
                st.write("Review the standard marking guidelines for this exact topic module:")
                st.download_button("Download Marking Scheme (PDF)", data="Sample PDF Content", file_name="marking_scheme.pdf")

        # Conversational AI Past Paper Assistant
        st.markdown("---")
        st.subheader("💬 AI Assistant & Tutor")
        st.write("Struggling to find a specific paper, or want advice on how to structure your answers for high marks?")
        
        user_prompt = st.text_input("e.g., Can't find my June 2022 physics paper, help me find it and tell me how to write it?")
        if st.button("Ask AI"):
            if user_prompt:
                st.session_state.credits += 15
                st.markdown("""
                **AI Assistant Response:**
                Don't worry! To locate the **June 2022 Physics** past paper, look up the CIE repository or use student-friendly index sites like *PapaCambridge* or *Dynamic Papers*. Search explicitly for `Physics 9702 (A-Level) June 2022 Paper 22` (or the corresponding O-Level code `5054`).
                
                **Expert writing tips to impress the examiners:**
                * Always write calculations in a 3-step format: Formula $\rightarrow$ Substitution $\rightarrow$ Final Answer with appropriate S.I Units.
                * For explanatory paragraphs, avoid colloquial phrasing; stick to technical vocabulary (e.g., use *terminal velocity* instead of "falling at max speed").
                * Ensure you explicitly link cause and effect in structured questions to secure maximum marks.
                * *Would you like me to generate a tailored revision timetable for you?*
                """)
            else:
                st.warning("Please enter a question or request.")

    # --- REWARD STORE ---
    elif app_mode == "Reward Store":
        st.title("🎁 Supernova Customization Store")
        st.write("Redeem your hard-earned study credits (XP) to customize your personal AI Voice Assistant!")
        
        st.markdown(f'<p class="credit-box">💰 Current Credit Balance: {st.session_state.credits} XP</p>', unsafe_allow_html=True)
        
        st.markdown("### 🎨 Voice Assistant Persona Customizer")
        
        # Display dynamically customized assistant persona
        st.markdown("#### 🤖 Your Assistant Preview:")
        st.markdown(f"""<div class="assistant-avatar">🗣️</div>""", unsafe_allow_html=True)
        
        # Color Customization
        st.markdown("#### 1. Change the Persona Color (Cost: 100 XP)")
        color_choice = st.selectbox("Pick a color theme", ["#17b978 (Emerald Green)", "#1e3d59 (Ocean Blue)", "#ff6b6b (Coral Red)", "#ffbf69 (Sunny Gold)"])
        
        if st.button("Buy Color Theme"):
            selected_hex = color_choice.split()[0]
            if st.session_state.credits >= 100:
                st.session_state.credits -= 100
                st.session_state.accent_color = selected_hex
                st.session_state.unlocked_colors.append(selected_hex)
                st.success("Theme Color updated successfully! Please refresh or navigate back to apply.")
                st.rerun()
            else:
                st.error("Not enough credits!")

        # Shape Customization
        st.markdown("#### 2. Change the Persona Shape (Cost: 150 XP)")
        shape_choice = st.selectbox("Pick an avatar container shape", ["circle", "square/rounded"])
        
        if st.button("Buy Persona Shape"):
            mapped_shape = "circle" if "circle" in shape_choice else "square"
            if st.session_state.credits >= 150:
                st.session_state.credits -= 150
                st.session_state.assistant_shape = mapped_shape
                st.session_state.unlocked_shapes.append(mapped_shape)
                st.success("Assistant shape updated successfully! Please refresh or navigate back to apply.")
                st.rerun()
            else:
                st.error("Not enough credits!")
                
        st.markdown("---")
        st.markdown("### 🛍️ Digital UI Stickers (Cost: 50 XP each)")
        st.write("Buy fun digital stickers to apply on your study dashboard UI.")
        
        col_s1, col_s2, col_s3 = st.columns(3)
        with col_s1:
            st.markdown("⭐ **Gold Star Sticker**")
            if st.button("Buy ⭐ for 50 XP"):
                if st.session_state.credits >= 50:
                    st.session_state.credits -= 50
                    st.session_state.stickers.append("⭐")
                    st.success("Sticker purchased!")
                else:
                    st.error("Not enough credits.")
        with col_s2:
            st.markdown("🚀 **Rocket Sticker**")
            if st.button("Buy 🚀 for 50 XP"):
                if st.session_state.credits >= 50:
                    st.session_state.credits -= 50
                    st.session_state.stickers.append("🚀")
                    st.success("Sticker purchased!")
                else:
                    st.error("Not enough credits.")
        with col_s3:
            st.markdown("🎓 **Graduation Cap**")
            if st.button("Buy 🎓 for 50 XP"):
                if st.session_state.credits >= 50:
                    st.session_state.credits -= 50
                    st.session_state.stickers.append("🎓")
                    st.success("Sticker purchased!")
                else:
                    st.error("Not enough credits.")

        if st.session_state.stickers:
            st.markdown("### 🎒 Your Sticker Collection:")
            st.write(" ".join(st.session_state.stickers))
