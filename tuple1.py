fruits=("apple","banana","orange")
fruits_prices={"apple":68,"banana":70,"orange":90}
l=list(fruits_prices)
s=input("Enter input")
if s in fruits_prices:
    print("price of fruit is:",{fruits_prices[s]}) 
else:
    print("not found")
p=input("please enter yes")
if p=="yes":
    name=input("Enter fruit")
    price=int(input("Enter price"))
    fruits_prices.update({name:price})
    print(fruits_prices)
else:print("no need")



