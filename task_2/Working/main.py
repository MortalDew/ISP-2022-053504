import math
from serializer.create_serializer import create_serializer

import sys
sys.setrecursionlimit(20000)

a = 13
my_dict = {
    "qwe": a,
    "qwe1": 123,
    "123": "q23124"
}

class a:
    qwe = 234

    def _show(self):
        return self.qwe + 2042


c = 42
def f(x):
    a = 123
    return math.sin(x * a * c)

def main():
    mytoml = create_serializer("toml")
    myyaml = create_serializer("yaml")
    myjson = create_serializer("json")
    with open("/home/mortaldew/Code/ISP_4_sem/ISP-2022-053504-dev-task-2/task_2/data/data.toml", "w") as file:
        file.write(mytoml.dumps(f))
        file.close()
    print(mytoml.load("/home/mortaldew/Code/ISP_4_sem/ISP-2022-053504-dev-task-2/task_2/data/data.toml")(1))

    myyaml.dump(a, "/home/mortaldew/Code/ISP_4_sem/ISP-2022-053504-dev-task-2/task_2/data/data.yaml")
    serclass = myyaml.load("/home/mortaldew/Code/ISP_4_sem/ISP-2022-053504-dev-task-2/task_2/data/data.yaml")
    print(serclass.qwe)
    print(serclass._show(serclass))

    myjson.dump(my_dict, "/home/mortaldew/Code/ISP_4_sem/ISP-2022-053504-dev-task-2/task_2/data/data.json")
    print(myjson.load("/home/mortaldew/Code/ISP_4_sem/ISP-2022-053504-dev-task-2/task_2/data/data.json"))


if __name__ == "__main__":
    main()

