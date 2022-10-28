#
# def hello():
#     print("Hi")
#
# def goodbye():
#     print("So Long")
#
# userchoice = input(
# """
# Press "H" for a hello
# Press "G" for a goodbye
# Press "X" to exit
# """
# ).upper()
# if userchoice in ("H"):
#     hello()
# elif userchoice in ("G"):
#     goodbye()
# elif userchoice in ("X"):
#     pass
# else:
#     valid = "no"

# def add(num1, num2, name):
#     new = num1 + num2
#     print(f"That was {new}, thanks {name}")
#
# #choice = int(input("Enter A number"))
# add(2,7,"Andy")

# def make_string(val, times):
#     print("Calculating.........")
#     res = str(val) * times
#     return res
#
# mystr = make_string(8,10)
#
# print(mystr * 6)

#Default Definition Values
# def print_vat(gross, vatpc=20, message='Summary: '):
#     net = gross / (1 + (vatpc/100))
#     vat = gross - net
#     print(message,'Net: {0:5.2f} Vat: {1:5.2f}'.format(net,vat))
#
# userin = float(input("Enter Cost"))
# print_vat(userin)
# print_vat(11.67, message="final", vatpc=17.5)

# def my_funct(*, file, dir, user='root'):
#     print('file: {:}, dir {:}, to: {:}'.format(file, dir, user))
#     print(f"file: {file}, dir: {dir}, to: {user}")
#
# #by position
# my_funct(file='one', dir='two')

#by Default Values
#my_funct('one','two')

#by name

#my_funct(file='one', user='bob', dir='two')

#variadic functions

# def myFunct(a,b,c):
#     print(a,b,c)
#     print(a)
#
# mytup = 23,45,88
#
# myFunct(*mytup)
#
# def myfun(dir, *args):
#     print('Dir:', dir, 'Files:', args)
#
# myfun('C:/myFiles','f1.txt','f2.txt','f3.pdf')

#**kwargs

# def print_vat(**kwargs):
#     print(kwargs)
#
# # print_vat(vatpc = 17.5, gross=9.54, message="sum: ")
#
# argsdict = dict(vatpc=17.5, gross=9.54, message="sum: ")
# print(argsdict)
# print_vat(**argsdict)


#variables and Scope

# myvar = 7 #Global - used in any part of the code
#
# def scope_test(myvar):
#     myvar = 42 #variable created in subs stay in sub
#     print(myvar)
#     return myvar
#
# print(myvar)
# scope_test(myvar)
# print(myvar)#after subroutine

score = 46

def score_change(score,points):
    global score
    newscore = score
    newscore += points
    return f"Your new Credit Score is {newscore}"

print(score_change(score,8))
print(score)
































