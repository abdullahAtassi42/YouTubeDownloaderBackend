from flask import Flask, request, send_file
from yt_dlp import YoutubeDL

app = Flask(__name__)
@app.route('/download')
def download():
    url = request.args.get('url')

    ydl_opts = {
        'format': 'best',
        'outtmpl': 'video.%(ext)s',
    }


    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return send_file('video.mp4', as_attachment=True)
app.run(host="0.0.0.0", port=5000)