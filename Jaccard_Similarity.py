import pandas as pd
from sklearn.metrics import jaccard_score
from sklearn.feature_extraction.text import CountVectorizer

# read the excel file
df = pd.read_excel("ExcelPath")  # Excel dosyasının adını ve yolunu belirtin

# Excel Cells
cumle1 = df.iloc[7, 2]  # 9. satır, 2. sütun (0'dan başlayan indeksleme)
cumle2 = df.iloc[7, 3]  # 9. satır, 3. sütun (0'dan başlayan indeksleme)

# Sentences
vectorizer = CountVectorizer(binary=True)
vectorizer.fit([cumle1, cumle2])
cumle1_vector = vectorizer.transform([cumle1])
cumle2_vector = vectorizer.transform([cumle2])

# Jaccard Similarity calculation
jaccard_sim = jaccard_score(cumle1_vector.toarray()[0], cumle2_vector.toarray()[0])

# Result
print("Jaccard Similarity:", jaccard_sim)

#Saving in Excel
'''
from openpyxl import load_workbook
wb = load_workbook('FilePath')
ws = wb['Sheet1']


ws.cell(row=3,column=7).value = jaccard_sim



wb.save('FilePath')

'''
