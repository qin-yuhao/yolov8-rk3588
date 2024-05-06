#y: fps , x thread_num
import matplotlib.pyplot as plt
import numpy as np
import os


if __name__ == '__main__':

    fps_list = [83.20205262876419, 122.99568080095644, 105.58604339266819, 129.8679616604555, 152.89294850068237, 135.62710410491565, 147.8267066491186, 161.4680718683335, 142.40346176262065, 153.48842860172883, 164.18654906218853, 149.8834181634387, 156.13622639169128, 163.93290385035397, 155.39270677883968, 160.46675070729947, 163.24497207678013, 156.34081945576762, 158.15481623433152, 155.874844173617, 148.812759645075, 157.0122252522645, 156.98138516861738, 151.9547081713754, 151.09287273015983, 153.2989487100503, 152.32900855384875, 154.03077851002587, 154.23825870051806]
    #取两位小数
    fps_list = [round(i) for i in fps_list]
    fps_list = np.array(fps_list)
    thread_num = np.arange(1, 30)
    #标注出最大值,最小值,画出每个y值

    max_fps = max(fps_list)
    min_fps = min(fps_list)
    max_index = fps_list.tolist().index(max_fps)
    min_index = fps_list.tolist().index(min_fps)
    plt.annotate('max fps:{}'.format(max_fps), xy=(max_index+1, max_fps), xytext=(max_index, max_fps+10),
                 arrowprops=dict(facecolor='black', shrink=0.05))
    # plt.annotate('min fps:{}'.format(min_fps), xy=(min_index+1, min_fps), xytext=(min_index, min_fps),
    #                 arrowprops=dict(facecolor='black', shrink=0.05))
    for i in range(len(thread_num)):
        plt.text(thread_num[i], fps_list[i], fps_list[i], ha='center', va='bottom', fontsize=10)

    
    plt.plot(thread_num, fps_list)
    plt.xlabel('Thread number')
    plt.ylabel('FPS')
    plt.title('FPS vs Thread number yolov8n on rk3588')
    plt.savefig('500times.png')
    #plt.show()
    print(fps_list)
    print(thread_num)