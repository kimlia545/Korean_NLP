import numpy as np
import konlpy

def pos_noun(text_list):
  total_list = []
  for i, text in enumerate(text_list):
      okt = konlpy.tag.Okt()
      clean_words = []
      if type(text) == str:
          for word in okt.pos(text, stem=True): 
                  #print(word)
                  if word[1] in ['Noun'] : # 'Verb' # 필요한 형태소 입력
                      clean_words.append(word[0])     
      else:
          pass
      total_list.append(clean_words)
  return total_list

def pos_adjective(text_list):
  total_list = []
  for i, text in enumerate(text_list):
      okt = konlpy.tag.Okt()
      clean_words = []
      if type(text) == str:
          for word in okt.pos(text, stem=True): 
                  #print(word)
                  if word[1] in ['Adjective'] :
                      clean_words.append(word[0])     
      else:
          pass
      total_list.append(clean_words)
  return total_list