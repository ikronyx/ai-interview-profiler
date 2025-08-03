
def generate_feedback(filler_count, avg_len, grammar_score):
    tips = []

    if filler_count > 5:
        tips.append("Try reducing filler words like 'um', 'uh', and 'like'.")
    if avg_len > 20:
        tips.append("Consider using shorter sentences for clarity.")
    if grammar_score < 70:
        tips.append("Improve grammatical structure for better flow.")

    return "\n".join(tips or ["Great job! You're on the right track."])
