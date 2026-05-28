import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.graph_objects as go
from datetime import datetime

model = pickle.load(open("mental_health_model.pkl", "rb"))

st.set_page_config(
    page_title="MindGuard - Teen Mental Health",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
.main-header {
    font-size: 2.8rem;
    font-weight: bold;
    text-align: center;
    color: #667eea;
    margin-bottom: 0.5rem;
}
.sub-header {
    font-size: 1.2rem;
    text-align: center;
    color: #888;
    margin-bottom: 2rem;
}
</style>
""", unsafe_allow_html=True)

mental_health_tips = [
    "Drink at least 8 glasses of water daily",
    "Start your day with 5 minutes of deep breathing",
    "Put your phone away 1 hour before bedtime",
    "A 10-minute walk outside can boost your mood",
    "Write 3 things you are grateful for every morning",
    "Listen to calming music when feeling stressed",
    "Practice 5 minutes of mindfulness meditation daily",
    "Reach out to a friend or family member today",
    "Spend at least 20 minutes in nature every day",
    "Maintain a consistent sleep schedule",
    "Exercise releases endorphins - your natural mood boosters",
    "Reading for 30 minutes can reduce stress significantly",
    "Express yourself creatively - draw, paint or write",
    "Eat a balanced diet - gut health is linked to mental health",
    "Give someone a compliment today"
]

motivational_quotes = [
    {"quote": "You do not have to be positive all the time. It is okay to feel sad or anxious.", "author": "Lori Deschene"},
    {"quote": "Mental health is not a destination but a process.", "author": "Noam Shpancer"},
    {"quote": "You are not alone in this. The bravest thing you can do is ask for help.", "author": "Unknown"},
    {"quote": "It is okay to not be okay - as long as you are not giving up.", "author": "Karen Salmansohn"},
    {"quote": "Your present circumstances do not determine where you can go.", "author": "Nido Qubein"},
    {"quote": "Self-care is not selfish. You cannot serve from an empty vessel.", "author": "Eleanor Brownn"},
    {"quote": "The strongest people are those who win battles we know nothing about.", "author": "Unknown"},
    {"quote": "You are enough. You have enough. You do enough.", "author": "Unknown"},
    {"quote": "Every day may not be good, but there is something good in every day.", "author": "Alice Morse Earle"},
    {"quote": "Healing is not linear. Be patient with yourself.", "author": "Unknown"}
]

wellness_goals = [
    "Wake up 30 minutes earlier than usual",
    "Drink 8 glasses of water today",
    "Walk for at least 20 minutes",
    "No social media before 9 AM",
    "Eat at least one healthy meal",
    "Write in your journal for 5 minutes",
    "Meditate for 10 minutes",
    "Call or text a friend you miss",
    "Read for 20 minutes",
    "Sleep before 11 PM",
    "Listen to music that makes you happy",
    "List 3 good things that happened today"
]

quiz_questions = [
    {
        "question": "How often do you feel overwhelmed by daily responsibilities?",
        "options": ["Never", "Sometimes", "Often", "Always"],
        "scores": [0, 1, 2, 3]
    },
    {
        "question": "How would you rate your sleep quality this week?",
        "options": ["Excellent", "Good", "Fair", "Poor"],
        "scores": [0, 1, 2, 3]
    },
    {
        "question": "How often do you feel lonely or isolated?",
        "options": ["Never", "Rarely", "Sometimes", "Often"],
        "scores": [0, 1, 2, 3]
    },
    {
        "question": "How often do you feel anxious without a specific reason?",
        "options": ["Never", "Rarely", "Sometimes", "Frequently"],
        "scores": [0, 1, 2, 3]
    },
    {
        "question": "How would you describe your energy levels?",
        "options": ["Very energetic", "Moderate", "Low energy", "Exhausted"],
        "scores": [0, 1, 2, 3]
    },
    {
        "question": "How often do you engage in activities you enjoy?",
        "options": ["Daily", "Few times a week", "Rarely", "Never"],
        "scores": [0, 1, 2, 3]
    },
    {
        "question": "How often do you feel hopeful about your future?",
        "options": ["Always", "Usually", "Sometimes", "Rarely"],
        "scores": [0, 1, 2, 3]
    },
    {
        "question": "How would you rate your ability to concentrate?",
        "options": ["Excellent", "Good", "Fair", "Poor"],
        "scores": [0, 1, 2, 3]
    }
]

with st.sidebar:
    st.markdown("## 🧠 MindGuard")
    st.markdown("Your Mental Health Companion")
    st.markdown("---")
    page = st.radio("Navigate", [
        "🏠 Home and Predictor",
        "📋 Self Assessment Quiz",
        "📈 Progress Tracker",
        "🎯 Daily Wellness Goals",
        "🌬️ Breathing Exercise",
        "📊 Analytics",
        "ℹ️ About"
    ])
    st.markdown("---")
    st.markdown("### Tip of the Day")
    tip_index = datetime.now().day % len(mental_health_tips)
    st.info(mental_health_tips[tip_index])
    st.markdown("---")
    st.markdown("### Quote of the Day")
    quote_index = datetime.now().day % len(motivational_quotes)
    q = motivational_quotes[quote_index]
    st.markdown(f"*{q['quote']}*")
    st.caption(f"— {q['author']}")
    st.markdown("---")
    st.caption("Jeppiaar University | AIML Dept")
    st.caption("Dheeraj Varma | 3rd Year B.Tech")

if page == "🏠 Home and Predictor":
    st.markdown("<p class='main-header'>🧠 MindGuard</p>", unsafe_allow_html=True)
    st.markdown("<p class='sub-header'>AI-Powered Teen Mental Health Risk Predictor</p>", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Dataset Size", "2500 Teens")
    with c2:
        st.metric("Model Accuracy", "85 percent plus")
    with c3:
        st.metric("Features", "11 Factors")
    with c4:
        st.metric("Prediction Time", "Under 1 Second")

    st.markdown("---")
    st.markdown("## Enter Your Details")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Personal Info")
        age = st.slider("Age", 13, 20, 16)
        gender = st.selectbox("Gender", ["male", "female"])
        academic_performance = st.slider("Academic Performance GPA", 0.0, 4.0, 3.0, 0.1)
        st.markdown("### Social Media")
        daily_social_media_hours = st.slider("Daily Social Media Hours", 0.0, 12.0, 3.0, 0.5)
        platform_usage = st.selectbox("Primary Platform", ["Instagram", "TikTok", "YouTube", "Facebook", "Other"])

    with col2:
        st.markdown("### Sleep and Lifestyle")
        sleep_hours = st.slider("Sleep Hours Per Night", 3.0, 10.0, 7.0, 0.5)
        screen_time_before_sleep = st.slider("Screen Time Before Sleep hours", 0.0, 5.0, 1.0, 0.5)
        physical_activity = st.slider("Physical Activity hours per day", 0.0, 5.0, 1.0, 0.5)
        st.markdown("### Mental Health")
        social_interaction_level = st.selectbox("Social Interaction Level", ["low", "medium", "high"])
        stress_level = st.slider("Stress Level 1 to 10", 1, 10, 5)
        anxiety_level = st.slider("Anxiety Level 1 to 10", 1, 10, 5)

    st.markdown("---")

    if st.button("Analyze My Mental Health", type="primary", use_container_width=True):
        gender_enc = 1 if gender == "male" else 0
        platform_map = {"Facebook": 0, "Instagram": 1, "Other": 2, "TikTok": 3, "YouTube": 4}
        platform_enc = platform_map.get(platform_usage, 2)
        social_map = {"high": 0, "low": 1, "medium": 2}
        social_enc = social_map.get(social_interaction_level, 1)

        input_data = np.array([[age, gender_enc, daily_social_media_hours,
                                platform_enc, sleep_hours, screen_time_before_sleep,
                                academic_performance, physical_activity,
                                social_enc, stress_level, anxiety_level]])

        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0]

        risk_map = {0: "HIGH RISK", 1: "LOW RISK", 2: "MEDIUM RISK"}
        result = risk_map.get(prediction, "Unknown")

        if prediction == 1:
            st.balloons()
        else:
            st.snow()

        st.markdown("## Your Mental Health Analysis")

        r1, r2, r3 = st.columns(3)
        with r1:
            if prediction == 1:
                st.success(f"Result: {result}")
            elif prediction == 0:
                st.error(f"Result: {result}")
            else:
                st.warning(f"Result: {result}")
        with r2:
            st.metric("Confidence", f"{probability[prediction]*100:.1f}%")
        with r3:
            overall = int((1 - probability[0]) * 100)
            st.metric("Wellness Score", f"{overall} out of 100")

        fig = go.Figure(go.Bar(
            x=["High Risk", "Low Risk", "Medium Risk"],
            y=[probability[0]*100, probability[1]*100, probability[2]*100],
            marker_color=["#ff4444", "#44bb44", "#ffaa00"],
            text=[f"{probability[0]*100:.1f}%", f"{probability[1]*100:.1f}%", f"{probability[2]*100:.1f}%"],
            textposition="outside"
        ))
        fig.update_layout(title="Risk Probability Breakdown", yaxis_title="Probability percent", height=350)
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("### Your Wellness Radar")
        categories = ["Sleep Quality", "Digital Balance", "Physical Health", "Stress Control", "Social Life", "Academic Balance"]
        values = [
            min(100, (sleep_hours / 8) * 100),
            max(0, 100 - (daily_social_media_hours / 12) * 100),
            min(100, (physical_activity / 2) * 100),
            max(0, 100 - (stress_level / 10) * 100),
            {"low": 30, "medium": 65, "high": 100}[social_interaction_level],
            min(100, (academic_performance / 4) * 100)
        ]

        fig_radar = go.Figure(go.Scatterpolar(
            r=values + [values[0]],
            theta=categories + [categories[0]],
            fill="toself",
            fillcolor="rgba(102, 126, 234, 0.3)",
            line_color="#667eea"
        ))
        fig_radar.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            showlegend=False, height=400,
            title="Mental Wellness Radar Chart"
        )
        st.plotly_chart(fig_radar, use_container_width=True)

        st.markdown("---")
        st.markdown("## Personalized Remedies and Recommendations")

        tab1, tab2, tab3, tab4 = st.tabs(["Diet and Food", "Sleep Tips", "Exercise", "Meditation"])

        with tab1:
            st.markdown("### Food and Diet Recommendations")
            st.markdown("""
Foods That Boost Mental Health:

- Fatty Fish like Salmon and Tuna - Rich in Omega-3, reduces depression - 2 to 3 times per week
- Blueberries - Antioxidants reduce anxiety - Daily
- Dark Leafy Greens - Folate boosts mood - Daily
- Nuts and Seeds - Magnesium reduces stress - Daily snack
- Dark Chocolate 70 percent plus - Releases serotonin - Small piece daily
- Bananas - Tryptophan for better sleep - 1 to 2 daily
- Eggs - Vitamin D and B12 for mood - Daily breakfast

Foods to Avoid:
- Excessive caffeine increases anxiety
- Sugary drinks and junk food cause energy crashes
- Processed and packaged foods
- Energy drinks disrupt sleep

Hydration Tips:
- Drink 8 to 10 glasses of water daily
- Start morning with warm lemon water
- Herbal teas like chamomile and lavender reduce anxiety
            """)

        with tab2:
            st.markdown("### Sleep Improvement Plan")
            if sleep_hours < 6:
                st.error(f"You are only getting {sleep_hours} hours of sleep. You need at least 7 to 8 hours.")
            elif sleep_hours < 7:
                st.warning(f"Your {sleep_hours} hours of sleep is below recommended. Try to get 7 to 8 hours.")
            else:
                st.success(f"Your {sleep_hours} hours of sleep is good. Maintain this habit.")

            st.markdown("""
7 Day Sleep Improvement Plan:

Day 1 - Set a fixed bedtime at 10:30 PM and wake time at 6:30 AM
Day 2 - No screens 1 hour before bed. Read a book instead.
Day 3 - Make bedroom dark and cool. 18 to 20 degrees Celsius is ideal.
Day 4 - Try 4-7-8 breathing technique before sleeping
Day 5 - Avoid caffeine after 2 PM
Day 6 - Take a warm shower before bed
Day 7 - Review your sleep quality and continue what works

Bedtime Routine:
10:00 PM - Put phone on Do Not Disturb
10:15 PM - Light stretching or yoga
10:30 PM - Read a book for 15 minutes
10:45 PM - Deep breathing exercise
11:00 PM - Sleep time
            """)

        with tab3:
            st.markdown("### Exercise Routine for Mental Health")
            if physical_activity < 0.5:
                st.error("Your physical activity is very low. Start with small steps today.")

            st.markdown("""
Weekly Exercise Plan - Beginner Friendly:

Monday - Cardio Day:
- 20 min brisk walk or jogging
- 10 min jumping jacks and skipping
- 5 min cool down stretching

Tuesday - Yoga and Flexibility:
- 15 min morning yoga
- 10 min stretching routine
- 5 min breathing exercises

Wednesday - Strength Training:
- 15 min bodyweight exercises like pushups, squats, lunges
- 10 min core exercises like planks and crunches
- 5 min cool down

Thursday - Active Rest:
- 30 min light walk in nature
- 10 min meditation

Friday - Cardio and Dance:
- 20 min dance workout
- 10 min fun sports activity

Saturday - Outdoor Activity:
- Cycling, swimming, or team sports for 30 to 45 minutes

Sunday - Complete Rest:
- Light stretching only
- Focus on recovery and relaxation

Why Exercise Helps Mental Health:
- Releases endorphins which are natural mood boosters
- Reduces cortisol which is the stress hormone
- Improves sleep quality significantly
- Boosts self confidence and body image
            """)

        with tab4:
            st.markdown("### Meditation and Breathing Techniques")

            med_col1, med_col2 = st.columns(2)

            with med_col1:
                st.markdown("""
4-7-8 Breathing Technique - Best for Anxiety Relief:

1. Sit comfortably and close your eyes
2. Inhale through nose for 4 seconds
3. Hold your breath for 7 seconds
4. Exhale through mouth for 8 seconds
5. Repeat 4 times

Box Breathing - Best for Focus and Calm:

1. Inhale for 4 seconds
2. Hold for 4 seconds
3. Exhale for 4 seconds
4. Hold for 4 seconds
5. Repeat 5 to 10 times
                """)

            with med_col2:
                st.markdown("""
5 Minute Morning Meditation - Best for Starting Day Positively:

1. Sit quietly and close eyes for 1 minute
2. Focus on your breathing for 1 minute
3. Visualize a peaceful place for 1 minute
4. Set your intention for the day for 1 minute
5. Slowly open eyes and stretch gently for 1 minute

Recommended Free Apps:
- Headspace - Guided meditation and mindfulness - 4.8 out of 5 stars
- Calm - Sleep stories and meditation - 4.8 out of 5 stars
- Insight Timer - Free meditation timer and guides - 4.9 out of 5 stars
                """)

        st.markdown("---")
        st.markdown("## Mental Health Helplines India")
        help_col1, help_col2, help_col3 = st.columns(3)
        with help_col1:
            st.error("AASRA - 91-22-27546669 - Available 24 hours 7 days")
        with help_col2:
            st.warning("iCall - 022-25521111 - Professional Counseling")
        with help_col3:
            st.info("Vandrevala Foundation - 1860-2662-345 - Free Support")

elif page == "📋 Self Assessment Quiz":
    st.markdown("# Mental Health Self Assessment Quiz")
    st.markdown("Answer honestly for the most accurate results")
    st.markdown("---")
    st.info("This quiz has 8 questions and takes about 2 minutes.")

    answers = []
    for i, q in enumerate(quiz_questions):
        st.markdown(f"Question {i+1}: {q['question']}")
        answer = st.radio("Select your answer", q["options"], key=f"quiz_{i}", horizontal=True)
        score = q["scores"][q["options"].index(answer)]
        answers.append(score)
        st.markdown("---")

    if st.button("Get My Results", type="primary", use_container_width=True):
        total_score = sum(answers)

        if total_score <= 6:
            status = "GOOD MENTAL HEALTH"
            color = "success"
            description = "Your mental health appears to be in good shape. Keep maintaining your healthy habits."
        elif total_score <= 12:
            status = "MILD CONCERN"
            color = "warning"
            description = "You may be experiencing some stress. Consider implementing some self-care practices."
        elif total_score <= 18:
            status = "MODERATE CONCERN"
            color = "warning"
            description = "Your responses suggest moderate challenges. Consider talking to a counselor."
        else:
            status = "HIGH CONCERN"
            color = "error"
            description = "Your responses suggest significant challenges. Please reach out for professional support."

        st.markdown("## Your Quiz Results")

        if color == "success":
            st.success(f"Result: {status}")
        elif color == "error":
            st.error(f"Result: {status}")
        else:
            st.warning(f"Result: {status}")

        wellness = int((1 - total_score/24) * 100)
        sc1, sc2 = st.columns(2)
        with sc1:
            st.metric("Your Score", f"{total_score} out of 24")
        with sc2:
            st.metric("Wellness Score", f"{wellness} percent")

        st.markdown(description)

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=wellness,
            title={"text": "Mental Wellness Score"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "darkblue"},
                "steps": [
                    {"range": [0, 40], "color": "#ff4444"},
                    {"range": [40, 70], "color": "#ffaa00"},
                    {"range": [70, 100], "color": "#44bb44"}
                ]
            }
        ))
        fig.update_layout(height=350)
        st.plotly_chart(fig, use_container_width=True)
        st.info("This quiz is for self-awareness only. For professional diagnosis please consult a mental health expert.")

elif page == "📈 Progress Tracker":
    st.markdown("# Mental Health Progress Tracker")
    st.markdown("Track your daily mood and wellbeing over time")
    st.markdown("---")

    st.markdown("## Log Today Entry")
    log_col1, log_col2 = st.columns(2)

    with log_col1:
        today_mood = st.select_slider("Todays Mood", options=["Very Low", "Low", "Neutral", "Good", "Excellent"])
        today_sleep = st.slider("Sleep Hours Last Night", 3.0, 10.0, 7.0, 0.5)
        today_stress = st.slider("Stress Level Today 1 to 10", 1, 10, 5)

    with log_col2:
        today_activity = st.selectbox("Physical Activity Today", ["None", "Light Walk", "Moderate Exercise", "Intense Workout"])
        today_social = st.selectbox("Social Interaction Today", ["Isolated", "Minimal", "Moderate", "Very Social"])
        today_notes = st.text_area("Any notes about today?", placeholder="How are you feeling today?")

    if st.button("Save Todays Entry", use_container_width=True):
        st.success(f"Entry saved for {datetime.now().strftime('%B %d %Y')}. Keep tracking daily for better insights!")

    st.markdown("---")
    st.markdown("## Sample Progress Visualization")
    st.info("This shows how your tracker will look after 2 weeks of daily logging")

    days = ["Day 1","Day 2","Day 3","Day 4","Day 5","Day 6","Day 7",
            "Day 8","Day 9","Day 10","Day 11","Day 12","Day 13","Day 14"]
    mood_scores = [2, 3, 2, 4, 3, 5, 4, 3, 4, 5, 4, 5, 4, 5]
    stress_scores = [8, 7, 9, 6, 7, 5, 6, 7, 5, 4, 5, 4, 5, 3]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=days, y=mood_scores, mode="lines+markers",
                            name="Mood Score", line=dict(color="#44bb44", width=2)))
    fig.add_trace(go.Scatter(x=days, y=stress_scores, mode="lines+markers",
                            name="Stress Level", line=dict(color="#ff4444", width=2)))
    fig.update_layout(title="14 Day Mood and Stress Trend",
                     xaxis_title="Days", yaxis_title="Score", height=400)
    st.plotly_chart(fig, use_container_width=True)

elif page == "🎯 Daily Wellness Goals":
    st.markdown("# Daily Wellness Goals")
    st.markdown(f"Today is {datetime.now().strftime('%A %B %d %Y')}")
    st.markdown("---")
    st.markdown("## Todays Wellness Checklist")
    st.info("Check off goals as you complete them throughout the day!")

    completed = 0
    for i, goal in enumerate(wellness_goals):
        if st.checkbox(goal, key=f"goal_{i}"):
            completed += 1

    st.markdown("---")
    progress = completed / len(wellness_goals)
    st.progress(progress)
    st.markdown(f"### Progress: {completed} out of {len(wellness_goals)} goals completed - {int(progress*100)} percent")

    if completed == len(wellness_goals):
        st.balloons()
        st.success("AMAZING! You completed ALL wellness goals today!")
    elif completed >= 8:
        st.success(f"Excellent work! You completed {completed} goals today!")
    elif completed >= 5:
        st.info(f"Good progress! {completed} goals done. Keep going!")
    elif completed >= 1:
        st.warning(f"Great start! {completed} goal done. You can do more!")
    else:
        st.error("Start your wellness journey and check off your first goal!")

    st.markdown("---")
    st.markdown("## Quote of the Day")
    quote_index = datetime.now().day % len(motivational_quotes)
    q = motivational_quotes[quote_index]
    st.markdown(f"*{q['quote']}*")
    st.caption(f"— {q['author']}")

elif page == "🌬️ Breathing Exercise":
    st.markdown("# Guided Breathing Exercises")
    st.markdown("Take a moment to breathe and relax")
    st.markdown("---")

    exercise = st.selectbox("Choose Your Exercise", [
        "4-7-8 Breathing for Anxiety Relief",
        "Box Breathing for Focus and Calm",
        "Deep Belly Breathing for Stress Relief",
        "Alternate Nostril Breathing for Balance"
    ])

    if exercise == "4-7-8 Breathing for Anxiety Relief":
        st.markdown("## 4-7-8 Breathing Technique")
        st.success("Best for anxiety relief and falling asleep")
        st.markdown("""
How to Practice:

1. Sit comfortably with your back straight
2. Exhale completely through your mouth
3. Inhale through nose for 4 seconds - count 1 2 3 4
4. Hold breath for 7 seconds - count 1 through 7
5. Exhale through mouth for 8 seconds - count 1 through 8
6. Repeat 4 times to complete one cycle

Each cycle takes about 19 seconds.
Total time for 4 cycles is about 76 seconds.
        """)
        if st.button("Start 4-7-8 Breathing Session", use_container_width=True):
            import time
            for cycle in range(1, 5):
                st.markdown(f"### Cycle {cycle} of 4")
                with st.spinner("INHALE through nose for 4 seconds..."):
                    time.sleep(4)
                with st.spinner("HOLD your breath for 7 seconds..."):
                    time.sleep(7)
                with st.spinner("EXHALE through mouth for 8 seconds..."):
                    time.sleep(8)
                if cycle < 4:
                    st.success(f"Cycle {cycle} complete!")
                    time.sleep(2)
            st.success("Session Complete! How do you feel?")
            st.balloons()

    elif exercise == "Box Breathing for Focus and Calm":
        st.markdown("## Box Breathing Technique")
        st.success("Best for focus, concentration and calming nerves before exams")
        st.markdown("""
How to Practice:

1. Sit upright and relax your shoulders
2. Inhale slowly for 4 seconds
3. Hold for 4 seconds
4. Exhale for 4 seconds
5. Hold for 4 seconds
6. Repeat 5 to 10 times

Visualize drawing a square as you breathe with one side per step.
        """)

    elif exercise == "Deep Belly Breathing for Stress Relief":
        st.markdown("## Deep Belly Breathing")
        st.success("Best for instant stress relief and lowering blood pressure")
        st.markdown("""
How to Practice:

1. Lie down or sit comfortably
2. Place one hand on chest and one on belly
3. Inhale deeply through nose - belly should rise not chest
4. Exhale slowly through pursed lips
5. Feel belly fall as you exhale
6. Repeat for 5 to 10 minutes

Your chest should remain relatively still.
Your belly should be the one moving.
This activates the parasympathetic nervous system.
        """)

    else:
        st.markdown("## Alternate Nostril Breathing")
        st.success("Best for balance, clarity and removing brain fog")
        st.markdown("""
How to Practice:

1. Sit comfortably with spine straight
2. Use right hand - thumb closes right nostril, ring finger closes left
3. Close right nostril with thumb, inhale through left nostril for 4 seconds
4. Close both nostrils and hold for 4 seconds
5. Close left nostril and exhale through right nostril for 4 seconds
6. Inhale through right nostril for 4 seconds
7. Hold both closed for 4 seconds
8. Exhale through left nostril for 4 seconds
9. This is one complete round - do 5 to 10 rounds
        """)

elif page == "📊 Analytics":
    st.markdown("# Dataset Analytics and Insights")
    st.markdown("---")

    sc1, sc2, sc3, sc4 = st.columns(4)
    with sc1:
        st.metric("Total Records", "2500")
    with sc2:
        st.metric("Model Accuracy", "85 percent plus")
    with sc3:
        st.metric("Features", "11")
    with sc4:
        st.metric("Risk Categories", "3")

    st.markdown("---")
    st.markdown("## Top 5 Mental Health Risk Factors")

    factors = ["Stress Level", "Anxiety Level", "Sleep Hours", "Social Media Usage", "Physical Activity"]
    importance = [0.28, 0.24, 0.18, 0.15, 0.15]

    fig = go.Figure(go.Bar(
        x=importance, y=factors,
        orientation="h",
        marker_color=["#ff4444", "#ff6644", "#ffaa00", "#44aaff", "#44bb44"],
        text=[f"{v*100:.1f}%" for v in importance],
        textposition="outside"
    ))
    fig.update_layout(title="Feature Importance in Depression Risk Prediction",
                     xaxis_title="Importance Score", height=350)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
        st.success("""
Protective Factors:
- 7 to 8 hours sleep per night
- Less than 3 hours social media daily
- 30 plus minutes physical activity
- High social interaction
- Low stress below 4 out of 10
- Good academic performance GPA 3 plus
        """)

    with col2:
        st.error("""
Risk Factors:
- Less than 6 hours sleep
- More than 5 hours social media daily
- High stress levels 8 plus out of 10
- No physical activity
- Low social interaction
- Poor academic performance
        """)

else:
    st.markdown("# About MindGuard")
    st.markdown("---")
    st.markdown("""
## About This Project

MindGuard is an AI-powered mental health risk prediction system developed as a
mini project for B.Tech AIML at Jeppiaar University Chennai.

## Mission
To use Machine Learning to help teenagers identify mental health risks early
and take proactive steps toward better mental wellbeing.

## Technical Stack
- Language: Python 3.12
- Machine Learning: Scikit-learn Random Forest Classifier
- Web App: Streamlit
- Visualization: Plotly Matplotlib Seaborn
- Data Processing: Pandas NumPy
- Deployment: Streamlit Cloud

## Model Performance
- Algorithm: Random Forest with Hyperparameter Tuning
- Accuracy: 85 percent plus
- Dataset: 2500 teen records
- Cross Validation: 3-fold CV

## Developer
Name: Dheeraj Varma
Course: B.Tech AIML 3rd Year
Institution: Jeppiaar University Chennai
Year: 2024-25

## Disclaimer
This tool is for educational purposes only and is NOT a substitute for
professional medical advice. Please consult a licensed professional
if you are experiencing mental health challenges.

## Crisis Support India
- AASRA: 91-22-27546669
- iCall: 022-25521111
- Vandrevala Foundation: 1860-2662-345
- SNEHA: 044-24640050
    """)

st.markdown("---")
st.caption("MindGuard - Teen Mental Health Prediction System - Jeppiaar University - AIML Dept")
st.caption("Developed by Dheeraj Varma - B.Tech AIML 3rd Year - 2024-25")
st.caption("For educational purposes only. Not a substitute for professional medical advice.")
