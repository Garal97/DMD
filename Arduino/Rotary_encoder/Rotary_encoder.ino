/*#define DT 11
#define CLK 12
#define SW 13
int position_count = 0;
bool CLK_current;
bool CLK_last;

void setup() {
  pinMode (DT, INPUT_PULLUP);
  pinMode (CLK, INPUT_PULLUP);
  pinMode (SW, INPUT_PULLUP);
  CLK_last = digitalRead (CLK);
  Serial.begin (9600);
}

void loop() {
  CLK_current = digitalRead (CLK);
  if (CLK_current != CLK_last) {
    if (digitalRead (DT != CLK_current)){
      position_count++;
    }
    else {
      position_count--;
    }
    
  }
  Serial.println (position_count);
}*/
int pinA = 12;
int pinB = 11;
int encoderPosCount = 0;
int pinALast; int aVal;
boolean bCW;
void setup() { 
  pinMode (pinA,INPUT); 
  pinMode (pinB,INPUT);
  pinALast = digitalRead(pinA);
  Serial.begin (9600);
}
void loop() { 
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
}
