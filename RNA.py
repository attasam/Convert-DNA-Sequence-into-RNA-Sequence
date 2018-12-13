"""
Created on Mon Oct 31 16:22:20 2016

@author: attasam
"""

if __name__=="__main__":

    myfile= open("Input.txt", "r")
    data=myfile.readlines()

    map = {"UUU":"Phenylalanine", "UUC":"Phenylalanine", "UUA":"Leucine", "UUG":"Leucine",
           "UCU":"Serine", "UCC":"Serine", "UCA":"Serine", "UCG":"Serine",
           "UAU":"Tyrosine", "UAC":"Tyrosine", "UAA":"STOP", "UAG":"STOP",
           "UGU":"Cysteine", "UGC":"Cysteine", "UGA":"STOP", "UGG":"Tryptophan",
           "CUU":"Leucine", "CUC":"Leucine", "CUA":"Leucine", "CUG":"Leucine",
           "CCU":"Proline", "CCC":"Proline", "CCA":"Proline", "CCG":"Proline",
           "CAU":"Histidine", "CAC":"Histidine", "CAA":"Glutamine", "CAG":"Glutamine",
           "CGU":"Arginine", "CGC":"Arginine", "CGA":"Arginine", "CGG":"Arginine",
           "AUU":"Isoleucine", "AUC":"Isoleucine", "AUA":"Isoleucine", "AUG":"Methionine",
           "ACU":"Threonine", "ACC":"Threonine", "ACA":"Threonine", "ACG":"Threonine",
           "AAU":"Asparagine", "AAC":"Asparagine", "AAA":"Lysine", "AAG":"Lysine",
           "AGU":"Serine", "AGC":"Serine", "AGA":"Arginine", "AGG":"Arginine",
           "GUU":"Valine", "GUC":"Valine", "GUA":"Valine", "GUG":"Valine",
           "GCU":"Alanine", "GCC":"Alanine", "GCA":"Alanine", "GCG":"Alanine",
           "GAU":"Aspartate", "GAC":"Aspartate", "GAA":"Glutamate", "GAG":"Glutamate",
           "GGU":"Glycine", "GGC":"Glycine", "GGA":"Glycine", "GGG":"Glycine",}

    

    positions = []
    infile = open('exon.txt', 'r')
    line=infile.readlines()
    for i in line:
        a = i.split(",")
        start=a[0]
        end=a[1]
        
        positions.append((start, end))
    infile.close()
    





    

for i in range(0,len(data)):
    
    DNA=data[i].replace('T','U') 
    RNA=DNA.strip()
    start = RNA.find('AUG')
    if start!= -1:
        while start+2 < len(RNA):
            codon = RNA[start:start+3]
            if codon == "UAG" or codon == "UAA" or codon == "UGA":
                print("*************************************\nSTOP\n*************************************")
                break;
            elif codon =='AUG':
                print("-------------------------------------\nNo STOP mRNA Sequence Found\n-------------------------------------")
            print(map[codon])
            start+=3
            
