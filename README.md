[![author](https://img.shields.io/badge/author-feliperoll-purple.svg)](https://www.linkedin.com/in/felipe-roll/)

# Inspired by: [Email Automation](https://www.youtube.com/watch?v=gOn0yw6k6u4&list=LL&index=23&t=6265s)

# Project Overview: 
<b>This project aims to gather information about shares of a certain company and send some of this information to someone on an email automatically</b>.

# Code and Resources used:

* **python = "^3.12"**
* **yfinance = "^0.2.41"**
* **matplotlib = "^3.9.1.post1"**
* **pyautogui = "^0.9.54"**
* **pandas = "^2.2.2"**

# How to use
* Create a virtual enviroment using poetry;
* Install the libraries by running ```poetry install```;
* Make sure you are logged in on *Gmail*;
* Change *destinatario* content to the email of the person you want to send the email to;
* Change *assunto* content to the desired subject of the email;
* CHange *mensagem* content to the message you want to write;
* Run the code

OBS: 
* You may need to change the coordinates of the two ```pyautogui.click(x=-1251, y=338)``` to match the button to create a message first and to send it afterwards (check the coordinates by running ```time.sleep(5)```and ```pyautogui.position()``` and leaving the mouse on top of the buttons)
* You may also need to change the ```time.sleep(5)``` if it takes longer to load your webpage


# Developed by: 
  * [Felipe Roll - LinkedIn](https://www.linkedin.com/in/felipe-roll)
  * [Felipe Roll - GitHub](https://github.com/FelipeLRoll)
  * [Felipe Roll - Gmail](felipelroll@gmail.com)
