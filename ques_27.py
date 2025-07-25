# Check if a number entered by the user is prime.
num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is NOT a prime number")  # 0 aur 1 prime nahi hote
else:
    for i in range(2, num):  # 2 se num-1 tak check karo
        if num % i == 0:     # agar divide ho gaya to prime nahi hai
            print(num, "is NOT a prime number")
            break
    else:
        print(num, "is a PRIME number")