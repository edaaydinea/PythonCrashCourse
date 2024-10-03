def make_car(manufacturer, model, **car_info):
    """Store information about a car in a dictionary."""
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car

# Call the function with additional keyword arguments
car = make_car(manufacturer="maserati",
               model="quattroporte",
               year=2019,
               color="black",
               engine="V8",
               transmission="automatic")

print(car)
