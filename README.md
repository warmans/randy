Some versions of the Audi MMI don't let you play all files on an SD card randomly i.e. shuffle. This script just
generates as many random playlists as you want to simulate the shuffle feature.

    usage: randy.py [-h] [--outdir OUTDIR] [--num NUM] [--exclude EXCLUDE] target

    Create several random playlists fom a collection of MP3s

    positional arguments:
      target             The base path containing your media files

    optional arguments:
      -h, --help         show this help message and exit
      --outdir OUTDIR    Output to the following path
      --num NUM          Number of playlists to create
      --exclude EXCLUDE  Exclude files with a path that matches this regex