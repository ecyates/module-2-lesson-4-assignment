# 2. Double Scoop with Nested Loops
# Objective: The aim of this assignment is to practice using nested loops in Python.

# Task 1: Your Mood Tracker 
# Simulate a mood tracker that records your mood at three different times 
# of the day (morning, afternoon, evening) for each day of the week. 
# Use nested loops to implement this: the outer loop should iterate over the days, 
# and the inner loop should iterate over the times of the day. 
# For each time, randomly select a mood from a predefined list and print it. 
# Use the random module again to randomly select the mood.

# Example Outcome: An example would be "On Tuesday afternoon you were sad" 
# "On Tuesday night you were happy" 
# "On Wednesday morning you were tired"

# Import the random module
import random

# Define the times of the day
times_of_the_day = ["morning", "afternoon", "evening"]
# Define the days of the week
days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# Define the possible moods
moods = ["happy", "sad", "energetic", "calm", "nervous", "stressed", "frustrated", "angry", "overwhelmed", "scared", "anxious", "energetic", "excited", "worried", "depressed", "loved", "cherished", "cared for", "insecure", "strong", "trusting", "important", "self-assured"]

# Iterate over the days of the week
for day in days_of_the_week: 
    # Iterate over the times of day
    for time in times_of_the_day: 
        # Declare the randomly selected mood
        print("In the", time, "on", day, "you were feeling", random.choice(moods))
