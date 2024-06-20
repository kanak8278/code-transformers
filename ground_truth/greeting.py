def greet(name, age, email, phone):
    """Greet a person by their name and include additional information."""
    if not (name and age and email and phone):
        raise ValueError("All parameters: name, age, email, and phone must be provided.")
    
    return f"Hello, {name}! You are {age} years old. We have your email as {email} and your phone number as {phone}."
