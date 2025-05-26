
# This is a test comment
# Prompt user for weather input
weather = input("What's the weather like today? (sunny/rainy/cold): ")
# ... (rest of your code) ...
# 
Prompt user for weather input
weather = input("What's the weather like today? (sunny/rainy/cold): ")

# Convert input to lowercase to handle case-insensitivity (e.g., "Sunny" vs "sunny")
weather_lower = weather.lower()

# Provide clothing recommendations based on the input
if weather_lower == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather_lower == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather_lower == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
