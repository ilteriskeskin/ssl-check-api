# ssl-check-api

This api returns the ssl expiration date of the hostname. Default port 443.

Request Url: [https://79w38kh2pa.execute-api.eu-central-1.amazonaws.com/](https://79w38kh2pa.execute-api.eu-central-1.amazonaws.com/)

---

## Postman Screenshot

![Postman Screenshot](/screenshot/ss1.png "Postman Screenshot")

---

## How to send request?

Bash:
```Bash
curl --location --request POST 'https://79w38kh2pa.execute-api.eu-central-1.amazonaws.com/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "hostname": "stackoverflow.com",
    "port": "443"
}'
```

---

Python:
```Python
import requests
import json

url = "https://79w38kh2pa.execute-api.eu-central-1.amazonaws.com/"

payload = json.dumps({
  "hostname": "stackoverflow.com",
  "port": "443"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

---

Go:
```Go
package main

import (
  "fmt"
  "strings"
  "net/http"
  "io/ioutil"
)

func main() {

  url := "https://79w38kh2pa.execute-api.eu-central-1.amazonaws.com/"
  method := "POST"

  payload := strings.NewReader(`{
    "hostname": "stackoverflow.com",
    "port": "443"
}`)

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, payload)

  if err != nil {
    fmt.Println(err)
    return
  }
  req.Header.Add("Content-Type", "application/json")

  res, err := client.Do(req)
  if err != nil {
    fmt.Println(err)
    return
  }
  defer res.Body.Close()

  body, err := ioutil.ReadAll(res.Body)
  if err != nil {
    fmt.Println(err)
    return
  }
  fmt.Println(string(body))
}
```