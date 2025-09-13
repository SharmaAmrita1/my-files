def even_odd_difference(A):
    even_count = 0
    odd_count = 0
    for num in A:
        if num % 2==0:
            even_count +=1
        else:
            odd_count +=1
    return abs(even_count - odd_count )
A = [1,2,3,4]
print(even_odd_difference(A)) 