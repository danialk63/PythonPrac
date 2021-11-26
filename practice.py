# # # gros = ['bread', "milk", "cookies"]
# # # print (gros)
# # #
# # # # For Loop
# # #
# # # exp = [2340, 2500, 2100, 3100, 2980]
# # # total = 0 ;
# # #
# # # for i in exp:
# # #
# # #         total = total+i
# # # print(total)
# #
# #
# #
# # # 2
# #
# # # for i in range(1,11):
# # #     print(i)
# #
# #
# # # 3
# #
# # key_location = "chair"
# # locations = ["bed Room", "Lounge", "garage", "chair", "Kitchen"]
# #
# # for i in locations:
# #     if i == key_location:
# #         print("Key is found in ", i)
# #         break
# #
# #     else:
# #         print("Key is not found in ", i)
# #
# #
# #
# #
# #
# # # Functionsq
# #
#
#
# def Calculate_Total(exp):
#     total = 0;
#     for i in exp:
#         total = total + i;
#
#     return total;
#
#
# Ali_exp = [700, 500, 200]
# Ahmad_exp = [2100, 3400, 3500]
#
# # To calculate the total of both of them individually
#
# Ali_Total = Calculate_Total(Ali_exp)
# Ahmad_Total = Calculate_Total(Ahmad_exp)
# print("Ali Expenses is ", Ali_Total)
# print("Ahmad Expenses is ", Ahmad_Total)
#


# Dictionary

d = {"Ali": 123456, "asad":4567890, "Enujm" : 3989897};
# print (d['asad'])


# To add into dictionary

d["ahmad"]=1098765;
print(d)

# To delete element into dictionary
del d["Enujm"]
print(d)



for key in d:
    print("Key:" , key, "value: ", d[key])