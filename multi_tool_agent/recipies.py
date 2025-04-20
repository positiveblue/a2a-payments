from google.adk.agents import Agent

from . import constants    

INGREDIENTS = [
    # Protein
    {
        "name": "chicken breast", "price": 1.50,
        "nutrition": {"protein": 25, "fat": 3, "carbs": 0, "calories": 130},
        "tags": ["protein", "meat", "non-vegetarian"]
    },
    {
        "name": "pepperoni", "price": 1.20,
        "nutrition": {"protein": 6, "fat": 9, "carbs": 1, "calories": 100},
        "tags": ["protein", "meat", "spicy"]
    },
    {
        "name": "bacon", "price": 1.30,
        "nutrition": {"protein": 5, "fat": 12, "carbs": 0, "calories": 110},
        "tags": ["protein", "meat", "non-vegetarian"]
    },
    {
        "name": "ham", "price": 1.10,
        "nutrition": {"protein": 7, "fat": 4, "carbs": 1, "calories": 80},
        "tags": ["protein", "meat"]
    },
    {
        "name": "tuna", "price": 1.40,
        "nutrition": {"protein": 20, "fat": 2, "carbs": 0, "calories": 100},
        "tags": ["protein", "fish"]
    },
    {
        "name": "sausage", "price": 1.60,
        "nutrition": {"protein": 8, "fat": 10, "carbs": 1, "calories": 120},
        "tags": ["protein", "meat", "spicy"]
    },
    {
        "name": "tofu", "price": 1.00,
        "nutrition": {"protein": 10, "fat": 5, "carbs": 2, "calories": 90},
        "tags": ["protein", "vegetarian", "vegan"]
    },
    {
        "name": "tempeh", "price": 1.10,
        "nutrition": {"protein": 12, "fat": 6, "carbs": 5, "calories": 110},
        "tags": ["protein", "vegetarian", "vegan"]
    },

    # Cheese & Dairy
    {
        "name": "mozzarella", "price": 0.80,
        "nutrition": {"protein": 6, "fat": 5, "carbs": 1, "calories": 70},
        "tags": ["cheese", "vegetarian"]
    },
    {
        "name": "cheddar", "price": 0.90,
        "nutrition": {"protein": 7, "fat": 6, "carbs": 0, "calories": 80},
        "tags": ["cheese", "vegetarian"]
    },
    {
        "name": "parmesan", "price": 1.00,
        "nutrition": {"protein": 8, "fat": 4, "carbs": 0, "calories": 75},
        "tags": ["cheese", "vegetarian"]
    },
    {
        "name": "feta", "price": 0.85,
        "nutrition": {"protein": 4, "fat": 6, "carbs": 1, "calories": 60},
        "tags": ["cheese", "vegetarian"]
    },
    {
        "name": "ricotta", "price": 0.95,
        "nutrition": {"protein": 5, "fat": 4, "carbs": 2, "calories": 65},
        "tags": ["cheese", "vegetarian"]
    },

    # Sauces
    {
        "name": "tomato sauce", "price": 0.40,
        "nutrition": {"protein": 1, "fat": 0, "carbs": 4, "calories": 20},
        "tags": ["sauce", "vegetarian", "vegan"]
    },
    {
        "name": "alfredo sauce", "price": 0.60,
        "nutrition": {"protein": 1, "fat": 6, "carbs": 2, "calories": 70},
        "tags": ["sauce", "vegetarian"]
    },
    {
        "name": "bbq sauce", "price": 0.50,
        "nutrition": {"protein": 1, "fat": 0, "carbs": 6, "calories": 40},
        "tags": ["sauce", "sweet", "vegetarian"]
    },
    {
        "name": "spicy chili sauce", "price": 0.45,
        "nutrition": {"protein": 0, "fat": 0, "carbs": 3, "calories": 25},
        "tags": ["sauce", "spicy", "vegan"]
    },
    {
        "name": "pesto", "price": 0.70,
        "nutrition": {"protein": 2, "fat": 9, "carbs": 1, "calories": 90},
        "tags": ["sauce", "vegetarian"]
    },

    # Vegetables
    {
        "name": "bell peppers", "price": 0.30,
        "nutrition": {"protein": 1, "fat": 0, "carbs": 5, "calories": 25},
        "tags": ["vegetable", "vegan"]
    },
    {
        "name": "mushrooms", "price": 0.35,
        "nutrition": {"protein": 2, "fat": 0, "carbs": 2, "calories": 20},
        "tags": ["vegetable", "vegan"]
    },
    {
        "name": "red onions", "price": 0.25,
        "nutrition": {"protein": 1, "fat": 0, "carbs": 4, "calories": 20},
        "tags": ["vegetable", "vegan"]
    },
    {
        "name": "spinach", "price": 0.30,
        "nutrition": {"protein": 2, "fat": 0, "carbs": 1, "calories": 15},
        "tags": ["vegetable", "vegan"]
    },
    {
        "name": "olives", "price": 0.40,
        "nutrition": {"protein": 0, "fat": 4, "carbs": 1, "calories": 45},
        "tags": ["vegetable", "vegan", "salty"]
    },
    {
        "name": "jalapeños", "price": 0.30,
        "nutrition": {"protein": 1, "fat": 0, "carbs": 2, "calories": 15},
        "tags": ["vegetable", "vegan", "spicy"]
    },
    {
        "name": "pineapple", "price": 0.35,
        "nutrition": {"protein": 0, "fat": 0, "carbs": 6, "calories": 35},
        "tags": ["fruit", "vegan", "sweet"]
    },

    # Toppings & Seasoning
    {
        "name": "chili flakes", "price": 0.10,
        "nutrition": {"protein": 0, "fat": 0, "carbs": 1, "calories": 5},
        "tags": ["spicy", "vegan"]
    },
    {
        "name": "garlic", "price": 0.10,
        "nutrition": {"protein": 0, "fat": 0, "carbs": 1, "calories": 5},
        "tags": ["vegan", "flavor"]
    },
    {
        "name": "basil", "price": 0.10,
        "nutrition": {"protein": 0, "fat": 0, "carbs": 0, "calories": 1},
        "tags": ["herb", "vegan"]
    },
    {
        "name": "oregano", "price": 0.10,
        "nutrition": {"protein": 0, "fat": 0, "carbs": 0, "calories": 1},
        "tags": ["herb", "vegan"]
    },
    {
        "name": "anchovies", "price": 1.00,
        "nutrition": {"protein": 7, "fat": 4, "carbs": 0, "calories": 70},
        "tags": ["fish", "salty"]
    }
]


