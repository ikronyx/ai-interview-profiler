
import streamlit as st
from utils.transcribe import transcribe_audio
from utils.analyze_text import count_fillers, avg_sentence_length, grammar_score
from utils.feedback import generate_feedback

st.title("🎤 AI Interview Skill Profiler")

uploaded_file = st.file_uploader("Upload a 1–2 min voice response", type=["wav", "mp3"])

if uploaded_file:
    with open("audio/user_audio.wav", "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("Transcribing..."):
        transcript = transcribe_audio("audio/user_audio.wav")
        st.markdown("### 📝 Transcript")
        st.write(transcript)

    filler_count = count_fillers(transcript)
    avg_len = avg_sentence_length(transcript)
    clarity = grammar_score(transcript)

    st.markdown("### 📊 Analysis")
    st.write(f"**Filler Words**: {filler_count}")
    st.write(f"**Avg. Sentence Length**: {avg_len} words")
    st.write(f"**Grammar Clarity Score**: {clarity}/100")

    st.markdown("### 💡 Feedback")
    st.info(generate_feedback(filler_count, avg_len, clarity))
