class NotThreeMultipleError(Exception):
    def __init__(self):
        super().__init__('3의 배수가 아닙니다.')

def ThreeMultiple():
    try:
        x = int(input('3의 배수를 입력하세요 : '))
        if x % 3 != 0:
            raise NotThreeMultipleError
        print(x)
    except Exception as e:
        print('예외가 발생하였습니다',e)

ThreeMultiple()
