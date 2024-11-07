# # import complex math module
# import cmath
#
# a = float(input('Enter a: '))
# b = float(input('Enter b: '))
# c = float(input('Enter c: '))
#
# # calculate the discriminant
# d = (b ** 2) - (4 * a * c)
#
# # find two solutions
# sol1 = (-b - cmath.sqrt(d)) / (2 * a)
# sol2 = (-b + cmath.sqrt(d)) / (2 * a)
# print('The solution are {0} and {1}'.format(sol1, sol2))




# Python program to find roots of quadratic equation
import math

# function for finding roots
def equationroots(a, b, c):
    # calculating discriminant using formula
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))

    # checking condition for discriminant
    if dis > 0:
        print("real and different roots")
        print((-b + sqrt_val) / (2 * a))
        print((-b - sqrt_val) / (2 * a))

    elif dis == 0:
        print("real and same roots")
        print(-b / (2 * a))

        # when discriminant is less than 0
    else:
        print("Complex Roots")
        print(- b / (2 * a), + i, sqrt_val / (2 * a))
        print(- b / (2 * a), - i, sqrt_val / (2 * a))

    # Driver Program


a = 5
b = 4
c = -20

# If a is 0, then incorrect equation
if a == 0:
    print("Input correct quadratic equation")

else:
    equationroots(a, b, c)
