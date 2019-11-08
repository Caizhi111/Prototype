# Prototype
ID 5415 Prototyping connected products, IDE faculty, TU Delft
| By Group 9: Zhi Cai, Yiling Liu, Yufei He

# Explanation video
https://drive.google.com/open?id=1U6dykhN0eDotX_F5fxs2396cdGym8p--
https://drive.google.com/open?id=1E0v_8iJ1IGYeomsYGjJwX7aWqiKgnjtD

# Final prototype
![alt text](https://github.com/Caizhi111/Prototype/blob/master/DSC00029.JPG)

# Design Context
![alt text](https://github.com/Caizhi111/Prototype/blob/master/Design%20Context.jpeg?raw=true)

# Design Brief
Our team aims to create an alarming system for the care givers of the wheelchair users. It detects and records fall-down accidents of the wheelchair that may be risky for the users during outdoor activities, which enables their care givers to receive the notification and location, thus react to the situation in time.

# Final decision on Sensors and Actuators
- Sensors: Button, IMU, GPS
- Actuators: LED, Camera, Web page, Instant Messenger(Wechat)
- Cloud Server: DCD hub
- Others: Arduino Mega, Raspberry Pi, Power bank

# IoT Architecture
![alt text](https://github.com/Caizhi111/Prototype/blob/master/IoT%20Architecture.jpeg?raw=true)

# How the prototype works
1. Find a envrionment with both eduroam and GPS signal.
2. After the Raspberry Pi is powered on by the power bank, type in "./auto_run.sh" in the terminal. 
3. Then, the wheelchair user needs to scan the QR code in Wechat. 
4. After successfully scaning the QR code, the wheelchair user can press the button on the breadboard to start the sensors. Blinking white led means the GPS has no signal, and a lighted white led without blinking means the GPS is working properly. 
5. When the wheelchair user falls down, the specified people in their Wechat account will receive three messages, such as follows:
- There is a likely accident happened to the wheelchair user, the location is as follows:
- Landbergstraat 5, 2628 CE Delft, Netherlands
- Check the recorded video:http://145.94.153.90:5000/static/video/video.mp4 (can only be accessed when server.py is running)


Python code on Raspberry Pi:
  - videoRecording.py (path: Prototype/serial_to_dcdhub2.py)
  - serial_to_dcdhub2.py (path: Protoype/camera/videoRecording.py)
  - wechat_sending.py (path: Prototype/web/static/wechat/wechat_sending.py )
  - server.py (path: Prototype/web/server.py)
  
Arduino code:
  - sketch_oct04b.ino

Run all the python code at one time:
  - Type in "./auto_run.sh" in the terminal 
  
Kill all the python code at one time:
  - Type in "./kill_script.sh" in the terminal

# List of testing items
1. Transfer IMU and GPS data to the cloud server.
2. Build a web page to review the 30s video.
3. Constantly record video by a camera, but only store the latest 30s video, and transfer it to the web page.
4. Find out IMU value pattern when falling down happens.
5. Connect the system with API of an instant messenger. 
6. When falling down happens, automatically send the messages to designated people via the instant messenger.

# .env
THING_ID=my1wheelchair-b5a0
THING_TOKEN=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1NzAxNjgyNzIsImV4cCI6MTg4NTc0Nzg3MiwiYXVkIjoiaHR0cHM6Ly9kd2QudHVkZWxmdC5ubDo0NDMvYXBpIn0.KldzQIk2U8LDUSyc_m7PMZgbWoNeU9BWcpJqviDVnAKc48S66AtATXZZrA5efkIJG5aRZj8DXQcRhBaaPNrLbcE8osWuivHWW9vf6m54YouAVE2Q9Tyxg5KiApmTUo7FvY_EehlGdFuba93DT4n66Izf1vOMQRbnPPlgUDGB0WuIrnnkST5p7SZ5PFPgFu-LAjVjUKnTUoAIElp169e2eJRupudnuOYVYy68ToyNBqdMuT-nEPBrIfnhFVno31hg04xhiOWrnxYEOSmJBh_1SWXbGxlUlsN48jSqz6E_EKrQ_3xbVu_48wenSRKP_20Bm1hXKI5bIQ1Bi1jLlT00k1iwOJD3wDlDbqSyuFaRi54CtX4z7Uso5bX-l7p7SUjhUwC2aS51-SKTiVVx1TtmxGlQtu66oIl9ul1M6K5TON7MeIur5_FbanAHd8MtcdHRM-7Da5S4utZ8Cf6I0TeAwb-sxm16GtReLJnh2haaISALL1CujHdsiWwKMeXtlSXZgRTQOCsRVeXQcbk3BNPr7e4EmHgpg5J-9z02bFp9fUwhx5E2g7ZaxyffbG7jUpJ4rrPDyLBJFNYpzrQFEM_3Eg6AEZh4IB0O6TdKcq3ykafefXLkHrZK183RCd6HY3JVfThQEpT0g2hpz5ioMbaLJOQVUft71vUpOMiIY8L_6h4

Hey group 9, you should be able to login with:
user: group9@test.test
password: group9

your thing id (also visible on the hub) is dcd:things:my-test-thing-556e
your token is
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1NzA0MzYwODgsImV4cCI6MTg4NjAxNTY4OCwiYXVkIjoiaHR0cHM6Ly9kd2QudHVkZWxmdC5ubDo0NDMvYXBpIn0.CgFqOdt-c2pNvReLZxhILpjr_yF1BnEJzBfvY2Nkc0FCnlqI_KjUUZ0YWDjoml5Ocfhmmg3xUnoaQS8QA6PnaO-kvFQ6cgCg-m2RYSO8_YVhSdQ13_eM7xtfLMbivkPJn3XVNXjJXy7pWF7w6sh8mhkjYHns6QqDkDnAQsgE4meEvF5jlUQS-X-fkWidxcLBWdcZP6hmQQ6YYQAeh6sph8Vr1g1hcDVtQs8H0Iicu4y_8l6vKZBZQm_PnpKCf-bdPDJgOITO8j9nOv8y9RE4Mpa7SrfEBEamSdbK7tb7PPt-57NmHTDmp5K_y-7PoekbFOuIKRJ-M7wY8oBa5ulwy6j1-UKZ4PJBga8u1HgKAhCAcQa5xsWLOtS7WB-0RwdklH3PANMaXYSd3IYVz-p14BKtoey4DsI1wPUtCKdGq5mHOi9S3dTe8Ubh6md44DhiyfvG-nH81mYk7kNFGBlvgs5F-DlTBszva9fuwYeIs_B0ChLN97F1LnLLTHw_Xl6IIiaMZIDUTqqejEliZzQqtNyW88rr6f4GXD94AN1l97Chz5l768yDWQl_FWJH_37r-ow6Iwxb6aT8kc1-y_JFBr5hYTigSoFvZpOxzKNqpR5CAQjh608ZNogAL7UVs3gt2_yisU7-fj5uce3MgivczBt28E1ACLphtfexOoUvXPw

# week 1.1
Brainstorm and decide design direction. (see file Inter-connected wheelchair.pdf)
![alt text](https://github.com/Caizhi111/Prototype/blob/master/Initial%20IoT%20Architecture.jpg?raw=true)

Other potential design directions:
- Navigation system for wheelshair users
A navigation system specially designed for the wheelchair users to find the most suitable way to their destination. It helps to select the ideal route based on the feedback of the road conditions and the user experience from other users.
- Alarm system for indoor accidents:
When accidents happens when wheelchair users doing indoor acticities, such as going to the toilet, taking a shower and moving from wheelchair to other chairs or beds, the alarming system can notificate their care givers to help immediately. 
- Exercise competition among wheelchair users:
Since wheelchair users usually keep the sitting gesture, a game is designed for motivating them to exercise more.
- Balancing system for steep slope:
When wheelchair users go uphill and downhill, their body position is perpendicular to slope instead of the horizontal plane, which might result in uncomfortable and turning over. A balancing system is designed for keeping their body position is always perpendicular to the horizontal plane.

Exploration on sensors and actuators:
![alt text](https://github.com/Caizhi111/Prototype/blob/master/sensors.jpeg?raw=true)
![alt text](https://github.com/Caizhi111/Prototype/blob/master/Actuators.jpeg?raw=true)


# week 1.2
Changes in the IoT structure:
  - a physical button to turn on/off the device instead of automatical switch enabled by FSR
  - IMU instead of MPU
  - University WIFI instead of SMS module for prototyping purpose
  - API to instant messagers to send emergency messages to care givers (whatsapp, wechat....)

We achieved:
  - Set up an IMU sensor on Arduino
  - Bluetooth connection between IMU and our phone via Adafruit Feather. We can check the IMU data on an app called eBeacon.

# week 1.3
Changes in the IoT structure:
  - Since the IMU will be attached to the wheelchair, Bluetooth is then not neccessary for us. We decided to used USB cable for the Serial communication between Arduino and Raspberry Pi. We have therefore hooked IMU onto Arduino mega instead.
  
We achieved:
  - Set up internet connection between Respberry Pi and DCD hub (eduroam)
  - Transfer IMU data from serial port on Raspberry Pi to DCD hub
  - Find the API for Wechat. We are able to send messages to a specific person defined in the code. The people who are specified to receive the messages can be adjusted in the code

Challenges remained:
  - For realizing the the function of automatically sending messages to a specified person, the user who are going to send the messages has to firstly log in by scanning a QR code. This means we probably need a screen connected to raspberry pi. 

# week 1.4
We achieved:
  - Recording video by the camera connected to Raspberry Pi
  - Always store the latest 30s video in a local folder in Raspberry Pi, which saves the storage space. The duration of the video can be adjusted in the code.
  - Add google maps service, which could tranfer longtitude and latitude into address and postcode

Challenges remained:
  - Send the video via the instant messenger
  - The location cannot be open in the map embedded in Wechat, which means the users needs to copy the address and paste in google map to search the location.
    
# week 1.5
We achieved:
  - Set up a GPS breakout
  - Read the longitude and latitude on DCD hub
  - A physical button connected to Arduino to switch on/off the sensors
  - The messages been send automatically includes a description, a video link, and an address with street name, house number, post code, city, country.

Challenges remained:
  - The signal of the GPS is often blocked inside a bulding. Maybe add antennas.

# week 1.6
Changes in the IoT structure:
  - Since sending videos via instant messengers is quite data consuming, thus, we decide to use a web page to show the video. The link of the website will be included in the auto-replying mesaages.
  
We achieved:
  - Build a web page for users to review the video
  - Create a service for run all the python code at one time
  - Add two LEDs on Arduino to show the status of IMU and GPS status: blue led for IMU, and white led for GPS. When leds are constantly lighted up, the IMU and GPS are working properly. When the white led is blinking, the GPS is getting a fix.

# week 1.7
We achieved:
  - Find the IMU value pattern when falling down
  - Use real-time data of IMU to control send-message command (add the while loop in wechat_sending.py)
  - When the falling-down condition is satisfied, the real-time data of GPS is also retrieved from DCD hub.

Challenges remained:
  - Automatically run all the python code after Raspberry Pi is powered on
  - The website address needs to be changed everytime the IP address changes.
