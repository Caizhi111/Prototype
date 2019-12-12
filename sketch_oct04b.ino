#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

#include <Adafruit_GPS.h>   // Adafruit GPS Library

Adafruit_GPS GPS(&Serial1); // We'll be using the Mega's serial port 1
                            // (R&TX1), but you can also use 2 and 3

// Set GPSECHO to 'false' to turn off echoing the GPS data to the Serial console
// Set to 'true' if you want to debug and listen to the raw GPS sentences
#define GPSECHO  false

/* This driver reads raw data from the BNO055

   Connections
   ===========
   Connect SCL to analog 5
   Connect SDA to analog 4
   Connect VDD to 3.3V DC
   Connect GROUND to common ground

   History
   =======
   2015/MAR/03  - First release (KTOWN)
*/

/* Set the delay between fresh samples */
#define BNO055_SAMPLERATE_DELAY_MS (500)

// Check I2C device address and correct line below (by default address is 0x29 or 0x28)
//                                   id, address
Adafruit_BNO055 bno = Adafruit_BNO055(-1, 0x28);

int LEDpin = 6;
int LEDpin2 = 2;

int delayval = 100; // delay for half a second

// the follow variables are long's because the time, measured in miliseconds,
// will quickly become a bigger number than can be stored in an int.
long time = 0;         // the last time the output pin was toggled
unsigned long debounce = 50;   // the debounce time, increase if the output flickers
int inPin = 7;         // the number of the button
int state;      // the current state of the output pin
int lastState = LOW;   // the previous reading from the input pin
int reading;           // the current reading from the input pin
unsigned long lastDebounceTime = 0;  // the last time the output pin was toggled

boolean readingData = false;
/**************************************************************************/
/*
    Arduino setup function (automatically called at startup)
*/
/**************************************************************************/

// Keeps track of whether we're using the interrupt
// off by default!
boolean usingInterrupt = false;

void setup(void)
{
  Serial.begin(115200);
  //Serial.println("Orientation Sensor Raw Data Test"); Serial.println("");

  Serial.println("Adafruit GPS library basic Parsing test!");
  // 9600 NMEA is the default baud rate for Adafruit MTK GPS's- some use 4800
  GPS.begin(9600);

  // You can adjust which sentences to have the module emit, below
  
  // Uncomment this line to turn on RMC (recommended minimum) and GGA (fix data) including altitude
  GPS.sendCommand(PMTK_SET_NMEA_OUTPUT_RMCGGA);
  // Uncomment this line to turn on only the "minimum recommended" data for high update rates!
  //GPS.sendCommand(PMTK_SET_NMEA_OUTPUT_RMCONLY);
  
  // For parsing data, anything but either RMC only or RMC+GGA is not recommended, since
  // the parser doesn't care about other sentences at this time
  
  // Set the update rate
  GPS.sendCommand(PMTK_SET_NMEA_UPDATE_1HZ);   // 1 Hz update rate
  // For the parsing code to work nicely and have time to sort through the data, and
  // print it out using anything higher than 1 Hz is not suggested 

  // Request updates on antenna status, comment out to keep quiet
  GPS.sendCommand(PGCMD_ANTENNA);

  // This code can have a timer0 interrupt go off
  // every 1 millisecond, and read data from the GPS. That makes the
  // loop code  a lot easier!
  useInterrupt(true);

  /* Initialise the sensor */
  if(!bno.begin())
  {
    /* There was a problem detecting the BNO055 ... check your connections */
    //Serial.print("Ooops, no BNO055 detected ... Check your wiring or I2C ADDR!");
    while(1);
  }

  delay(1000);

  /* Display the current temperature 
  int8_t temp = bno.getTemp();
  Serial.print("Current Temperature: ");
  Serial.print(temp);
  Serial.println(" C");
  Serial.println("");*/

  bno.setExtCrystalUse(true);

  //Serial.println("Calibration status values: 0=uncalibrated, 3=fully calibrated");

  pinMode(LEDpin, OUTPUT);
  pinMode(LEDpin2, OUTPUT);
  digitalWrite(LEDpin, LOW);
  digitalWrite(LEDpin2, LOW);

  // Ask for firmware version
  Serial1.println(PMTK_Q_RELEASE);
}

// Interrupt is called once a millisecond, looks for any new GPS data, and stores it
SIGNAL(TIMER0_COMPA_vect) {
  char c = GPS.read();
  // if you want to debug, this is a good time to do it!
#ifdef UDR0
  if (GPSECHO)
    if (c) UDR0 = c;  
    // writing direct to UDR0 is much much faster than Serial.print 
    // but only one character can be written at a time. 
#endif
}

