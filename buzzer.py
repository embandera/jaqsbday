import pygame
import time

# Initialize Pygame
pygame.init()

# Set up the sound
buzzer_sound = pygame.mixer.Sound("buzzer.wav")

# Function to play the buzzer sound
def play_buzzer():
    buzzer_sound.play()
    time.sleep(1)  # Play sound for 1 second
    buzzer_sound.stop()

if __name__ == "__main__":
    # Load the buzzer sound file
    play_buzzer()
    pygame.quit()
