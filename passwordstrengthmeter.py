import streamlit as st
import re

st.markdown(
    """
    <style>
        body {
            background-color: #f0f0f0;
        }
        .stApp {
            background-color: #f0f0f0;
        }
    </style>
    """,
    unsafe_allow_html=True
)

def check_password_strength(password):
    strength = 0
    suggestions = []

    # Length Check
    if len(password) >= 8:
        strength += 1
    else:
        suggestions.append("Make the password at least 8 characters long.")

    # Uppercase & Lowercase Check
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        strength += 1
    else:
        suggestions.append("Use both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r'\d', password):
        strength += 1
    else:
        suggestions.append("Include at least one number.")

    # Special Character Check
    if re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        strength += 1
    else:
        suggestions.append("Add special characters like @, #, $ for better security.")

    # Strength Levels
    if strength == 4:
        return "🟢 Very Strong", []
    elif strength == 3:
        return "🟡 Strong", suggestions
    elif strength == 2:
        return "🟠 Moderate", suggestions
    elif strength == 1:
        return "🔴 Weak", suggestions
    else:
        return "❌ Very Weak", suggestions

# Streamlit UI
st.title("🔐 Password Strength Meter:")
st.title("*✅ Easily generate a strong & secure password! 🔒✨*")
st.write("🚀 Enter a password below to check its strength.")

# User Input
password = st.text_input("Enter Password", type="password")

if password:
    strength, tips = check_password_strength(password)
    st.subheader(f"Password Strength: {strength}")

    if tips:
        st.warning("Suggestions to improve your password:")
        for tip in tips:
            st.write(f"- {tip}")