class NumberOperate():
    def __init__(self):
        self.a = 0
        self.b = 0
    def get_a_b(self):
        v = NumberOperate()
        v.a = int(input("ใส่ค่าตัวเลข a: "))
        v.b = int(input("ใส่ค่าตัวเลข b: "))
        return v
    def add(self,v):
        result_add = v.a + v.b
        return result_add
    def subtract(self,v):
        result_subtract = v.a - v.b
        return result_subtract
    def multiply(self,v):
        result_mul = v.a * v.b
        return result_mul
    def divide(self,v):
        result_div = v.a // v.b
        return result_div

class mainNumberOperate():
    def get_ans():
        tester = NumberOperate()
        test_get_input = tester.get_a_b()
        print("ผลบวกของ a กับ b คือ",tester.add(test_get_input))
        print("ผลลบของ a กับ b คือ",tester.subtract(test_get_input))
        print("ผลคูณของ a กับ b คือ",tester.multiply(test_get_input))
        print("ผลหารของ a กับ b คือ",tester.divide(test_get_input))

mainNumberOperate.get_ans()


