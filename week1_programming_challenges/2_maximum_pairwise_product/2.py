# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    max1=0
    max2=0
    for i in range(n):
        if max1<numbers[i]:
            max1 = numbers[i]
            k=i
    for i in range(n):
        if max2 < numbers[i] and i!=k:
            max2 = numbers[i]
    max_product = max1 * max2
    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
