import OpenDartReader
import pandas as pd

### 0. 객체 생성 ###
# 객체 생성 (API KEY 지정) 
api_key = 'bb556bda4c3044c4f8c31fc48a1739037787d36d'
dart = OpenDartReader(api_key) 

print(dart.list('삼성전자'))  # 공시 목록
print(dart.company('삼성전자'))  # 개황 정보

# 공시서류 원문 텍스트를 html 파일로 저장하는 코드
xml_text = dart.document('20220816001711')

# if isinstance(xml_text, list):
#     xml_text = "\n".join(xml_text)  # 리스트의 요소들을 줄바꿈으로 연결하여 문자열로 변환
# # txt 파일로 저장
# with open('output.txt', 'w', encoding='utf-8') as file:  # output.txt라는 파일 생성 및 쓰기 모드로 열기
#     file.write(xml_text)  # xml_text 내용을 파일에 쓰기

# XML 텍스트 확인 및 저장
if isinstance(xml_text, str):  # xml_text가 문자열인지 확인
    with open('document_20220816001711.html', 'w', encoding='utf-8') as file:
        file.write(xml_text)  # xml_text 내용을 HTML 파일로 저장
    print("HTML 파일이 성공적으로 저장되었습니다.")
else:
    print("HTML 콘텐츠가 문자열이 아닙니다.")

print(dart.find_corp_code('삼성전자'))


