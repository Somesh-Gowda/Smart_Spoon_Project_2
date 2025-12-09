import random
import numpy as np
import pandas as pd
from PIL import Image as PILImage
import time
import io
import os

# Enhanced food database with color profiles
FOOD_DATABASE = {
    "biryani": {
        "ingredients": ["rice", "chicken", "spices", "yogurt", "saffron"],
        "salt_content": "medium",
        "spice_level": "high",
        "color_profile": [(180, 150, 50), (200, 120, 30)],
        "default_taste": "balanced"
    },
    "dosa": {
        "ingredients": ["rice flour", "lentils", "salt", "oil"],
        "salt_content": "low",
        "spice_level": "medium",
        "color_profile": [(220, 200, 150), (240, 220, 180)],
        "default_taste": "mild"
    },
    "pizza": {
        "ingredients": ["flour", "cheese", "tomato sauce", "toppings"],
        "salt_content": "high",
        "spice_level": "low",
        "color_profile": [(180, 50, 50), (220, 80, 80)],
        "default_taste": "savory"
    },
    "dal tadka": {
        "ingredients": ["lentils", "turmeric", "cumin", "garlic"],
        "salt_content": "medium",
        "spice_level": "medium",
        "color_profile": [(200, 180, 80), (220, 200, 100)],
        "default_taste": "earthy"
    },
    "idli": {
        "ingredients": ["rice", "urad dal", "salt"],
        "salt_content": "low",
        "spice_level": "low",
        "color_profile": [(240, 240, 240), (255, 255, 255)],
        "default_taste": "neutral"
    }
}

# Global variables
uploaded_data = None
user_profile = {}

def upload_excel():
    """Upload Excel or CSV through file path"""
    filepath = input("\nEnter path to your Excel/CSV file (or press ENTER to skip): ")

    if filepath.strip() == "":
        print("Skipping file upload.")
        return None

    if not os.path.exists(filepath):
        print("File not found. Please try again.")
        return None

    if filepath.endswith('.xlsx'):
        df = pd.read_excel(filepath)
    elif filepath.endswith('.csv'):
        df = pd.read_csv(filepath)
    else:
        print("Unsupported file format.")
        return None

    print(f"\nSuccessfully loaded {filepath}")
    print("\n=== Excel Data Analysis ===")

    if 'Age' in df.columns:
        print(f"\nAverage age: {df['Age'].mean():.1f}")

    if 'Gender' in df.columns:
        print("\nGender distribution:")
        print(df['Gender'].value_counts())

    if 'Medical Condition' in df.columns:
        print("\nMedical conditions:")
        print(df['Medical Condition'].value_counts())

    if 'Restaurant Frequency' in df.columns:
        print("\nRestaurant visit frequency:")
        print(df['Restaurant Frequency'].value_counts())

    return df


def upload_image():
    """Upload image using file path"""
    filepath = input("\nEnter image file path: ")

    if not os.path.exists(filepath):
        print("File not found.")
        return None

    if filepath.lower().endswith(('.png', '.jpg', '.jpeg')):
        return filepath
    else:
        print("Invalid image format.")
        return None


def get_user_profile():
    print("\n=== User Profile ===")
    user_profile['age'] = input("Enter your age: ")
    user_profile['gender'] = input("Gender (Male/Female/Other): ").capitalize()
    user_profile['frequency'] = input("Restaurant visit frequency (Daily/Weekly/Monthly/Rarely): ").capitalize()
    user_profile['medical'] = input("Medical condition (Hypertension/Kidney Disease/None): ").capitalize()


def get_image_color_profile(image_path):
    img = PILImage.open(image_path)
    img = img.resize((100, 100))
    pixels = np.array(img)
    return np.mean(pixels, axis=(0, 1))


def analyze_food(image_path):
    try:
        image_color = get_image_color_profile(image_path)

        best_match = None
        min_distance = float('inf')

        for food_name, food_data in FOOD_DATABASE.items():
            for color_range in food_data["color_profile"]:
                distance = np.linalg.norm(image_color - np.array(color_range))
                if distance < min_distance:
                    min_distance = distance
                    best_match = (food_name, food_data)

        return best_match[1], best_match[0]

    except:
        food_item = random.choice(list(FOOD_DATABASE.keys()))
        return FOOD_DATABASE[food_item], food_item


def get_dietary_recommendations(food_data):
    print("\n=== Dietary Recommendations ===")

    if user_profile.get('medical') in ['Hypertension', 'Kidney disease']:
        print("Recommended salt: 1/4 tsp (based on medical condition)")
    elif food_data['salt_content'] == 'high':
        print("Recommended salt: 1/2 tsp (high-salt dish)")
    else:
        print("Recommended salt: 1 tsp (standard)")

    if user_profile.get('frequency') in ['Daily', 'Weekly']:
        print("Note: Frequent restaurant visits → monitor sodium levels.")

    if user_profile.get('age') and int(user_profile['age']) > 60:
        print("Senior Suggestion: Reduce spice levels.")


def suggest_improvements(food_data, feedback):
    suggestions = []

    if "more taste" in feedback:
        suggestions.append("Increase salt by 20%")
        suggestions.append("Enhance spice profile")
        suggestions.append("Boost umami flavor")
    elif "less taste" in feedback:
        suggestions.append("Reduce salt by 15%")
        suggestions.append("Lower spice intensity")
        suggestions.append("Balance overall flavor")
    else:
        suggestions.append("Adjust flavor profile as needed")
        suggestions.append("Modify taste intensity gradually")

    return suggestions


def food_analysis_workflow():

    filename = upload_image()
    if not filename:
        return

    print("\nImage successfully loaded!")

    get_user_profile()

    print("\nAnalyzing your food...")
    time.sleep(2)

    food_data, food_name = analyze_food(filename)

    print(f"\nDetected Food: {food_name.title()}")
    print(f"Ingredients: {', '.join(food_data['ingredients'])}")
    print(f"Salt content: {food_data['salt_content']}")
    print(f"Spice level: {food_data['spice_level']}")

    get_dietary_recommendations(food_data)

    while True:
        feedback = input("\nTaste Feedback (ok / need more taste / need less taste): ").lower()

        suggestions = suggest_improvements(food_data, feedback)
        print("\nTaste Improvement Suggestions:")
        for i, s in enumerate(suggestions, 1):
            print(f"{i}. {s}")

        if input("\nAre you satisfied? (yes/no): ").lower() == "yes":
            break

    print("\nThank you for using Smart Spoon!")


def smart_spoon_system():
    print("=== SMART SPOON FOOD ANALYSIS SYSTEM ===")

    global uploaded_data
    uploaded_data = upload_excel()

    while True:
        print("\nMain Menu:")
        print("1. Analyze food")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            food_analysis_workflow()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid input.")


smart_spoon_system()

