# If the alien's color is green, the player earns 5 points; otherwise, the player earns 10 points.

alien_color = 'read'

if alien_color == 'green':
    print("You just earned 5 points for shooting the alien!")
elif alien_color == 'yellow':
    print("You just earned 10 points for shooting the alien!")
elif alien_color == 'red':
    print("You just earned 15 points for shooting the alien!")
else:
    print("You didn't shoot any aliens.")