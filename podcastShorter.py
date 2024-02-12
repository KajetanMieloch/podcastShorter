import sys

if len(sys.argv) != 2:
    print("Usage python podcastShorter.py filename.mp4")
    sys.exit(1)

file = sys.argv[1]

try:
    with open(file, 'r') as f:
        zawartosc = f.read()
        print(zawartosc)
except FileNotFoundError:
    print(f"file {file} does not exist.")
    sys.exit(1)
except:
    print("Error occured.")
    sys.exit(1)