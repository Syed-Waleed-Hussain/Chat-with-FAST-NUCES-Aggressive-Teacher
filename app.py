import os
import time
import json
from datetime import datetime
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

st.set_page_config(
    page_title="FAST NUCES Strict Teacher AI 🤬",
    page_icon="🤬",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_dotenv()

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root {
    --bg-base: #090c15;
    --bg-card: rgba(18, 22, 36, 0.8);
    --border-color: rgba(239, 68, 68, 0.2);
    --accent-red: #ef4444;
    --accent-amber: #f59e0b;
    --accent-primary: #dc2626;
    --text-primary: #f8fafc;
    --text-secondary: #cbd5e1;
    --text-muted: #94a3b8;
    --glass-blur: blur(16px);
}

html, body {
    overflow-x: hidden;
    max-width: 100vw;
}

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    color: var(--text-primary);
}

.stApp {
    background-color: var(--bg-base);
    background-image: 
        radial-gradient(at 10% 10%, rgba(239, 68, 68, 0.15) 0px, transparent 50%),
        radial-gradient(at 90% 10%, rgba(245, 158, 11, 0.12) 0px, transparent 50%),
        radial-gradient(at 50% 90%, rgba(185, 28, 28, 0.15) 0px, transparent 50%);
    background-attachment: fixed;
}

header[data-testid="stHeader"] {
    background: transparent !important;
}
#MainMenu, footer {
    visibility: hidden;
}

.hero-container {
    padding: 1.2rem 1rem 0.8rem 1rem;
    text-align: center;
    position: relative;
    margin-bottom: 1rem;
}

.hero-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 6px 16px;
    border-radius: 9999px;
    background: rgba(239, 68, 68, 0.15);
    border: 1px solid rgba(239, 68, 68, 0.4);
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.05em;
    color: #fca5a5;
    margin-bottom: 0.6rem;
    box-shadow: 0 0 20px rgba(239, 68, 68, 0.25);
    animation: pulse 2.5s infinite ease-in-out;
}

.hero-pill .dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #ef4444;
    box-shadow: 0 0 10px #ef4444;
}

@keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.85; transform: scale(1.02); }
}

.hero-title {
    font-size: 2.5rem;
    font-weight: 800;
    letter-spacing: -0.03em;
    line-height: 1.15;
    margin-bottom: 0.4rem;
    background: linear-gradient(135deg, #ffffff 20%, #fca5a5 60%, #ef4444 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    word-break: break-word;
}

.hero-subtitle {
    font-size: 1rem;
    color: var(--text-secondary);
    max-width: 680px;
    margin: 0 auto 1rem auto;
    line-height: 1.45;
}

.warning-bar {
    background: rgba(239, 68, 68, 0.12);
    border: 1px dashed rgba(239, 68, 68, 0.4);
    border-radius: 12px;
    padding: 8px 14px;
    max-width: 680px;
    margin: 0 auto 1.2rem auto;
    font-size: 0.82rem;
    color: #fecaca;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    flex-wrap: wrap;
    text-align: center;
}

.prompt-chips-title {
    font-size: 0.82rem;
    font-weight: 700;
    color: #f87171;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 0.6rem;
    text-align: center;
}

[data-testid="stChatMessage"] {
    background: var(--bg-card) !important;
    border: 1px solid var(--border-color) !important;
    border-radius: 16px !important;
    padding: 0.9rem 1.1rem !important;
    margin-bottom: 0.8rem !important;
    box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.4) !important;
    backdrop-filter: var(--glass-blur) !important;
    transition: transform 0.2s ease, border-color 0.2s ease;
}

[data-testid="stChatMessage"]:hover {
    border-color: rgba(239, 68, 68, 0.35) !important;
}

[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.7) 0%, rgba(15, 23, 42, 0.9) 100%) !important;
    border-left: 3px solid #38bdf8 !important;
}

[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarAssistant"]) {
    background: linear-gradient(135deg, rgba(28, 18, 24, 0.9) 0%, rgba(36, 15, 20, 0.85) 100%) !important;
    border-left: 3px solid #ef4444 !important;
}

code {
    font-family: 'JetBrains Mono', monospace !important;
    background: rgba(15, 23, 42, 0.8) !important;
    padding: 2px 6px !important;
    border-radius: 6px !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    font-size: 0.88em !important;
    word-break: break-word;
}

