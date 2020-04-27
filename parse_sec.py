import os
from bs4 import BeautifulSoup

f = open('companies.txt', 'r')
stickers = f.read().splitlines()
f.close()


for sticker in stickers: 
  path = "sec_edgar_filings/"+sticker+"/10-K"
  files = os.listdir(path)
  for report in files:
    print("LOL "+ report)
    if not report.startswith("."):
  
      report_path = path+"/"+report
      annual_report = open(report_path,"r").read()
      soup = BeautifulSoup(annual_report, 'html.parser')
      print(soup.children)
      for i in soup.children:
         if i.name == 'sec-document': 
          doc = i.document
          for c in doc.children:
            for l in c: 
              if(type(l) == str):
                print(len(l))
              else: 
                #soup1 = BeautifulSoup(l, 'html.parser') 
                print(children)         
                
      gross_profit = soup.find("DOCUMENT")
      print(gross_profit)

  break
