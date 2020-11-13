#include <HTTPClient.h> // https://arduinojson.org/v6/how-to/use-arduinojson-with-httpclient/
#include <ArduinoJson.h>

#define api "http://192.168.1.163:9999"

DynamicJsonDocument apiRequest(int capacity, String url) {
    DynamicJsonDocument doc(capacity);

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

    DynamicJsonDocument status = apiRequest(JSON_OBJECT_SIZE(1) + 80, url);

    return status["status"] == "Healthy";
}

Drink * getDrinks() {
    String url = String(api) + "/drinks";

    DynamicJsonDocument doc = apiRequest(JSON_ARRAY_SIZE(5) + 5 * JSON_OBJECT_SIZE(5) + 80, url);

    Drink drinks[3];

    int i = 0;

    for (JsonVariant v : doc.as<JsonArray>()) {
        drinks[i] = Drink {
           v["name"].as<const char*>()
        };

        i++;
    }

    return drinks;
}
