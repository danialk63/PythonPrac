# # # # # # gros = ['bread', "milk", "cookies"]
# # # # # # print (gros)
# # # # # #
# # # # # # # For Loop
# # # # # #
# # # # # # exp = [2340, 2500, 2100, 3100, 2980]
# # # # # # total = 0 ;
# # # # # #
# # # # # # for i in exp:
# # # # # #
# # # # # #         total = total+i
# # # # # # print(total)
# # # # #
# # # # #
# # # # #
# # # # # # 2
# # # # #
# # # # # # for i in range(1,11):
# # # # # #     print(i)
# # # # #
# # # # #
# # # # # # 3
# # # # #
# # # # # key_location = "chair"
# # # # # locations = ["bed Room", "Lounge", "garage", "chair", "Kitchen"]
# # # # #
# # # # # for i in locations:
# # # # #     if i == key_location:
# # # # #         print("Key is found in ", i)
# # # # #         break
# # # # #
# # # # #     else:
# # # # #         print("Key is not found in ", i)
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # # # Functionsq
# # # # #
# # # #
# # # #
# # # # def Calculate_Total(exp):
# # # #     total = 0;
# # # #     for i in exp:
# # # #         total = total + i;
# # # #
# # # #     return total;
# # # #
# # # #
# # # # Ali_exp = [700, 500, 200]
# # # # Ahmad_exp = [2100, 3400, 3500]
# # # #
# # # # # To calculate the total of both of them individually
# # # #
# # # # Ali_Total = Calculate_Total(Ali_exp)
# # # # Ahmad_Total = Calculate_Total(Ahmad_exp)
# # # # print("Ali Expenses is ", Ali_Total)
# # # # print("Ahmad Expenses is ", Ahmad_Total)
# # # #
# # #
# # #
# # # # Dictionary
# # #
# # # d = {"Ali": 123456, "asad":4567890, "Enujm" : 3989897};
# # # # print (d['asad'])
# # #
# # #
# # # # To add into dictionary
# # #
# # # d["ahmad"]=1098765;
# # # print(d)
# # #
# # # # To delete element into dictionary
# # # del d["Enujm"]
# # # print(d)
# # #
# # #
# # #
# # # for key in d:
# # #     print("Key:" , key, "value: ", d[key])
# #
# #
# #
# #
# # #JSON Format
# #
# # book={}
# #
# # book['Ali'] = {
# #     'Name': 'Ali',
# #     'address':'Raiwind road lahore',
# #     'phone': 1234556666
# # }
# #
# # book["Usman"] = {
# #     'Name': "Usman",
# #     'address':'Johar Town',
# #     'phone': 1867675656687
# # }
# #
# # book["Ahmad"] = {
# #     'Name': "Ahmad",
# #     'address':'Model Town',
# #     'phone': 536484778788
# # }
# #
# #
# # import json
# # s= json.dumps( book)
# # # print(s)
# #
# # with open("D:\DS\project", "w") as ba:
# #     ba.write(s)
# #
# #
#
# # Classes in python
#
#
# class Human:
#     def __init__(self, n,o):
#         self.name = n
#         self.occupation = o;
#
#
#     def do_work(self):
#         if self.occupation == "Programmer":
#             print(self.name, "Code a program")
#
#         elif self.occupation == "Businessman":
#             print(self.name, "Own business")
#
#
#     def speak(self):
#         print(self.name, "Say's Hello")
#
#
# ahmad = Human("Ahmad", "Programmer")
# ahmad.do_work()
# ahmad.speak()
# ali = Human("ALi", "Businessman")
# ali.do_work()
# ali.speak()
#








