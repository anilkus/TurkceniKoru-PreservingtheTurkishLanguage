import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Excel dosyasını oku
df = pd.read_excel("filePath")  # Excel dosyasının adını ve yolunu belirtin

# Excel cells
cumle1 = df.iloc[8, 2]  # 9. satır, 2. sütun (0'dan başlayan indeksleme)
cumle2 = df.iloc[8, 3]  # 9. satır, 3. sütun (0'dan başlayan indeksleme)

# TfidfVectorizer 
vectorizer = TfidfVectorizer()
vectorizer.fit([cumle1, cumle2])
cumle1_vector = vectorizer.transform([cumle1])
cumle2_vector = vectorizer.transform([cumle2])

# Cosine Similarity calculation
cos_sim = cosine_similarity(cumle1_vector, cumle2_vector)

# Result
print("Cosine Similarity:", cos_sim[0][0])


#Save in Excel
'''
from openpyxl import load_workbook
wb = load_workbook('FilePath')
ws = wb['Sheet1']


ws.cell(row=3,column=6).value = cos_sim[0][0]



wb.save('FilePath')

'''
