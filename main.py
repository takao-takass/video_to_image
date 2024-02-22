import cv2
from pathlib import Path

def save_frames(video_path: Path, output_dir: Path, interval: float):
    cap = cv2.VideoCapture(str(video_path))
    fps = round(cap.get(cv2.CAP_PROP_FPS) * interval)

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    total_seconds = total_frames // fps

    frame_num = 0
    frame_seconds = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame_num % fps == 0:
            output_path = output_dir / f"frame_{frame_num // fps}.png"
            cv2.imwrite(str(output_path), frame)
            frame_seconds += 1
        frame_num += 1
        print(f"Processed {frame_seconds / total_seconds * 100:.2f}% : {frame_seconds} of {total_seconds} frames.", end="\r")
    cap.release()

video_path = Path("./videos/a.mp4")
output_dir = Path("./videos")
interval = 1.0
save_frames(video_path, output_dir, interval)
