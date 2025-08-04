
import streamlit as st
from utils.transcribe import transcribe_audio
from utils.analyze_text import count_fillers, avg_sentence_length, grammar_score
from utils.feedback import generate_feedback
import os

st.title("🎤 AI Interview Skill Profiler")

uploaded_file = st.file_uploader("Upload a 1–2 min voice response v1", type=["wav", "mp3"])

if uploaded_file:

    save_path = os.path.join("/tmp", uploaded_file.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.read())

    print(f"[DEBUG] File saved at: {save_path}")
    
    # with st.spinner("Transcribing..."):
    #     transcript = transcribe_audio(fixed_path)
    #     st.markdown("### 📝 Transcript")
    #     st.write(transcript)

    # filler_count = count_fillers(transcript)
    # avg_len = avg_sentence_length(transcript)
    # clarity = grammar_score(transcript)

    # st.markdown("### 📊 Analysis")
    # st.write(f"**Filler Words**: {filler_count}")
    # st.write(f"**Avg. Sentence Length**: {avg_len} words")
    # st.write(f"**Grammar Clarity Score**: {clarity}/100")

    # st.markdown("### 💡 Feedback")
    # st.info(generate_feedback(filler_count, avg_len, clarity))
