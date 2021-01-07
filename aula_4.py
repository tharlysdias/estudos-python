# Try Except Else Finally
try:
	1/0
except (Exception, BaseException, ArithmeticError, ZeroDivisionError) as e:
	print(e)
else:
	print("No Exception")
finally:
	print("Finally")