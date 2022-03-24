const int trigPin1 = 13;
const int echoPin1 = 12;
const int buzzer=5;
void setup() {
  // put your setup code here, to run once:
  pinMode(trigPin1,OUTPUT);
  pinMode(echoPin1,INPUT);
  pinMode(buzzer,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(trigPin1,HIGH);
  delayMicroseconds(1000);
  digitalWrite(trigPin1,LOW);
  int duration = pulseIn(echoPin1,HIGH);
  int distance = (duration/2)/29.1;
  if(distance<20){
    tone(buzzer,3000);
    delay(100);
    noTone(buzzer);
    delay(100);
  }
  else if(distance<35){
    tone(buzzer,2000);
    delay(100);
    noTone(buzzer);
    delay(1000);
  }
}
