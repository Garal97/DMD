
#include <Adafruit_SSD1306.h>
//#include <splash.h>
#include <Wire.h>
Adafruit_SSD1306 oled (128, 64, &Wire, -1);
int contador=0;
String Cadena1= "Contador: ";
void setup() {
  oled.begin (SSD1306_SWITCHCAPVCC, 0x3C);
  oled.clearDisplay(); //limpia el buffer
  oled.fillScreen (0); //Color de fondo; 0 para negro 1 para blanco
  oled.setTextSize (1);
  oled.setTextColor (WHITE);
}

void loop() {
  oled.setCursor (51, 27);
  oled.print ("Hola");
  oled.setRotation (1);
  oled.display ();
}
