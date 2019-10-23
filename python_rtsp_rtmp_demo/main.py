from flask import Flask, render_template, Response
import cv2

class VideoCamera():
    def __init__(self,vurl):
        # 通过opencv获取实时视频流
        self.video = cv2.VideoCapture(vurl)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        #转化为字节流
        return jpeg.tobytes()

# app是Flask的实例，它接收包或者模块的名字作为参数，但一般都是传递__name__
app = Flask(__name__)
@app.route('/')  # 主页
def index():
    return render_template('index.html')

@app.route('/video1_feed')  # 这个地址返回rtsp视频流响应
def video1_feed():
    return Response(gen1(VideoCamera("rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mov")), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video2_feed')  # 这个地址返回rtmp视频流响应
def video2_feed():
    return Response(gen2(VideoCamera("rtmp://202.69.69.180:443/webcast/bshdlive-pc")), mimetype='multipart/x-mixed-replace; boundary=frame')\

@app.route('/video3_feed')  # 这个地址返回rtmp视频流响应
def video3_feed():
    return Response(gen3(VideoCamera("rtmp://media3.sinovision.net:1935/live/livestream")), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video4_feed')  # 这个地址返回rtmp视频流响应
def video4_feed():
    return Response(gen4(VideoCamera("rtmp://58.200.131.2:1935/livetv/hunantv")), mimetype='multipart/x-mixed-replace; boundary=frame')

def gen1(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
def gen2(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
def gen3(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
def gen4(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port = 5000)
