#include <HTTPClient.h> // https://arduinojson.org/v6/how-to/use-arduinojson-with-httpclient/
#include <ArduinoJson.h>

#define api "http://192.168.1.2:9999"

DynamicJsonDocument apiRequest(String url) {
    DynamicJsonDocument doc(2048);

    HTTPClient http;

    http.useHTTP10(true);
    http.begin(url);
    
    int httpCode = http.GET();
 
    if (httpCode > 0) {
        Serial.println(httpCode);

        deserializeJson(doc, http.getStream());
    } else {
        Serial.println("Error on HTTP request");
    }

    http.end();

    return doc;
}

bool apiHealthy() {
    String url = String(api) + "/health";

    DynamicJsonDocument status = apiRequest(url);

    return status["status"] == "Healthy";
}

JsonArray getDrinks() {
    String url = String(api) + "/drinks";

    DynamicJsonDocument drinks = apiRequest(url);

    return drinks.as<JsonArray>();
}
