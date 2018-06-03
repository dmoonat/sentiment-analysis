import csv

in_filenames=['042017-062017.csv','072017-092017.csv','102017-122017.csv - 102017-122017.csv','012018-042018.csv - 012018-042018.csv']

out_file='axis_bank.csv'
output_file=open(out_file,'a',newline='',encoding="utf8")
writer=csv.DictWriter(output_file,fieldnames=['Date','Tweet'])
writer.writeheader()

for file1 in in_filenames:
    input_file=open(file1,'r',encoding="utf8",errors='ignore')
    readlines=input_file.readlines()
    #writer=csv.DictWriter(output_file,fieldnames=['Date','Tweet'])
    #writer.writeheader()

    tweets=[line.split(";") for line in readlines]
    xs=[Type[1] for Type in tweets]
    ys=[Type[4] for Type in tweets]
    for x,y in zip(xs,ys):
        writer.writerow({'Date':x,'Tweet':y})
        
    input_file.close()

output_file.close()
