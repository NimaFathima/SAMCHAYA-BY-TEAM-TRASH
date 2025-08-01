#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <DHT.h>

// --- WiFi & Server Config ---
const char* ssid = "Sakhil";
const char* password = "sakhil@1234";
const char* serverIp = "192.168.246.176"; // Your backend server IP
const int serverPort = 5000;             // Your backend server port

// --- Pin Assignments ---
#define DHTPIN D4
#define DHTTYPE DHT11
#define IR_SENSOR_PIN D5

DHT dht(DHTPIN, DHTTYPE);

unsigned long previousSendTime = 0;
const unsigned long sendInterval = 60000; // 1 minute in milliseconds

void setup() {
  Serial.begin(115200);
  delay(10);

  dht.begin();
  pinMode(IR_SENSOR_PIN, INPUT);

  Serial.println();
  Serial.print("Connecting to WiFi: ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi connected.");
  Serial.print("ESP IP address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  int irState = digitalRead(IR_SENSOR_PIN);

  if (irState == LOW) { 
    // Object is detected at ~8cm, send data every 1 min
    unsigned long currentMillis = millis();

    if (currentMillis - previousSendTime >= sendInterval) {
      previousSendTime = currentMillis;

      float temperature = dht.readTemperature();

      if (isnan(temperature)) {
        Serial.println("Failed to read from DHT11 sensor!");
      } else {
        Serial.printf("Cup detected! Temperature: %.1f°C\n", temperature);

        // Determine message based on temperature range
        String tempMessage;
        if (temperature >= 45.0 && temperature <= 85.0) {
          tempMessage = "hot";
        } else if (temperature < 30.0) {
          tempMessage = "cold";
        } else {
          tempMessage = "moderate";
        }

        sendToBackend(tempMessage);
      }
    }
  } else {
    // No cup detected, reset timer so it will send immediately on next detection
    previousSendTime = 0;
    Serial.println("No cup detected.");
  }

  delay(100); // small delay for stability
}

void sendToBackend(String tempMessage) {
  if (WiFi.status() == WL_CONNECTED) {
    WiFiClient client;
    HTTPClient http;

    String serverUrl = "http://" + String(serverIp) + ":" + String(serverPort) + "/trigger?";
    serverUrl += "temp_status=" + tempMessage;

    Serial.print("Sending GET request to: ");
    Serial.println(serverUrl);

    http.begin(client, serverUrl);
    int httpCode = http.GET();

    if (httpCode > 0) {
      Serial.printf("HTTP Response code: %d\n", httpCode);
    } else {
      Serial.printf("GET request failed: %s\n", http.errorToString(httpCode).c_str());
    }

    http.end();
  } else {
    Serial.println("WiFi not connected. Cannot send data.");
  }
}
