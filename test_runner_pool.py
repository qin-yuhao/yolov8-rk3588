import cv2
import yolov8_runner_pool 
import time
import threading
import numpy as np
from multiprocessing import Process

def test_runner_pool(thread_num):
    run= yolov8_runner_pool.yolov8_runner_pool('model/yolov8.rknn',thread_num,0.25,0.45,80)
    img=cv2.imread('model/bus.jpg')
    #init pool
    for i in range(thread_num):
        result = run.inference(img)

    star_time = time.time()
    times = 500
    # for i in range(times):
    #     result = run.inference_all(imgs)
    for i in range(times):
        result = run.inference(img)
    print('avg ms :', (time.time()-star_time)*1000/times)
    print('fps :', 1/((time.time()-star_time)/times))
    fps = 1/((time.time()-star_time)/times)
    for box in result:
        clas_id,left,top,right,bottom,scor = box
        cv2.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (0, 255, 0), 2)
        cv2.putText(img, str(clas_id), (int(left), int(top)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(img, str(round(scor, 2)), (int(left), int(top)+20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imwrite('model/bus_out.jpg', img)
    time.sleep(5)
    return fps
   
if __name__ == '__main__':
    fps_list = []
    for i in range(1,30):
        #print('thread num:',i+1)
        fps = test_runner_pool(i+1)
        fps_list.append(fps)
        print('fps:{},thread num:{}'.format(fps,i+1))

    print('fps list:',fps_list)