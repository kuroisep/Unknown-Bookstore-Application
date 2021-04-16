import datetime
import os


# def demo_append():
#     with open("Account_User.txt", "r", encoding="utf-8") as f:
#         f.read()
#         f.close()

# # def cash_register():
# #     d = {"m": "mocha", "l": "latte", "e": "espresso", "c": "cappuccino"}
   
# #     with open("1.Login_Page/Regiser/Account_User.txt", mode = "r", encoding="utf-8") as f:
# #         while True:
# #             menu = input("[m]ocha, [l]atte, [e]spresso, [c]appuccino, [q]uit: ")
# #             if menu != "q":
# #                 dt = datetime.datetime.now().strftime("%Y%m%d %H:%M:%S")
# #                 f.write("{},{}\n".format(d[menu], dt))
# #             else:
# #                 break
# #     f.close()

# demo_append()
# # cash_register()


# save_path = '/home'
# file_name = "test.txt"

# completeName = os.path.join(save_path, file_name)
# print(completeName)

# file1 = open(completeName, "w")
# file1.write("file information")
# file1.close()


flieobj = open("1.Login_Page/Regiser/Account_User.txt", mode="r", encoding = "utf-8")

# flieobj.write("User: ")
# flieobj.write("Pass: ")
print(flieobj.read())
flieobj.close()