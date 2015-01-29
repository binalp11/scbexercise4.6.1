Binal Patel
604048887

How many times will 'hello' be printed?

# 1)
for i in range(3, 17):
    print 'hello'
#will print "hello" 14 times (from 3 to 16)

# 2)
for j in range(12):
    if j % 3 == 0:
       print 'hello'
#will print "hello" when integers from 0 to 11 are perfectly divisible by 3 (0, 3, 6, 9)
# prints "hello" 4 times
 
# 3)
for j in range(15):
	if j % 5 == 3:
		print 'hello'
	elif j % 4 == 3:
		print 'hello'
#will print "hello" when integers from 0-14 are divisible by 5 and have a remainder of 3 (3,8,13)or when the integers are divisible by 4 and have a remainder of 3 (3,7,11)
#prints "hello" 5 times

# 4)
z=0
while z != 15:
	print 'hello'
	z=z+3
#prints "hello" while z is not 15. Each iteration 3 is added to z. Stops when z = 15
#prints "hello" 5 times

# 5)
z = 12
while z < 100:
	if z == 31:
		for k in range(7):
			print 'hello'
	elif z == 18:
		print 'hello' 
	z=z+1
#prints "hello" while z is less that 100, if z equals 31 then it will print "hello" 7 times, else when z equals 18 it will print hello
#prints "hello" 8 times



# What does fooXX do?


def foo1(x):
    return x ** 0.5

#defines a function, foo1, with variable x. The function takes the squareroot of x

def foo2(x, y): 
	ifx>y:
￼￼￼   return x
	return y
#defines a function, foo2, with 2 variables, x and y. If x is greater than y then it will return x, else it will print y. 


def foo3(x, y, z):
	if x > y:
		tmp = y
		y=x
		x = tmp
	if y > z:
		tmp = z
		z=y
		y = tmp
	if x > y:
		tmp = y
		y=x
		x = tmp
	return [x, y, z]
#makes a function where there are 3 variables, (x, y, and z). If x is larger than y, then x and y will switch. If y is greater than z, then y and z will switch.



def foo4(x):
	result = 1
	for i in range(1, x + 1):
		result = result * i
    return result
#makes a function where there is a variable x. Then there is a for loop from 1 to x+1 (or just x since exclusive). Then the value, i, in the for loop is multiplied by the result. The next loop the value, i, is mulitplied by the new result. 



# This is a recursive function
# meaning that the function calls itself
# read about it at
# en.wikipedia.org/wiki/Recursion_(computer_science)


def foo5(x):
    if x == 1:
       return 1
return x * foo5(x - 1)

#this function returns 1 if x equals 1. Then it will take the variable x and multiply by the result of itself (foo5) with the variable being (x-1)
#i wasn't too sure on this one, it is hard to wrap my head around because it is like inception