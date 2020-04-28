Module Module1
    Sub Main()
        'TASK 1 – Set up arrays
        'Set-up one dimensional arrays to store:
        '• Student names
        '• Student marks for Test 1, Test 2 and Test 3
        'o Test 1 is out of 20 marks
        'o Test 2 is out of 25 marks
        'o Test 3 is out of 35 marks
        '• Total score for each student
        'Input and store the names for 30 students. 
        'You may assume that the students’ names are unique.
        'Input and store the students’ marks for Test 1, Test 2 and Test 3. 
        'All the marks must be validated on
        'entry and any invalid marks rejected.

        Dim StuName(3) As String
        Dim classTot, index, Test1(30), test2(30), test3(30), total(30) As Integer
        Dim classAvg As Single

        'Initialise
        For index = 1 To 3
            StuName(index) = ""
            Test1(index) = 0
            test2(index) = 0
            test3(index) = 0
            total(index) = 0
        Next
        For index = 1 To 3
            Console.Write("Enter name of student " & index & ": ")
            StuName(index) = Console.ReadLine()

            Console.Write("Enter Test 1 marks of student " & index & ": ")
            'Range check
            Test1(index) = Console.ReadLine()
            While Test1(index) < 0 Or Test1(index) > 20
                Console.Write("Incorrect, ReEnter Please.")
                Test1(index) = Console.ReadLine
            End While

            Console.Write("Enter Test 2 marks of student " & index & ": ")
            'Range check
            test2(index) = Console.ReadLine()
            While test2(index) < 0 Or test2(index) > 25
                Console.Write("Incorrect, ReEnter Please.")
                test2(index) = Console.ReadLine
            End While

            Console.Write("Enter Test 3 marks of student " & index & ": ")
            'Range check
            test3(index) = Console.ReadLine()
            While test3(index) < 0 Or test3(index) > 35
                Console.Write("Incorrect, ReEnter Please.")
                test3(index) = Console.ReadLine
            End While
        Next
        ' TASK 2 – Calculate
        'Calculate the total score for each student and store in the array.
        'Calculate the average total score for the whole class.
        'Output each student’s name followed by their total score.
        'Output the average total score for the class.
        For index = 1 To 3
            total(index) = Test1(index) + test2(index) + test3(index)
            classTot = classTot + total(index)
            Console.WriteLine(StuName(index) & " " & total(index))
        Next
        classAvg = classTot / 3
        Console.WriteLine("Class average marks are = " & classAvg)

        'TASK 3 – Select
        'Select the student with the highest total score 
        'and output their name and total score. 
        Dim highest As Integer = -1000
        Dim highStuNm As String = ""
        For index = 1 To 3
            If total(index) > highest Then
                highest = total(index)
                highStuNm = StuName(index)
            End If
        Next
        Console.WriteLine("Highest score is of " & highStuNm & " , which is " & highest)
        Console.ReadKey()
    End Sub
End Module
