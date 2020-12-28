import requests
from bs4 import BeautifulSoup

CATEGORY_NO = {
    '전자제품': '213', '우주항공과국방': '216', '복합유틸리티': '193', '디스플레이장비및부품': '199', '자동차': '44', '사무용전자제품': '231', '도로와철도운송': '220', 
    '상업서비스와공급품': '208', '디스플레이패널': '222', '복합기업': '191', '전문소매': '167', '가스유틸리티': '168', '반도체와반도체장비': '202', '해운사': '212', 
    '음료': '145', '전자장비와기기': '197', '철강': '62', '핸드셋': '207', '운송인프라': '189', '전기유틸리티': '176', '은행': '20', '광고': '177', '담배': '182', 
    '기타': '25', '레저용장비와제품': '219', '게임엔터테인먼트': '235', '자동차부품': '36', '기타금융': '183', '가정용기기와용품': '214', '손해보험': '190', '방송과엔터테인먼트': '204', 
    '에너지장비및서비스': '205', '화장품': '206', '통신장비': '136', '건축제품': '171', '식품': '38', '교육서비스': '201', '비철금속': '53', '무선통신서비스': '184', 
    '다각화된통신서비스': '228', '양방향미디어와서비스': '236', '판매업체': '164', 'IT서비스': '154', '가정용품': '174', '증권': '12', '무역회사와판매업체': '226', '건축자재': '162', 
    '화학': '140', '부동산': '229', '가구': '200', '항공화물운송과물류': '234', '백화점과일반상점': '198', '카드': '185', '소프트웨어': '33', '전기제품': '221', '호텔,레스토랑,레저': '161', 
    '석유와가스': '217', '조선': '215', '기계': '138', '섬유,의류,신발,호화품': '134', '인터넷과카탈로그소매': '210', '생명보험': '192', '생물공학': '146', '포장재': '173', 
    '식품과기본식료품소매': '227', '창업투자': '109', '종이와목재': '196', '컴퓨터와주변기기': '203', '건강관리장비와용품': '211', '건설': '42', '항공사': '187', '제약': '35', 
    '전기장비': '144', '문구류': '230', '건강관리 기술': '194', '출판': '166', '건강관리업체및서비스': '233', '생명과학도구및서비스': '218', '독립전력생산및에너지거래': '232'}

URL = "https://finance.naver.com/sise/sise_group.nhn?type=upjong"
res = requests.get(URL)

res.raise_for_status() # If there is any problem on state, quit immediately

soup = BeautifulSoup(res.text, 'html.parser')
# lxml parser와 html.parser를 사용하는 것의 차이점에 대해서 알아보자
# html.parser has decent speed, Lenient(=Generous), and Batteries included
# lxml parer is very fast and lenient but dependency on External C
# html5lib is extremely lenient, and parses pages the same way a web browser does, creates valid HTML5 but very slow and External Python dependency

# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soup 객체에서 처음 발견되는 a element 출력
# print(soup.a.attrs) # a element의 속성 정보를 출력
# print(soup.a["href"]) # a element의 href 속성 값 정보를 출력
# print(soup.find("a", attrs={"class":"Nbtn_upload"}))

TD = soup.find_all("td", attrs={"style":"padding-left:10px;"})
# TD변수의 구조
# <td style="padding-left:10px;"><a href="/sise/sise_group_detail.nhn?type=upjong&amp;no=213">전자제품</a></td>

sept = "/sise/sise_group_detail.nhn?type=upjong&no="

NO = []
C = []

for e in TD:
    C.append(e.get_text())
    dummy, number = e.a["href"].split("/sise/sise_group_detail.nhn?type=upjong&no=")
    NO.append(number)

FINAL = dict(zip(C, NO))

print(FINAL)