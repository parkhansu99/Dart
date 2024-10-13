import OpenDartReader
import dart_fss as dart  # dart-fss에서 dart 모듈 임포트
import pandas as pd

### 0. 객체 생성 ###
# 객체 생성 (API KEY 지정) 
api_key = 'bb556bda4c3044c4f8c31fc48a1739037787d36d'

dart = OpenDartReader(api_key) 

### 7. 여러 가지 확장 기능 ###

# 지정한 날짜의 공시 목록 가져오기
date = '2024-08-14'  # 조회할 날짜 지정
dataframe_1 = dart.list_date_ex(date)  # 공시 목록 가져오기

# CSV 파일로 저장
csv_file_path_1 = 'disclosure_list_2024_08_14.csv'  # 저장할 CSV 파일명 지정
dataframe_1.to_csv(csv_file_path_1, index=False, encoding='utf-8-sig')  # DataFrame을 CSV로 저장

print(f"공시 목록이 '{csv_file_path_1}'로 저장되었습니다.")

# 하위 문서(sub_docs)
rcp_no = '20220308000798' 
dataframe_2 = dart.sub_docs(rcp_no, match='감사의견')  # 하위 문서(제목, url) + 제목이 잘 매치되는 순서로 소트(정렬)
csv_file_path_2 = '하위문서_20220308000798_감사의견.csv'  # 저장할 CSV 파일명 지정
dataframe_2.to_csv(csv_file_path_2, index=False, encoding='utf-8-sig')  # DataFrame을 CSV로 저장

print(f"공시 목록이 '{csv_file_path_2}'로 저장되었습니다.")

# 첨부 문서(attach_docs)

dataframe_3 = dart.attach_docs(rcp_no, match='감사의의견서') # 첨부 문서(i.e. 감사보고서) 제목과 URL
csv_file_path_3 = '첨부문서_20220308000798_감사의의견서.csv'  # 저장할 CSV 파일명 지정
dataframe_3.to_csv(csv_file_path_3, index=False, encoding='utf-8-sig')  # DataFrame을 CSV로 저장

print(f"공시 목록이 '{csv_file_path_3}'로 저장되었습니다.")

# 첨부 파일 제목과 URL
print(dart.attach_files(rcp_no))

# URL을 지정한 파일로 다운로드
url = 'http://dart.fss.or.kr/pdf/download/excel.do?rcp_no=20220308000798&dcm_no=8446647&lang=ko'
fn = '[삼성전자]사업보고서_재무제표(2022.03.08)_ko.xls'
dart.download(url, fn)