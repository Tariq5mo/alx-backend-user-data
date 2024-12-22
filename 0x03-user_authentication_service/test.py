def example_function(**kwargs):
    print(", ".join(f"{key}={value}" for key, value in kwargs.items()))

# Calling the function with arbitrary keyword arguments
example_function(name="Alice", age=30, city="Wonderland")
