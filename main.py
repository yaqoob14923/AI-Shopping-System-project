# Function for generating personalized recommendations
def personalized_recommendations(user_preferences, products):
    recommended_products = []
    for product in products:  # Loop through all products
        if product['category'] in user_preferences:  # Nested condition 1
            if product['rating'] > 4.0:  # Nested condition 2
                recommended_products.append(product['name'])  # Add to recommendations
    return recommended_products

# Example Input Data
user_preferences = ['electronics', 'books']
products = [
    {'name': 'Smartphone', 'category': 'electronics', 'rating': 4.5},
    {'name': 'Laptop', 'category': 'electronics', 'rating': 4.2},
    {'name': 'Book A', 'category': 'books', 'rating': 3.8},
    {'name': 'Book B', 'category': 'books', 'rating': 4.6},
    {'name': 'Headphones', 'category': 'accessories', 'rating': 4.3}
]

# Calling the function
recommended = personalized_recommendations(user_preferences, products)

# Output the recommended products
print("Recommended Products:", recommended)
