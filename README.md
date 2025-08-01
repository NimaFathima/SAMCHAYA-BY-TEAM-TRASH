# SAMCHAYA-BY-TEAM-TRASH

# "Samchaya" - The Talking Tea Coaster 🎯

### Basic Details

**Team Name:** `TRASH`

### Team Members

  * **Team Lead:** `NIMA FATHIMA`- `ADI SHANKARA INSTITUTE OF ENGINEERING AND TECHNOLOGY,KALADY`
  * **Member 2:** `SAKHIL N MAJU`- `ADI SHANKARA INSTITUTE OF ENGINEERING AND TECHNOLOGY,KALADY`
    
### Project Description

**Samchaya** (from *Samsaaram* for conversation and *Chaya* for tea) is an AIoT smart coaster that gives your beverage a voice. It senses your drink's status and uses Generative AI to speak unique, context-aware dialogues in a natural voice, preventing the tragedy of forgotten, cold tea.

### The Problem (that doesn't exist)

We are tackling the silent epidemic known as **Cold Chaya Syndrome (CCS)**. Every day, millions of productive hours are lost and countless souls are disheartened when a perfectly good cup of tea or coffee goes cold, forgotten amidst the chaos of work. This first-world problem leads to decreased morale and the existential dread of a lukewarm sip.

### The Solution (that nobody asked for)

The **Samchaya** coaster is a hyper-intelligent, slightly judgmental beverage companion. It doesn't just buzz or blink; it *talks*. Using an ESP8266 brain and an array of sensors, it monitors your drink and your level of neglect, delivering timely (and often sarcastic) vocal interventions to save you from the horror of CCS.

### Technical Details

#### Technologies/Components Used

**For Software:**

  * **Languages:** Python, C++ (for Arduino)
  * **Frameworks:** Flask
  * **Libraries:** `google-generativeai` (for Gemini AI), `google-cloud-texttospeech`, `pygame` (for audio), `ESP8266WiFi`, `ESP8266HTTPClient`, `DHT`
  * **Tools & Services:** Arduino IDE, Visual Studio Code, Google AI Studio, Google Cloud Platform

**For Hardware:**

  * **Main Components:** NodeMCU ESP8266, DHT11 Temperature Sensor, IR Proximity Sensor
  * **Specifications:** Wi-Fi enabled microcontroller, digital temperature/humidity sensing, infrared presence detection.
  * **Tools Required:** Jumper Wires, Micro-USB Data Cable

### Implementation

#### For Software:

**Installation**
*Clone the repository and set up the Python virtual environment:*

```bash
# Navigate to project folder
cd samchaya-coaster-backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
# source venv/bin/activate

# Install required packages
pip install Flask google-generativeai google-cloud-texttospeech pygame
```

**Run**
*Execute the Flask server:*

```bash
python app.py
```

### Project Documentation

#### For Software:

**Screenshots (Add at least 3)**

<img width="1617" height="653" alt="image" src="https://github.com/user-attachments/assets/312b9ff5-6d25-4ba4-80d3-5d489768afd3" />
**Caption:** The Python Flask server running successfully in the terminal, showing the local network IP address it's listening on.


![WhatsApp Image 2025-08-02 at 02 05 35_4b5b5bd2](https://github.com/user-attachments/assets/ce1e4d6b-8b3e-4746-8ccd-a9815c7c4646)
**Caption:** The Arduino IDE Serial Monitor showing the ESP8266 connecting to Wi-Fi and successfully sending a GET request to the server upon cup detection.


<img width="1907" height="185" alt="image" src="https://github.com/user-attachments/assets/e579dc5b-cef6-450d-81eb-9947a242616a" />
**Caption:** The Python server terminal after receiving a trigger, showing the AI-generated dialogue before it is converted to speech.


**Diagrams**

# Schematic & Circuit
<img width="2048" height="2048" alt="ARCHITECTURE" src="https://github.com/user-attachments/assets/bf98d645-e846-436f-8e8f-58e47f70a011" />
**Caption:** Architecture diagram showing the data flow from the ESP8266 coaster, across the Wi-Fi network to the Flask server, which then communicates with Google's AI & TTS APIs before playing the final audio on the laptop.

#### For Hardware:
**Build Photos**

![WhatsApp Image 2025-08-02 at 02 10 25_83216993](https://github.com/user-attachments/assets/816650d2-e45b-4d7a-9b72-c23e5bcc305e)
**Caption:** All the hardware components used in the project laid out: NodeMCU ESP8266, DHT11, IR Sensor, Breadboard, and Jumper Wires.


![WhatsApp Image 2025-08-02 at 02 19 55_41153f31](https://github.com/user-attachments/assets/6d17f7a4-13b4-4637-bfac-cfab196d6767)
**Caption:** The final Samchaya Coaster prototype in action with a cup of tea placed on it.


### Project Demo

**Video**

`https://drive.google.com/drive/folders/1oMwyX-DQe85ZkyySmYkZdrJtXqmmoJzb?usp=sharing`

**Caption:** A short video demonstrating the full end-to-end functionality: a cup is placed on the coaster, the logs appear on the screens, and the unique AI-generated audio is played from the laptop's speakers.

### Team Contributions

  * **`SAKHIL N MAJU`**: Responsible for the entire hardware assembly, wiring the ESP8266 and sensors, and writing the C++/Arduino firmware to read sensor data and trigger the backend over Wi-Fi.
  * **`NIMA FATHIMA`**: Responsible for setting up the Python backend, creating the Flask server, integrating with Google Gemini and Text-to-Speech APIs, and managing the audio playback with Pygame.

-----

Made with ❤️ at TinkerHub Useless Projects
