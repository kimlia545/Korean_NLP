# 개인정보 마스킹 코드

# 주민번호 # 마지막 4자리 제외 991225-211****
def solution(phone_number):
	return "*"*(len(phone_number)-4)+phone_number[-4:]

# 전화번호  # 뒷번호만 남기기 *********3294
def mask_numer(social_security_number): 
    return social_security_number[:len(social_security_number) - 4] + '****'

# 휴대폰 전화번호 # 010-12**-**78
import re
number = '010-1234-5678'
def phone_number(number): 
    n1 = re.sub('(\d{3})-(\d{2})(\d{2})-(\d{2})(\d{2})', r'\1-\2**-**\5', number) 
    return n1

# 이름 김**
def name_mask(name):
    print('test')
    first_name = name[0]
    last_name = len(name[1:])
    return first_name + "*" * last_name

# 이메일 'test@google.com' # t#####t@google.com
import re 
email = 'test@google.com'
def email_mask(email): 
    lo = email.find('@')
    if lo>0:
        return email[0]+'#####'+email[lo-1:]
    else:
        return 'email address error'

# 이메일 'test@google.com' # t***@******.com
import re 
email_id = 'test@google.com' 
def email_masked(email_id):
    email_split = re.split('[@|.]', email_id)
    username, domain_front, *domain_back_list = email_split
    username_masked = username[0]+'*'*(len(username)-1)
    domain_front_masked = '*'*len(domain_front)
    domain_back = '.'.join(domain_back_list)
    return '{}@{}.{}'.format(username_masked, domain_front_masked, domain_back)

# ip 주소 '172.168.10.12' # 172.168.***.12
import re 
sip = '172.168.10.12'
p1 = re.compile(r"(\d+)[.](\d+)[.](\d+)[.](\d+)") 
def ip_address(sip): 
    m1 = p1.search(sip)
    return m1.group(1) + '.' + m1.group(2) + '.' + '***' + '.' + m1.group(4)
test = ip_address(sip)
#print(test)

# 은행 계좌번호  000*******456 계좌번호 설정(은행 계좌번호 11 ~ 13자리 사이)
account_num = "0001111123456"
def account_mask(account_num):
    mask = len(account_num[3:-3])
    return account_num[0:3] + '*' * mask + account_num[-3:]

# 자동차 등록번호 '02허3391'  # 0*허3**1
import re
car_num = '02허3391' 
def car_mask(car_num):
    c1 = re.sub("([0-9])([가-힣])([\d])([\d]{2})([\d])", r"*\2\3**\5", car_num)
    return c1

# 카드 번호 1234-1234-1234-1234 1234-****-****-1234
import re
def card_mask(card_num):
    cr1 = re.compile(r"(\d{4})-(\d{4})-(\d{4})-(\d{4})")
    result = cr1.search(card_num)
    return result.group(1) + '-****-****-' + result.group(4)

# 카드 유효기간 '34/12' **/**
def card_expired(date_ex):
    return '**' + '/' + '**'

# ID 앞두자리 'test123' te*****
def id_mask(id):
    return id[0:2] + '*' * len(id[2:])

# 운전면허 번호 '11-12-345678-90' 11-**-******-90
def drive_mask(drive_num):
    p = re.compile(r"(\d{2})-(\d{2})-(\d{6})-(\d{2})")
    result = p.search(drive_num)
    return result.group(1) + '-**-******-' + result.group(4)

# 특수문자 제거
import re 
text = '안녕하세요~!!!'
regex_text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', text)

# 주소 숫자만 바꾸기 부산광역시 연제구 연산동 중앙대로 **** *동 ***호
address = '부산광역시 연제구 연산동 중앙대로 1001 1동 101호' 
list = []
def adress_mask(address):
    text = address.split(' ')
    for t in text:
        num = re.findall("[0-9]+", t)
        if num != [] :
            size = len(num[0])
            t = re.sub("[0-9]+",size * "*",t)
        list.append(t+' ')
    return ''.join(list)

# 주소 서울특별시 강남구 신사동 *****
address = '부산광역시 연제구 연산동 중앙대로 1001' #부산광역시 연제구 연산동 *********
p = re.compile(r"[가-힣]+(\d{1,5}|\d{1,5}(,|.)\d{1,5}|)+(읍|면|동|가|리)(^구|)((\d{1,5}(~|-)\d{1,5}|\d{1,5})(가|리|)|)")
def address_masked(address):
    result1 = p.search(address) # 우동
    num = result1.span()
    mask = num[1]
    return address[:mask] + ' ' + len(address[mask+1:]) *  '*'

# 영문 이름 KIM******
def eng_name_mask(name):
    return name[:3] + '*' * len(name[3:])
    
# 생년월일 1999-**-**
def birth_mask(birth):
    p = re.compile(r"(\d{4})-(\d{2})-(\d{2})")
    result = p.search(birth)
    return result.group(1) + '-**-**'


'''
# 주소 정규식 코드
address = '부산광역시 해운대구 우동 APEC로 55'

#"((([가-힣]+(\d{1,5}|\d{1,5}(,|.)\d{1,5}|)+(읍|면|동|가|리))(^구|)((\d{1,5}(~|-)\d{1,5}|\d{1,5})(가|리|)|))([](산(\d{1,5}(~|-)\d{1,5}|\d{1,5}))|)|(([가-힣]|(\d{1,5}(~|-)\d{1,5})|\d{1,5})+(로|길)))"

p = re.compile(r"[가-힣]+(\d{1,5}|\d{1,5}(,|.)\d{1,5}|)+(읍|면|동|가|리)(^구|)")
result2 = p.search(address) # 우동
print('result2',result2)

p = re.compile(r"(|)((\d{1,5}(~|-)\d{1,5}|\d{1,5})(가|리|)|)")
result3 = p.search(address) # ''
print('result3',result3)

p = re.compile(r"(([가-힣]+(시|도))( |)[가-힣]+(시|군|구))")
result4 = p.search(address) # 부산광역시 해운대구
print('result4',result4)

p = re.compile(r"(([가-힣]+(d|d(,|.)d|)+(읍|면|동|가|리))(^구|)((d(~|-)d|d)(가|리|)|))([ ](산(d(~|-)d|d))|)|(([가-힣]|(d(~|-)d)|d)+(로|길))")
result5 = p.search(address) # 부산광역시 해운대구
print('result5',result5)
'''