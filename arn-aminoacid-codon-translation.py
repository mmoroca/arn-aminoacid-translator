# ARN Aminoacid translator by @mmoroca (2020)
import sys
import os

aminoacids_1_1 = [
"A", "GCN",
"R", "CGN",
"N", "AAY",
"D", "GAY",
"B", "RAY",
"C", "UGY",
"Q", "CAR",
"E", "GAR",
"Z", "SAR",
"G", "GGN",
"H", "CAY",
"I", "AUH",
"L", "CUN",
"K", "AAR",
"M", "AUG",
"F", "UUY",
"P", "CCN",
"S", "UCN",
"T", "ACN",
"W", "UGG",
"Y", "UAY",
"V", "GUN"
]

aminoacids_1_2 = [
"A", "GCN",
"R", "AGR",
"N", "AAY",
"D", "GAY",
"B", "RAY",
"C", "UGY",
"Q", "CAR",
"E", "GAR",
"Z", "SAR",
"G", "GGN",
"H", "CAY",
"I", "AUH",
"L", "UUR",
"K", "AAR",
"M", "AUG",
"F", "UUY",
"P", "CCN",
"S", "AGY",
"T", "ACN",
"W", "UGG",
"Y", "UAY",
"V", "GUN"
]

def tradARN(line, var):
    for letter in line:
        if var == "1":
            print(aminoacids_1_1[aminoacids_1_1.index(letter)+1], end=" ")
        else:
            print(aminoacids_1_2[aminoacids_1_2.index(letter)+1], end=" ")
    print()

if len(sys.argv) > 1:
    if os.path.isfile(sys.argv[1]):
        if len(sys.argv) > 2:
            variation = sys.argv[2]
        else:
            variation = "1"
        f = open(sys.argv[1], "r")
        line = f.readline()
        print("locus: " + line[5:].lstrip(), end="")
        while line:
            begingene = line.find("gene")
            if begingene!= -1:
                gene = line[begingene+6:-2]
                #print("gen: " + gene)
            begintranslation = line.find("translation")
            if begintranslation != -1:
                templine = ""
                line = line[begintranslation+13:]
                endtranslation = line.find("\"")
                #if endtranslation != -1:
                #    line = line[:endtranslation]
                #    templine = templine + line.strip()
                while endtranslation == -1:
                    templine = templine + line.strip()
                    line = f.readline()
                    endtranslation = line.find("\"")
                line = line[:endtranslation]
                templine = templine + line.strip()
                print("gene: " + gene)
                tradARN(templine, variation)
            line = f.readline()
        f.close()
    else:
        print(sys.argv[0])
        print("Translate ARN amino acid to standard genetic code compressed using IUPAC notation (cc @mmoroca 2020)")
        print("Usage: " + sys.argv[0] + " filename variation (file in genbank format, IUPAC notation variation 1 or 2)")
else:
    print(sys.argv[0])
    print("Translate ARN amino acid to standard genetic code compressed using IUPAC notation (cc @mmoroca 2020)")
    print("Usage: " + sys.argv[0] + " filename variation (file in genbank format, IUPAC notation variation 1 or 2)")
