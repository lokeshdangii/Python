year = int(input("Enter year:"))

# if year%4==0:
# 	print("Given year {} is leap".format(year))
# 	if year%100!=0:
# 		print("Given year{} is leap".format(year))
# 	else:
# 		if year%400==0:
# 			print("Given year {} is leap".format(year))
# 		else:
# 			print("not leap year")
# else:
# 	print("Not")

if year%400==0 and year%100==0 or year%4==0:
	print("year{} is leap".format(year))
elif year%4==0 and year%100!=0:
	print("year{} is leap".format(year))
else:
	print("year{} is not leap".format(year))