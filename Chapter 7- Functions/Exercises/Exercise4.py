def make_shirts(size = "large" , message = "I love Python"):
    """Summarize the shirt that is going to be made."""
    print(f"\nI am going to make a {size} shirt")
    print(f"The message is, '{message}'.")
make_shirts()
make_shirts(size = "medium")
make_shirts("small" , "Be Happy")