pre {
    background: #080a10 !important;
    border: 1px solid rgba(239, 68, 68, 0.2) !important;
    border-radius: 12px !important;
    padding: 0.8rem !important;
    overflow-x: auto !important;
}

.msg-meta-bar {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-top: 6px;
    padding-top: 6px;
    border-top: 1px solid rgba(255, 255, 255, 0.05);
    font-size: 0.7rem;
    color: var(--text-muted);
    flex-wrap: wrap;
}

.msg-meta-badge {
    background: rgba(239, 68, 68, 0.15);
    border: 1px solid rgba(239, 68, 68, 0.3);
    padding: 2px 7px;
    border-radius: 6px;
    color: #fca5a5;
    font-weight: 600;
}

[data-testid="stChatInput"] {
    border-radius: 14px !important;
    border: 1px solid rgba(239, 68, 68, 0.3) !important;
    background: rgba(15, 23, 42, 0.9) !important;
    backdrop-filter: var(--glass-blur) !important;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4) !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
}

[data-testid="stChatInput"]:focus-within {
    border-color: #ef4444 !important;
    box-shadow: 0 0 0 2px rgba(239, 68, 68, 0.25), 0 8px 32px rgba(0, 0, 0, 0.5) !important;
}

[data-testid="stSidebar"] {
    background-color: #0c0f18 !important;
    border-right: 1px solid var(--border-color) !important;
}

.sidebar-title {
    font-size: 1.1rem;
    font-weight: 800;
    color: #fecaca;
    margin-bottom: 0.3rem;
    display: flex;
    align-items: center;
    gap: 8px;
}

div.stButton > button {
    border-radius: 12px !important;
    font-weight: 600 !important;
    font-size: 0.88rem !important;
    border: 1px solid rgba(239, 68, 68, 0.25) !important;
    transition: all 0.2s ease !important;
}

div.stButton > button:hover {
    border-color: #ef4444 !important;
    box-shadow: 0 0 16px rgba(239, 68, 68, 0.3) !important;
    transform: translateY(-1px) !important;
}

.clear-btn-container button {
    background: rgba(239, 68, 68, 0.15) !important;
    color: #fca5a5 !important;
    border-color: rgba(239, 68, 68, 0.35) !important;
}
.clear-btn-container button:hover {
    background: rgba(239, 68, 68, 0.25) !important;
    border-color: #ef4444 !important;
}

/* ---------------------------------------------------- */
/* Mobile Responsiveness Rules                          */
/* ---------------------------------------------------- */
@media (max-width: 768px) {
    .hero-title {
        font-size: 1.85rem !important;
    }
    .hero-subtitle {
        font-size: 0.9rem !important;
        padding: 0 8px;
    }
    .hero-pill {
        font-size: 0.72rem !important;
        padding: 4px 12px !important;
    }
    .warning-bar {
        font-size: 0.75rem !important;
        flex-direction: column;
        gap: 4px;
        padding: 8px 10px;
    }
    [data-testid="stChatMessage"] {
        padding: 0.75rem 0.85rem !important;
        border-radius: 14px !important;
        font-size: 0.92rem !important;
    }
    .msg-meta-bar {
        font-size: 0.65rem !important;
        gap: 6px !important;
    }
    div.stButton > button {
        font-size: 0.8rem !important;
        padding: 6px 8px !important;
    }
}

@media (max-width: 480px) {
    .hero-title {
        font-size: 1.55rem !important;
    }
    .hero-container {
        padding: 0.8rem 0.2rem 0.5rem 0.2rem;
    }
}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

DEFAULT_SYSTEM_PROMPT = """You are a strict, aggressive, and sarcastic professor at FAST National University (FAST-NUCES).
CRITICAL RULES FOR LENGTH & TONE:
1. MANDATORY: KEEP EVERY SINGLE RESPONSE SHORT, CONCISE, AND PUNCHY (MAXIMUM 2 TO 4 SHORT SENTENCES, OR UNDER 75 WORDS TOTAL). Never write long explanations or essays! A busy FAST professor never writes essays for lazy students.
2. Tone: Aggressive, harsh, impatient, and no-nonsense. You constantly suspect students of low attendance (<80%), missing classes, or plagiarizing assignments.
3. Language style: Speak primarily in strict English mixed naturally with hilarious FAST campus phrases (e.g., 'Attendance short hai tumhari!', 'Flex pe F lagaunga!', 'Dafa ho jao!', 'Zero marks!', 'Assignment copy ki hai!').
4. Answer directly: Give a quick brutal scolding, state the exact technical answer or code fix in 1-2 sharp lines, and finish with a harsh warning. Keep it strictly brief."""

