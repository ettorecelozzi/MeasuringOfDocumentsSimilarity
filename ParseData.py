from PdfMining import rename_pdf
from PdfMining import tokenizePdf
from Shingling import generateShingles
from StringHashing import generateHash
import os


def parsedata(pdfdir, txtdir, matrix, startcount, m, doTokenShingle=False):
    dirpath = './' + pdfdir + '/'
    txtpath = './' + txtdir + '/'
    rename_pdf(dirpath, startcount)
    numFiles = len([f for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, f))])  # minHash()
    if doTokenShingle is True:
        print("Shingles generation" + pdfdir + " started")
        for i in range(startcount, startcount + numFiles):
            tokenizePdf("Doc" + str(i), txtpath, dirpath)
            generateShingles("Doc" + str(i), txtpath)
        print("Shingles generation" + pdfdir + " ended")
    print("Matrix of hashes creation " + pdfdir + " started")
    for i in range(startcount, startcount + numFiles):
        generateHash("Doc" + str(i), txtpath, m, matrix, i)
    print("Matrix of hashes creation " + pdfdir + " ended")
    print(" ")
    return numFiles
