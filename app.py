# 註解: ctrl+?
# 複製同一行 ctrl+d

# # 練習print 字串
# output = "我是康尼"
# print(output)
# output_type = type(output)
# print(output_type)
# print(10)

# # 練習list
# fruit_list = ["apple", "watermelon", "banana"]
# print(fruit_list)
# print(type(fruit_list))
#
# number_list = [3, 5, 10]
# print(number_list)
# print(type(number_list))

# # 練習取得list 長度
# fruit_list = ["apple", "watermelon", "banana"]
# fruit_list_len = len(fruit_list)
# print(fruit_list_len)

# # 練習dict
# my_info = {
#     "name": "connie",
#     "phone": "0939351859",
#     "sex": "female"
# }
# print(my_info)
# print(type(my_info))
#
# print(my_info["name"])
# print(my_info["phone"])
# print(my_info["sex"])
#
# print(my_info.get("name"))
# print(my_info.get("phone"))
# print(my_info.get("sex"))
# print(my_info.get("birth", "NO data"))  # get沒有key 返回預設值 沒有帶入預設值參數回傳none

# # 練習set
# name_set = set()
# name_set.add("connie")
# name_set.add("eddie")
# name_set.add("connie")
# print(name_set)
# print(type(name_set))

# # 練習for 迴圈 遍歷fruit_list，print資料
# fruit_list = ["apple", "watermelon", "banana"]
# for i in fruit_list:
#     print(i)

# # 練習for 迴圈 遍歷fruit_list，用set()取得不同水果
# fruit_list = ["apple", "watermelon", "banana", "banana", "lemon", "watermelon", "guava"]
# fruit_set = set()
# for i in fruit_list:
#     fruit_name = i
#     fruit_set.add(i)
#
# print(fruit_set)

# 練習for 迴圈 遍歷fruit_list，用set()取得不同水果, 顯示有幾種水果
fruit_list = ["apple", "watermelon", "banana", "banana", "lemon", "watermelon", "guava"]
fruit_set = set()
for i in fruit_list:
    fruit_name = i
    fruit_set.add(i)

print(len(fruit_set))

# # 練習建立名單與取得不同名字資料筆數
# member_info_list = [{"name": "connie", "phone": "0939351859", "sex": "female"},
#                     {"name": "eddie", "phone": "0987329087", "sex": "male"},
#                     {"name": "johnathon", "phone": "091234567", "sex": "male"},
#                     {"name": "connie", "phone": "0939351859", "sex": "female"},
#                     ]
# print(member_info_list)
# print(type(member_info_list))
# print("=========================================")
# name_set = set()
# # 遍歷 member_info_list 的資料
# for member_info in member_info_list:
#     print(member_info)
#     print(type(member_info))
#     member_name = member_info["name"]
#     print(member_name)
#     name_set.add(member_name)
#
#
# print(len(member_info_list))
# print(len(name_set))


