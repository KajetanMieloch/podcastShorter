import sys
import cv2

if len(sys.argv) != 2:
    print("Usage python podcastShorter.py filename.mp4")
    sys.exit(1)

file = sys.argv[1]

try:
    video = cv2.VideoCapture(file)
    # Save the video
    fps = video.get(cv2.CAP_PROP_FPS)
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWriter('output.avi', fourcc, fps, (width, height))
except FileNotFoundError:
    print(f"file {file} does not exist.")
    sys.exit(1)
except:
    print("Error occurred.")
    sys.exit(1)

while True:
    ret, frame = video.read()
    if not ret:
        break
    out.write(frame)

video.release()
out.release()
