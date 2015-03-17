import essentia
import essentia.standard
import os
import csv
import operator
import pdb

PATH = ['/Users/Xesc/Desktop/DATASET_LAB5/Happy/', '/Users/Xesc/Desktop/DATASET_LAB5/Sad/',
        '/Users/Xesc/Desktop/DATASET_LAB5/Aggressive/', '/Users/Xesc/Desktop/DATASET_LAB5/Non-Aggressive/']
OUTPUT_FILE = ['/Users/Xesc/Desktop/HappyRes.csv', '/Users/Xesc/Desktop/SadRes.csv',
            '/Users/Xesc/Desktop/AggressiveRes.csv', '/Users/Xesc/Desktop/Non-AggresiveRes.csv']
HEADER = ('File Name', 'Danceability (0-3)')



def filterroot(mainroot):
    res = []
    for root, dirs, files in os.walk(mainroot):
        for name in files:
            if name[0] != '.':
                res.append(os.path.join(root, name))
    return res


def audioLoader(file):
    inst = essentia.standard.MonoLoader(filename = file)
    res = inst()
    return res


def danceable(audioVec):
    inst = essentia.standard.Danceability()
    danc = inst(audioVec)
    return danc


def writeRes(outfile_name, header, body):
    outfile = open(outfile_name,'wb')
    wr = csv.writer(outfile)
    wr.writerow(header)
    wr.writerows(body)
    outfile.close()

    print 'Process finished'

for i in range(len(PATH)):
    files = filterroot(PATH[i])
    body = []
    for file in range(len(files)):
        audiovector = audioLoader(files[file])
        danc = danceable(audiovector)
        body.append((str(files[file]),str(danc)))
    body = sorted(body, key=operator.itemgetter(1), reverse=True)
    writeRes(OUTPUT_FILE[i], HEADER,body)