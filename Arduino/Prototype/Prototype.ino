#define col1 13
#define col2 12
#define row1 3
#define row2 4
int SW = 8;
int pinA = 11;
int pinB = 10;
int encoderPosCount = 0;
int pinALast; int aVal;
boolean bCW;
String data;
//void Send_Byte;
void setup() {
  pinMode (pinA,INPUT); 
  pinMode (pinB,INPUT);
  pinMode (SW, INPUT);
  pinALast = digitalRead(pinA);
  Serial.begin (9600);
  pinMode (row1, INPUT_PULLUP);
  pinMode (row2, INPUT_PULLUP);
  pinMode (col1, OUTPUT);
  pinMode (col2, OUTPUT);
  digitalWrite (col1, HIGH);
  digitalWrite (col2, HIGH);
  //attachInterrupt(digitalPinToInterrupt(pinA), Encoder, RISING);
  //attachInterrupt(digitalPinToInterrupt(pinB), Encoder, RISING);
}

void loop() {
  digitalWrite (col1, LOW);
  if (digitalRead (row1) ==LOW){
    //Serial.println ("Q");
    data = "Q";
    Send_Byte ();
    
  }
  if (digitalRead (row2) ==LOW){
    data = "E";
    Send_Byte ();
  }
  digitalWrite (col1, HIGH);
  digitalWrite (col2, LOW);
  if (digitalRead (row1) == LOW){
      data = "W";
    Send_Byte ();
  }
  if (digitalRead (row2) ==LOW){
    data = "K";
    Send_Byte ();
  }
  digitalWrite (col2, HIGH);
  if (digitalRead (SW) == HIGH){
    Serial.println ("SW");
    
  }
}
/*void Encoder (){
  aVal = digitalRead(pinA);
  if (aVal != pinALast){
    if (digitalRead(pinB) != aVal) {
      encoderPosCount ++;
      bCW = true;
    }
    else {
      bCW = false;
      encoderPosCount--;
    }
    Serial.print ("Rotated: ");
    if (bCW){ 
      Serial.println ("clockwise"); 
      }
      else{ 
        Serial.println("counterclockwise"); 
        } 
        Serial.print("Encoder Position: "); 
        Serial.println(encoderPosCount);
  }
    pinALast = aVal;
}*/
void Send_Byte() {
  Serial.println (data);
  delay (300);
}
