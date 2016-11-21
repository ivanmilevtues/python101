def is_prime(n):
    if(n < 2):
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def goldbach(n):
    result = []
    for i in range(n // 2 + 1):
        # print(str(is_prime(i)) + ' ' + str(i))
        if is_prime(i):
            if is_prime(n - i):
                result.append((i, n - i))
    return sorted(result)


def main():
    print(goldbach(4))
    print(goldbach(6))
    print(goldbach(8))
    print(goldbach(10))
    print(goldbach(100))


if __name__ == '__main__':
    main()
