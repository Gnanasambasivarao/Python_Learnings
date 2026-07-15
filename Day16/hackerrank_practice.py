'''
Task 1: Find the runner up score

Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given  scores.
Store them in a list and find the score of the runner-up.
'''


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # Single Line printing ( O(N) )
    print(sorted(set(arr))[-2])
    
    # Normal Code ( O(N*N) ) 
    # res=[]
    # for i in sorted(arr):
    #     if i not in res:
    #         res.append(i) 
    # print(res[-2])
    
    # Option 2: O(N*N)
    # out=[]
    # result=[out.append(i) for i in sorted(arr) if i not in out]
    # print(out[-2])
    
'''
TASK2: List comprehension
Let's learn about list comprehensions! You are given three integers x,y,z and
n representing the dimensions of a cuboid along with an integer.
Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i,j,k is not equal to n .
Here,0<=i,j,k <= x,y,z. Please use list comprehensions rather than multiple loops, as a learning exercise.


'''
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    sol=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k !=n ]
    print(sol)
    
'''
Task 3: Nested lists
Given the names and grades for each student in a class of N students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically and
print each name on a new line.
'''
if __name__ == '__main__':
    result=[]
    scores=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        result.append([name, score])
        scores.append(score)
    
    unique_scores=sorted(list(set(scores)))
    second_value=unique_scores[1]
    
    solution=sorted([i[0] for i in result if i[1] == second_value])
    
    for name in solution:
        print(name)
