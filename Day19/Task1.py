n=int(input("Enter a number of students"))
marks=[i for i in range(n)]
def avg(n, arr):
    return sum(arr)/n
    
def calculate(n, marks):
    print("Report: ")
    print("total Students: " ,n)
    print(max(marks))
    print(min(marks))
    print(sum(marks))
    print(avg(marks))

calculate(n, marks)
