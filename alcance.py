value = 114

def func_1(pf1):
    def func_2(pf2):
        testValue = 99
        newV = pf2 + 10
        print(f'inside func2: {newV}:{value}')
    func_2(pf1)
    # print(f'Test value: {testValue}')


func_1(value)