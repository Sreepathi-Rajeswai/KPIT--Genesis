class car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def display_info(self):
        print(self.make)
        print(self.model)
        print(self.year)
    def calculate_depreciation(self,years):
        return years
        for i in range(self,years):
            d_r=0.15
            y=years-self.year
            d_v=self.model*(1-d_r)**y
info=car("sara","bmw",2001)
info.display_info()
years=input("Enter years")
print(info.calculate_depreciation(years))