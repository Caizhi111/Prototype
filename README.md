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
1. Finding out when the wheelchair falling down, how would to IMU value change. (Last week and this week)
2. Test how would the camera send video clips to the user. (This week)
3. Connecting the system with API of an instant chatting app. (whis week)

# Progress of last week
We tried to follow the tutorials to set up the internet connection between Raspberry pi and DCD hub, and the bluetooth connection between raspberry pi and Feathure. We used the example code and successfully turned on the LED.

When switching the LED to the IMU, the bluetooth connection is not working and took us almost the whole week to degug the issue.
Since our IMU will be atached to the wheelchair, Bluetooth is then not neccessary for us. We decided to used USB cable for the Serial communication between Arduino and Raspberry Pi. We have therefore hooked IMU onto Arduino mega instead. The Arduino code bno055_rotations.ino will be used. 

# .env
THING_ID=group-9-wheelchair-df49
THING_TOKEN=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE1Njk4MzA1MTMsImV4cCI6MTg4NTQxMDExMywiYXVkIjoiaHR0cHM6Ly9kd2QudHVkZWxmdC5ubDo0NDMvYXBpIn0.HxNI-eI1fiPG_rQENeHM9j6-g6SbK1NJHXZRRIQtv2qEro9dwzlN7MiPNGZtYZBABWa_U5A2PNdGNRsGRb80eVFjMDcLtjNHIBFHqZKCQEJAGY2HRXsLHJEy_hYOCjV81vmU4IKpizAhsx0HScrj1YERxPeSswTZuG4P_46hsID5EZibPxiJl96IDRcr7Mj_a2kfz9I41z1Tl3dd1DDJXifeGFvg9UQk6De-N4u1piwW8QRdSBoJHH1c4wUEcLJBt9frlFAKBGR8QJOCPH35xKCHE5KHTjYPmj8uAVH_c-w1-etTeeL5rE_OZkMppY4nTRW8YNbEU2vL1iCCEBfrMomieLz2OwrapP_1yGaEBOfj9ajlrKrUtiHycJpU7xaKzwMYILnpvL00F_GtgGxU5oQRIXhOUrj1SNPGQmx_ZMI4V_Nhi0yc_Ztz-SgYLp6Z2s4QIm5M9Z1XJ_qHg5tKsdDp_JT8bjF0WZOFvdBlo8VAQEoQOR0tk5NN68L5kWFdKsoDgREJLqVhCMFfWZCieWQC4Xt7_WgOGParOvXW3BgYDZ4Da9ssLnBIxAb2hVp4AR23DCgQma32XbxFPYE9nMQmSylcjZDZswAZqw8W6z64-y3D6C8qPzvSHzm7rxV4DvbzvvOyKCnEydvnbSbYg2LbXABXsv_d9hab8QVXryg

