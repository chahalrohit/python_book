def main():
    totalMarks = 0
    nSubjects = 0
    while True:
        marks = input('Marks for subject ' + str(nSubjects+1)+': ')
        if marks == '':  # end of input
            break
        marks = float(marks)
        if marks < 0 or marks > 100:
            print('INVALID MARKS !!')
            continue  # marks to be entered again
        nSubjects = nSubjects+1
        totalMarks += marks
    percentage = totalMarks/nSubjects
    print('Total marks : ', int(totalMarks))
    print('Number of Subjects : ', nSubjects)
    print('Percentage : ', round(percentage, 2))


if __name__ == '__main__':
    main()
