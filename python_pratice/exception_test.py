# 사용자 정의 예외 - 클래스
# 1. Exception을 상속받는 사용자정의 예외클래스 정의
# 2. 함수 예외상황이 발생했을 때 raise 이용 강제로 예외 발생
# 3. 호출하는 쪽에서 처리
# try :
#   사용자 정의 예외 발생하는 함수 호출
# except    사용자 정의 예외 클래스 타입 :
#   예외처리 실행문
# finally :
#   무조건 실행되는 실행문

class UserException(Exception) :
    # def __init__(self) :
    #     Exception.__init__(self)

# raise UserException

    def __init__(self, message) :
        super().__init__(message)

raise UserException("사용자 정의 오류 발생")