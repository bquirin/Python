def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def coprime(a,b):
    print(gcd(a,b) == 1)

coprime(2,10)
