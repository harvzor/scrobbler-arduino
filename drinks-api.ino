#include <HTTPClient.h> // https://arduinojson.org/v6/how-to/use-arduinojson-with-httpclient/
#include <ArduinoJson.h>

#define api "http://192.168.1.2:9999"

JsonArray getDrinks() {
    String url = String(api) + "/drinks";
    JsonArray drinksArray;

    HTTPClient http;

    http.useHTTP10(true);
    http.begin(url);
    
    int httpCode = http.GET();
 
    if (httpCode > 0) {
        Serial.println(httpCode);

        DynamicJsonDocument drinks(2048);
        
        deserializeJson(drinks, http.getStream());

        drinksArray = drinks.as<JsonArray>();
    } else {
        Serial.println("Error on HTTP request");
    }

    http.end();

    return drinksArray;
}
