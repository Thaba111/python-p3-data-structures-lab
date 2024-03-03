spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [food["name"]for food in spicy_foods]
    return names
#Testing function
print(get_names(spicy_foods))


def get_spiciest_foods(spicy_foods):
    sorted_foods = sorted(spicy_foods,key=lambda x:x["heat_level"], reverse=True)
    max_heat_level = sorted_foods[0]["heat_level"]
    spiciest_foods = [food for food in sorted_foods if food["heat_level"] == max_heat_level]
    return spiciest_foods

    #Testing function
print(get_spiciest_foods(spicy_foods))


def print_spicy_foods(spicy_foods):
    # Define a function to convert heat level to 🌶 emojis
    def heat_level_to_emojis(heat_level):
        return "🌶" * heat_level
    
    # Print details of each spicy food item
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        
        # Convert heat level to 🌶 emojis
        heat_emojis = heat_level_to_emojis(heat_level)
        
        # Print food details
        print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")

print_spicy_foods(spicy_foods)




def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # Filter the list to include only foods with the given cuisine
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    
    # If no matching food is found, return None
    return None

# Test case
def test_get_spicy_food_by_cuisine(self):
    '''contains function get_spicy_food_by_cuisine that returns the food that matches a cuisine.'''
    assert(get_spicy_food_by_cuisine(TestDataStructures.SPICY_FOODS, "American") == {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    })



def print_spiciest_foods(spicy_foods):
    # Define a dictionary to map heat levels to corresponding 🌶 emojis
    heat_level_emojis = {
        1: "🌶",
        2: "🌶🌶",
        3: "🌶🌶🌶",
        4: "🌶🌶🌶🌶",
        5: "🌶🌶🌶🌶🌶",
        6: "🌶🌶🌶🌶🌶🌶",
        7: "🌶🌶🌶🌶🌶🌶🌶",
        8: "🌶🌶🌶🌶🌶🌶🌶🌶",
        9: "🌶🌶🌶🌶🌶🌶🌶🌶🌶",
        10: "🌶🌶🌶🌶🌶🌶🌶🌶🌶🌶",
    }

    # Print details of each food with a heat level over 5
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        
        # Check if heat level is over 5
        if heat_level > 5:
            # Format heat level using 🌶 emojis
            heat_emojis = heat_level_emojis.get(heat_level, "Unknown")
            
            # Print food details
            print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")

print_spiciest_foods(spicy_foods)


def get_average_heat_level(spicy_foods):
    # Calculate the average heat level
    total_heat_level = sum(food['heat_level'] for food in spicy_foods)
    average_heat_level = total_heat_level / len(spicy_foods)
    return average_heat_level

def create_spicy_food(spicy_foods, spicy_food):
    # Add the new spicy food to the list
    spicy_foods.append(spicy_food)
    return spicy_foods

# Test the functions
print_spiciest_foods(spicy_foods)
print("Average Heat Level:", get_average_heat_level(spicy_foods))

new_spicy_food = {
    "name": "Fufu",
    "cuisine": "Nigerin",
    "heat_level": 2,
}

spicy_foods = create_spicy_food(spicy_foods, new_spicy_food)
print_spiciest_foods(spicy_foods)
