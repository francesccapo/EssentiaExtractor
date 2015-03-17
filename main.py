import essentiaExtractor as ee
import pdb


INPUT_PATH = ['/Users/Xesc/Desktop/DATASET_LAB5/Happy/', '/Users/Xesc/Desktop/DATASET_LAB5/Sad/',
        '/Users/Xesc/Desktop/DATASET_LAB5/Aggressive/', '/Users/Xesc/Desktop/DATASET_LAB5/Non-Aggressive/']
OUTPUT_PATH_FILE = ['/Users/Xesc/Desktop/HappyRes.csv', '/Users/Xesc/Desktop/SadRes.csv',
            '/Users/Xesc/Desktop/AggressiveRes.csv', '/Users/Xesc/Desktop/Non-AggresiveRes.csv']

FEATURES = [
            ('danceability', 'Danceability'),
            ('beatsLoudness', 'Loudness', 'LoudnessBandRatio'),
            ]

for folder in range(len(INPUT_PATH)):
    files = ee.filterroot(INPUT_PATH[folder])
    body = []
    for file in range(len(files)):
        audiovector = ee.audioLoader(files[file])
        res = [files[file]]
        for feat in range(FEATURES.__len__()):
            callfunc = getattr(ee, FEATURES[feat][0])
            resfeat = ''
            pdb.set_trace()
            resfeat = callfunc(audiovector)

            if type(resfeat) is float:
                res.append(resfeat)
            else:
                for numres in range(len(resfeat)):
                    res.append(resfeat[numres])
        body.append(res)
    header = ['File name']
    pdb.set_trace()
    for feat in range(FEATURES.__len__()):
        for headitem in range(len(1,stop=FEATURES[feat])):
            header.append(FEATURES[feat][headitem])
    ee.writeRes(OUTPUT_PATH_FILE[folder], header, body)
