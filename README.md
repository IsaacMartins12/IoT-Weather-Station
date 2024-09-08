# IoT Weather Station with MQTT and Real-Time Data Visualization

## 📋 Description

This project consists of an IoT weather station that collects temperature and humidity data using the **DHT22** sensor. The data is sent to an **MQTT broker**, stored in a database (MongoDB via **PyMongo** or **SQLite**), and displayed in interactive, real-time graphs using **Matplotlib**. The station connects to a Wi-Fi network and connect the mqtt host and updates the graphic every 5 seconds.

## 🚀 Features

- Collects weather data using the **DHT22** sensor (temperature and humidity).
- Sends data via **MQTT** to a broker.
- Stores data in a MongoDB or SQLite database.
- Real-time data visualization with animated graphs using **Matplotlib**.
- Connects to Wi-Fi for data sending and time synchronization with **Threads**
- Updates graphs every 5 seconds.
- Simulation with wokwi

## 🛠️ Technologies Used

- **MicroPython** or **Python** (for data collection and MQTT sending)
- **Paho MQTT** (library for MQTT communication)
- **MongoDB** (via **PyMongo**) or **SQLite** for data storage
- **Matplotlib** (for graphical visualization)
- **Threading** (to run the graphs in a separate thread)
- **dotenv** (for managing environment variables securely)

## 📦 Installation

### Requirements

- Python 3.x
- Paho MQTT library
- Matplotlib library
- PyMongo (if using MongoDB Atlas)
- SQLite3 (if using SQLite)
- dotenv (for environment variables)

### Installation Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/IsaacMartins12/IoT-Weather-Station.git
    ```

2. Install dependencies:
    ```bash
    pip install paho-mqtt matplotlib python-dotenv
    ```

3. Configure the `.env` file with environment variables:

    Create a `.env` file in the root directory of the project and add the necessary variables for MongoDB Atlas and the database:

    ```env
    DB_NAME=weather_data  # Database name
    MQTT_BROKER=broker.mqttdashboard.com  # MQTT broker address
    MQTT_PORT = "1883"  # MQTT default port
    MQTT_TOPIC = "wokwi-weather"  # Topic for subscribe
    ```

4. Run the main application:

    ```bash
    python app.py
    ```

## 🚦 Usage

### Weather Station (MicroPython)

1. Upload the MicroPython script to your **ESP32** or **ESP8266** device.
2. The device will connect to the Wi-Fi network, collect data from the **DHT22** sensor, and send the data to the MQTT broker.

### Python Backend (Data Collection and Visualization)

1. The Python backend will connect to the MQTT broker, process the received data, and store it in the database.
2. The graph will be displayed in a separate window, updating with new data every 5 seconds.

### Example Graphs

The following graphs will be generated and updated as new data is received:

- **Temperature over Time**
- **Humidity over Time**

## 📊 Database Structure

- **timestamp**: Date and time when the data was recorded.
- **temperature**: Temperature value collected by the sensor.
- **humidity**: Humidity value collected by the sensor.

## ⚙️ Customization

- To use a different MQTT broker, modify the `MQTT_BROKER` variable in the `.env` file.
- To change the graph update interval, modify the `interval` parameter in the `animation.FuncAnimation` function.

## 🧑‍💻 Contribution

Feel free to submit pull requests or report issues on the [Issues page](https://github.com/IsaacMartins12/IoT-Weather-Station/issues).

1. Fork the project.
2. Create a branch for the new feature (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Create a new Pull Request.

## 📜 License

This project is licensed under the [MIT License](LICENSE).