PERSONA_PROMPTS = {
    "🤬 Dr. Flex (Strict Course Instructor)": DEFAULT_SYSTEM_PROMPT,
    "💀 Head of FYP Evaluation Committee": """You are the terrifying Head of the FYP Committee at FAST-NUCES.
CRITICAL RULE: KEEP ALL RESPONSES VERY SHORT (UNDER 3-4 SENTENCES). Suspect everything is a GitHub clone, demand IEEE papers, and answer their query sharply with zero fluff and maximum strictness.""",
    "📝 Brutal Lab Instructor (Zero Tolerance)": """You are a ruthless Lab Instructor at FAST-NUCES.
CRITICAL RULE: KEEP ALL RESPONSES VERY SHORT (UNDER 3-4 SENTENCES). Deduct marks for indentation, yell about 11:59 PM deadlines, give the exact fix directly in one line, and tell them to leave the lab.""",
    "📋 Attendance Incharge (Zero Medical Leave)": """You are the FAST-NUCES Attendance Incharge.
CRITICAL RULE: KEEP ALL RESPONSES VERY SHORT (UNDER 3 SENTENCES). Reject any medical leaves, yell about 79.9% being an F grade, and answer their question with utter impatience."""
}
BASE_MODELS = [
    "qwen/qwen3.8-27b",
    "openai/gpt-oss-120b",
    "openai/gpt-oss-20b",
    "llama-3.3-70b-versatile",
    "llama-3.1-8b-instant",
    "llama-3.1-70b-versatile",
    "deepseek-r1-distill-llama-70b",
    "mixtral-8x7b-32768",
    "gemma2-9b-it",
    "allam-2-7b",
    "✏️ Enter Custom Model..."
]

if "messages" not in st.session_state:
    st.session_state.messages = []

if "total_tokens_used" not in st.session_state:
    st.session_state.total_tokens_used = 0

if "selected_quick_prompt" not in st.session_state:
    st.session_state.selected_quick_prompt = None

groq_api_key = os.getenv("GROQ_API_KEY", "")
if not groq_api_key and hasattr(st, "secrets"):
    try:
        groq_api_key = str(st.secrets.get("GROQ_API_KEY", ""))
    except Exception:
        pass
groq_api_key = groq_api_key.strip()

