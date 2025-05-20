def generate_odd_sequence(n: int):
    if n % 2 == 1:  
        count = n
    else:  
        count = n - 1 if n > 1 else 1

    
    result = [str(2*i + 1) for i in range(count)]
    print(", ".join(result))


if __name__ == "__main__":
    a = int(input("Enter a number: "))
    generate_odd_sequence(a)