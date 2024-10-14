import os
import matplotlib.pyplot as plt

class SaveFig:
    # Save all images to images folder
    def save_fig(self, fig_id, tight_layout=True):
        
        # Create a folder to save images
        PROJECT_ROOT_DIR = "."
        IMAGES_PATH = os.path.join(PROJECT_ROOT_DIR, "images")
        os.makedirs(IMAGES_PATH, exist_ok=True)
        
        # Save the image
        path = os.path.join(IMAGES_PATH, fig_id)
        print("Saving figure", fig_id)
        if tight_layout:
            plt.tight_layout()
        plt.savefig(path, format='png', dpi=300)
        
        