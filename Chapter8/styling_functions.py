def make_sandwich(*items):
    """Summarize the sandwich being made."""
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")


make_sandwich('turkey', 'ham', 'lettuce', 'tomato')
make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey mustard')
make_sandwich('peanut butter', 'strawberry jam')