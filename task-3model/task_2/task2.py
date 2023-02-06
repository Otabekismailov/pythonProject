'    task 2 3-model    '

'''
task 1 - misol

'''

#
# #
# def task1(n):
#     b = n
#     while True:
#         yield n
#         n += b
#
#
# a = 13
# s = task1(a)
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))
# print(next(s))

'''
task 2 - misol

'''

#
# def task2(n=1000):
#     for Number in range(1, n + 1):
#         count = 0
#         for i in range(2, (Number // 2 + 1)):
#             if Number % i == 0:
#                 count = count + 1
#                 break
#         if count == 0 and Number != 1:
#             yield Number
#
#
# s = task2()
# print(next(s))
# print(next(s))
# print(next(s))


'''

task 3 - misol

'''

# def add(fn):
#     def add1(*args):
#         return fn(*args) * 2
#
#     return add1
#
#
# # print(add())
# @add
# def add2(*args):
#     return sum(args)
#
#
# print(add2(5, 5))

''''

tas 4 - misol 
 
 
'''

# def only_even_parameters(fn):
#     def fun(*args):
#         if any([i for i in args if i % 2 != 0]):
#             return "Please add even numbers"
#         return fn(*args)
#     return fun

# print(only_even_parameters(22, 17))

# @only_even_parameters
# def add2(s, b):
#     return s * b
#
#
# print(add2(6, 6))
'''''
task 5 - misol

'''

#
# def list1(l: list):
#     if type(l) == list:
#         s = 0
#         for i, v in enumerate(l):
#             s += i
#         return s
#
#     else:
#         return f'{l},{"iltimos list kiriting"}'
#
#
# print(list1((2, 4, 5, 6)))
# print(list1([2, 4, 5, 6]))
