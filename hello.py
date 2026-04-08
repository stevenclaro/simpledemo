# simple-demo / hello.py
def say_hello():
    print("Hello, Open Source!")

# 新增：加法函数
def add(a, b):
    return a + b
    
if __name__ == "__main__":
    say_hello()
    # 调用加法函数演示
    print("10 + 20 =", add(10, 20))
