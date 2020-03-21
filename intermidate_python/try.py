# try:
#     open("demo.txt")
# except Exception as e:
#     print(e)


try:
    print("This is try block")
    open("req.txt")
except Exception as e:
    print("This is expection ")
except Exception as e:
    print("This is expection 1111")
else:
    print("this is else block")

finally:
    print("this block will exequte at any cost")

