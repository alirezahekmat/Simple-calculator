a = int(input())
c = input()
b = int(input())
class Calc:
    def sum(self,first_number,secend_number):
        return  first_number + secend_number
    def sub(self,first_number,secend_number):
        return first_number - secend_number
    def multi(self,first_number,secend_number):
        return first_number * secend_number
    def div(self,first_number,secend_number):
        return first_number / secend_number
calc=Calc();

if c=="+":
    print(calc.sum(a,b))
if c=="-":
    print(calc.sub(a,b))
if c=="*" or c=="×":
    print(calc.multi(a,b))
if c=="/":
    print(calc.div(a,b))