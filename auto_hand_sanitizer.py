#include <Servo.h>

// Define pins for ultrasonic sensor and servo motor
const int trigPin = 9;  // Trigger pin for ultrasonic sensor
const int echoPin = 10; // Echo pin for ultrasonic sensor
const int servoPin = 8; // Servo motor pin

Servo myServo; // Create a servo object

// Variables for ultrasonic sensor
long duration;
int distance;

// Threshold distance for hand detection (in cm)
const int thresholdDistance = 10;

void setup() {
  // Initialize serial communication
  Serial.begin(9600);

  // Set pin modes
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  // Attach servo to the servo pin
  myServo.attach(servoPin);
  myServo.write(0); // Set servo to initial position (sanitizer not dispensed)
}

void loop() {
  // Measure distance using ultrasonic sensor
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH); // Read the echo pulse duration
  distance = duration * 0.034 / 2;  // Convert duration to distance in cm

  // Print distance to serial monitor for debugging
  Serial.print("Distance: ");
  Serial.println(distance);

  // Check if hand is within the threshold distance
  if (distance <= thresholdDistance && distance > 0) {
    dispenseSanitizer(); // Dispense sanitizer
    delay(2000);         // Wait for 2 seconds before next detection
  }
}

// Function to dispense sanitizer
void dispenseSanitizer() {
  myServo.write(180); // Rotate servo to dispense sanitizer
  delay(500);         // Wait for 0.5 seconds
  myServo.write(0);   // Return servo to initial position
}
