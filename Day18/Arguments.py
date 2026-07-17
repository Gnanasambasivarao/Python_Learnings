# # variable length arguments: It will be store values in tuple and we use this in star arguments 
# # In default it will take the values in tuple
# def check(*a):
#     print(a)
#     print(type(a))
# check()
# b=[1,2,3,4,5,6]
# check(*b)
# c={4,5,6,7,8}
# check(*c)
# d={'Year':2004,'age':23}
# check(*d)

# def check1(*a):
#     q=1
#     print(a)
#     print(type(a))
#     for i in a:
#         if type(i) in (int,float):
#             q=q+i
#             print(q)
# check1()        
# check1(2,3,4,5,6)        
# check1(2,3,4,5,6,2.3,4.5,7.8)
# check1(7,8,9,8,5,0.5,6.7,"Samba") 

# # Keyword length argumnets:
# # kwargs(**kwaargs)
# # In default it will take values in dictionary

# def information(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
# information()
# w={"marks":[60,70,80,90],"name":"Samba","Age":23}
# information(**w)

# def info(**args):
#     print(args)
#     print(type(args))
#     for i in args:
#         print(i)
#     for i in args.keys():
#         print(i)
#     for i in args:
#         print(args[i])
#     for i in args.values():
#         print(i)
#     for i in args:
#         print(i, args[i])
        
# r={"name":"Samba","age":23,"gender":"Male","scores":[90,100,20,50,80]}
# info(**r)

# combining both *args, **kwargs

def final(*args,**kwargs):
    print(args)
    print(type(args))
    print(kwargs)
    print(type(kwargs))
    t=2
    for i in args:
        t=t+i
        print(t)
    for i,j in kwargs.items():
        print("key",i)
        print("value",j)
  
final()
data=(2,3,4,5,6,7,2.5,3.5,6.9,7.9)
data1={"name":"Samba","age":23,"gender":"Male","scores":[90,100,20,50,80]}
final(*data, **data1)
