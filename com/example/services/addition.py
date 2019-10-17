import sys

print("to get result, enter =")

nums = []
obj = input("Please enter a number :")

while obj != "=":
    try:
        nums.append(int(obj))
    except Exception as e:
        print(f"Exception occurred : {e}")
        print("try again!")
        sys.exit()
    finally:
        print("yahooo....")
    obj = input("Please enter a number :")

print(nums)

result = sum(nums)
print(f"Sum is {result}")
