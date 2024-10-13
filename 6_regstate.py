import OpenDartReader
import dart_fss as dart  # dart-fss에서 dart 모듈 임포트
import pandas as pd

### 0. 객체 생성 ###
# 객체 생성 (API KEY 지정) 
api_key = 'bb556bda4c3044c4f8c31fc48a1739037787d36d'

dart = OpenDartReader(api_key) 

### 6. 증권 신고서 ###

print(dart.regstate('하림지주', '주식의포괄적교환이전'))
print(dart.regstate('사조대림', '합병'))
print(dart.regstate('에스앤케이', '증권예탁증권'))
print(dart.regstate('BNK금융지주', '채무증권'))
print(dart.regstate('금호전기', '지분증권'))
print(dart.regstate('케이씨씨', '분할'))