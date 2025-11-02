from flask import Flask, Response, render_template
import cv2
import time
import threading
import subprocess
import os

app = Flask(__name__)

# === RTSP Camera URL ===
RTSP_URL = "rtsp://192.168.2.224:554/stream1"

# === MJPEG Stream Generator ===
def generate_frames():
    cap = cv2.VideoCapture(RTSP_URL)
    if not cap.isOpened():
        print("❌ Cannot open RTSP stream")
        return

    while True:
        success, frame = cap.read()
        if not success:
            break

        # === Encode Frame as JPEG ===
        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        # === Yield MJPEG Frame ===
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return render_template('index.html')

# === Recording Loop: 30-Minute Chunks ===
def record_loop():
    os.makedirs("recordings", exist_ok=True)
    while True:
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"recordings/{timestamp}.mp4"
        print(f"🎥 Recording: {filename}")
        subprocess.run([
            "ffmpeg",
            "-rtsp_transport", "tcp",
            "-i", RTSP_URL,
            "-t", "7400",  # 30 minutes
            "-c", "copy",
            filename
        ])
        print(f"✅ Saved: {filename}")

# === Cleanup Loop: Delete Files Older Than 2 Hours ===
def cleanup_loop():
    while True:
        now = time.time()
        for file in os.listdir("recordings"):
            path = os.path.join("recordings", file)
            if os.path.isfile(path):
                age = now - os.path.getmtime(path)
                if age > 8400:  # 2 hours
                    os.remove(path)
                    print(f"🗑️ Deleted: {file}")
        time.sleep(60)

# === Launch Flask + Background Threads ===
if __name__ == '__main__':
    threading.Thread(target=record_loop, daemon=True).start()
    threading.Thread(target=cleanup_loop, daemon=True).start()
    app.run(host='0.0.0.0', port=5051, threaded=True)
