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
![greenLight](https://lh3.googleusercontent.com/rNjc5xhIxvdAsmhu81ta1KBaB9rxc7ReN7kaM3VllXBXfxmiJrCXVoTS_eTbcyXV0DRNfYePTcxuBbGZHuerl_KJpssZoK4JgBO1fkosKozJ6jtz8ygwSljxdpyUwnMCuKIHx5e0Ks_NF9-mnkIaL9-8gVfuaSr_KVb56TAnIA8H-4s-oJw7wQAtN4cxsWbqdSSMsdinN8oZdNMFaZuPCY6KpKhKZ8zZ9HFXDvk3M-EG_hC8X3QwC5V_MDTSSA8R8zYiT0l8cY0ifU2oh3k58SwqcWxc7bOGDqN7AFJKWnx15di3w4Q0rs75yHZ63Mkt4jxcb5c3QLPKjQBUyBx-Nky8WB-UILgUAcq2TEDX-q8blhSlMVs1vdLi4BUNBC0LbtW9IhhasvJRA9pXN3JPgY7eWjc_cZKwlLr2rqQkQvgSaaKfcApGtWsBfHu2VBz_MAgPr4AudZxDV6Zrab-Cjv9wVyHQ6fA2MEzpNa3rxYu-iY3r7A6tNg33f9ylA5Zw0Yi06d33KFfWyHQj__I0k8kAboRPrx0TeigSq522aRTqH0TV0T0u5qCQbCyGs4oRcU7Qv2igw_XNAIT7TW7tIBCZQ6A_cG--dM0Nx505eACrbkpno2PopcWk42_qNbH3nTtEhGuUxKJ1ua3QUorCpZdcLo99sCM1zVJoJx3LKXRDRk3BtBsagQo=w1124-h843-no)
When switching the LED to the IMU, the bluetooth connection is not working and took us almost the whole week to degug the issue.
Since our IMU will be atached to the wheelchair, Bluetooth is then not neccessary for us. We decided to used USB cable for the Serial communication between Arduino and Raspberry Pi. We have therefore hooked IMU onto Arduino mega instead. The Arduino code IMU.ino will be used. 
