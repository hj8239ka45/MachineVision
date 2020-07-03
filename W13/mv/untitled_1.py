# Untitled - By: hj823 - 週二 五月 26 2020

import sensor, image, time,math

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False)
sensor.set_auto_whitebal(False)
clock = time.clock()

while(True):
    clock.tick()
    img = sensor.snapshot()
    #讀取家族 判斷
    for tag in img.find_apriltags(families=image.TAG16H5):
        img.draw_rectangle(tag.rect(),color=(255,0,0))
        img.draw_cross(tag.cx(),tag.cy(),color=(0,255,0))
        degress = 180*tag.rotation()/math.pi
        print(tag.id(),degress,tag.x_translation(),
        tag.y_translation(),tag.z_translation())
