num = 1

sum = 0

while num <= 5:
    factor_result = 1
    temp = 1
    while temp <= num:
        factor_result *= temp
        temp += 1

    sum += factor_result
    num += 1

print(f'sum is {sum}')