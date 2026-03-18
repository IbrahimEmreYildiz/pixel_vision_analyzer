import numpy as np
from image_loader import ImageLoader
from analyzer import Analyze
from utils import pixel_generator


loader = ImageLoader()
image = loader.loadFromFile()

analyzer = Analyze(image)
analyzer.brightnessCalculator()




while True:
    select = int(input("\n*******MENU*******\n1-Show analyze results\n2-Quit\nChoose one of them: "))
    if select==2:
        print("\nTerminating the Application")
        break
    elif select==1:
        choice=int(input("\nWill you load from file or use generate random(1: Load from file - 2: Use generate random): "))
        if choice==1:
            loader = ImageLoader()
            obj=loader.loadFromFile()
            analyzer = Analyze(obj)
            
            print("\nBrightness: ", analyzer.brightnessCalculator())
            if analyzer.classifyLight():
                print("\nPicture is lighter.")
            else:
                print("\nPicture is darker.")
            
            print("\nEdge Count: ", len(analyzer.edgeDetector()))

            print("\nEdge Pixels Coordinats: ", analyzer.edgeDetector())



            
        elif choice==2:
            rows=int(input("Please enter the number of rows: "))
            cols=int(input("Please enter the number of cols: "))
            loader = ImageLoader()
            obj=loader.generateRandom(rows,cols)
            analyzer = Analyze(obj)
            
            print("\nBrightness: ", analyzer.brightnessCalculator())
            if analyzer.classifyLight():
                print("\nPicture is lighter.")
            else:
                print("\nPicture is darker.")
            
            print("\nEdge Count: ", len(analyzer.edgeDetector()))

            print("\nEdge Pixels Coordinats: ", analyzer.edgeDetector())




        
