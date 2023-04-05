# MachineVision HomeWork &amp; Project @NCU_ME_machine_vision
透過 QR code 進行擴增實境  
===
本專題使用 pygame 把 3D 影像開啟後，再將此立體圖投影至 2D 的即時影像中。由於 pygame 可以做到遊戲的基本光影特效，因此在投影上顯示會更加逼真。  
本專題將程式架構分為以下四個檔案：
* main.py: 執行主程式，將所有系統串聯  
* webcam.py: 透過 webcam 取得環境影像  
* QR_gesture.py: 將取得的 webcam 影像判讀 QR code 位置，並透過 cv2.SOLVEPNP 計算 QR code 位姿  
* draw_obj.py: 使用 glReadPixels 將 pygame 影像取出，經格式轉換並分解成 r,g,b,a 資料，再透過cv2.merge合併為完整影像，最後再就由 cv2.bitwise_not 將 webcam 原始影像對應之位置資料去除，此時再透過cv2.add將兩者結合  

[QR code設計]  
-------  
本次專題針對兩個不同物件進行投影，因此根據 QR code 紀錄資料不同，可投影不同的影像。另外，QR code 可透過角落的三個方格進行方向定位，因此很適合用來判讀物件位置及面向。
[成品圖]  
-------  
![image](https://user-images.githubusercontent.com/39979565/229982373-f1101ed0-f1fa-4a89-bfd1-0ee933d61ecb.png)
