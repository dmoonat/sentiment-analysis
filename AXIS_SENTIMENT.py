import csv
from textblob import TextBlob
import xlrd

workbook = xlrd.open_workbook('axis_bank.xlsx', encoding_override='utf-8')
sheet=workbook.sheet_by_index(0)
    
with open('axis_sentiment.csv','a',newline='',encoding='utf-8') as f:
    writer=csv.DictWriter(f,fieldnames=['Date','Tweet','Sentiment'])
    writer.writeheader()
    for i in range(3,sheet.nrows):
        
        date=sheet.row_values(i)[0]
        tweet=sheet.row_values(i)[1]
        
        analysis=TextBlob(tweet)
        sentiment=analysis.sentiment.polarity
        if sentiment>0:
            polarity=1
        elif sentiment<0:
            polarity=-1
        else:
            polarity=0
        writer.writerow({'Date':date,'Tweet':tweet,'Sentiment':polarity})
    
    
