class Apple:
    # 实现构造器
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight
    # 重写__repr__方法，用于实现Apple对象的“自我描述”
    def __repr__(self):
        return "Apple[color=" + self.color +","+'''
weight=''' + str(self.weight) + "]"+3*'h'
a = Apple("红色" , 5.68)
# 打印Apple对象
print(a)
dict={"Name":"ycy","Age":12}
a=sum(i*j for i in range(3) for j in range(3))
print(a)
b=[3 for i in range(3)]
print(b)