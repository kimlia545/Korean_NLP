import numpy as np
import re
#from konlpy.tag import Mecab
#from eunjeon import Mecab
from hanspell import spell_checker
from spellchecker import SpellChecker
#import nltk
#from nltk.corpus import stopwords
import pandas as pd

# 한국어만 포함
def only_kor(text_list):
  total_list = []
  for i, text in enumerate(text_list):
    if type(text) == str:
      
      text = re.sub(r'[^ 가-힣]', '', text) # [^ㄱ-ㅎㅏ-ㅣ가-힣 ]
    total_list.append(text)
  return total_list
  
# 불용어 제거  
def remove_stopwords(text_list):
  from konlpy.tag import Mecab
  mecab = Mecab()
  stopwords = ['의','이','있','하','들','그','되','수','보','않','없','나','사람','아','등','같','오','있','한'] #원하는 불용어를 리스트안에 넣으세요
  total_list = []
  for text in text_list:
    if type(text) == str:
      text = [i for i in mecab.nouns(text) if i not in stopwords] # 불용거 제거한 명사만 # 전체에서 제거 # [i for i in text if i not in stop_list]  
    total_list.append(text)
  return total_list

def remove_stoptxt(text_list):
  word_list = open("kr_stop.txt", "r", encoding="utf-8") # 기본적인 불용어 리스트 제거
  stop_list = []
  while True:
    line = f.readline()
    if not line: break
    stop_list.append(line)
  f.close()
  total_list = []
  for text in text_list:
    if type(text) == str:
      text = [i for i in text if i not in stop_list]
      total_list.append(text)
    else:
      total_list.append(text)
  return total_list

# 한글자 제거  
def remove_oneword(word_list):
  total_list = []
  for text in text_list:
    print('text', text, type(text))
    if type(text) == str:
      
      import ast
      text = ast.literal_eval(text)
      text = [x for x in text if len(x)>1] 
    total_list.append(text)
  return total_list


'''
csv_path = 'tiny_test.csv' # csv 파일 경로
df = pd.read_csv(csv_path, encoding='cp949') # utf-8
text_col = df["refine_result"] # text 컬럼명
text_val = text_col.values
text_list = text_val.tolist()
'''

'''
######################### 한글 추출
kr_list = only_kor(text_list) 
df['kr'] = kr_list
df.to_csv(csv_path[:-4]+'_kr.csv', index=False, encoding='utf-8') # 저장할 파일명
'''

'''
######################### 불용어 리스트 제거
remove_words = remove_stopwords(text_list) 
df['filter'] = remove_words
df.to_csv(csv_path[:-4]+'_filter.csv', index=False, encoding='utf-8') # 저장할 파일명
'''

'''
######################### 불용어사전 제거
remove_stoptxt = remove_stopwords(text_list) 
df['filter2'] = remove_stoptxt
df.to_csv(csv_path[:-4]+'_filter2.csv', index=False, encoding='utf-8') # 저장할 파일명
'''
 
'''
######################### 한글자 제거
remove_one = remove_oneword(text_list) # input 행값 ['귤','사과','바나나']
df['filter3'] = remove_one
df.to_csv(csv_path[:-4]+'_filter3.csv', index=False, encoding='utf-8') # 저장할 파일명
'''

'''
######################### 전체
kr_list = only_kor(text_list) # 특수문자, 영어, 숫자 제거
remove_stoptxt = remove_stopwords(kr_list) # 불용어 제거
df['test'] = remove_stoptxt
remove_one = remove_oneword(remove_stoptxt) # 한글자 제거
df['clean'] = remove_one
df.to_csv(csv_path[:-4]+'_clean.csv', index=False, encoding='utf-8') # columns =
'''