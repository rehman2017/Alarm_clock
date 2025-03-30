import datetime
import streamlit as st
import time

# Initialize session state
if "alarm_set" not in st.session_state:
    st.session_state.alarm_set = False
if "alarm_time" not in st.session_state:
    st.session_state.alarm_time = None
if "sound_file" not in st.session_state:
    st.session_state.sound_file = None

# Streamlit UI
st.set_page_config(page_title="⏰ Streamlit Alarm Clock", layout="centered")

st.title("⏰ Streamlit Alarm Clock with Sound")

# Display live clock
current_time = datetime.datetime.now().strftime("%H:%M:%S")
st.subheader(f"Current Time: {current_time}")

# User selects alarm time
alarm_time = st.time_input("Set Alarm Time:", value=datetime.time(7, 0))  # Default to 7:00 AM
uploaded_file = st.file_uploader("Upload Alarm Sound (MP3/WAV)", type=["mp3", "wav"])

# Set alarm button
if st.button("🔔 Set Alarm"):
    st.session_state.alarm_time = alarm_time.strftime("%H:%M:%S")

    if uploaded_file:
        st.session_state.sound_file = uploaded_file
        st.session_state.alarm_set = True
        st.success(f"Alarm set for {st.session_state.alarm_time}")
    else:
        st.error("Please upload a sound file for the alarm.")

# Alarm check mechanism
if st.session_state.alarm_set:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    if current_time == st.session_state.alarm_time:
        st.warning("⏰ Wake up! It's time!")

        if st.session_state.sound_file:
            try:
                # Play the uploaded audio file
                st.audio(st.session_state.sound_file, format="audio/mp3")
            except Exception as e:
                st.error(f"Error playing sound: {e}")

        # Reset alarm after it rings
        st.session_state.alarm_set = False

st.markdown("---")
st.text("Made by Engr Sir Abdul Rehman Ansari - A Full Stack Developer")
