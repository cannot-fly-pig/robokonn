import depthai as dai
import cv2
import numpy as np
import time
import threading
import rclpy
from rclpy.node import Node

from team6_msgs.msg import Goal, Back, Direction


class Camera(Node):

    def __init__(self):
        super().__init__('camera') # node name
        # Goal Publisher
        self.goal_publisher = self.create_publisher(Goal, 'goal_pub', 10)

        # Back Publisher
        self.back_publisher = self.create_publisher(Back, 'back_pub', 10)

        self.i = 0
        self.direction = None

        self.subscription = self.create_subscription(
            Direction,
            'direction_pub',
            self.callback_sub,
            10)
        self.subscription
    
    
    def callback_goal_pub(self, diff):
        msg = Goal()
        msg.diff = diff  # ここにズレを代入
        self.goal_publisher.publish(msg)
        self.get_logger().info('Publishing diff : "%s"' % msg.diff)

    def callback_back_pub(self, pos, degree, diff):
        msg = Back()
        msg.pos = pos
        msg.degree = degree
        msg.diff = diff
        self.back_publisher.publish(msg)
        self.get_logger().info('Pos, degree, diff: "%s %s %s"' % (msg.pos,msg.degree,msg.diff))

    def callback_sub(self, msg):
            self.direction = msg.direction
            self.get_logger().info('Subscribing direction : "%s"' % msg.direction)


