

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

void setup() {
  Serial.begin (9600);
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
}

void loop() {
  digitalWrite (A, LOW);
  if (digitalRead (X) ==LOW){
    data = ("Q");
    Send_Byte ();
  }
  if (digitalRead (Y) ==LOW){
    data = ("W");
    Send_Byte ();
  }
    if (digitalRead (Z) ==LOW){
    data = ("E");
    Send_Byte ();
  }
  
  digitalWrite (A, HIGH);
  digitalWrite (B, LOW);
  if (digitalRead (X) == LOW){
    data = ("A");
    Send_Byte ();
  }
  if (digitalRead (Y) ==LOW){
    data = ("S");
    Send_Byte ();
  }
  if (digitalRead (Z) ==LOW){
    data = ("D");
    Send_Byte ();
  }
  
  digitalWrite (B, HIGH);
  digitalWrite (C, LOW);
  if (digitalRead (X) == LOW){
    data = ("Z");
    Send_Byte ();
  }
  if (digitalRead (Y) ==LOW){
    data = ("X");
    Send_Byte ();
  }
  if (digitalRead (Z) ==LOW){
    data = ("C");
    Send_Byte ();
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
    aState = digitalRead(encoderA); // Reads the "current" state of the outputA
   // If the previous and the current state of the outputA are different, that means a Pulse has occured
   if (aState != aLastState){   
     // If the outputB state is different to the outputA state, that means the encoder is rotating clockwise
     if (digitalRead(encoderB) != aState) { 
       counter --;
     } else {
       counter ++;
     }
     c = !c;
     if (c ==1) {
     Serial.print("Position: ");
     Serial.println(counter/2);
     }
   } 
   aLastState = aState; // Updates the previous state of the outputA with the current state
}
