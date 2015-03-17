import essentia
import essentia.standard
import os
import csv
import pdb


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