def main(args=None):
    rclpy.init(args=args)

    camera = Camera()


    thread = threading.Thread(target=rclpy.spin, args=(camera,))
    thread.start()

    count = 0
    flag = 1  

    # Create pipeline
    pipeline = dai.Pipeline()

    # create nodes
    monoLeft = pipeline.create(dai.node.MonoCamera)
    edgeDetectorMono = pipeline.create(dai.node.EdgeDetector)
    xout_edgeMono = pipeline.create(dai.node.XLinkOut)
    xout_mono = pipeline.create(dai.node.XLinkOut)
    control = pipeline.create(dai.node.XLinkIn)

    xout_edgeMono.setStreamName("edge_mono")
    xout_mono.setStreamName("mono")
    control.setStreamName("control")

    # configure color camera
    monoLeft.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
    monoLeft.setBoardSocket(dai.CameraBoardSocket.LEFT)
    height = monoLeft.getResolutionHeight()
    width = monoLeft.getResolutionWidth()
    sum_pixel = height*width

    # linking
    monoLeft.out.link(edgeDetectorMono.inputImage)
    edgeDetectorMono.outputImage.link(xout_edgeMono.input)
    monoLeft.out.link(xout_mono.input)
    control.out.link(monoLeft.inputControl)

    #kernel for the goal script
    kernel_1 = np.ones((10,10), np.uint8)
    kernel_2 = np.ones((25,25), np.uint8)
    kernel_3 = np.ones((3,3), np.uint8)

    #kernel for the back script
    kernel_v = np.ones((10,1), np.uint8)
    kernel_v2 = np.ones((1,5), np.uint8)
    kernel_h = np.ones((1,30), np.uint8)

    #back 検出する輪郭の最小ｙ座標
    y_min = int(height/2) 
    x_min = 0
    x_max = width

    ######FPS#######
    fps = 0
    tenF_time = 0
    f_count = 0
    fmax_count = 10
    start = time.time()
    ################

    with dai.Device(pipeline) as device:

        # in/out queues
        q_edgeMono = device.getOutputQueue(name="edge_mono", maxSize=4, blocking=False)
        q_mono = device.getOutputQueue(name="mono", maxSize=4, blocking=False)
        q_control = device.getInputQueue(name="control", maxSize=4, blocking=False)

        # set focus position
        ctrl = dai.CameraControl()
        ctrl.setManualFocus(55)
        q_control.send(ctrl)


        print("start loop")
        while(True):
            #Goal Script
            while(camera.direction == "goal"):
                count = 0
                flag = 0

                edgeMono = q_edgeMono.get()

                edgeMonoFrame = edgeMono.getCvFrame()

                
                edgeMonoFrame = cv2.resize(edgeMonoFrame, (640, 400)) #２値化画像サイズ　実装時削除
                _, edgeMonoFrame = cv2.threshold(edgeMonoFrame, 125, 255, cv2.THRESH_BINARY) # 2値化
                #edgeMonoFrame = cv2.morphologyEx(edgeMonoFrame, cv2.MORPH_OPEN, kernel_3) # モルフォロジー変換
                #edgeMonoFrame = cv2.morphologyEx(edgeMonoFrame, cv2.MORPH_CLOSE, kernel_2) # モルフォロジー変換
                edgeMonoFrame = cv2.dilate(edgeMonoFrame, kernel_1, iterations=1) # 膨張処理　


                contours, hierarchy = cv2.findContours(edgeMonoFrame, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_TC89_L1)
                
                
                contours = [contour for i, contour in enumerate(contours) if hierarchy[0, i, 3] == -1]
        
                contours = list(filter(lambda x: cv2.contourArea(x) > 500 and cv2.contourArea(x) < sum_pixel*0.7 and  
                                    (cv2.contourArea(x) / (cv2.boundingRect(x)[2] * cv2.boundingRect(x)[3])) > 0.8, contours))


                # find rectangles
                rect_num = 0
                for contour in contours:
                    x,y,w,h = cv2.boundingRect(contour)               
                    rectRatio = cv2.contourArea(contour) / (w * h)
                    hwRatio = h/w
                    if rectRatio > 0.8 and h*w < (height*width)*0.65 and hwRatio > 0.6 and hwRatio < 1 and x > 20 and (x+w) < (width-20) and y > 20 and (y+h) < (height-20): #　検出した四角形の面積が画面の65%未満の場合　ゴール穴まで30cm接近時の下限
                        diff = int(x+(w-1)/2) - int(width/2)
                        print("difference from center: ", diff)
                        camera.callback_goal_pub(diff)
                        rect_num += 1 # 見つけた長方形の数
                rect_num = 0
                
                #########FPS#########
                if f_count == fmax_count:
                    end = time.time()
                    tenF_time = end - start
                    fps = fmax_count/(tenF_time)
                    start = time.time() 
                    f_count = 0
                    print("FPS : ", str(round(fps, 1)))

                f_count += 1
                cv2.putText(edgeMonoFrame, "FPS: " + str(round(fps, 1)) + " time: " + str(round(tenF_time, 3)) + "s", (10, 18), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
                #####################

                cv2.imshow("edge mono", edgeMonoFrame)


                if cv2.waitKey(1) == ord('q'):
                    break

            if flag == 0:
                cv2.destroyAllWindows()
                flag = 1
            

            #Back Script
            while (camera.direction == "back"):
                count = 0
                flag = 0

                inMono = q_mono.get()

                mono = inMono.getCvFrame()
                gray = inMono.getCvFrame()
                
                #黒抽出
                gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 151, 11)

                
                
                gray_v = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel_v) # 垂直方向の抽出
                gray_v = cv2.morphologyEx(gray_v, cv2.MORPH_OPEN, kernel_v2)
                
                gray_h = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel_h) # 水平方向の抽出

                
                contours_v, _ = cv2.findContours(gray_v[y_min:, x_min:x_max], cv2.RETR_LIST, cv2.CHAIN_APPROX_TC89_L1)
                contours_h, _ = cv2.findContours(gray_h[y_min:, x_min:x_max], cv2.RETR_LIST, cv2.CHAIN_APPROX_TC89_L1)


                contours_v = list(filter(lambda x: cv2.contourArea(x) > 300 and cv2.contourArea(x) < 0.3*((height-y_min)*(x_max-x_min))
                                        and 1.5*cv2.boundingRect(x)[2] < cv2.boundingRect(x)[3], contours_v)) #輪郭の条件
                contours_h = list(filter(lambda x: cv2.contourArea(x) > 100 and cv2.contourArea(x) < 0.3*((height-y_min)*(x_max-x_min))
                                        and cv2.boundingRect(x)[2] > 3*cv2.boundingRect(x)[3], contours_h)) #輪郭の条件
                
                cv2.line(mono, (0, y_min), (width, y_min), (0, 0, 0), 2) # 検出範囲
                cv2.line(mono, (x_min, y_min), (x_min, height), (0, 0, 0), 2)
                cv2.line(mono, (x_max, y_min), (x_max, height), (0, 0, 0), 2)
                cv2.line(mono, (int(width/2), y_min), (int(width/2), height), (0, 0, 0), 2)
                #cv2.imshow("Gray", mono)
            

            
                #cv2.drawContours(rgb_v, contours_v, -1, (0, 0, 255), 2) #輪郭の描写
                #cv2.drawContours(rgb_h, contours_h, -1, (0, 0, 255), 2) #輪郭の描写


                for contour_v in contours_v: # 垂直方向
                    contour_v[:, :, 1] += y_min
                    contour_v[:, :, 0] += x_min
                    rect_v = cv2.minAreaRect(contour_v)
                    box_v = cv2.boxPoints(rect_v)
                    box_v = np.int0(box_v)
                    if cv2.contourArea(box_v) != 0:
                        if (cv2.contourArea(contour_v) / cv2.contourArea(box_v)) > 0.2:
                            cv2.drawContours(mono, [box_v], 0, (0, 0, 0), 2)
 
                            for contour_h in contours_h: # 水平方向
                                contour_h[:, :, 1] += y_min
                                contour_h[:, :, 0] += x_min
                                rect_h = cv2.minAreaRect(contour_h)
                                box_h = cv2.boxPoints(rect_h)
                                box_h = np.int0(box_h)
                                if rect_h[1][0] > rect_h[1][1]:
                                    h_long_side = rect_h[1][0]
                                else:
                                    h_long_side = rect_h[1][1]
                                if cv2.contourArea(box_h) != 0:
                                    if (cv2.contourArea(contour_h) / cv2.contourArea(box_h)) > 0.2:
                                        cv2.drawContours(mono, [box_h], 0, (0, 0, 0), 2)
                                        retval, intersectionRegion = cv2.rotatedRectangleIntersection(rect_v, rect_h) # 縦横ラインの交点
                                        #print(intersectionRegion)
                                        if intersectionRegion is not None:
                                            for xy in intersectionRegion:
                                                #rgb_v = cv2.circle(rgb_v, (int(xy[0][0]), int(xy[0][1])), 2, (0, 255, 255), 2)
                                                if (rect_h[0][0] + h_long_side/2 - 30) <= xy[0][0]: # ラインの右中左判定
                                                    pos = "right"
                                                    degree = round(rect_v[2], 2)
                                                    diff = int(rect_v[0][0])-int(width/2)
                                                    cv2.putText(mono, "R:"+str(degree)+"deg, diff"+str(diff), (int(rect_v[0][0]), int(rect_v[0][1]-(rect_v[1][1]/2)-5)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
                                                    camera.callback_back_pub(pos, degree, diff)
                                                    #print("left")
                                                elif (rect_h[0][0] + h_long_side/2 - 30 > xy[0][0]) and (rect_h[0][0] - h_long_side/2 + 30 < xy[0][0]):
                                                    pos = "center"
                                                    degree = round(rect_v[2], 2)
                                                    diff = int(rect_v[0][0])-int(width/2)
                                                    cv2.putText(mono, "C:"+str(degree)+"deg, diff"+str(diff), (int(rect_v[0][0]), int(rect_v[0][1]-(rect_v[1][1]/2)-5)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
                                                    camera.callback_back_pub(pos, degree, diff)
                                                    #print("center")
                                                elif (rect_h[0][0] - h_long_side/2 + 30 >= xy[0][0]):
                                                    pos = "left"
                                                    degree = round(rect_v[2], 2)
                                                    diff = int(rect_v[0][0])-int(width/2)
                                                    cv2.putText(mono, "L:"+str(degree)+"deg, diff"+str(diff), (int(rect_v[0][0]), int(rect_v[0][1]-int(rect_v[1][1]/2)-5)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
                                                    camera.callback_back_pub(pos, degree, diff)
                                                    #print("right")

            
                #########FPS#########
                if f_count == fmax_count:
                    end = time.time()
                    fps = fmax_count/(end - start)
                    start = time.time() 
                    f_count = 0

                f_count += 1
                cv2.putText(mono, "FPS: " + str(round(fps, 1)), (10, 18), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
                #####################

                cv2.imshow("Mono", mono)
                #cv2.imshow("Gray vertical", gray_v)
                #cv2.imshow("Gray horizon", gray_h)
                

                if cv2.waitKey(1) == ord('q'):
                    break    

            if flag == 0:
                cv2.destroyAllWindows()
                flag = 1
            time.sleep(1)
            print("loop", str(count))
            count += 1

    camera.destroy_node()
    rclpy.shutdown()
    print("finish")


if __name__ == '__main__':
    main()
