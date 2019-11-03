# Prototype
ID 5415 Prototyping connected products, IDE faculty, TU Delft
By Group 9: Zhi Cai, Yiling Liu, Yufei He

# Design Context
---------------------------------------Add image of Design Context--------------------------------------------

# Design Brief
Our team aims to create an alarming system for the care givers of the wheelchair users. It detects and records fall-down accidents of the wheelchair that may be risky for the users during outdoor activities, which enables their care givers to receive the notification and location, thus react to the situation in time.

# Selection of Sensors and Actuators
- Sensors: Button, IMU, GPS
- Actuators: LED, Camera, Web page, Instant Messager(Wechat)
- Cloud Server: DCD Hub
- Others: Arduino Mega, Raspberry Pi, Power bank

# IoT Architecture
---------------------------------------Add image of IoT Architecture--------------------------------------------

# List of testing items
1. Transfer IMU and GPS data to the cloud server.
2. Build a web page to review the 30s video.
3. Only store the latest 30s video, and transfer it to the web page.
4. Find out IMU value pattern when falling down happens.
5. Connect the system with API of an instant messager. 
6. When falling down happens, automatically send the messages to designated people via the instant messager.

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

Other potential design directions:
- Navigation system for Wheelshair users
A navigation system specially designed for the wheelchair users to find the most suitable way to their destination. It helps to select the ideal route based on the feedback of the road conditions and the user experience from other users.
- 

# week 1.2
Changes in the IoT structure, we use:
  - a physical button to turn on/off the device instead of automatical switch enabled by FSR
  - IMU instead of MPU
  - University WIFI instead of SMS module for prototyping purpose
  - API to instant messagers to send emergency messages to care givers (whatsapp, wechat....)

The challenges we have:
  - Fall-down detection condition for IMU code
  - set up camera and refresh the footage every 30s
  - trigger data transition stored in Raspberry Pi (GPS and 30s video footage) from Pi to cloud
  - notification

# week 1.3
We tried to follow the tutorials to set up the internet connection between Raspberry pi and DCD hub.

When switching the LED to the IMU, the bluetooth connection is not working and took us almost the whole week to degug the issue.
Since our IMU will be atached to the wheelchair, Bluetooth is then not neccessary for us. We decided to used USB cable for the Serial communication between Arduino and Raspberry Pi. We have therefore hooked IMU onto Arduino mega instead. The Arduino code bno055_rotations.ino will be used.

We figured out the api for wechat. We are able to send message to a specific people via api. One problem is that to log in wechat, we need to scan the QR code, which means we probably need a screen connected to raspberry pi.

# week 1.4


# week 1.5


# week 1.6


# week 1.7
