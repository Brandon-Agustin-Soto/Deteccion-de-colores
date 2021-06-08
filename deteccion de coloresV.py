import cv2
import numpy as np

captura=cv2.VideoCapture(0)

rojo_Bajo1=np.array((0, 100, 20), np.uint8)
rojo_Alto1=np.array((8, 255, 255), np.uint8)

rojo_Bajo2=np.array((175, 100, 20), np.uint8)
rojo_Alto2=np.array((179, 255, 255), np.uint8)

naranja_Bajo=np.array((15, 100, 20), np.uint8)
naranja_Alto=np.array((25, 255, 255), np.uint8)

amarillo_Bajo=np.array((25, 100, 20), np.uint8)
amarillo_Alto=np.array((35, 255, 255), np.uint8)

verde_Bajo=np.array((35, 100, 20), np.uint8)
verde_Alto=np.array((85, 255, 255), np.uint8)

celeste_Bajo=np.array((85, 100, 20), np.uint8)
celeste_Alto=np.array((100, 255, 255), np.uint8)

azul_Bajo=np.array((100, 100, 20), np.uint8)
azul_Alto=np.array((130, 255, 255), np.uint8)

violeta_Bajo=np.array((135, 100, 20), np.uint8)
violeta_Alto=np.array((145, 255, 255), np.uint8)

rosa__Bajo=np.array((145, 100, 20), np.uint8)
rosa_Alto=np.array((165, 255, 255), np.uint8)

def detectar(mask, color):
	_,contornos, hierarchy=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	for i in contornos:
	 	area=cv2.contourArea(i)
	 	if area > 3000:
	 		M=cv2.moments(i)
	 		if (M["m00"]==0):M["m00"]=1
	 		x = int(M["m10"]/M["m00"])
	 		y = int(M["m01"]/M["m00"])
	 		cv2.circle(frame, (x, y), 7, (0, 255, 0), -1)
	 		font=cv2.FONT_HERSHEY_SIMPLEX
	 		cv2.putText(frame,'{},{}'.format(x,y),(x+10,y), font, 0.5,(0,255,0),1,cv2.LINE_AA)
	 		suavizado=cv2.convexHull(i)
	 		cv2.drawContours(frame, [suavizado], 0, color, 2)

while True:

	ret, video=captura.read()

	if ret==True:
		HSV_video=cv2.cvtColor(video, cv2.COLOR_BGR2HSV)
		maskRed1=cv2.inRange(video, rojo_Bajo1, rojo_Alto1)
		maskRed2=cv2.inRange(video, rojo_Bajo2, rojo_Alto2)
		mask_Red=cv2.add(maskRed1, maskRed2)
		mask_Orange=cv2.inRange(video, naranja_Bajo, naranja_Alto)
		mask_Yellow=cv2.inRange(video, amarillo_Bajo, amarillo_Alto)
		mask_Green=cv2.inRange(video, verde_Bajo, verde_Alto)
		mask_Light_blue=cv2.inRange(video, celeste_Bajo, celeste_Alto)
		mask_Blue=cv2.inRange(video, azul_Bajo, azul_Alto)
		mask_Purple=cv2.inRange(video, violeta_Bajo, violeta_Alto)
		mask_Rose=cv2.inRange(video, rosa__Bajo, rosa_Alto)
		detectar(mask_Red, (0, 255, 0))
		detectar(mask_Orange, (20, 255, 0))
		detectar(mask_Yellow, (0, 255, 0))
		detectar(mask_Green, (0, 255, 0))
		detectar(mask_Light_blue, (0, 255, 0))
		detectar(mask_Blue, (0, 255, 0))
		detectar(mask_Purple, (0, 255, 0))
		detectar(mask_Rose, (0, 255, 0))
		cv2.imshow("Deteccion de color",video)
		if cv2.waitKey(1) & 0xFF == ord ("F"):
			break

	else:
		break


captura.release()
cv2.destroyAllWindows()
