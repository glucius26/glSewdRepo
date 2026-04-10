int potPin = A0;     // Analog pin the potentiometer is connected to
int potVal;          // Variable to store the reading
int br = 9600;       // Baud rate for Serial Monitor
int wt = 100;        // Wait time (delay) in milliseconds
const int buzzer = 10;

void setup() {
    pinMode(potPin, INPUT);    // Set the analog pin as input
    pinMode(13, OUTPUT);       // Set red LED to pin 13
    pinMode(12, OUTPUT);       // Set yellow LED to pin 12
    pinMode(11, OUTPUT);       // Set green LED to pin 11
    pinMode(buzzer, OUTPUT);   // Declares the buzzer on pin 10
    Serial.begin(br);         // Start Serial Monitor at baud rate
    Serial.println("Potentiometer reader ready");
}

void loop() {
    //digitalWrite(12, HIGH);
    //digitalWrite(11, HIGH);
    potVal = analogRead(potPin);    // Read the voltage (0-1023)

    Serial.print("Value: ");
    Serial.println(potVal);

    delay(wt);    // Small delay so the Serial Monitor isn't overwhelmed

    if (potVal >= 0 && potVal < 448) {
        digitalWrite(13, HIGH);      // Turn on red LED
        digitalWrite(12, LOW);       //Turn off yellow LED
        digitalWrite(11, LOW);         //Turn off green LED
        tone(buzzer, 800, 200);      // 500Hz beep for 200ms
        delay(1000);                  // Wait 1 second between beeps
    } else if (potVal >= 448 && potVal < 687) {
        digitalWrite(13, LOW);      // Turn off red LED
        digitalWrite(12, HIGH);     // Turn on yellow LED
        digitalWrite(11, LOW);        //Turn off green LED
        tone(buzzer, 0, 0);      // Turn off buzzer
    } else if (potVal >= 687) {
        digitalWrite(13, LOW);      // Turn off red LED
        digitalWrite(12, LOW);     // Turn off yellow LED
        digitalWrite(11, HIGH);        //Turn on green LED
        tone(buzzer, 0, 0);        // Turn off buzzer
    }
}