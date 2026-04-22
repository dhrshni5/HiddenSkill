import random

import streamlit as st


# Page
st.set_page_config(
    page_title="HiddenSkill",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Premium dark theme UI (no backend logic changes)
st.markdown(
    """
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@600;700&display=swap');

  :root{
    --bg0:#0b1020;
    --bg1:#0f172a;
    --card:#1e293b;
    --card2:#243349;
    --text:#e5e7eb;
    --muted:#a7b1c3;
    --border:rgba(148,163,184,.22);
    --shadow:0 18px 42px rgba(2,8,23,.55);
    --a1:#7c3aed;
    --a2:#22d3ee;
  }

  html, body, [class*="css"]{font-family:'Inter',system-ui,-apple-system,sans-serif;}

  .stApp{
    background:
      radial-gradient(circle at 14% 10%, rgba(124,58,237,.30) 0%, rgba(124,58,237,0) 42%),
      radial-gradient(circle at 88% 82%, rgba(34,211,238,.20) 0%, rgba(34,211,238,0) 46%),
      linear-gradient(165deg, var(--bg0) 0%, var(--bg1) 100%);
    color:var(--text);
  }

  .block-container{
    max-width: 900px;
    padding-top: 2.2rem;
    padding-bottom: 3.2rem;
  }

  #MainMenu, footer{visibility:hidden;}

  /* Sidebar */
  [data-testid="stSidebar"]{
    background: linear-gradient(180deg, rgba(30,41,59,.98) 0%, rgba(15,23,42,.98) 100%);
    border-right: 1px solid var(--border);
  }
  [data-testid="stSidebar"] *{color:var(--text) !important;}
  [data-testid="stSidebar"] hr{border-color: rgba(148,163,184,.18) !important;}

  /* Header */
  .hs-hero{
    text-align:center;
    padding: 2.35rem 1.6rem 2.05rem;
    margin-bottom: 1.1rem;
    border-radius: 26px;
    border: 1px solid var(--border);
    background: linear-gradient(135deg, rgba(30,41,59,.90) 0%, rgba(36,51,73,.86) 100%);
    box-shadow: var(--shadow);
    backdrop-filter: blur(6px);
  }
  .hs-badge{
    display:inline-block;
    font-size:.72rem;
    letter-spacing:.12em;
    text-transform:uppercase;
    color:#cbd5e1;
    border:1px solid rgba(124,58,237,.45);
    background: rgba(124,58,237,.18);
    padding:.35rem .75rem;
    border-radius:999px;
    margin-bottom:.9rem;
    font-weight:700;
  }
  .hs-title{
    margin:0;
    font-family:'Space Grotesk',sans-serif;
    font-size:2.6rem;
    line-height:1.12;
    letter-spacing:-.02em;
    background: linear-gradient(90deg, #d8b4fe 0%, #93c5fd 45%, #67e8f9 100%);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    background-clip:text;
  }
  .hs-subtitle{
    margin:.7rem 0 0 0;
    font-size:1.02rem;
    color:var(--muted);
  }

  /* Labels */
  .hs-label{
    font-size:.76rem;
    font-weight:800;
    letter-spacing:.12em;
    text-transform:uppercase;
    color:#94a3b8;
    margin:0 0 .65rem .15rem;
  }

  /* Cards */
  .hs-card{
    background: linear-gradient(160deg, rgba(30,41,59,.96) 0%, rgba(36,51,73,.92) 100%);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 1.35rem 1.4rem;
    margin-bottom: 1.05rem;
    box-shadow: var(--shadow);
    transition: transform .2s ease, box-shadow .22s ease, border-color .2s ease;
  }
  .hs-card:hover{
    transform: translateY(-2px);
    box-shadow: 0 24px 45px rgba(2,8,23,.62);
    border-color: rgba(124,58,237,.42);
  }
  .hs-card-title{
    margin:0 0 .85rem 0;
    font-size:1.08rem;
    font-weight:800;
    color:#f3f4f6;
    display:flex;
    align-items:center;
    gap:.55rem;
  }
  .hs-card-body{
    color:var(--muted);
    font-size:.96rem;
    line-height:1.68;
  }
  .hs-card-body ul{margin:.15rem 0 0 1.05rem; padding:0;}
  .hs-card-body li{margin-bottom:.35rem;}

  .hs-career-name{color:#f3f4f6;margin:.55rem 0 .2rem 0;font-weight:700;}
  .hs-career-reason{
    margin:0 0 .75rem 0;
    color:var(--muted);
    border-left:3px solid rgba(34,211,238,.65);
    padding-left:.55rem;
  }

  .hs-divider{
    height:1px;
    margin:1.45rem 0 1.35rem 0;
    background: linear-gradient(90deg, transparent, rgba(148,163,184,.42), transparent);
  }

  /* Results heading */
  .hs-results{ text-align:center; margin:.35rem 0 .9rem 0; }
  .hs-results h2{ margin:0; font-size:1.28rem; color:#e2e8f0; }
  .hs-results p{
    margin:.3rem 0 0 0;
    font-size:.78rem;
    letter-spacing:.1em;
    text-transform:uppercase;
    color:#94a3b8;
    font-weight:700;
  }

  /* Score highlight */
  .hs-score{
    background: linear-gradient(135deg, rgba(124,58,237,.20) 0%, rgba(34,211,238,.12) 100%);
    border: 1px solid rgba(124,58,237,.40);
    border-radius: 20px;
    padding: 1.2rem 1.35rem 1.05rem;
    box-shadow: 0 20px 40px rgba(2,8,23,.56);
    margin-bottom:.7rem;
  }
  .hs-score-title{ margin:0; color:#f8fafc; font-size:1.08rem; font-weight:800; }
  .hs-score-value{
    margin:.5rem 0 .15rem 0;
    font-size:2.05rem;
    line-height:1;
    font-weight:900;
    background: linear-gradient(90deg, #c4b5fd 0%, #67e8f9 100%);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    background-clip:text;
  }

  /* Progress bar accent */
  div[data-testid="stProgress"] > div > div{
    background: rgba(148,163,184,.20) !important;
    border-radius: 999px !important;
  }
  div[data-testid="stProgress"] > div > div > div > div{
    background: linear-gradient(90deg, var(--a1), var(--a2)) !important;
    border-radius: 999px !important;
  }

  /* Inputs */
  [data-testid="stWidgetLabel"] > div, label, .stSelectbox label{
    color:#d1d5db !important;
    font-weight:600 !important;
  }
  div[data-baseweb="select"] > div{
    background: rgba(15,23,42,.55) !important;
    border: 1px solid rgba(148,163,184,.22) !important;
    border-radius: 14px !important;
  }
  div[data-baseweb="select"] *{ color: var(--text) !important; }

  /* Buttons */
  .stButton > button{
    width:100%;
    background: linear-gradient(90deg, var(--a1) 0%, var(--a2) 100%);
    color:#06101a !important;
    font-weight:900;
    font-size:1.02rem;
    padding:.7rem 1.25rem;
    border-radius: 14px;
    border: none;
    box-shadow: 0 16px 34px rgba(124,58,237,.25);
    transition: transform .15s ease, box-shadow .2s ease, filter .2s ease;
  }
  .stButton > button:hover{
    transform: translateY(-1px);
    filter: brightness(1.04);
    box-shadow: 0 18px 40px rgba(34,211,238,.18);
  }

  .stDownloadButton > button{
    width:100%;
    background: rgba(15,23,42,.35);
    color: var(--text) !important;
    font-weight:800;
    border: 1px solid rgba(34,211,238,.35);
    border-radius: 14px;
    padding:.65rem 1.1rem;
    transition: transform .15s ease, border-color .2s ease, background .2s ease;
  }
  .stDownloadButton > button:hover{
    transform: translateY(-1px);
    border-color: rgba(34,211,238,.70);
    background: rgba(34,211,238,.08);
  }

  .hs-download-hint{
    text-align:center;
    font-size:.82rem;
    color:#94a3b8;
    margin-top:.55rem;
  }
</style>
""",
    unsafe_allow_html=True,
)

# Sidebar
with st.sidebar:
    st.markdown("### About HiddenSkill")
    st.markdown(
        """
        **HiddenSkill** turns a short preference quiz into a structured snapshot of
        personality signals, strengths, and career paths that may fit your style.
        """
    )
    st.markdown("---")
    st.markdown("### How to use")
    st.markdown(
        """
        1. Answer each question honestly; there are no “right” choices.
        2. Click **Analyze Me** to generate your profile.
        3. Review the cards below, then **download** your text report if you like.
        """
    )
    st.markdown("---")
    st.caption("For exploration and reflection—not a replacement for professional career counseling.")

# Main: header
st.markdown(
    """
<div class="hs-hero">
  <div class="hs-badge">AI-Powered Career Insight</div>
  <h1 class="hs-title">HiddenSkill</h1>
  <p class="hs-subtitle">Discover your hidden strengths using AI</p>
</div>
""",
    unsafe_allow_html=True,
)

# Input: two-column layout with clear section label
with st.container():
    st.markdown('<p class="hs-label">Your answers</p>', unsafe_allow_html=True)
    st.markdown(
        """
<div class="hs-card" style="margin-bottom:1.15rem;">
  <div class="hs-card-title">🧩 Questionnaire</div>
  <div class="hs-card-body">Choose the option that fits you most of the time. You can tweak answers and run <strong style="color:#e5e7eb;">Analyze Me</strong> again.</div>
</div>
""",
        unsafe_allow_html=True,
    )
    c1, c2 = st.columns(2, gap="medium")
    with c1:
        q1 = st.selectbox(
            "1. When solving a problem, you:",
            [
                "Research deeply before acting",
                "Jump in and try immediately",
                "Ask others for help",
                "Break it into smaller parts",
            ],
        )
        q2 = st.selectbox(
            "2. What excites you more?",
            [
                "Building something",
                "Explaining ideas",
                "Solving complex puzzles",
                "Leading people",
            ],
        )
        q3 = st.selectbox(
            "3. You prefer:",
            ["Safe and stable career", "High risk, high reward"],
        )
        q4 = st.selectbox(
            "4. Work style:",
            ["Work alone", "Work in a team"],
        )
    with c2:
        q5 = st.selectbox(
            "5. Learning style:",
            [
                "Watching videos",
                "Hands-on practice",
                "Reading",
                "Teaching others",
            ],
        )
        q6 = st.selectbox(
            "6. What would you do for free?",
            [
                "Coding/building",
                "Teaching/helping",
                "Designing/creating",
                "Analyzing problems",
            ],
        )
        q7 = st.selectbox(
            "7. When stressed, you:",
            [
                "Analyze more",
                "Avoid it",
                "Talk to someone",
                "Push harder",
            ],
        )

    st.markdown("<div class='hs-divider'></div>", unsafe_allow_html=True)
    analyze = st.button("Analyze Me", type="primary", use_container_width=True)

if analyze:
    st.divider()

    strengths = []
    weaknesses = []
    careers = []

    # Personality inference
    if "Research" in q1 or "Break" in q1:
        strengths.append("Strong analytical thinking")
        careers.append("Data Scientist")
    else:
        strengths.append("Action-oriented mindset")
        weaknesses.append("May act without deep analysis")
        careers.append("Startup Founder")

    if "Building" in q2 or "Coding" in q6:
        strengths.append("Builder mindset")
        careers.append("Software Developer")

    if "Explaining" in q2 or "Teaching" in q6:
        strengths.append("Strong communication skills")
        careers.append("Teacher / Content Creator")

    if "Solving complex puzzles" in q2 or "Analyzing" in q6:
        strengths.append("Problem-solving ability")
        careers.append("AI Engineer")

    if "Leading" in q2:
        strengths.append("Leadership potential")
        careers.append("Product Manager")

    if "Work alone" in q4:
        strengths.append("Independent worker")
        weaknesses.append("May prefer isolation over collaboration")

    if "Work in a team" in q4:
        strengths.append("Team collaboration skills")

    if "Safe" in q3:
        weaknesses.append("Risk-averse mindset may limit opportunities")
    else:
        strengths.append("Comfortable with risk")

    st.markdown(
        """
<div class="hs-results">
  <h2>🔍 Your AI analysis</h2>
  <p>Your results</p>
</div>
""",
        unsafe_allow_html=True,
    )

    # Personality
    st.markdown(
        """
<div class="hs-card">
  <div class="hs-card-title">🧠 Personality Summary</div>
  <div class="hs-card-body">
    You demonstrate a unique combination of behavioral traits shaped by your
    decision-making style, interests, and work preferences.
  </div>
</div>
""",
        unsafe_allow_html=True,
    )

    # Strengths
    strengths_list = "".join(f"<li>{s}</li>" for s in set(strengths))
    st.markdown(
        f"""
<div class="hs-card">
  <div class="hs-card-title">💪 Strengths</div>
  <div class="hs-card-body"><ul>{strengths_list}</ul></div>
</div>
""",
        unsafe_allow_html=True,
    )

    # Weaknesses
    weak_list = "".join(f"<li>{w}</li>" for w in set(weaknesses))
    st.markdown(
        f"""
<div class="hs-card">
  <div class="hs-card-title">⚠️ Weaknesses</div>
  <div class="hs-card-body"><ul>{weak_list}</ul></div>
</div>
""",
        unsafe_allow_html=True,
    )

    # Careers — each path in the card
    career_blocks = []
    for c in set(careers):
        if c == "Software Developer":
            reason = "Your interest in building and coding shows strong alignment with development roles."
        elif c == "Data Scientist":
            reason = "Your analytical thinking and problem-solving mindset fit data-driven roles."
        elif c == "AI Engineer":
            reason = "Your ability to solve complex problems and analyze patterns suits AI-based roles."
        elif c == "Product Manager":
            reason = "Your leadership and decision-making traits align with managing products and teams."
        elif c == "Teacher / Content Creator":
            reason = "Your ability to explain and communicate ideas makes you suited for teaching roles."
        elif c == "Startup Founder":
            reason = "Your action-oriented mindset and risk-taking ability suit entrepreneurial paths."
        else:
            reason = "Your overall profile shows potential in this area."
        career_blocks.append(
            f'<p class="hs-career-name">{c}</p>'
            f'<p class="hs-career-reason">→ {reason}</p>'
        )
    careers_html = "\n".join(career_blocks)
    st.markdown(
        f"""
<div class="hs-card">
  <div class="hs-card-title">🚀 Career Paths</div>
  <div class="hs-card-body">
    {careers_html}
  </div>
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
<div class="hs-card">
  <div class="hs-card-title">📈 Skill Roadmap</div>
  <div class="hs-card-body">
    Focus on building real-world projects, improving consistency, and exploring your strengths
    deeper through hands-on experience.
  </div>
</div>
""",
        unsafe_allow_html=True,
    )

    score = random.randint(75, 95)

    st.markdown(
        f"""
<div class="hs-score">
  <div class="hs-score-title">🎯 Career Fit Score</div>
  <div class="hs-score-value">{score}%</div>
</div>
""",
        unsafe_allow_html=True,
    )
    st.progress(score)
    st.markdown(
        f"""
<p style="text-align:center;margin-top:0.35rem;color:#a7b1c3;font-size:0.95rem;">
  Your profile matches your suggested careers by <strong style="color:#67e8f9;">{score}%</strong>
</p>
""",
        unsafe_allow_html=True,
    )

    report = f"""
    AI CAREER MIRROR REPORT
    -----------------------

    PERSONALITY SUMMARY:
    You demonstrate a unique combination of behavioral traits shaped by your responses.

    STRENGTHS:
    {chr(10).join(['- ' + s for s in set(strengths)])}

    WEAKNESSES:
    {chr(10).join(['- ' + w for w in set(weaknesses)])}

    CAREER SUGGESTIONS:
    {chr(10).join(['- ' + c for c in set(careers)])}

    CAREER FIT SCORE:
    {score}%

    NEXT STEPS:
    Focus on building real-world projects and improving your core strengths.
    """
    st.download_button(
        label="Download full report",
        data=report,
        file_name="AI_Career_Report.txt",
        mime="text/plain",
        use_container_width=True,
    )
    st.markdown(
        '<p class="hs-download-hint">Plain text — open in any editor or share with a mentor.</p>',
        unsafe_allow_html=True,
    )
