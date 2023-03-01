def max3(n1, n2, n3):
    def max2(n1, n2):
        if n1 > n2:
            return n1
        else:
            return n2
    return max2(max2(n1, n2), n3)


def main():
    n1 = int(input('Enter first number : '))
    n2 = int(input('Enter second number : '))
    n3 = int(input('Enter third number : '))
    maximum = max3(n1, n2, n3)
    print('Maximum number is : ', maximum)


if __name__ == '__main__':
    main()
