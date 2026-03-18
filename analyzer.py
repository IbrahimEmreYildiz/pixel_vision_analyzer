import numpy as np

class Analyze:


    def __init__(self):
        pass


    def brightnessCalculator(image_matris):
        brightness = np.mean(image_matris)
        
        return brightness


    def classifyLight(light):
        
        if light >=128:
            classify="Lighter"
        else:
            classify="Darker"
            
        return classify


    def edgeDetector(image_matris):
        
        result = np.diff(image_matris)
        
        if np.any(result>=30):
            alarm="Edge Detected"
        else:
            alarm="Flat Surface"

        return alarm



