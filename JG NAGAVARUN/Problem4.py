

def count_multiples(nums):
    counts = {}
    for i in range(1, 10):
        counts[i] = sum(1 for num in nums if num % i == 0)
    return counts


if __name__ == "__main__":
    input_list = [1,2,8,9,12,46,76,82,15,20,30]
    result = count_multiples(input_list)
    print(result)