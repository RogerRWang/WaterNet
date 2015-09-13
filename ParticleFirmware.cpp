// This #include statement was automatically added by the Particle IDE.
#include "Adafruit_DHT/Adafruit_DHT.h"
#define DHTPIN 2     // what pin we're connected to
#define DHTTYPE DHT22   // DHT 22 (AM2302)

// Connect pin 1 (on the left) of the sensor to +5V
// Connect pin 2 of the sensor to whatever your DHTPIN is
// Connect pin 4 (on the right) of the sensor to GROUND
// Connect a 10K resistor from pin 2 (data) to pin 1 (power) of the sensor

DHT dht(DHTPIN, DHTTYPE);

// -----------------------------------
// Controlling LEDs over the Internet
// -----------------------------------

// First, let's create our "shorthand" for the pins
// Same as in the Blink an LED example:
// led1 is D0, led2 is D7

int led1 = D6;
int led2 = D7;
float humidity = 0;
float tempC = 0;
float tempF = 0;

double tempFDouble = 0;
double humidityDouble = 0;
// Last time, we only needed to declare pins in the setup function.
// This time, we are also going to register our Spark function
char myIpString[24];

void setup()
{
   dht.begin();
   
   IPAddress myIp = WiFi.localIP();
   sprintf(myIpString, "%d.%d.%d.%d", myIp[0], myIp[1], myIp[2], myIp[3]);
   Spark.variable("ipAddress", myIpString, STRING);
   Spark.variable("temperature",&tempFDouble,DOUBLE);
   Spark.variable("humidity",&humidityDouble,DOUBLE);
   // Here's the pin configuration, same as last time
   pinMode(led1, OUTPUT);
   pinMode(led2, OUTPUT);

   // We are also going to declare a Spark.function so that we can turn the LED on and off from the cloud.
   Spark.function("led",ledToggle);
   // This is saying that when we ask the cloud for the function "led", it will employ the function ledToggle() from this app.

   // For good measure, let's also make sure both LEDs are off when we start:
   digitalWrite(led1, LOW);
   digitalWrite(led2, LOW);

}


// Last time, we wanted to continously blink the LED on and off
// Since we're waiting for input through the cloud this time,
// we don't actually need to put anything in the loop

void loop()
{
   // Nothing to do here
   // Wait a few seconds between measurements.
  delay(2000);
// Reading temperature or humidity takes about 250 milliseconds!
// Sensor readings may also be up to 2 seconds 'old' (its a 
// very slow sensor)
   humidity = dht.getHumidity();
   humidityDouble = humidity;
// Read temperature as Celsius
   tempC = dht.getTempCelcius();
   
// Read temperature as Farenheit
   tempF = dht.getTempFarenheit();
   tempFDouble = tempF;
  
// Check if any reads failed and exit early (to try again).
  if (isnan(humidity) || isnan(tempC) || isnan(tempF)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
}

// We're going to have a super cool function now that gets called when a matching API request is sent
// This is the ledToggle function we registered to the "led" Spark.function earlier.


int ledToggle(String command) {
    /* Spark.functions always take a string as an argument and return an integer.
    Since we can pass a string, it means that we can give the program commands on how the function should be used.
    In this case, telling the function "on" will turn the LED on and telling it "off" will turn the LED off.
    Then, the function returns a value to us to let us know what happened.
    In this case, it will return 1 for the LEDs turning on, 0 for the LEDs turning off,
    and -1 if we received a totally bogus command that didn't do anything to the LEDs.
    */

    if (command=="on") {
        digitalWrite(led1,HIGH);
        digitalWrite(led2,HIGH);
        return 1;
    }
    else if (command=="off") {
        digitalWrite(led1,LOW);
        digitalWrite(led2,LOW);
        return 0;
    }
    else {
        return -1;
    }
}

