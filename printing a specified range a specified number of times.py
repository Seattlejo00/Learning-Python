#Getting user inputs for range floor and ceiling
minima = int(input("Enter range minima: "))
premaxima = int(input("Enter range maxima: "))
#The for loop will exclude the maxima so we add one
maxima = premaxima + 1

#Getting the desired number of prints from the user
input = int(input("Enter number of prints: "))
i = 1
while i <= input:
    i = i + 1
    for index in range(minima, maxima):
        print(index)
print("Done!")
