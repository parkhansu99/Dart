import OpenDartReader
import dart_fss as dart  # dart-fss에서 dart 모듈 임포트
import pandas as pd

### 0. 객체 생성 ###
# 객체 생성 (API KEY 지정) 
api_key = 'bb556bda4c3044c4f8c31fc48a1739037787d36d'

dart = OpenDartReader(api_key) 

### 4. 지분공시(Shareholding disclosure) ###
# 대량보유 상황보고 (종목코드, 종목명, 고유번호 모두 지정 가능)
print(dart.major_shareholders('삼성전자'))

# 임원ㆍ주요주주 소유보고 (종목코드, 종목명, 고유번호 모두 지정 가능)
print(dart.major_shareholders_exec('삼성전자'))

