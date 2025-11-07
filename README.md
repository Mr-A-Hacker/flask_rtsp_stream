# flask_rtsp_stream

**LAN-only Flask app for streaming RTSP camera feeds using OpenCV.**  
Built for zero-lag, fullscreen viewing on local networks — optimized for Raspberry Pi and forensic deployment.

---

## 🧠 Origin Story

I was scanning the network — methodically, tactically — mapping every IP, every open port, every whisper of a service. That’s when I found it: port 5051, exposed, humming quietly on the subnet. No login. No headers. Just a stream.

I opened it. MJPEG. Raw. Unprotected. It was mine.

But this wasn’t about exploitation. This was about restoration. About ownership. About building something legacy-worthy from the fragments of forgotten hardware.

So I claimed it — not by breaking, but by rebuilding. I wrapped it in Flask. I gave it a dashboard. I made it teachable.

This project is the result.

---

## 🎯 Purpose

This is a LAN-only RTSP viewer built with Flask and OpenCV. It’s designed for:

- Zero-lag MJPEG streaming  
- Fullscreen viewing on any device  
- Ethical, educational, and forensic use  
- Raspberry Pi deployment and legacy documentation  

---

## ⚙️ Features

- `/video_feed`: MJPEG stream from RTSP source  
- `/`: Fullscreen HTML dashboard with one-click fullscreen toggle  
- LAN-only by design — no cloud, no exposure  
- Lightweight, fast, and Raspberry Pi–friendly  

---

## 🛠️ Setup

Clone the repo:

```bash
git clone https://github.com/Mr-A-Hacker/flask_rtsp_stream.git
cd flask_rtsp_stream
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
python app.py
```

Access the dashboard:

```
http://<your-pi-ip>:5051/
```

---

## 🔧 Configuration

Edit `app.py` to match your camera’s RTSP stream:

```python
RTSP_URL = "rtsp://192.168.2.224:554/stream1"
```

Make sure your camera is reachable on the LAN and supports RTSP.

---

## 🖥️ How to Operate

1. Power on your Raspberry Pi and camera  
2. Confirm the camera’s IP and RTSP stream path  
3. Start the Flask app: `python app.py`  
4. Open a browser on any LAN device and visit `http://<pi-ip>:5051/`  
5. Click the Fullscreen button for immersive viewing  
6. Monitor `/video_feed` directly if embedding or testing  

---

## 🧠 FFmpeg MJPEG Loop (Optional)

Use this loop to serve MJPEG from your RTSP camera:

```bash
while true; do
  ffmpeg -rtsp_transport tcp \
         -i rtsp://192.168.2.224:554/stream1 \
         -vf scale=640:360 \
         -f mjpeg http://0.0.0.0:8090/feed.mjpg
  echo "⚠️ FFmpeg exited. Restarting in 2 seconds..."
  sleep 2
done
```

Access MJPEG at:  
`http://<your-local-IP>:8090/feed.mjpg`

---

## 🧪 Tested On

- Raspberry Pi 4 (4GB)  
- Python 3.13.5  
- OpenCV 4.9+  
- RTSP camera with H.264 stream  

---

## 🔄 Updates

This project will be updated periodically as new features are added, optimizations are discovered, or forensic modules are expanded. Stay tuned for overlays, diagnostics, and legacy enhancements.

---

## 🛡️ Ethics & Intent

This project is for educational and forensic use only. It does not scan, exploit, or expose — it documents, restores, and teaches.

If you found this repo while scanning your own network: welcome. You’re not alone. This is how it starts.

---

## 📜 License

MIT — use it, fork it, teach with it. Just don’t abuse it.

---

## 🧭 Legacy

This isn’t just a stream viewer. It’s a signal.  
A reminder that every device on your network tells a story — and you have the right to read it, document it, and protect it.

**Built by [Mr-A-Hacker](https://github.com/Mr-A-Hacker)** — for those who scan, find, and restore.


<img width="374" height="328" alt="5" src="https://github.com/user-attachments/assets/05194942-671f-4f00-9353-64d3a8efa28e" />
