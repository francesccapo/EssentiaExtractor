import essentia
import essentia.standard
import os
import csv
import numpy as np
import pdb



ticks = []

def filterroot(mainroot):
    res = []
    for root, dirs, files in os.walk(mainroot):
        for name in files:
            if name[0] != '.':
                res.append(os.path.join(root, name))
    return res


def audioLoader(file):
    inst = essentia.standard.MonoLoader(filename=file)
    res = inst()
    return res


def danceability(audioVec):
    inst = essentia.standard.Danceability()
    danc = inst(audioVec)
    return danc


def rhythm2013(audioVec):
    global ticks
    inst = essentia.standard.RhythmExtractor2013()
    bpm,ticks,_,_,_ = inst(audioVec)
    return bpm


def beatsLoudness(audioVec):
    global ticks
    inst = essentia.standard.BeatsLoudness(beats=ticks)
    _,loudnessBandRatio = inst(audioVec)
    loudnessBandRatio = np.array(loudnessBandRatio)
    average_loudnessBandRatio = np.mean(loudnessBandRatio,0)
    return average_loudnessBandRatio

#def rythm

def writeRes(outfile_name, header, body):
    outfile = open(outfile_name,'wb')
    wr = csv.writer(outfile)
    wr.writerow(header)
    wr.writerows(body)
    outfile.close()

    print 'Writing file finished'


