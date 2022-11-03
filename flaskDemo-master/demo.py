class rabbit_pair:

    def __init__(self):
        self.age = 0
    def update(self):
        self.age+=1

def simulate(n):  # n 是需要模拟的月数
    total = [rabbit_pair()]  # total 存储当前所有兔子对，初始时只有一对月龄为 0 的兔子
    for i in range(1, n + 1):  # 从第一个月开始模拟
        for rb in total:  # 遍历现有的所有兔子对
            rb.update()  # 每过一个月，现有的所有兔子对月龄加1
            if rb.age >= 2:  # 如果该对兔子月龄大于等于2，将生下一对新兔子
                total.append(rabbit_pair())  # 将新出生的兔子加入现有的大家庭
    return len(total)  # 返回兔子的对数，如果是只数，则乘以 2


if __name__=='__main__':
    for i in range(20):
        print(simulate(i), end=" ")
    print("\n")