def get_calories(fruit):
    fruits ={
        "apple": 130,
        "banana": 110,
        "cherries": 50,
        "grapes": 90,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80,
        "avocado":50
    }
    return fruits.get(fruit.lower())

def main():
    fruit =input("Fruits: ").strip().lower()
    calories= get_calories(fruit)
    if calories:
        print(f"Calories: {calories}")

main()
