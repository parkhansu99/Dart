import OpenDartReader
import dart_fss as dart  # dart-fss에서 dart 모듈 임포트
import pandas as pd

### 0. 객체 생성 ###
# 객체 생성 (API KEY 지정) 
api_key = 'bb556bda4c3044c4f8c31fc48a1739037787d36d'

dart = OpenDartReader(api_key) 

### 3. 재무 정보 ###

# 기업 목록과 연도 지정
companies = '삼성전자, SK하이닉스, 현대자동차'  # 삼성전자, SK하이닉스, 현대자동차의 고유 코드
year = 2021

financial_data = dart.finstate(companies, year)  # 재무 상태 가져오기
    
# HTML 파일로 저장
html_content = financial_data.to_html(index=False)  # DataFrame을 HTML로 변환
html_file_path = 'financial_report.html'  # 저장할 파일명 지정
with open(html_file_path, 'w', encoding='utf-8') as f:
    f.write(html_content)  # HTML 내용을 파일에 쓰기

print(f"재무 상태가 '{html_file_path}'로 저장되었습니다.")

dart.finstate_xml('20220308000798', save_as='삼성전자_2021_사업보고서_XBRL.zip')
