pip install pygame

import streamlit as st
import pygame
import os

# Initialize Pygame
pygame.mixer.init()

# Load the buzzer sound file
buzzer_sound_path = "buzzer.wav"
if os.path.exists(buzzer_sound_path):
    buzzer_sound = pygame.mixer.Sound(buzzer_sound_path)
else:
    st.error("Buzzer sound file not found. Please ensure 'buzzer.wav' is in the same directory.")

# Function to play the buzzer sound
def play_buzzer():
    buzzer_sound.play()

# Streamlit UI
st.title("Buzzer App")
if st.button("Press to Sound the Buzzer"):
    play_buzzer()
    st.success("Buzzer sounded!")
