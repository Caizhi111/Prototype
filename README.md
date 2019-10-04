# Prototype
Prototype connected products tudelft group 9
By zhicai Ryan

# Design Brief Navigation system for Wheelshair users
This navigation system specially designed for the wheelchair users to find the most suitable way to the wanted destination. It helps to select the ideal route based on the feedback of the road conditions and the user experience from other users.

# Selection of Sensors and Actuators
Sensors: Button, IMU, GPS
| Actuator: LED/Buzzer, Camera, Skype message API

# IoT Architecture
  ![Architecture](https://lh3.googleusercontent.com/LzEYbPEtdMqo06LO1q7WaU1OoMFI5NcEfIEbCoFsny6N7CpCJrI5PK2MvOI39yQOq73Vdqml7Cmq6lu_bdum3TU1zY-_SOM3JrPZwoX5sJmx5KrjBLtWr51oUEO9dp3Or6KtW-W1AihBCWtQWeHu6M89ouCuGxAyVqQrPM1hAcvTqR9m6FFWOyBdKjrQd4CALYHKuc9lleUn4dOX6V8ihxexNsej6KkCn41s-NrESDR4B_V0UOPH1Uws4tZKxYpyBWrjy3AzKlI1O6r_4g6JKPTfgQKnFDO6t3UXcmPO_TLktjGkRraaWUpV6MVthpwcZJ5vSkXY3D9NRw952x2EXC-wrxooMzbP34UK2eXdCtIF8B_4tMav3u_GaqdB77ZFUrWrKhzWOW9YeP0NfcRzMJrSOr37cVfxKXd0pONmSIFtkpRqpTiSUx5mRpUcSJNC-WZ2HOfcbh1GTKx3EsT8sptl7RNq-mMVGC2fnBCsF4O6e_mItfec7tLQh5QJabg0rEHFWRxErFhuu3rmqedEvppwtzi7YeZUM04zuVsdKRg5_8jG1zCOxdgSEykAvzJIo5gCb_wupoC_VZg8yNXtMi1lbVR4Glpp-r5A7xttaj_kf3XbGqdL7XrftdbIPr2F6v0xeyeA2fKk69LZxFQyeQY-CzIyGESnu15_nzwThl46wNDijD7lAn8=w1499-h843-no)

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

# week 1.4


# .env
THING_ID=my1wheelchair-b5a0
THING_TOKEN=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1NzAxNjgyNzIsImV4cCI6MTg4NTc0Nzg3MiwiYXVkIjoiaHR0cHM6Ly9kd2QudHVkZWxmdC5ubDo0NDMvYXBpIn0.KldzQIk2U8LDUSyc_m7PMZgbWoNeU9BWcpJqviDVnAKc48S66AtATXZZrA5efkIJG5aRZj8DXQcRhBaaPNrLbcE8osWuivHWW9vf6m54YouAVE2Q9Tyxg5KiApmTUo7FvY_EehlGdFuba93DT4n66Izf1vOMQRbnPPlgUDGB0WuIrnnkST5p7SZ5PFPgFu-LAjVjUKnTUoAIElp169e2eJRupudnuOYVYy68ToyNBqdMuT-nEPBrIfnhFVno31hg04xhiOWrnxYEOSmJBh_1SWXbGxlUlsN48jSqz6E_EKrQ_3xbVu_48wenSRKP_20Bm1hXKI5bIQ1Bi1jLlT00k1iwOJD3wDlDbqSyuFaRi54CtX4z7Uso5bX-l7p7SUjhUwC2aS51-SKTiVVx1TtmxGlQtu66oIl9ul1M6K5TON7MeIur5_FbanAHd8MtcdHRM-7Da5S4utZ8Cf6I0TeAwb-sxm16GtReLJnh2haaISALL1CujHdsiWwKMeXtlSXZgRTQOCsRVeXQcbk3BNPr7e4EmHgpg5J-9z02bFp9fUwhx5E2g7ZaxyffbG7jUpJ4rrPDyLBJFNYpzrQFEM_3Eg6AEZh4IB0O6TdKcq3ykafefXLkHrZK183RCd6HY3JVfThQEpT0g2hpz5ioMbaLJOQVUft71vUpOMiIY8L_6h4
