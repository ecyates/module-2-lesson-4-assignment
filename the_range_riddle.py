# 1. The Range Riddle
# Objective: The aim of this assignment is to deepen your understanding of Python's range() function.

# Task 1: Your Mood Today 
# Write a program that prints off different moods for each day of the week. 
# Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm". Using the range() function, 
# loop through every day of the week and for each day, randomly select a mood from the list and print it. 
# Ensure that your program includes the use of the random module to select the mood.

# Example Outcome: An example output could be "On Wednesday, you were feeling happy." 
# "On Thursday you were feeling sad."

# Import the random module
import random

# Define the days of the week
days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# Define the possible moods
moods = ["happy", "sad", "energetic", "calm", "nervous", "stressed", "frustrated", "angry", "overwhelmed", "scared", "anxious", "energetic", "excited", "worried", "depressed", "loved", "cherished", "cared for", "insecure", "strong", "trusting", "important", "self-assured"]

# Iterate through the days of the week
for day in days_of_the_week:
    # Declare the day's mood (randomly selected)
    print("On", day, "you were feeling", random.choice(moods))