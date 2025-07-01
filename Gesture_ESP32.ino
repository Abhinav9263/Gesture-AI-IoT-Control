#include <WiFi.h>
#include <WebServer.h>

const char* ssid = "AirFiber-e54e72";
const char* password = "XKYX3uQs2f6yFRL6";

WebServer server(80);

#define LED_PIN 2
#define MOTOR_PIN 4

void setup() {
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
  pinMode(MOTOR_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);
  digitalWrite(MOTOR_PIN, LOW);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) delay(500);
  Serial.println(WiFi.localIP());

  server.on("/on", []() {
    digitalWrite(LED_PIN, HIGH);
    digitalWrite(MOTOR_PIN, HIGH);
    server.send(200, "text/plain", "LED + Motor ON");
  });

  server.on("/off", []() {
    digitalWrite(LED_PIN, LOW);
    digitalWrite(MOTOR_PIN, LOW);
    server.send(200, "text/plain", "LED + Motor OFF");
  });

  server.begin();
}

void loop() {
  server.handleClient();
}
