def rect_area():
	Length = int(input("Enter Length:"))
	Breadth = int(input("Enter Breadth:"))

	Area = Length*Breadth
	print("Area of Rectangle:", Area)
'''
rect_area()
rect_area()
rect_area()
rect_area()
'''

for i in range(4):
	rect_area()