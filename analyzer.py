import numpy as np

class Analyze:


    def __init__(self,image):
        self.image=image
        

    def brightnessCalculator(self):
        brightness = np.mean(self.image)

        return brightness


    def classifyLight(self):
        return self.brightnessCalculator()>100


    def edgeDetector(self):
        edges=[]
        rows,cols= self.image.shape

        for i in range(rows-1):
            for j in range(cols-1):
                diff=abs(int(self.image[i][j])- int(self.image[i][j+1]))
                if diff>30:
                    edges.append((i,j))
        return edges