with st.sidebar:
    st.markdown('<div class="sidebar-title">🤬 Faculty Office (Strict AI)</div>', unsafe_allow_html=True)
    st.caption("FAST-NUCES Department of Strict Evaluation")
    st.markdown("---")

    if groq_api_key:
        st.markdown('<div style="background: rgba(34, 197, 94, 0.1); border: 1px solid rgba(34, 197, 94, 0.3); border-radius: 8px; padding: 6px 12px; font-size: 0.8rem; color: #86efac; margin-bottom: 12px;">🔒 Server API Connected</div>', unsafe_allow_html=True)
    else:
        st.error("⚠️ GROQ_API_KEY is not configured in .env or Streamlit Secrets.")

    available_models = list(BASE_MODELS)
    if groq_api_key:
        try:
            client_probe = Groq(api_key=groq_api_key)
            fetched_models = [m.id for m in client_probe.models.list().data if not m.id.startswith("whisper") and "guard" not in m.id]
            if fetched_models:
                merged = []
                for m in fetched_models:
                    if m not in merged:
                        merged.append(m)
                for m in BASE_MODELS:
                    if m not in merged:
                        merged.append(m)
                available_models = merged
        except Exception:
            pass

    st.markdown("#### 🧠 Teacher Inference Engine")
    model_choice = st.selectbox(
        "Active Model",
        options=available_models,
        index=0,
        help="Model generating furious responses at Groq LPU speeds"
    )

    if model_choice == "✏️ Enter Custom Model...":
        selected_model = st.text_input("Custom Model ID", value="llama-3.3-70b-versatile").strip()
    else:
        selected_model = model_choice

    st.markdown("#### 🎭 Faculty Persona")
    selected_persona_name = st.selectbox(
        "Select Instructor",
        options=list(PERSONA_PROMPTS.keys()),
        index=0
    )
    custom_system_prompt = st.text_area(
        "Teacher Instructions",
        value=PERSONA_PROMPTS[selected_persona_name],
        height=130,
        help="Aggression level & strict teacher context (keeps answers short)"
    )

    st.markdown("#### ⚙️ Strictness Parameters")
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        temperature = st.slider("Strict Temperature", min_value=0.0, max_value=2.0, value=0.75, step=0.05)
    with col_t2:
        top_p = st.slider("Top P", min_value=0.0, max_value=1.0, value=0.9, step=0.05)

    max_tokens = st.slider("Max Scolding Words (Tokens)", min_value=64, max_value=1024, value=256, step=32, help="Restricts answer length to keep responses short and punchy")
    enable_streaming = st.toggle("Live Fury Streaming", value=True)

    st.markdown("---")

    st.markdown("#### 📊 Academic Punishment Telemetry")
    metric_col1, metric_col2 = st.columns(2)
    with metric_col1:
        st.metric("Questions Asked", len(st.session_state.messages))
    with metric_col2:
        st.metric("Total Tokens Spent", f"{st.session_state.total_tokens_used:,}")

    st.markdown("#### 🛠️ Disciplinary Actions")
    
    if st.session_state.messages:
        chat_markdown = "# FAST-NUCES Strict Teacher Inquiry Record\n\n"
        chat_markdown += f"*Hearing Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n---\n\n"
        for msg in st.session_state.messages:
            role_label = "🎒 **Student**" if msg["role"] == "user" else f"🤬 **Teacher ({msg.get('model', selected_model)})**"
            chat_markdown += f"{role_label}\n\n{msg['content']}\n\n---\n\n"
        
        st.download_button(
            label="📥 Download Disciplinary Charge Sheet",
            data=chat_markdown,
            file_name=f"fast_strict_inquiry_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
            mime="text/markdown",
            use_container_width=True
        )

        chat_json = json.dumps(st.session_state.messages, indent=2)
        st.download_button(
            label="💾 Export Inquiry Log (JSON)",
            data=chat_json,
            file_name=f"fast_inquiry_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json",
            use_container_width=True
        )

    st.markdown('<div class="clear-btn-container">', unsafe_allow_html=True)
    if st.button("🧹 Beg for Forgiveness (Clear Chat)", use_container_width=True):
        st.session_state.messages = []
        st.session_state.total_tokens_used = 0
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.caption("FAST-NUCES Attendance Portal • Powered by Groq LPU™")

st.markdown("""
<div class="hero-container">
    <div class="hero-pill">
        <span class="dot"></span>
        WARNING: ATTENDANCE SHORTAGE DETECTED (&lt; 80%)
    </div>
    <h1 class="hero-title">FAST-NUCES Strict Teacher AI</h1>
    <p class="hero-subtitle">
        <i>"Dafa ho jao meri class se! Asking questions when your attendance is 68%? You are getting an F grade on the Flex portal!"</i>
    </p>
    <div class="warning-bar">
        <span>⚠️ <b>RULE 1:</b> Short answers only.</span>
        <span>🚫 <b>RULE 2:</b> Medical leaves rejected.</span>
        <span>💀 <b>RULE 3:</b> Strict grading.</span>
    </div>
</div>
""", unsafe_allow_html=True)

if len(st.session_state.messages) == 0:
    st.markdown('<div class="prompt-chips-title">⚠️ Common Student Excuses (Click to Get Roasted)</div>', unsafe_allow_html=True)
    
    quick_prompts = [
        ("🩺 Medical Certificate", "Sir, I had severe dengue fever last week. Please accept my medical certificate and mark my attendance present."),
        ("⏰ 2 Minutes Late", "Sir, I was just 2 minutes late to the 8:30 AM lecture because the bus was stuck in traffic. Please allow me inside."),
        ("💻 Code chal nahi raha", "Sir, my code is giving a Segmentation Fault error on line 42. Can you please debug it for me?"),
        ("📊 79.2% Attendance", "Sir, my attendance is 79.2%. Can you please round it off to 80% so I can sit in the final exam?")
    ]
    
    row1_cols = st.columns(2)
    with row1_cols[0]:
        if st.button(quick_prompts[0][0], use_container_width=True, key="quick_prompt_0"):
            st.session_state.selected_quick_prompt = quick_prompts[0][1]
            st.rerun()
    with row1_cols[1]:
        if st.button(quick_prompts[1][0], use_container_width=True, key="quick_prompt_1"):
            st.session_state.selected_quick_prompt = quick_prompts[1][1]
            st.rerun()
            
    row2_cols = st.columns(2)
    with row2_cols[0]:
        if st.button(quick_prompts[2][0], use_container_width=True, key="quick_prompt_2"):
            st.session_state.selected_quick_prompt = quick_prompts[2][1]
            st.rerun()
    with row2_cols[1]:
        if st.button(quick_prompts[3][0], use_container_width=True, key="quick_prompt_3"):
            st.session_state.selected_quick_prompt = quick_prompts[3][1]
            st.rerun()

