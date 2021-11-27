
# -*- coding: cp949 -*-
from nltk.tokenize import sent_tokenize # 문장 분할

def sent_token(text_list):  
  result = []
  for text in text_list:
    if type(text) == str:
      sents = sent_tokenize(text)
      result.append(sents)
      print(sents)
    else:
      result.append(text) # nan
  return result
  