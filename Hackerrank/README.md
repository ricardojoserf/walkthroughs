### Find the Runner-Up Score!

https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains n. The second line contains an array A[] of n integers each separated by a space.

Constraints
- 2 <= n <= 10
- -100 <= A[i] <= 100 

Output Format

Print the runner-up score.


```
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    
    max_number = -101
    for i in range(0,n):
        #print(i)
        if arr[i] > max_number:
            max_number = arr[i]
    #print(max_number)
    
    runnerup = -101
    for i in range(0,n):
        if arr[i] > runnerup and arr[i] != max_number:
            runnerup = arr[i]
    print (runnerup)
```

--------------------------------------

### Nested Lists

https://www.hackerrank.com/challenges/nested-list/problem

Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Input Format

The first line contains an integer, N, the number of students.
The 2N subsequent lines describe each student over 2 lines.
- The first line contains a student's name.
- The second line contains their grade.

Constraints

There will always be one or more students having the second lowest grade.

Output Format

Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input 0

```
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
```

Sample Output 0

```
Berry
Harry
```

```
if __name__ == '__main__':
    aux_list = []
    aux_scores = []
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        aux_list.append([name, score])
        aux_scores.append(score)
    #print(aux_list)
    
    min_number = 100
    for i in range(0,len(aux_scores)):
        #print(i)
        if aux_scores[i] < min_number:
            min_number = aux_scores[i]
    #print(min_number)
    
    secondlowest = 100
    for i in range(0,len(aux_scores)):
        if aux_scores[i] < secondlowest and aux_scores[i] != min_number:
            secondlowest = aux_scores[i]
    #print (secondlowest)
    
    aux_names = []
    for i in aux_list:
        if i[1] == secondlowest:
            aux_names.append(i[0])
    
    for i in sorted(aux_names):
        print(i)
```

--------------------------------------

### Finding the percentage

https://www.hackerrank.com/challenges/finding-the-percentage/problem

The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

Input Format

The first line contains the integer , the number of students' records. The next  lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.

Constraints
- 2 <= n <= 10
- 0 <= marks[i] <= 100
- length of marks array = 3

Output Format

Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

Sample Input 0

```
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
```

Sample Output 0

```
56.00
```

```
if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    number_marks = 0
    total_marks = 0
    for i in student_marks.get(query_name):
        number_marks += 1
        total_marks += i 
    print("%.2f" % float(total_marks/number_marks))
```
