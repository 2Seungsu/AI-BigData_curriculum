'''

    경고
    이 소스코드는 오직 빅데이터 4기의 데이터 분석 및
    인터넷 파싱 연습을 위한 용도 및 과제 용도로,

    외부 서비스에 대한 디컴파일,
    리버싱, 분해, 작업 등을 의미하지 않습니다.

    즉 단순 공개된 자료에 대한 분석일 뿐
    기타 목적으로 외부에 배포하거나 공개 용도로 작성되지 아니합니다.

    따라서 본 소스코드는 다른 서비스사의
    서비스를 방해할 목적이 전혀 아니며 개인 공부 용도로 사용됨을 명시합니다.

    본 소스코드는 있는 그대로(ASIS) 업로드되며,
    이용 및 참고에 대한
    발생할 수 있는 그 모든 문제에 대해서
    소스코드 작성자는 책임지지 아니합니다.

'''

import time
class Logger:
    def __init__(self, logFile):
        self.__logFile = logFile

    def write(self,type,msg):
        file = open(self.__logFile,"a",encoding="UTF-8")
        file.write("[" + str(time.time()) + "] "  + f"<{type}> " + msg + "\n")
        file.flush()
        file.close()

    def info(self,msg):
        self.write("INFO",msg)

    def warn(self,msg):
        self.write("WARN",msg)

    def error(self,msg):
        self.write("ERR",msg)
