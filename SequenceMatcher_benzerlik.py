import pandas as pd
from difflib import SequenceMatcher

def benzerlik_olcumu(cumle1, cumle2):
    benzerlik_orani = SequenceMatcher(None, cumle1, cumle2).ratio()
    return benzerlik_orani

# reading excel
df = pd.read_excel("Path")  # Excel dosyasının adını ve yolunu belirtin

# Excel Cells
cumle1 = df.iloc[1, 2]  # 9. satır, 2. sütun (0'dan başlayan indeksleme)
cumle2 = df.iloc[1, 3]  # 9. satır, 3. sütun (0'dan başlayan indeksleme)

# Similarity Calculation
benzerlik_orani = benzerlik_olcumu(str(cumle1), str(cumle2))

# Result
print("İki cümlenin benzerlik oranı:", benzerlik_orani)

print(cumle1)
print(cumle2)

#Saving..
'''
from openpyxl import load_workbook
wb = load_workbook('Path')
ws = wb['Sheet1']


ws.cell(row=3,column=5).value = benzerlik_orani



wb.save('Path')

'''