void useInterrupt(boolean v) {
  if (v) {
    // Timer0 is already used for millis() - we'll just interrupt somewhere
    // in the middle and call the "Compare A" function above
    OCR0A = 0xAF;
    TIMSK0 |= _BV(OCIE0A);
    usingInterrupt = true;
  } else {
    // do not call the interrupt function COMPA anymore
    TIMSK0 &= ~_BV(OCIE0A);
    usingInterrupt = false;
  }
}

uint32_t timer = millis();

/**************************************************************************/
/*
    Arduino loop function, called once 'setup' is complete (your own code
    should go here)
*/
/**************************************************************************/
void loop(void)
{

  int reading = digitalRead(inPin);
  
  if (reading != lastState) {
 
      lastDebounceTime = millis();
  }
      
  if((millis() - lastDebounceTime) > debounce){
      if (reading != state){
        state = reading;
        if (state == HIGH){
            readingData = !readingData;
        }
      }
      
  }

  lastState = reading;

  if (readingData == false){
    digitalWrite(LEDpin, LOW);
    digitalWrite(LEDpin2, LOW);
  }

  if(readingData == true){
  // Possible vector values can be:
  // - VECTOR_ACCELEROMETER - m/s^2
  // - VECTOR_MAGNETOMETER  - uT
  // - VECTOR_GYROSCOPE     - rad/s
  // - VECTOR_EULER         - degrees
  // - VECTOR_LINEARACCEL   - m/s^2
  // - VECTOR_GRAVITY       - m/s^2
  imu::Vector<3> euler = bno.getVector(Adafruit_BNO055::VECTOR_EULER);
  imu::Vector<3> accelerometer = bno.getVector(Adafruit_BNO055::VECTOR_ACCELEROMETER);

  Serial.print("EULER");
  Serial.print(",");
  Serial.print(euler.x());
  Serial.print(",");
  Serial.print(euler.y());
  Serial.print(",");
  Serial.println(euler.z());

  digitalWrite(LEDpin2, HIGH);

  /* Display the floating point data 
  Serial.print("Wheelchair acceleration");
  Serial.print(",");
  Serial.print(accelerometer.x());
  Serial.print(",");
  Serial.print(accelerometer.y());
  Serial.print(",");
  Serial.println(accelerometer.z());*/

  /* Display calibration status for each sensor. 
  uint8_t system, gyro, accel, mag = 0;
  bno.getCalibration(&system, &gyro, &accel, &mag);
  Serial.print("CALIBRATION: Sys=");
  Serial.print(system, DEC);
  Serial.print(" Gyro=");
  Serial.print(gyro, DEC);
  Serial.print(" Accel=");
  Serial.print(accel, DEC);
  Serial.print(" Mag=");
  Serial.println(mag, DEC);
  */

// in case you are not using the interrupt above, you'll
  // need to 'hand query' the GPS, not suggested.
  if (! usingInterrupt) {
    // read data from the GPS in the 'main loop'
    char c = GPS.read();
     // Interest point for debugging
    if (GPSECHO)
      if (c) Serial.print(c);
  }
  
  // if a sentence is received, we can check the checksum, and then parse it...
  if (GPS.newNMEAreceived()) {
    // If we print the NMEA sentence, or data
    // we end up not listening and catching other sentences! 
    // so be very wary if using OUTPUT_ALLDATA and trying to print out data
    //Serial.println(GPS.lastNMEA());   // this also sets the newNMEAreceived() flag to false
  
    if (!GPS.parse(GPS.lastNMEA()))   // this also sets the newNMEAreceived() flag to false
      return;  // we can fail to parse a sentence in which case we should just wait for another
  }

  // if millis() or timer wraps around, we'll just reset it
  if (timer > millis())  timer = millis();

  // approximately every 2 seconds or so, print out the current GPS stats
  if (millis() - timer > 500) { 
    timer = millis(); // reset the timer 
    
    if (GPS.fix) {      //Only If there is a GPS Fix, we print out.
      
      digitalWrite(LEDpin, HIGH);
      
      Serial.print("GPS");
      Serial.print(",");
      Serial.print(GPS.latitudeDegrees, 4);
      Serial.print(", "); 
      Serial.println(GPS.longitudeDegrees, 4);
    }

    else{
      //Serial.println("GPS, no fix");
      Serial.print("GPS: no fix");
      Serial.print(",");
      Serial.print("0");
      Serial.print(", "); 
      Serial.println("0");
      
      digitalWrite(LEDpin, HIGH);
      delay(500);
      digitalWrite(LEDpin, LOW);
      delay(500);
    }
  }

  delay(BNO055_SAMPLERATE_DELAY_MS);

  }
  
}
