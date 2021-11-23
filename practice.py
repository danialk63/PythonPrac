# gros = ['bread', "milk", "cookies"]
# print (gros)
#
# # For Loop
#
# exp = [2340, 2500, 2100, 3100, 2980]
# total = 0 ;
#
# for i in exp:
#
#         total = total+i
# print(total)



# 2

# for i in range(1,11):
#     print(i)


# 3

key_location = "chair"
locations = ["bed Room", "Lounge", "garage", "chair", "Kitchen"]

for i in locations:
    if i == key_location:
        print("Key is found in ", i)
        break

    else:
        print("Key is not found in ", i)