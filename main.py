deadlineUser = int(input("Enter the date: "))
if deadlineUser == 1:
    print("Full mark")
else:
    if 1 - deadlineUser < 24 :
        print("Late Submission")
    else:
        print("Submitted within 5 days")





