def printTable(nTables=10, nMultiples=10):
    for multiple in range(1, nMultiples+1):
        for num in range(1, nTables+1):
            print('{0:>2}'.format(num), '*',
                  '{0:>2}'.format(multiple), '=',
                  '{0:>3}'.format(num*multiple), '\t', end='')
        print()


def main():
    nTables = int(input('Enter number of multiplication tables : '))
    printTable(nTables)


if __name__ == "__main__":
    main() 