PIZZAS = [
    {
        "name": "Spicy Chicken Deluxe",
        "ingredients": [
            "chicken breast", "mozzarella", "spicy chili sauce",
            "bell peppers", "red onions", "chili flakes"
        ]
    },
    {
        "name": "Veggie Supreme",
        "ingredients": [
            "mozzarella", "tomato sauce", "mushrooms",
            "spinach", "olives", "bell peppers", "red onions"
        ]
    },
    {
        "name": "Meat Lover's Feast",
        "ingredients": [
            "pepperoni", "bacon", "ham", "sausage",
            "cheddar", "tomato sauce"
        ]
    },
    {
        "name": "Pineapple Paradise",
        "ingredients": [
            "ham", "mozzarella", "pineapple", "tomato sauce"
        ]
    },
    {
        "name": "Mediterranean Magic",
        "ingredients": [
            "feta", "olives", "spinach", "garlic", "tomato sauce", "basil"
        ]
    },
    {
        "name": "BBQ Chicken Crunch",
        "ingredients": [
            "chicken breast", "bbq sauce", "cheddar", "red onions"
        ]
    },
    {
        "name": "Classic Margherita",
        "ingredients": [
            "mozzarella", "tomato sauce", "basil", "oregano"
        ]
    },
    {
        "name": "Green Vegan",
        "ingredients": [
            "tofu", "spinach", "mushrooms", "red onions", "pesto"
        ]
    },
    {
        "name": "Anchovy Firestorm",
        "ingredients": [
            "anchovies", "parmesan", "spicy chili sauce", "chili flakes", "tomato sauce"
        ]
    },
    {
        "name": "Tropical Heat",
        "ingredients": [
            "tuna", "pineapple", "jalapeños", "mozzarella", "bbq sauce"
        ]
    }
]

def calculate_pizza_nutrition(pizza: str) -> tuple[dict, float]:
    """
    Calculate the nutritional information and price of a pizza.
    
    Args:
        pizza: Pizza name string
    """
    total_nutrition = {"protein": 0, "fat": 0, "carbs": 0, "calories": 0}
    total_price = 0
    
    # Find the pizza by name
    pizza_obj = None
    for p in PIZZAS:
        if p["name"] == pizza:
            pizza_obj = p
            break
    
    if not pizza_obj:
        return total_nutrition, total_price
    
    for ingredient_name in pizza_obj["ingredients"]:
        for ingredient in INGREDIENTS:
            if ingredient["name"] == ingredient_name:
                total_nutrition["protein"] += ingredient["nutrition"]["protein"]
                total_nutrition["fat"] += ingredient["nutrition"]["fat"]
                total_nutrition["carbs"] += ingredient["nutrition"]["carbs"]
                total_nutrition["calories"] += ingredient["nutrition"]["calories"]
                total_price += ingredient["price"]
                break

    return total_nutrition, total_price

def get_ingredients(pizza: str) -> list[str]:
    """Get the ingredients for a pizza"""
    for p in PIZZAS:
        if p["name"] == pizza:
            return p["ingredients"]
    return []

pizza_builder_agent = Agent(
    name="pizza_builder_agent",
    model=constants.MODEL,
    description=(
        "Help the user select a pizza based on their preferences."
    ),
    instruction=(
        f"""
        You are a pizza builder agent. You will be given a list of ingredients and a list of pizzas. You will need to build a pizza based on the user's preferences

        Here are the pizzas:
        {PIZZAS}
        """
    ),
    tools=[calculate_pizza_nutrition, get_ingredients],
)