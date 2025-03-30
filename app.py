import datetime
import time
import streamlit as st
from pydub import AudioSegment
from pydub.playback import play


def set_alarm(alarm_time, sound_file):
    try:
        # Handle both 12-hour and 24-hour formats
        if "AM" in alarm_time.upper() or "PM" in alarm_time.upper():
            parsed_time = datetime.datetime.strptime(alarm_time, "%I:%M %p")
        else:
            parsed_time = datetime.datetime.strptime(alarm_time, "%H:%M:%S")
    except ValueError:
        st.error("Invalid time format! Please enter time in HH:MM:SS or HH:MM AM/PM format.")
        return

    alarm_time_str = parsed_time.strftime("%H:%M:%S")
    st.success(f"Alarm set for {alarm_time_str}")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time_str:
            st.warning("Wake up! It's time!")
            try:
                sound = AudioSegment.from_file(sound_file)
                play(sound)
            except Exception as e:
                st.error(f"Error playing sound: {e}")
            break
        time.sleep(1)


if __name__ == "__main__":
    st.title("⏰ Alarm Clock with Sound")
    alarm_time = st.text_input("Enter the alarm time (e.g., HH:MM:SS or HH:MM AM/PM):")
    sound_file = st.text_input("Enter the path to your alarm sound file (e.g., C:/path/to/your/alarm.mp3):")

    if st.button("Set Alarm") and alarm_time and sound_file:
        set_alarm(alarm_time, sound_file)

    st.markdown("---")
    st.text("Made by Engr Sir Abdul Rehman Ansari A full stack developer")
