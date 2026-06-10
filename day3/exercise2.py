num = [1,2,3,4,5,6,7,8,9,10,11,12,13,141,1511,19]
gen = (num ** 2 for num in range(10))

print(next(gen))
print(next(gen))
print(next(gen))

for value in gen:
    print(value)
    
# why this coding is important in backend because when me load over lakh rows at once the server runs out of ram and crashes 
#so generator loads one row process it move to the next memory stay flat no matter how big the data is

 
