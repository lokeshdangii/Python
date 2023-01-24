nominee1 = input("Enter the name of 1st nominee: ")
nominee2 = input("Enter the name of 2nd nominee: ")

# initially vote count 
nm1_votes = 0
nm2_votes = 0

voter_id = [1,2,3,4,5,6,7,8,9,10]

no_of_voter = len(voter_id)

while True:
    

    voter = int(input("Enter your voter id : "))
    if voter in voter_id:
        print("You are eligible voter ")
        voter_id.remove(voter) 

        print("------------------------------------------")
        print("To give vote to ",nominee1,"Press 1")
        print("To give vote to ",nominee2,"Press 2")
        print("------------------------------------------")

        vote = int(input("Enter your valuable vote : "))
        if vote == 1:
            nm1_votes += 1
        elif vote == 2:
            nm2_votes += 1
        elif vote == 0 or vote > 2:
            print("Check your Pressed Key ..!!")    
        else :
            print("You are not a waiter or already voted...!!")
    
    if voter_id == []:  # to check the list is over

        print("-----------------------------------")
        print("Voting Session is Over...!!")
        if nm1_votes > nm2_votes:
            percent = (nm1_votes/no_of_voter)*100
            print(nominee1,"has won the election with",percent,"% of votes")
            break 
        elif nm2_votes > nm1_votes:
            percent = (nm2_votes/no_of_voter)*100
            print(nominee2,"has won the election with",percent,"% of votes")
            break
        else:
            print("Both have equal number of votes...!!")
            break

        
        



