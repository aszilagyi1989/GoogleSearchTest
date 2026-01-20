from pypdf import PdfReader
import re

# open the pdf file
reader = PdfReader("mol csoport integrált éves jelentés 2024.pdf")

# get number of pages
num_pages = len(reader.pages)
print(num_pages)

# define key terms
string = "EREDMÉNYKIMUTATÁS" # nettó árbevétel # mérlegfőösszeg és az alkalmazottak száma
side = 0
# extract text and do the search
for page in reader.pages:
    text = page.extract_text() 
    res_search = re.search(string, text)
    side += 1
    if res_search != None:
      print(f"\n{side}. oldal:\n")
      print(text)
      # print(res_search)
      # break
