def percent(marks, maxMarks):
    percentage = (marks/maxMarks)*100
    return percentage


def main():
    maxMarks = float(input('Enter maximum marks :'))
    assert maxMarks >= 0 and maxMarks <= 500
    marks = float(input('Enter marks obtained : '))
    percentage = percent(marks*maxMarks)
    print('Percentage is : ', percentage)

    if __name__ == '__main__':
        main()
