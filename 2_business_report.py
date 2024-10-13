import OpenDartReader
import dart_fss as dart  # dart-fss에서 dart 모듈 임포트
import pandas as pd

### 0. 객체 생성 ###
# 객체 생성 (API KEY 지정) 
api_key = 'bb556bda4c3044c4f8c31fc48a1739037787d36d'

dart = OpenDartReader(api_key)

### 2. 사업보고서 ###

print(dart.report('삼성전자', '미등기임원보수', 2021))  # 미등기임원 보수현황
print(dart.report('삼성전자', '증자', 2021)) # 증자(감자) 현황
print(dart.report('삼성전자', '배당', 2018))  # 배당에 관한 사항