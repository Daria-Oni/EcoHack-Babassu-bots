from tabula import read_pdf
from tabulate import tabulate

#reads table from pdf file
df = read_pdf("test_set/pdfs/braga17.pdf",pages="all") #address of pdf file
print(df)
print(tabulate(df))
