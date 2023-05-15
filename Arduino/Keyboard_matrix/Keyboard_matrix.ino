#define col1 13
#define col2 12
#define row1 3
#define row2 4
void setup() {
  Serial.begin (9600);
  pinMode (row1, INPUT_PULLUP);
  pinMode (row2, INPUT_PULLUP);
  pinMode (col1, OUTPUT);
  pinMode (col2, OUTPUT);
  digitalWrite (col1, HIGH);
  digitalWrite (col2, HIGH);
}

void loop() {
  digitalWrite (col1, LOW);
  if (digitalRead (row1) ==LOW){
    Serial.println ("Q");
  }
  if (digitalRead (row2) ==LOW){
    Serial.println ("E");
  }
  digitalWrite (col1, HIGH);
  digitalWrite (col2, LOW);
  if (digitalRead (row1) == LOW){
    Serial.println ("W");
  }
  if (digitalRead (row2) ==LOW){
    Serial.println ("K");
  }
  digitalWrite (col2, HIGH);

}
