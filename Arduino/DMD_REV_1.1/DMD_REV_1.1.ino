

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
#define Z 7       //Defino las filas y columnas

#define encoderA 13
#define encoderB 12

 int counter = 0; 
 int aState;
 int aLastState;  //inicializo variables necesarias para el encoder

 bool c = 1;

String data;

String oled_info;
#include <Adafruit_SSD1306.h>
//#include <splash.h>
#include <Wire.h>
Adafruit_SSD1306 oled (128, 64, &Wire, -1); //librerias y variables para la pantalla OLED

String old_roll = "";


void setup() {
  Serial.begin (115200);


  pinMode (X, INPUT_PULLUP);
  pinMode (Y, INPUT_PULLUP);
  pinMode (Z, INPUT_PULLUP);
  
  pinMode (A, OUTPUT);
  pinMode (B, OUTPUT);
  pinMode (C, OUTPUT);    //Filas y columnas como entradas y salidas para el algoritmo de la matriz
  
  digitalWrite (A, HIGH);
  digitalWrite (B, HIGH);
  digitalWrite (C, HIGH); //Las filas empuezan en HIGH

  pinMode (encoderA, INPUT);
  pinMode (encoderB, INPUT);
  aLastState = digitalRead(encoderA); //Inicializo el encoder

  oled.begin (SSD1306_SWITCHCAPVCC, 0x3C);
  oled.clearDisplay(); //limpia el buffer
  oled.fillScreen (0); //Color de fondo; 0 para negro 1 para blanco
  oled.setTextSize (1.5);
  oled.setTextColor (WHITE);
  oled.display();       //Inicializo la pantalla OLED

}

void loop() {
  digitalWrite (A, LOW);      //Pongo a 0 una fila y reviso las columbas
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
  digitalWrite (B, LOW);    //Pongo a 1 la primera columna y a 0 la segunda para evitar bugs
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
    Send_Byte ();             //Reviso las columnas
  }
  
  digitalWrite (B, HIGH);
  digitalWrite (C, LOW);    //Pongo a 1 la primera columna y a 0 la segunda para evitar bugs
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
    Send_Byte ();         //Reviso las columnas
  }
  digitalWrite (C, HIGH);
  
  encoder ();     
  
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
    aState = digitalRead(encoderA); // Reviso el estado actual de A
   // Si es distinto del estado anterior es que ha ocurrido un movimiento
   if (aState != aLastState){   
     // Si A es distinto de B sabemos que se esta moviendo en la direccion de las agujas del reloj
     if (digitalRead(encoderB) != aState) { 
       counter = 1;
     } else {
       counter = 2 ;
     }
     c = !c;
     if (c ==1) {
     Serial.println(counter);
     }
   }                            // Esta pieza de codido minimiza los rebotes del hardware para obtener una lectura mas limpia

   aLastState = aState; // Acualiza el estado anterior
}


void serialEvent() { //Solo entra aqui cuando el buffer del puerto serie tiene informacion
  oled_info = Serial.readString();//.toInt ();    //Guardo la informacion del buffer en un string
  int split = oled_info.indexOf ('r');            
  String dice = oled_info.substring (0, split);
  String roll = oled_info.substring (split+1);
  String ultimo_roll = ("Ultima: " + dice + ' ' + roll);//Modifico ese string para poder mostrar los datos correctamente
  oled.clearDisplay ();
  oled.setCursor (0, 20);
  oled.print (ultimo_roll);
  Serial.print (ultimo_roll);
  Serial.println ("Recived"); //Acualizo la pantalla

  oled.setCursor (0, 40);
  oled.print (old_roll);
  oled.display();     //Pinto en la pantalla
  old_roll = ("Anterior: " + dice + ' ' + roll); //Acutualizo el resto de strings
  Serial.println ("Printed");
  
}
