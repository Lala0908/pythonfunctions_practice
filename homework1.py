def (hello):
    print("Hello World!")


def pack(1,2,3):
  return [1,2,3]


def eat_lunch(my_list):
  if len(my_list) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(my_list)):
      if i == 0:
        print(f"First I eat {my_list[0]}")
      else:
        print(f"Next I eat {my_list[i]}")

hello()
print(pack("1","2","3"))
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["pizza"])
eat_lunch(["apple","strawberry","pizza","soup"])