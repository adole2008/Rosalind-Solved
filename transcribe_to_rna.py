
f = open("data.txt", "r")
translated_rna = ""
for i in f.read():
    if i != "T":
        translated_rna += i
    else:
        translated_rna += "U"
print(translated_rna)
