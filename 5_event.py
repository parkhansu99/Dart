import OpenDartReader
import dart_fss as dart  # dart-fss에서 dart 모듈 임포트
import pandas as pd

### 0. 객체 생성 ###
# 객체 생성 (API KEY 지정) 
api_key = 'bb556bda4c3044c4f8c31fc48a1739037787d36d'

dart = OpenDartReader(api_key) 

### 5. 주요사항보고서 ###

print(dart.event('052220', '영업정지', '2019')) # iMBC(052220)
print(dart.event('휴림네트웍스', '유상증자')) # 휴림네트웍스(192410)
print(dart.event('미원상사', '무상증자')) # 미원상사(084990)
print(dart.event('헬릭스미스', '유무상증자')) # 헬릭스미스(084990)
print(dart.event('미원상사', '감자')) # 미원상사(084990)
print(dart.event('035720', '해외상장결정', '2017')) # 카카오(035720)
print(dart.event('017810', '전환사채발행')) # 풀무원(017810)
print(dart.event('키다리스튜디오', '신주인수권부사채발행')) #  키다리스튜디오(020120) 
print(dart.event('이스트소프트', '교환사채발행')) # 이스트소프트(047560)