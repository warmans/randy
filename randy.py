import os
import argparse
import re
import random

# Setup Args
parser = argparse.ArgumentParser(description='Create several random playlists fom a collection of MP3s')
parser.add_argument('target', type=str, nargs=1, help='The base path containing your media files')
parser.add_argument('--outdir', type=str, help='Output to the following path', default='.')
parser.add_argument('--num', type=int, help='Number of playlists to create', default=1)
parser.add_argument('--exclude', type=str, help='Exclude files with a path that matches this regex')

#Parse Args
args = parser.parse_args()

#collect file paths
paths = []
for root, subFolders, files in os.walk(args.target[0]):
    for filename in files:

        filePath = os.path.join(root, filename)
        fileExt = os.path.splitext(filename)[1][1:]

        if fileExt == 'mp3':
            if args.exclude is None or re.search(args.exclude, filePath) is None:
                paths.append({
                    'type': fileExt,
                    'filepath': filePath
                })

for num in range(0, int(args.num)):
    outfileName = os.path.join(args.outdir, "random-{0}.m3u".format(num))
    with open(outfileName, 'w') as outFile:
        random.shuffle(paths)
        for mp3info in paths:
            outFile.write("{0}\n".format(mp3info['filepath']))