import streamlit as st
import ollama
import time

st.set_page_config(
    page_title="Ninja Family Universe 🥷",
    page_icon="🥷",
    layout="centered"
)

# ---------------- PREMIUM UI CSS ----------------
st.markdown("""
<style>

/* Remove Scroll */
html, body, [class*="css"]  {
    overflow-x: hidden;
}

/* Animated Gradient Background */
.stApp {
    background: linear-gradient(-45deg, #89CFF0, #6CA6CD, #5F9EA0, #87CEFA);
    background-size: 400% 400%;
    animation: gradientMove 12s ease infinite;
    color: #0f172a;
}

/* Gradient Animation */
@keyframes gradientMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* ---------------- NINJA STAR BACKGROUND ---------------- */
.ninja-bg {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    z-index: -1;
    pointer-events: none;
}

/* Ninja Star Style */
.ninja-bg span {
    position: absolute;
    font-size: 40px;
    opacity: 0.08;
    animation: floatStar linear infinite;
}

/* Floating + Spinning */
@keyframes floatStar {
    0% {
        transform: translateY(110vh) rotate(0deg);
    }
    100% {
        transform: translateY(-10vh) rotate(1080deg);
    }
}

/* Title */
.title {
    font-size: 42px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 20px;
}

/* Chat Bubbles */
.user-bubble {
    background-color: #2563eb;
    color: white;
    padding: 14px;
    border-radius: 20px;
    margin: 10px 0;
}

.bot-bubble {
    background-color: #059669;
    color: white;
    padding: 14px;
    border-radius: 20px;
    margin: 10px 0;
}

/* Blade Animation */
.blade {
    position: fixed;
    font-size: 55px;
    z-index: 9999;
    animation: fly 1.3s linear infinite;
}

@keyframes fly {
    0% { left: -120px; transform: rotate(0deg); }
    100% { left: 110%; transform: rotate(1080deg); }
}

/* Creativity Box */
.creativity-box {
    background: rgba(255,255,255,0.85);
    padding: 10px;
    border-radius: 12px;
    margin-top: 10px;
}

/* Remove Send Button Hover */
div[data-testid="stFormSubmitButton"] button {
    background-color: #2563eb !important;
    color: white !important;
    border: none !important;
    box-shadow: none !important;
    transition: none !important;
}
div[data-testid="stFormSubmitButton"] button:hover {
    background-color: #2563eb !important;
    transform: none !important;
}
div[data-testid="stFormSubmitButton"] button:focus {
    outline: none !important;
    box-shadow: none !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown('<div class="title">🥷 Ninja Hattori Family Universe 🥷</div>', unsafe_allow_html=True)

# ---------------- ANIMATED NINJA STARS ----------------
st.markdown("""
<div class="ninja-bg">
    <span style="left:5%; animation-duration:18s;">✴️</span>
    <span style="left:12%; animation-duration:22s;">✵</span>
    <span style="left:20%; animation-duration:25s;">✦</span>
    <span style="left:28%; animation-duration:20s;">✪</span>
    <span style="left:36%; animation-duration:27s;">✴️</span>
    <span style="left:44%; animation-duration:19s;">✵</span>
    <span style="left:52%; animation-duration:23s;">✦</span>
    <span style="left:60%; animation-duration:21s;">✪</span>
    <span style="left:68%; animation-duration:26s;">✴️</span>
    <span style="left:76%; animation-duration:24s;">✵</span>
    <span style="left:84%; animation-duration:28s;">✦</span>
    <span style="left:92%; animation-duration:30s;">✪</span>
</div>
""", unsafe_allow_html=True)

# ---------------- CHARACTER SELECTOR ----------------
character = st.selectbox(
    "Choose who you want to talk to:",
    ["Ninja Hattori", "Kenichi", "Shishimaru", "Yumiko"]
)

character_prompts = {
    "Ninja Hattori": "You are Ninja Hattori. Energetic ninja. Always end with ding ding ding!",
    "Kenichi": "You are Kenichi. Cheerful school boy. Talk about school life and friends.",
    "Shishimaru": "You are Shishimaru, funny ninja dog. Talk playful and mention food.",
    "Yumiko": "You are Yumiko. Sweet and kind. Talk gently about hobbies and daily life."
}

# ---------------- MEMORY ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "current_character" not in st.session_state or st.session_state.current_character != character:
    st.session_state.messages = [
        {"role": "system", "content": character_prompts[character]}
    ]
    st.session_state.current_character = character

# ---------------- DISPLAY CHAT ----------------
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-bubble">🧑 You: {msg["content"]}</div>', unsafe_allow_html=True)
    elif msg["role"] == "assistant":
        st.markdown(f'<div class="bot-bubble">🎭 {character}: {msg["content"]}</div>', unsafe_allow_html=True)

# ---------------- INPUT ----------------
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Ask something...")
    submit = st.form_submit_button("Send")

# ---------------- CREATIVITY ----------------
st.markdown("---")
st.markdown('<div class="creativity-box">', unsafe_allow_html=True)

temperature = st.slider(
    "🎨 Creativity Level",
    min_value=0.0,
    max_value=1.0,
    value=0.4,
    step=0.1
)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- CHAT LOGIC ----------------
if submit and user_input:

    st.session_state.messages.append({"role": "user", "content": user_input})

    blade_placeholder = st.empty()

    blade_placeholder.markdown("""
    <div class="blade" style="top:40%;">🗡️</div>
    <div class="blade" style="top:65%; animation-delay:0.3s;">⚔️</div>
    """, unsafe_allow_html=True)

    time.sleep(1.2)

    response = ollama.chat(
        model="gemma3:1b",
        messages=st.session_state.messages,
        options={"temperature": temperature}
    )

    blade_placeholder.empty()

    reply = response["message"]["content"]

    if character == "Ninja Hattori":
        if not reply.lower().endswith("ding ding ding!"):
            reply += " ding ding ding!"

    st.session_state.messages.append({"role": "assistant", "content": reply})

    st.rerun()
