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
  * **Tools Required:** Solderless Breadboard, Jumper Wires, Micro-USB Data Cable

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

**Caption:** The Python Flask server running successfully in the terminal, showing the local network IP address it's listening on.

**Caption:** The Arduino IDE Serial Monitor showing the ESP8266 connecting to Wi-Fi and successfully sending a GET request to the server upon cup detection.

**Caption:** The Python server terminal after receiving a trigger, showing the AI-generated dialogue before it is converted to speech.

**Diagrams**
![Uploading image.png…]()


**Caption:** Architecture diagram showing the data flow from the ESP8266 coaster, across the Wi-Fi network to the Flask server, which then communicates with Google's AI & TTS APIs before playing the final audio on the laptop.

#### For Hardware:

**Schematic & Circuit**

**Caption:** A photo of the final circuit on the breadboard, showing the connections between the NodeMCU ESP8266, DHT11 sensor, and IR sensor.

**Build Photos**

**Caption:** All the hardware components used in the project laid out: NodeMCU ESP8266, DHT11, IR Sensor, Breadboard, and Jumper Wires.

**Caption:** The final Samchaya Coaster prototype in action with a cup of tea placed on it.

### Project Demo

**Video**

`[Add your YouTube or Google Drive link to the demo video here]`
**Caption:** A short video demonstrating the full end-to-end functionality: a cup is placed on the coaster, the logs appear on the screens, and the unique AI-generated audio is played from the laptop's speakers.

### Team Contributions

  * **`SAKHIL N MAJU`**: Responsible for the entire hardware assembly, wiring the ESP8266 and sensors, and writing the C++/Arduino firmware to read sensor data and trigger the backend over Wi-Fi.
  * **`NIMA FATHIMA`**: Responsible for setting up the Python backend, creating the Flask server, integrating with Google Gemini and Text-to-Speech APIs, and managing the audio playback with Pygame.

-----

Made with ❤️ at TinkerHub Useless Projects
