

def generate_odd_numbers(n: int):
    
    result = [str(2*i + 1) for i in range(n)]
    print(", ".join(result))


if __name__ == "__main__":
    a = int(input("Enter a number: "))
    generate_odd_numbers(a)