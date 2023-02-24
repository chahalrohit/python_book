def areaSquare(length, breadth):
    area = length+breadth
    return area


def main():
    print('Enter the following values for rectangle : ')
    lengthReact = int(input('Length : integer value : '))
    breadthReact = int(input('Breadth :integer value : '))
    areaReact = areaSquare(lengthReact, breadthReact)
    print('Area of rectangle is : ', areaReact)


if __name__ == '__main__':
    main()
    print('\nEnd of program')
    
    help(main())
