# Prototype
Prototype connected products tudelft group 9
By zhicai Ryan

# Design Brief Navigation system for Wheelshair users
This navigation system specially designed for the wheelchair users to find the most suitable way to the wanted destination. It helps to select the ideal route based on the feedback of the road conditions and the user experience from other users.

# Selection of Sensors and Actuators
Sensors: Button, IMU, GPS
| Actuator: LED/Buzzer, Camera, Skype message API

# IoT Architecture
  ![Architecture](https://lh3.googleusercontent.com/Ak5GyxKLRAY5n1n1s7cVBH04zdIv1LubZDKJxu0HcEB4ZD_f8oOE-RkgyqPU4WU-H4Oc7uDuEcLphTrGfIvccp7IqsIbDIQ57iLKLZex3Fs0Y4o4zY0UQLx7iA4OtLxWUz3wCbuE4Rh3B0BWGoLtBFtY-LyJbYugFCFWQDO5hsfTQMHmAxlBUih6Jce8T8HZy0RGXD9DaqNZ9h50N_UHCmrX9oIJtLcxZUvqQnmywFh44e2ty-N-dDT_QAJ7n0WSCKyCaD3yvKEto5KRt2y2Sy42EWv92R2W9mZNFV5PhpYX6g8E9k1UcT2QogNkDb92WT-OKm63C-mcQ_svwmJKfgMSqW8YG8zYBy1xclBl7My_2_cRume2WrA4e3GOOL7oaHENEwe9n9jXzDhZ1eJP2aciPB9u2wiFmKjLHn9vUpOJVsj2hEs6SfOEK1l09kzL9imnA_dG6ZSHBEyxVPUs4v44WvrkDraRr-UZ2C8FaCrsskybmwK8Io4_13N3wX6X3YmAieQXYI8foTc7wARacjwzgQhIhkSSBGa-3kCE48cUZE2k2P9AkQWKh6iXx-WZf49Rob4sYGddzDzX97LVR-eLH-EdENyF2uYnzGykY2DzUfxNwCdeB_UtLxFoSB0dz0kXCczEd3T3gXm7izbrENFO-4ezhc7ux8UWztQQVgA9s6PrfuVdgaA=w1570-h883-no)

# List of testing items
1. Finding out IMU value pattern when falling down happens, and set up GPS sensor. (week 1.3 & 1.4)
2. Test how would the camera send video clips to the user. (since week 1.3......)
3. Connecting the system with API of an instant chatting app. (since week 1.3.......)

# week 1.1
Brainstorm and decided design direction. (see file Inter-connected wheelchair.pdf)

# week 1.2
Followed tutorial connecting via bluetooth. The IMU data can be sent to Raspberry Pi via bluetooth, and the data can also be checked in the mobile App, eBeacon.

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
We tried to follow the tutorials to set up the internet connection between Raspberry pi and DCD hub, and the bluetooth connection between raspberry pi and Feathure. We used the example code and successfully turned on the LED.

When switching the LED to the IMU, the bluetooth connection is not working and took us almost the whole week to degug the issue.
Since our IMU will be atached to the wheelchair, Bluetooth is then not neccessary for us. We decided to used USB cable for the Serial communication between Arduino and Raspberry Pi. We have therefore hooked IMU onto Arduino mega instead. The Arduino code bno055_rotations.ino will be used.

We figured out the api for wechat. We are able to send message to a specific people via api. One problem is that to log in wechat, we need to scan the QR code, which means we probably need a screen connected to raspberry pi.

# week 1.4


# .env
THING_ID=my1wheelchair-b5a0
THING_TOKEN=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1NzAxNjgyNzIsImV4cCI6MTg4NTc0Nzg3MiwiYXVkIjoiaHR0cHM6Ly9kd2QudHVkZWxmdC5ubDo0NDMvYXBpIn0.KldzQIk2U8LDUSyc_m7PMZgbWoNeU9BWcpJqviDVnAKc48S66AtATXZZrA5efkIJG5aRZj8DXQcRhBaaPNrLbcE8osWuivHWW9vf6m54YouAVE2Q9Tyxg5KiApmTUo7FvY_EehlGdFuba93DT4n66Izf1vOMQRbnPPlgUDGB0WuIrnnkST5p7SZ5PFPgFu-LAjVjUKnTUoAIElp169e2eJRupudnuOYVYy68ToyNBqdMuT-nEPBrIfnhFVno31hg04xhiOWrnxYEOSmJBh_1SWXbGxlUlsN48jSqz6E_EKrQ_3xbVu_48wenSRKP_20Bm1hXKI5bIQ1Bi1jLlT00k1iwOJD3wDlDbqSyuFaRi54CtX4z7Uso5bX-l7p7SUjhUwC2aS51-SKTiVVx1TtmxGlQtu66oIl9ul1M6K5TON7MeIur5_FbanAHd8MtcdHRM-7Da5S4utZ8Cf6I0TeAwb-sxm16GtReLJnh2haaISALL1CujHdsiWwKMeXtlSXZgRTQOCsRVeXQcbk3BNPr7e4EmHgpg5J-9z02bFp9fUwhx5E2g7ZaxyffbG7jUpJ4rrPDyLBJFNYpzrQFEM_3Eg6AEZh4IB0O6TdKcq3ykafefXLkHrZK183RCd6HY3JVfThQEpT0g2hpz5ioMbaLJOQVUft71vUpOMiIY8L_6h4

Hey group 9, you should be able to login with:
user: group9@test.test
password: group9

your thing id (also visible on the hub) is dcd:things:my-test-thing-556e
your token is
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1NzA0MzYwODgsImV4cCI6MTg4NjAxNTY4OCwiYXVkIjoiaHR0cHM6Ly9kd2QudHVkZWxmdC5ubDo0NDMvYXBpIn0.CgFqOdt-c2pNvReLZxhILpjr_yF1BnEJzBfvY2Nkc0FCnlqI_KjUUZ0YWDjoml5Ocfhmmg3xUnoaQS8QA6PnaO-kvFQ6cgCg-m2RYSO8_YVhSdQ13_eM7xtfLMbivkPJn3XVNXjJXy7pWF7w6sh8mhkjYHns6QqDkDnAQsgE4meEvF5jlUQS-X-fkWidxcLBWdcZP6hmQQ6YYQAeh6sph8Vr1g1hcDVtQs8H0Iicu4y_8l6vKZBZQm_PnpKCf-bdPDJgOITO8j9nOv8y9RE4Mpa7SrfEBEamSdbK7tb7PPt-57NmHTDmp5K_y-7PoekbFOuIKRJ-M7wY8oBa5ulwy6j1-UKZ4PJBga8u1HgKAhCAcQa5xsWLOtS7WB-0RwdklH3PANMaXYSd3IYVz-p14BKtoey4DsI1wPUtCKdGq5mHOi9S3dTe8Ubh6md44DhiyfvG-nH81mYk7kNFGBlvgs5F-DlTBszva9fuwYeIs_B0ChLN97F1LnLLTHw_Xl6IIiaMZIDUTqqejEliZzQqtNyW88rr6f4GXD94AN1l97Chz5l768yDWQl_FWJH_37r-ow6Iwxb6aT8kc1-y_JFBr5hYTigSoFvZpOxzKNqpR5CAQjh608ZNogAL7UVs3gt2_yisU7-fj5uce3MgivczBt28E1ACLphtfexOoUvXPw
