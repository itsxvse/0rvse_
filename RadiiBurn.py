# ==========================================================
# 🔥 Calorie + Body Fat Calculator with Meal Suggestions
# ✍️ Developed by: @0rvse_ - Algeria 🇩🇿
# 📅 Version: 2025
# 🛡️ All rights reserved – For personal and educational use only
# ==========================================================

import time
import math

# ========== 🎬 Welcome ==========
def welcome_message():
    print("="*60)
    print("🔥 WELCOME TO THE ULTIMATE CALORIE + FAT TRACKER 🔥".center(60))
    print("💪 Built for legends who want RESULTS 💯".center(60))
    print("="*60)
    time.sleep(1.5)

# ========== ⚙️ Calculations ==========

def calculate_bmr(weight, height, age, gender):
    if gender == "male":
        return 10 * weight + 6.25 * height - 5 * age + 5
    elif gender == "female":
        return 10 * weight + 6.25 * height - 5 * age - 161
    else:
        raise ValueError("🚨 Error: Gender must be 'male' or 'female'.")

def calculate_tdee(bmr, activity_level):
    levels = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725,
        "very active": 1.9
    }
    if activity_level not in levels:
        raise ValueError("🚨 Invalid activity level.")
    return bmr * levels[activity_level]

def adjust_calories(tdee, goal):
    if goal == "lose":
        return tdee - 500
    elif goal == "gain":
        return tdee + 500
    elif goal == "maintain":
        return tdee
    else:
        raise ValueError("🚨 Invalid goal.")

def evaluate_calories(calories):
    if calories < 1500:
        return "⚠️ Too low – may be unhealthy!"
    elif calories <= 2500:
        return "✅ Normal range for most adults."
    else:
        return "⚠️ High – make sure it matches your goals."

def calculate_body_fat(gender, waist, neck, height, hip=None):
    if gender == "male":
        return round(495 / (1.0324 - 0.19077 * math.log10(waist - neck) + 0.15456 * math.log10(height)) - 450, 2)
    elif gender == "female":
        if hip is None:
            raise ValueError("Hip measurement is required for females.")
        return round(495 / (1.29579 - 0.35004 * math.log10(waist + hip - neck) + 0.221 * math.log10(height)) - 450, 2)
    else:
        raise ValueError("Invalid gender.")

def suggest_meals(goal):
    if goal == "gain":
        return [
            "🍚 Chicken + Rice + Olive Oil (~600 kcal)",
            "🥜 Peanut Butter Toast + Banana (~400 kcal)",
            "🥤 Mass Gainer Smoothie (Milk + Oats + Honey + Protein) (~700 kcal)"
        ]
    elif goal == "lose":
        return [
            "🥗 Tuna/Chicken Salad with Olive Oil (~350 kcal)",
            "🍳 Boiled Eggs + Veggies + Whole Grain Bread (~300 kcal)",
            "🥛 Low-fat Yogurt + Nuts (~250 kcal)"
        ]
    else:
        return ["🥦 Balanced Meals – Maintain with clean eating & variety."]

# ========== 📊 Display ==========
def display_results(bmr, tdee, goal_calories, status, fat_pct, goal):
    print("\n" + "="*60)
    print("📊 YOUR RESULTS".center(60))
    print("="*60)
    print(f"🔹 BMR (Basal Metabolic Rate):       {bmr:.2f} kcal/day")
    print(f"🔸 TDEE (Total Daily Energy):        {tdee:.2f} kcal/day")
    print(f"🎯 Goal Calories ({goal}):           {goal_calories:.2f} kcal/day")
    print(f"🧮 Body Fat Percentage:              {fat_pct:.2f}%")
    print(f"📌 Status:                           {status}")
    print("-"*60)
    print("🍽️ Recommended Meals:")
    for meal in suggest_meals(goal):
        print(f"   {meal}")
    print("="*60)
    print("👨‍💻 Developed by: @0rvse_  | 🇩🇿 Algeria")
    print("="*60)

# ========== 🚀 Main ==========
def main():
    welcome_message()

    try:
        # --- Input ---
        weight = float(input("⚖️  Enter your weight (kg): "))
        height = float(input("📏 Enter your height (cm): "))
        age = int(input("🎂 Enter your age (years): "))
        gender = input("🚻 Enter your gender (male/female): ").lower()
        waist = float(input("📏 Enter your waist size (cm): "))
        neck = float(input("📏 Enter your neck size (cm): "))
        hip = None
        if gender == "female":
            hip = float(input("📏 Enter your hip size (cm): "))
        activity = input("🏃 Activity level (sedentary / light / moderate / active / very active): ").lower()
        goal = input("🎯 Goal? (lose / maintain / gain): ").lower()

        # --- Calculation ---
        bmr = calculate_bmr(weight, height, age, gender)
        tdee = calculate_tdee(bmr, activity)
        goal_calories = adjust_calories(tdee, goal)
        status = evaluate_calories(goal_calories)
        fat_pct = calculate_body_fat(gender, waist, neck, height, hip)

        # --- Output ---
        display_results(bmr, tdee, goal_calories, status, fat_pct, goal)

    except Exception as e:
        print(f"❌ Error: {str(e)}")

# ========== 🔁 Run ==========
if __name__ == "__main__":
    main()
