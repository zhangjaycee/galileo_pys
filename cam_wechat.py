# -*- coding: utf-8 -*-
import cv2
import datetime

conf = {
    "show_video": True,
    "use_dropbox": False,
    "dropbox_key": "YOUR_DROPBOX_KEY",
    "dropbox_secret": "YOUR_DROPBOX_SECRET",
    "dropbox_base_path": "YOUR_DROPBOX_PATH",
    "min_upload_seconds": 3.0,
    "min_motion_frames": 8,
    "camera_warmup_time": 2.5,
    "delta_thresh": 5,
    "resolution": [640, 480],
    "fps": 16,
    "min_area": 5000
}

cap = cv2.VideoCapture(0)
avg = None
lastUploaded = datetime.datetime.now()
while True:
    timestamp = datetime.datetime.now()
    text = "ok"
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if avg is None:
        print "starting backfground model..."
        avg = gray.copy().astype("float")
        continue

    cv2.accumulateWeighted(gray, avg, 0.5)
    frameDelta = cv2.absdiff(gray, cv2.convertScaleAbs(avg))
    
    # 对变化图像进行阀值化, 膨胀阀值图像来填补
    # 孔洞, 在阀值图像上找到轮廓线
    thresh = cv2.threshold(frameDelta, conf["delta_thresh"], 255,
        cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)
    (cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
 
    # 遍历轮廓线
    for c in cnts:
        # if the contour is too small, ignore it
        if cv2.contourArea(c) < conf["min_area"]:
            continue
 
        # 计算轮廓线的外框, 在当前帧上画出外框,
        # 并且更新文本
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Attention!"
    print "[", text, "]"
    # 在当前帧上标记文本和时间戳
    ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
    #print ts
    cv2.putText(frame, "Room Status: {}".format(text), (10, 20),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(frame, ts, (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,
        0.35, (0, 0, 255), 1)
    
    if text == "Attention!":
        # 判断上传时间间隔是否已经达到
        if (timestamp - lastUploaded).seconds >= conf["min_upload_seconds"]:
            # 运动检测计数器递增
            motionCounter += 1
 
            # 判断包含连续运动的帧数是否已经
            # 足够多
            if motionCounter >= conf["min_motion_frames"]:
                # 判断Dropbox是否被使用
                if conf["use_dropbox"]:
                    # write the image to temporary file
                    t = TempImage()
                    cv2.imwrite(t.path, frame)
 
                    # 将图像上传至Dropbox并删除临时图片
                    print "[UPLOAD] {}".format(ts)
                    path = "{base_path}/{timestamp}.jpg".format(
                        base_path=conf["dropbox_base_path"], timestamp=ts)
                    client.put_file(path, open(t.path, "rb"))
                    t.cleanup()
                # 更新最近一次上传的时间戳并且重置运动
                # 计数器
                print "[ Dangerous! ]"
                lastUploaded = timestamp
                motionCounter = 0
    #否则, 该房间没有“被占领”
    else:
        motionCounter = 0  
        # 判断安保视频是否需要显示在屏幕上
    if conf["show_video"]:
        # 显示安视频
        cv2.imshow("Security Feed", frame)
        key = cv2.waitKey(1) & 0xFF
 
        # 如果q被按下，跳出循环
        if key == ord("q"):
            break  
