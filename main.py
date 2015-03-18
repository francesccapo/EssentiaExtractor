import essentiaExtractor as ee
import pdb


INPUT_PATH = ['/Users/Xesc/Desktop/DATASET_LAB5/Happy/', '/Users/Xesc/Desktop/DATASET_LAB5/Sad/',
        '/Users/Xesc/Desktop/DATASET_LAB5/Aggressive/', '/Users/Xesc/Desktop/DATASET_LAB5/Non-Aggressive/']
OUTPUT_PATH_FILE = ['/Users/Xesc/Desktop/HappyRes.csv', '/Users/Xesc/Desktop/SadRes.csv',
            '/Users/Xesc/Desktop/AggressiveRes.csv', '/Users/Xesc/Desktop/Non-AggresiveRes.csv']

FEATURES = [
            ('danceability', 'Danceability'),
            ('rhythm2013','bpm'),
            ('beatsLoudness', 'LoudnessBandRatio_average (20-150)','LoudnessBandRatio_average (150-400)','LoudnessBandRatio_average (400-3200)','LoudnessBandRatio_average (3200-7000)','LoudnessBandRatio_average (7000-22000)'), #Dependencies: rhythm2013
            #('rms','rms'),
            #('bpmhistogramdescriptors','firstPeakBmp','firstPeakWeight','firstPeakSpread','secondPeakBmp','secondPeakWeight','secondPeakSpread',)
            #('rythmdescriptors','beats_position','bpm','bpm_estimates','bpm_intervals','firstPeakBmp','firstPeakSpread','firstPeakWeight','secondPeakBmp','secondPeakSpread','secondPeakWeight')
            #('dynamiccomplexity','dynamiccomplexity','loudness')
            ]

for folder in range(len(INPUT_PATH)):
    files = ee.filterroot(INPUT_PATH[folder])
    body = []
    for file in range(len(files)):
        print 'Extracting features from ' + files[file]
        audiovector = ee.audioLoader(files[file])
        res = [files[file]]
        for feat in range(FEATURES.__len__()):
            callfunc = getattr(ee, FEATURES[feat][0])
            resfeat = ''
            resfeat = callfunc(audiovector)

            if type(resfeat) is float:
                res.append(resfeat)
            else:
                for numres in range(len(resfeat)):
                    res.append(resfeat[numres])

        body.append(res)
        if file == 4:
            break
    header = ['File name']
    for feat in range(len(FEATURES)):
        for headitem in range(len(FEATURES[feat])-1):
            header.append(FEATURES[feat][headitem+1])
    ee.writeRes(OUTPUT_PATH_FILE[folder], header, body)
