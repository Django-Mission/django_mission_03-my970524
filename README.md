# django_mission_03-my970524
## ❗️ 프로젝트 소개
고객센터 관리자 페이지 구성하기<br>
고객센터 앱(support)의 모델을 관리자페이지에 등록 구성

## ✅ Basic ver.
- 자주묻는질문(`Faq`)
   - 목록페이지 출력 필드 : 제목, 카테고리, 최종 수정 일시
   - 검색 필드 : 제목
   - 필터 필드 : 카테고리

![ezgif com-gif-maker (2)](https://user-images.githubusercontent.com/76423946/167328225-6a03362a-8168-4d53-862b-e63b587af6ce.gif)


- 1:1문의(`Inquiry`)
   - 목록페이지 출력 필드 : 질문 제목, 카테고리, 생성 일시, 생성자
   - 검색 필드 : 제목, 이메일, 전화번호
   - 필터 필드 : 카테고리
   - 인라인모델 : 답변(`Answer`)

![ezgif com-gif-maker](https://user-images.githubusercontent.com/76423946/167328350-f17a2ddf-1efa-4931-8194-30b1fcfa377a.gif)

- 답변(`Answer`)
   - 1:1문의 모델에 인라인모델로 추가


![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/76423946/167328511-678a1be5-3412-476a-ae85-6fee2abb5ecb.gif)

<br>
<br>


## ✅ Challenge ver.
- 1:1문의(`Inquiry`) 모델의 “상태” 필드 추가
    - 상태 : 문의 등록, 접수 완료, 답변 완료
- 1:1문의(`Inquiry`) 목록, 필터에 상태 추가
- 1:1문의 검색 필드 추가 : 사용자 모델의 `username`, `phone`, `email`
- 1:1문의 답변 완료 안내 발송 기능 추가
    - 관리자 페이지 체크된 문의 안내 발송
    - 1:1문의의 is_email, is_phone가 True인 경우 email, phone 데이터 `print()` 출력

![ezgif com-gif-maker (3)](https://user-images.githubusercontent.com/76423946/167329514-d7377668-b9a2-445b-a3bd-0ec693e73bca.gif)

