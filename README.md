## Overview
CryptoTelBot is a multi-functional project that includes a **Telegram Bot**, aimed at providing streamlined access to cryptocurrency data and insights.

## Features
- **Telegram Bot**: Interact with cryptocurrency data directly via Telegram.
- **API**: A standalone API to fetch real-time cryptocurrency prices and information.
- **Parser**: A robust parser to extract data from cryptocurrency exchanges and other sources.

##Bot examples
**Main Menu**
---
![image1](https://i.imgur.com/xreZcBT.png)
---
**Get values for all currencies**
---
![image2](https://i.imgur.com/AaO4UFH.png)
---
**Get certain currency value**
---
![image3](https://i.imgur.com/2X1UyC4.png)
---
**Subscribe to currency updates**
---
![image4](https://github.com/user-attachments/assets/eade3b9b-1ea1-4547-95f4-081f9cce3610)
---
## Api example
---
The main page will return a JSON file with all currencies and their values. It is important to note that if the parsing.py file is not run, these values will not be updated
---
http://127.0.0.1:5000/:
---
![image](https://github.com/user-attachments/assets/d211947c-e83e-45f8-9ff6-40dff9c1be04)
---
If we want to get the value of a specific currency, we should add its tag after the slash in the URL. For example, 127.0.0.1:5000/btc.
(In this case, we don't need to have parsing.py running.
---
http://127.0.0.1:5000/btc:
---
![image](https://github.com/user-attachments/assets/bada9861-3f65-424e-ace2-6ec21062a57e)
