# HackerRank 30 days code on python Day6
'''
Day6: Task
Given a string s, n  of length  that is indexed from 0 to N , print its even-indexed and odd-indexed characters as 2 space-separated strings
on a single line
Note: 0 is considered to be an even index.
Example
input=adbecf
Print abc def

Input Format
n=2
HAcker
Rank

OUTPUT:
    Hce Akr
    Rn ak
    
The first line contains an integer,  (the number of test cases).
Each line  of the  subsequent lines contain a string, .
'''
# Brute force
# for i in range(n):
#     user_input=input().strip()
#     res_even=[]
#     res_odd=[]
#     for i in range(len(user_input)):
#         if i%2==0:
#             res_even.append(user_input[i])
#         else:
#             res_odd.append(user_input[i])
#     print(f"{"".join(res_even)} {"".join(res_odd)}")

#  for i in range(n):
#     user_input=input().strip()
#     res_even=""
#     res_odd=""
#     for i in range(len(user_input)):
#         if i%2==0:
#             res_even=res_even + user_input[i]
#         else:
#             res_odd=res_odd+(user_input[i]
#     print(f"{res_even} {res_odd}")

n=int(input())
# Optimised version
for _ in range(n):
    s=input()
    print(f"{s[::2]} {s[1::2]}")
    
# => Python code. 
# Swapcase: it used to print vice vers of astinglike
# Example: SaMba 
# => It will print it in "sAmBA"
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# Split and join a string , replace spaces with hypen(-) by using split and join.
def split_and_join(line):
    line=line.split()
    return "-".join(line)
    # write your code here
    # return line.replace(" ","-")

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
    
# Priting first and last name into a string given by user.

def print_full_name(first, last):
    # Write your code here
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
    
# AS we know strings are immutable 
def mutate_string(string, position, character):
    # list1=list(string)
    # list1[position]=character
    # return "".join(list1)
    return f"{string[:position]}{character}{string[position+1:]}"

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
    
# Printing The lsit in reverse order into a single ine by removinf comma nd replacing with sinlge space between 2 numbers

if __name__ =='__main__':
    n=int(input().strip())
    arr=list(map(int, input().rstrip().strip()))
    arr.reverse()
    # Optimised version
    print(*arr)
    # Single line with same as brute force
    print(" ".join(str(i) for i in arr))
    # Brute force
    string=""
    for i in arr:
        string+=str(i)+' '
    print(string.strip)