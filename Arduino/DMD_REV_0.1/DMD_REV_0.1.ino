

/*#define PB0 8          // Identificamos los pines de salida del ARDUINO UNO con nombres 
#define PB1 9     
#define PB2 10 
#define PB3 11 
#define PB4 12 
#define PB5 13 
#define PD2 2 
#define PD3 3

#define PD7 7 
#define PC0 14 
#define PC1 15 
#define PC2 16 
#define PC3 17 
#define PC4 18 
#define PC5 19 

#define A PD2
#define B PD3
#define C PD4
#define X PD5
#define Y PD6
#define Z PD7*/

#define A 2
#define B 3
#define C 4
#define X 5
#define Y 6
#define Z 7

#define encoderA 13
#define encoderB 12

 int counter = 0; 
 int aState;
 int aLastState; 

 bool c = 1;

String data;

String oled_info;
#include <Adafruit_SSD1306.h>
//#include <splash.h>
#include <Wire.h>
Adafruit_SSD1306 oled (128, 64, &Wire, -1);

String old_roll = "";


void setup() {
  Serial.begin (115200);
  //pinMode (row1, INPUT_PULLUP);
  //pinMode (row2, INPUT_PULLUP);

  pinMode (X, INPUT_PULLUP);
  pinMode (Y, INPUT_PULLUP);
  pinMode (Z, INPUT_PULLUP);
  
  //pinMode (col1, OUTPUT);
  //pinMode (col2, OUTPUT);

  pinMode (A, OUTPUT);
  pinMode (B, OUTPUT);
  pinMode (C, OUTPUT);
  
  digitalWrite (A, HIGH);
  digitalWrite (B, HIGH);
  digitalWrite (C, HIGH);

  pinMode (encoderA, INPUT);
  pinMode (encoderB, INPUT);
  aLastState = digitalRead(encoderA); 

  oled.begin (SSD1306_SWITCHCAPVCC, 0x3C);
  oled.clearDisplay(); //limpia el buffer
  oled.fillScreen (0); //Color de fondo; 0 para negro 1 para blanco
  oled.setTextSize (1);
  oled.setTextColor (WHITE);
  oled.display();

  
  
}

void loop() {
  digitalWrite (A, LOW);
  if (digitalRead (X) ==LOW){
    data = ("Q");
    Send_Byte ();
  }
  if (digitalRead (Y) ==LOW){
    data = ("A");
    Send_Byte ();
  }
    if (digitalRead (Z) ==LOW){
    data = ("Z");
    Send_Byte ();
  }
  
  digitalWrite (A, HIGH);
  digitalWrite (B, LOW);
  if (digitalRead (X) == LOW){
    data = ("W");
    Send_Byte ();
  }
  if (digitalRead (Y) ==LOW){
    data = ("S");
    Send_Byte ();
  }
  if (digitalRead (Z) ==LOW){
    data = ("X");
    Send_Byte ();
  }
  
  digitalWrite (B, HIGH);
  digitalWrite (C, LOW);
  if (digitalRead (X) == LOW){
    data = ("E");
    Send_Byte ();
  }
  if (digitalRead (Y) ==LOW){
    data = ("D");
    Send_Byte ();
  }
  if (digitalRead (Z) ==LOW){
    data = ("C");
    Send_Byte ();
  }
  digitalWrite (C, HIGH);
  
  encoder ();
  //printOLED();
  
  if (digitalRead (11) == 0){
    data = ("Pressed!");
    Send_Byte ();
  }
}

void Send_Byte() {
  Serial.println (data);
  delay (200);
}

void encoder (){
    aState = digitalRead(encoderA); // Reads the "current" state of the outputA
   // If the previous and the current state of the outputA are different, that means a Pulse has occured
   if (aState != aLastState){   
     // If the outputB state is different to the outputA state, that means the encoder is rotating clockwise
     if (digitalRead(encoderB) != aState) { 
       counter = 1;
     } else {
       counter = 2 ;
     }
     c = !c;
     if (c ==1) {
     Serial.println(counter);
     }
   } 

   aLastState = aState; // Updates the previous state of the outputA with the current state
}

void printOLED() {
  if (Serial.available () > 0){
     oled_info = Serial.readString().toInt (); 
     Serial.println (oled_info);
     Serial.println ("Recived");
       oled.clearDisplay ();
  oled.setCursor (51, 27);
  oled.print (oled_info);
  oled.display();
  Serial.println ("Printed");
    
  }
  
}

void serialEvent() {
  oled_info = Serial.readString();//.toInt (); 
  int split = oled_info.indexOf ('r');
  String dice = oled_info.substring (0, split);
  String roll = oled_info.substring (split+1);
  String ultimo_roll = ("Ultima: " + dice + ' ' + roll);
  oled.clearDisplay ();
  oled.setCursor (0, 20);
  oled.print (ultimo_roll);
  Serial.print (ultimo_roll);
  Serial.println ("Recived");

  oled.setCursor (0, 40);
  oled.print (old_roll);
  oled.display();
  old_roll = ("Anterior: " + dice + ' ' + roll); 
  Serial.println ("Printed");
  
}