for msg in st.session_state.messages:
    role = msg["role"]
    avatar = "🎒" if role == "user" else "🤬"
    with st.chat_message(role, avatar=avatar):
        st.markdown(msg["content"])
        
        if role == "assistant" and "latency" in msg:
            st.markdown(
                f"""
                <div class="msg-meta-bar">
                    <span class="msg-meta-badge">🤬 {msg.get('model', selected_model)}</span>
                    <span>⏱️ {msg.get('latency', 0):.2f}s</span>
                    <span>⚡ ~{msg.get('speed', 0):.0f} rage-t/s</span>
                    <span>🕒 {msg.get('time', '')}</span>
                </div>
                """,
                unsafe_allow_html=True
            )

user_input = st.chat_input("Ask Sir your question or dare to present an excuse... (Enter to submit)")

if st.session_state.selected_quick_prompt:
    prompt_to_process = st.session_state.selected_quick_prompt
    st.session_state.selected_quick_prompt = None
elif user_input:
    prompt_to_process = user_input
else:
    prompt_to_process = None

if prompt_to_process:
    if not groq_api_key:
        st.error("🔑 Please set your `GROQ_API_KEY` in the `.env` file or provide it in the sidebar.")
        st.stop()

    st.session_state.messages.append({
        "role": "user",
        "content": prompt_to_process,
        "time": datetime.now().strftime("%I:%M %p")
    })

    with st.chat_message("user", avatar="🎒"):
        st.markdown(prompt_to_process)

    client = Groq(api_key=groq_api_key)

    messages_payload = [{"role": "system", "content": custom_system_prompt}]
    for m in st.session_state.messages:
        messages_payload.append({
            "role": m["role"],
            "content": m["content"]
        })

    with st.chat_message("assistant", avatar="🤬"):
        start_time = time.time()
        
        try:
            if enable_streaming:
                stream = client.chat.completions.create(
                    model=selected_model,
                    messages=messages_payload,
                    temperature=temperature,
                    max_tokens=max_tokens,
                    top_p=top_p,
                    stream=True
                )

                def chunk_generator():
                    for chunk in stream:
                        delta = chunk.choices[0].delta.content or ""
                        yield delta

                full_response = st.write_stream(chunk_generator)
            else:
                with st.spinner("🤬 Sir is reviewing your disastrous attendance on Flex..."):
                    completion = client.chat.completions.create(
                        model=selected_model,
                        messages=messages_payload,
                        temperature=temperature,
                        max_tokens=max_tokens,
                        top_p=top_p,
                        stream=False
                    )
                    full_response = completion.choices[0].message.content
                    st.markdown(full_response)

            elapsed_time = max(time.time() - start_time, 0.01)
            estimated_tokens = max(len(full_response) // 4, 1)
            tokens_per_second = estimated_tokens / elapsed_time
            st.session_state.total_tokens_used += estimated_tokens

            curr_time = datetime.now().strftime("%I:%M %p")
            st.markdown(
                f"""
                <div class="msg-meta-bar">
                    <span class="msg-meta-badge">🤬 {selected_model}</span>
                    <span>⏱️ {elapsed_time:.2f}s</span>
                    <span>⚡ ~{tokens_per_second:.0f} rage-t/s</span>
                    <span>🕒 {curr_time}</span>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.session_state.messages.append({
                "role": "assistant",
                "content": full_response,
                "model": selected_model,
                "latency": elapsed_time,
                "speed": tokens_per_second,
                "time": curr_time
            })

        except Exception as e:
            st.error(f"❌ Groq API Error: {str(e)}")
