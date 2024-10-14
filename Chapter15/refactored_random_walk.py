# refactored_random_walk.py
from random_walk import RandomWalk
import random
from save_fig import SaveFig
import matplotlib.pyplot as plt

class RefactoredRandomWalk(RandomWalk):
    def __init__(self, num_points=5000):
        super().__init__(num_points)

    def get_step(self):
        # Determine the direction and distance for a step.
        direction = random.choice([1, -1])
        distance = random.choice([0, 1, 2, 3, 4])
        return direction * distance

    def fill_walk(self):
        # Fill the walk with steps using the get_step method.
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

# Create the walk and plot it.
rw = RefactoredRandomWalk()
rw.fill_walk()

plt.figure(dpi=128, figsize=(10, 6))
plt.plot(rw.x_values, rw.y_values, linewidth=1)

savefig = SaveFig()
savefig.save_fig('refactored_random_walk.png')
