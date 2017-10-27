class Mobile():
    def __init__(self,brand,model,year,ScreenSize):
        self.brand = brand
        self.model = model
        self.year = year
        self.ScreenSize = ScreenSize

    def printMobileInfo(self):
        print("brand - " + self.brand.title() + "\n"
              "model - " + self.model.title() + "\n"
              "year  - " + str(self.year) + "\n"
              "screen size  - " + self.ScreenSize.title())


pixel = Mobile("Google","pixel xl",2017,"6 inch")

pixel.printMobileInfo()
