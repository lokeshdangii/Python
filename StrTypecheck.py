'''
int:- all numbers
float:- all numbers and one dot
str:- Any Characters

Int:-
 num_count:- 1 and more than 1
 dot_count:- 0
 other_cont:-0

Float:-
  num_count:- 1 and more than 1
  dot_count:- 1
  ohter_count:- 0

'''

num_char = ["0","1","2","3","4","5","6","7","8","9"]
num_count = 0
dot_count = 0
other_count = 0

user_value = input("Enter value:")
for i in user_value:
	if i in num_char:
		num_count += 1
	elif i ==".":
		dot_count +=1
	else:
		other_count+=1
	
if other_count==0 and dot_count ==0:
	user_value = int(user_value)
elif other_count==0 and dot_count==1:
	user_value = float(user_value)
else:
	user_value = str(user_value)

print("user value =",user_value)
print("Type",type(user_value))

