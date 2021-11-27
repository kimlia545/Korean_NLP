import pandas as pd
from summarize_text import sent_token 
from morpheme_analysis import pos_noun, pos_adjective 
from similarity_words import similar_words
  
csv_path = 'tiny_test.csv' # input csv path
df = pd.read_csv(csv_path, encoding='cp949') # utf-8

text_col = df["refine_result"] # text 컬럼명 refine_result
text_val = text_col.values
text_list = text_val.tolist()


'''
count noun  
from collections import Counter
counts = Counter(bucket_list)
print(counts)
'''

'''
######################### 문단 -> 문장 단위 자르기
sents_list = sent_token(text_list) 
df['sent_token'] = sents_list # 저장할 컬럼명
df.to_csv(csv_path[:-4]+'_sent.csv', index=False, encoding='utf-8') # 저장할 파일명
'''

'''
######################### 문장 -> 명사 추출
nouns_list = pos_text(text_list) 
df['noun'] = nouns_list
df.to_csv(csv_path[:-4]+'_noun.csv', index=False, encoding='utf-8') # 저장할 파일명
'''

'''
######################### 문장 -> 형용사 추출
nouns_list = pos_text(text_list) 
df['adjective'] = nouns_list
df.to_csv(csv_path[:-4]+'_adjective.csv', index=False, encoding='utf-8') # 저장할 파일명
'''