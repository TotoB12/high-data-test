import cv2
import numpy as np

# Define the codec using VideoWriter_fourcc and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
out = cv2.VideoWriter('output.mp4', fourcc, 30.0, (3840, 2160))

for _ in range(60):  # 30 frames per second, so 60 frames for 2 seconds
    # Generate a random 4K frame
    frame = np.random.randint(0, 256, (2160, 3840, 3), dtype=np.uint8)
    # Write the frame
    out.write(frame)

# Release the VideoWriter
out.release()
