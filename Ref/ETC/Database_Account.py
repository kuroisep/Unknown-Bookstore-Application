import csv 

login = False
while login == False:
    #A log in which uses a database to find multiple usernames and passwords 
    data = []
    Account_file_path = "1.Login_Page/Regiser/Account_User.txt"
    with open(Account_file_path,encoding = "utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    # print(data)
    un = input("Please enter username: ")
    pw = input("Please enter password: " )
    #loope through all the date in column 0 and 1 assigns it to a variable called 'cold/toll
    col0 = [x[0] for x in data]
    col1 = [x[1] for x in data]
    #print(cold)
    if un in col0:
        # literate. through the list for the length of the list 
        for k in range(0, len(col0)):
            # checks if username matches the pw in the ajoining column 
            if col0[k]	== un and col1[k] == pw:
                print("You are logged in")
                login = True
    else:
        print("Wrong username or password")
