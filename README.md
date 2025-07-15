# ✈️ echo1090

This project is a web application for tracking flights received by a local ADS-B receiver (e.g., FlightFeeder by Flightradar24), displayed on a real-time map using Leaflet.js.

## 🗺️ What does the app do?

- Connects to a local ADS-B receiver and retrieves a list of aircraft.
- For each flight, additionally loads detailed information (model, route, registration, airline, photo, etc.).
- Displays current aircraft positions on the map (Leaflet).
- Shows movement trajectories (trails) for each flight.
- Includes an interactive sidebar with a list of flights.

## 📡 Data source

- **Local receiver**: uses the `flights.json` file obtained from your ADS-B receiver (e.g., installed on a Raspberry Pi with FlightFeeder from Flightradar24). By default, the URL is set to:

  FLIGHTS_URL = 'http://192.168.0.117:8754/flights.json'

- **Additional data**: for each flight detected in the stream, a request is made to Flightradar24 to obtain:
  - flight number,
  - route (departure and arrival airports),
  - registration number,
  - aircraft model,
  - airline,
  - aircraft image (if available).

This data is fetched through sequential requests to an unofficial Flightradar24 API. It enriches the basic data available from the receiver and visualizes it on the map and in the sidebar.

## ⚙️ Installation and launch

1. Clone the repository:

   ```bash
   git clone https://github.com/ch3rryxc/echo1090
   cd flight-tracker

   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Update the configuration in config.py with your own settings.

4. Launch the application:

   ```bash
   python main.py
   ```

   

> ⚠️ This project uses an unofficial method to obtain data from Flightradar24.
> It is intended for personal use only.
> Public deployment or commercial use may violate Flightradar24's terms of service.

# License
This project is intended solely for demonstration, local use, and personal portfolio purposes. All data and images retrieved from Flightradar24 belong to their respective copyright holders.
The author is not responsible for the use of data from third-party sources.
