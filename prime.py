def prime():
    try:
        user_input = input("Enter numbers separated by spaces: ")
        numbers = [int(x) for x in user_input.split()]
        primes=[p for p in numbers if p>1 and all(p%i!=0 for i in range(2,int(p**0.5)+1))]
        print(f"Original values:  {numbers}")
        print(f"Prime numbers in the original data:  {primes}")
    except ValueError:
        print("Invalid input!Enter a valid number.")
if __name__=="__main__":
    prime()
