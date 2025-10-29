def say_hello(name):
    """
    A simple greeting function
    """
    return f"Hello, {name}! Welcome to our project."

def say_goodbye(name):
    """
    A simple farewell function
    """
    return f"Goodbye, {name}! See you soon."

if __name__ == "__main__":
    print(say_hello("World"))
    print(say_goodbye("World"))
