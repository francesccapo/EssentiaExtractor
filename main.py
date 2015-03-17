import essentiaExtractor as ee


INPUT_PATH = ['/Users/Xesc/Desktop/DATASET_LAB5/Happy/', '/Users/Xesc/Desktop/DATASET_LAB5/Sad/',
        '/Users/Xesc/Desktop/DATASET_LAB5/Aggressive/', '/Users/Xesc/Desktop/DATASET_LAB5/Non-Aggressive/']
OUTPUT_PATH_FILE = ['/Users/Xesc/Desktop/HappyRes.csv', '/Users/Xesc/Desktop/SadRes.csv',
            '/Users/Xesc/Desktop/AggressiveRes.csv', '/Users/Xesc/Desktop/Non-AggresiveRes.csv']

HEADER = ('File Name', 'Danceability (0-3)')

FEATURES = [[]]



for folder in range(len(INPUT_PATH)):
    files = ee.filterroot(INPUT_PATH[folder])
    body = []
    for file in range(len(files)):
        audiovector = ee.audioLoader(files[file])
        danc = ee.danceable(audiovector)
        body.append((str(files[file]), str(danc)))
    ee.writeRes(OUTPUT_PATH_FILE[folder], HEADER,body)
