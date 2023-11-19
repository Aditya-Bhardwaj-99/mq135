#include <MQ135.h>
#include <ESP8266WiFi.h>
#include <ArduinoWebsockets.h>
//#include <WebSocketClient.h>
//boolean handshakeFailed=0;
String data= "";
//char path[] = "/ws";   //identifier of this device
//const char* ssid     = "Aditya wifi";
//const char* password = "skbhardwaj";
//char* host = "192.168.1.41";  //replace this ip address with the ip address of your Node.Js server
//const int espport= 3000;
  
//WebSocketClient webSocketClient;
//unsigned long previousMillis = 0;
//unsigned long currentMillis;
//unsigned long interval=300; //interval for sending data to the websocket server in ms
// Use WiFiClient class to create TCP connections
using namespace websockets;
WebsocketsClient client;
const char* ssid = "Aditya wifi"; //Enter SSID
const char* password = "skbhardwaj"; //Enter Password
const char* websockets_server_host = "192.168.1.41"; //Enter server adress
const uint16_t websockets_server_port = 3000; // Enter server port

const int MQ135_PIN = A0; // Define the pin with the MQ135
MQ135 gasSensor = MQ135(MQ135_PIN);

void setup() {
  Serial.begin(9600); // Starts the serial communication
  Serial.println("MQ135 Gas Sensor with NodeMCU");
  WiFi.begin(ssid, password);
      
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
  }

//  wsconnect();
    bool connected = client.connect(websockets_server_host, websockets_server_port, "/ws");
    if(connected) {
        Serial.println("Connecetd!");
//        client.send("Hello Server");
    } else {
        Serial.println("Not Connected!");
    }
    
    // run callback when messages are received
//    client.onMessage([&](WebsocketsMessage message) {
//        Serial.print("Got Message: ");
//        Serial.println(message.data());
//    });
  delay(1000);
}

void loop() {

  float rzero = gasSensor.getRZero();
  float correctedRZero = gasSensor.getCorrectedRZero(20, 65); // Example values; use a DHT sensor for actual temperature and humidity
  float resistance = gasSensor.getResistance();
  float ppm = gasSensor.getPPM();
  
  // Example factors, not calibrated
  float ammonia = ppm * 0.01;
  float benzene = ppm * 0.005;
  float co2 = ppm * 0.9;
  float nitrox = ppm * 0.02;
  float alcohol = ppm * 0.004;

  Serial.printf("Ammonia: %.2f | Benzene: %.2f | CO2: %.2f | Nitrox: %.2f | Alcohol: %.2f\n",
     ammonia, benzene, co2, nitrox, alcohol);
    data = "{\"Ammonia\": "+(String)ammonia+" , \"Benzene\": "+(String)benzene+" , \"CO2\": "+(String)co2+" , \"Nitrox\": "+(String)nitrox+" , \"Alcohol\": "+(String)alcohol+"}";
    client.send(data);
    delay(200);
  delay(400); // Wait for a second to get stable readings
}
