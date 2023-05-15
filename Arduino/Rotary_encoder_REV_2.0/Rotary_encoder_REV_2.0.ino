#define encoderA 13
#define encoderB 12

 int counter = 0; 
 int aState;
 int aLastState; 

  bool c=1;

void setup() {
   pinMode (encoderA, INPUT);
   pinMode (encoderB, INPUT);
   Serial.begin (9600);
   aLastState = digitalRead(encoderA); 
   Serial.println ("Configured!!");
}

void loop() {


    aState = digitalRead(encoderA); // Reads the "current" state of the outputA
   // If the previous and the current state of the outputA are different, that means a Pulse has occured
   if (aState != aLastState){
      Serial.println ("Here");     
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
