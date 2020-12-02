# Calculate sum to range of numbers
print("Sum ",sum(list(range(10))))

# Calculate sum of even numbers
# 0+2+4+6+8
print("Sum of even-1",sum(list(range(0,10,2))))
print("Sum of even-2",sum(x for x in range(10) if x%2 == 0))
print("Sum of even-3",sum(filter(lambda x:x%2 ==0, [x for x in range(10)])))

sums=0
for i,v in enumerate(range(10)):
    if i%2 == 0:
        sums+=v
print("Sum of even-4",sums)

# Calculate sum of odd numbers
#1+3+5+7+9
print("Sum of odd-1",sum(list(range(1,10,2))))

# Product/Multiply
# We have an array of integers, and for each index we want to find the product of
# every integer except the integer at that index

l1=[5,7,3,4]
output=[]
for i,e1 in enumerate(l1):
    prod=1
    for j,e2 in enumerate(l1):
        if i!=j:
            prod*=e2
    output.append(prod)
    print("Product List:",output)
print("Final Result:",prod)