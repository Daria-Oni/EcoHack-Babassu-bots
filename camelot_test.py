import camelot

name ="braga17"
tables = camelot.read_pdf('test_set/pdfs/'+name+'.pdf', pages='all', flavor='stream')


#tables.export(name+'.csv', f='csv', compress=True) # json, excel, html, markdown, sqlite
print(tables[0])
tables[0].parsing_report

#tables[0].to_csv('foo.csv') # to_json, to_excel, to_html, to_markdown, to_sqlite

tables[0].df # get a pandas DataFrame!