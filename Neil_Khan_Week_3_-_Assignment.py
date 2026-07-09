# Student Name - Neil Khan
# Date - 16 June 2026
# Program Description - Personal Fitness Tracker (Week 3 Assignment)
# Tier Level - Base Level

# Function to calculate calories burned per minute
def calories_per_minute(calories_burned, workout_duration):
    calories_rate = calories_burned / workout_duration
    return round(calories_rate, 1)


# Function to determine workout intensity
def get_intensity(calories_rate):
    if calories_rate < 5.0:
        return "Low"
    elif calories_rate < 10.0:
        return "Moderate"
    else:
        return "High"


# Greeting
print("\n" + "=" * 60)
print("Welcome to the Personal Fitness Tracker app!")
print("=" * 60)

# Get and clean name
full_name = input("Please enter your full name: ").strip().title()

print(f"\nHi {full_name}, please log 3 workouts below:\n")

# Create a list to store workout information
workout_list = []

# Collect and process three workouts
for workout_number in range(1, 4):

    print(f"--- Workout {workout_number} ---")

    # Collect workout information
    workout_name = input("Workout name: ").strip().title()
    workout_duration = int(input("Duration (minutes): "))
    calories_burned = int(input("Calories burned: "))

    # Store workout data in a list
    workout_data = [workout_name, workout_duration, calories_burned]
    workout_list.append(workout_data)

    # Calculate calories per minute
    calories_rate = calories_per_minute(
        calories_burned,
        workout_duration
    )

    # Determine workout intensity
    intensity_label = get_intensity(calories_rate)

    # Display workout summary
    print(
        f"Result: {workout_name} | "
        f"{workout_duration} min | "
        f"{calories_burned} cal | "
        f"{calories_rate} cal/min | "
        f"Intensity: {intensity_label}\n"
    )

# Closing message
# print("\n" + "=" * 60)
print("=" * 60)
print(f"All workouts successfully logged. Great job staying active {full_name}!")
# print("All workouts logged. Great job staying active!")
print("=" * 60)
