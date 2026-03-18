import numpy as np

class ImageLoader:
    
    
    
    def __init__(self):
        pass




    def loadFromFile(self):
        with open ("image.txt", mode='r', encoding='UTF-8') as file:
            py_list=file.readlines()
            
            np_multi=([])
            for numbers in py_list:
                numbers = [int(x) for x in numbers.split()]
                np_multi.append(numbers)
            np_multi=np.array(np_multi)
        return np_multi   




    
    def generateRandom(self,row,column):          
        generate_array = np.random.randint(0,256,(row,column)) 
        return generate_array   