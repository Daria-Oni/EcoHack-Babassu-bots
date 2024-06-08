from unstructured.partition.auto import partition
from unstructured.partition.pdf import partition_pdf
from os import listdir
from os.path import isfile, join

files = [f for f in listdir("test_set/pdfs") if isfile(join("test_set/pdfs", f))]
print(files)
filepath = "test_set/pdfs/"
filepath_out="test_set/txts/"
for f in files:
    #elements = partition(filepath+f)
    elements = partition_pdf(filepath+f, strategy="hi_res")
    #print(elements)
    txt = "\n\n".join([str(el) for el in elements])
    f = open(filepath_out+f[:-4]+"_1.txt", "w")
    f.write(txt)
    f.close()