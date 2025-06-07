# ==========================================================
# 🔥 Daily Calorie Needs Calculator with Goal Support
# ✍️ Developed by: [0rvse_] - Algeria 🇩🇿
# 📅 Version: 2025
# 🛡️ All rights reserved – For personal and educational use only
# ==========================================================

import time

def welcome_message():
    print("="*55)
    print("🔥 WELCOME, LEGENDARY RADIYYIN 💪")
    print("🌟 Ready to dominate your health and crush your goals?")
    print("📈 Let's calculate your perfect daily calorie intake!")
    print("="*55)
    time.sleep(2)  # Optional delay for dramatic effect

def calculate_bmr(weight, height, age, gender):
    if gender.lower() == "male":
        return 10 * weight + 6.25 * height - 5 * age + 5
    elif gender.lower() == "female":
        return 10 * weight + 6.25 * height - 5 * age - 161
    else:
        raise ValueError("⚠️ Gender must be 'male' or 'female'.")

def calculate_tdee(bmr, activity_level):
    activity_multipliers = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725,
        "very active": 1.9
    }
    multiplier = activity_multipliers.get(activity_level.lower())
    if multiplier is None:
        raise ValueError("⚠️ Invalid activity level. Use: sedentary, light, moderate, active, very active.")
    return bmr * multiplier

def adjust_calories_for_goal(tdee, goal):
    if goal.lower() == "lose":
        return tdee - 500
    elif goal.lower() == "gain":
        return tdee + 500
    elif goal.lower() == "maintain":
        return tdee
    else:
        raise ValueError("⚠️ Invalid goal. Use: lose, maintain, or gain.")

def evaluate_calories(calories):
    if calories < 1500:
        return "⚠️ Too low – could be unhealthy for most adults."
    elif 1500 <= calories <= 2500:
        return "✅ Normal range for average adult."
    else:
        return "⚠️ High – make sure it matches your goal or training level."

# ========== 👑 Welcome ==========
welcome_message()

# ========== 📥 User Input ==========
print("🔥 Daily Calorie Calculator")
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (cm): "))
age = int(input("Enter your age (years): "))
gender = input("Enter your gender (male/female): ")
activity = input("Enter your activity level (sedentary / light / moderate / active / very active): ")
goal = input("What's your goal? (lose / maintain / gain): ")

# ========== 🧮 Calculations ==========
try:
    bmr = calculate_bmr(weight, height, age, gender)
    tdee = calculate_tdee(bmr, activity)
    goal_calories = adjust_calories_for_goal(tdee, goal)
    status = evaluate_calories(goal_calories)

    print("\n📊 RESULTS:")
    print(f"🔹 BMR (Basal Metabolic Rate): {bmr:.2f} kcal/day")
    print(f"🔸 TDEE (Total Daily Energy Expenditure): {tdee:.2f} kcal/day")
    print(f"🎯 Goal-based Calories ({goal.lower()}): {goal_calories:.2f} kcal/day")
    print(f"📌 Status: {status}")

    # 👤 Developer info
    print("\n👨‍💻 Developed by: @0rvse_")  # Replace with your actual username

except ValueError as ve:
    print(str(ve))