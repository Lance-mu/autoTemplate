# _*_ coding:utf-8 _*-
# @Time：2022/7/9 17:05
# 作者：qianwulin

class test:
    def __init__(self, n):
        self.n = n

    # def __len__(self):
    #     return len(self.n)


if __name__ == '__main__':
    t = test([1,2,3,4])
    print(len(t.n))

