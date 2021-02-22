class Date:
    @staticmethod
    def is_date_valid(strdate):
        year, month, day = map(int,strdate.split('-'))
        return month <= 12 and day <= 31

if Date.is_date_valid('2002-10-3'):
    print('올바른 날짜 형식입니다')
else:
    print('잘못된 날짜 형식입니다')

