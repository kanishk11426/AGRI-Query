# Aurora Weather App

A fully functional, visually stunning weather web application built as a single HTML file.

## Features

### Functionality
- **Real-time Weather Data**: Fetches current weather using the Open-Meteo API (free, no API key needed)
- **Geolocation Support**: Automatically detects and displays weather for your current location using the browser Geolocation API
- **City Search**: Search for any city worldwide using the Open-Meteo Geocoding API
- **Current Weather Display**:
  - Current temperature
  - Feels like temperature
  - Humidity percentage
  - Wind speed
  - Weather condition with emoji icons
- **7-Day Forecast**: Shows daily high/low temperatures and weather conditions
- **WMO Weather Code Mapping**: All weather codes (0-99) mapped to human-readable descriptions and appropriate emoji icons

### Design
- **Glassmorphism Aesthetic**: Beautiful frosted glass cards with backdrop blur effects
- **Aurora Gradient Backgrounds**: Dynamic gradient backgrounds that change based on weather conditions:
  - Sunny: Warm golden to blue gradient
  - Rainy: Dark grey gradient
  - Cloudy: Cool grey gradient
  - Snowy: White to dark blue gradient
- **Animated Weather Particles**:
  - Rain particles for rainy weather
  - Snow particles for snowy weather
- **Google Fonts Typography**:
  - Space Grotesk (headings and body text)
  - JetBrains Mono (monospace details)
- **Smooth Transitions**: All UI elements have smooth hover effects and transitions
- **Loading States**: Beautiful spinner animation while fetching data
- **Error Handling**: Graceful error messages for location denied, city not found, or fetch failures

### Responsive Design
- Fully responsive layout that works on mobile and desktop
- Adaptive grid layouts for weather details and forecast cards
- Touch-friendly buttons and inputs

## How to Use

### Option 1: Direct File Access
Simply open `weather.html` in any modern web browser:
```bash
# macOS
open weather.html

# Linux
xdg-open weather.html

# Windows
start weather.html
```

### Option 2: Local Web Server
For the best experience, serve it through a local web server:
```bash
# Python 3
python3 -m http.server 8000

# Then open http://localhost:8000/weather.html
```

### Using the App

1. **Auto-Location**: When you first load the app, it will ask for location permission and automatically show weather for your current location

2. **Manual Search**:
   - Type a city name in the search box
   - Press Enter or click the "Search" button
   - The app will fetch and display weather for that city

3. **View Details**:
   - Current weather with large temperature display
   - Feels like temperature
   - Humidity percentage
   - Wind speed in km/h
   - 7-day forecast with daily highs and lows

## Technical Details

### APIs Used
1. **Open-Meteo Weather API**:
   - Endpoint: `https://api.open-meteo.com/v1/forecast`
   - Free, no API key required
   - Provides current weather and 7-day forecast

2. **Open-Meteo Geocoding API**:
   - Endpoint: `https://geocoding-api.open-meteo.com/v1/search`
   - Converts city names to latitude/longitude coordinates

3. **Browser Geolocation API**:
   - `navigator.geolocation.getCurrentPosition()`
   - Requires user permission

### Technologies
- **Pure HTML/CSS/JavaScript**: No frameworks or build tools required
- **Google Fonts**: Space Grotesk and JetBrains Mono (only external dependency)
- **Modern CSS**: Glassmorphism, backdrop filters, gradients, animations
- **Async/Await**: Clean asynchronous API calls
- **Responsive Design**: CSS Grid and Flexbox

### Weather Code Mapping
The app maps WMO weather codes to descriptions and emojis:
- Clear sky (0) → ☀️
- Partly cloudy (1-3) → 🌤️ ⛅ ☁️
- Fog (45-48) → 🌫️
- Drizzle (51-57) → 🌦️ 🌧️
- Rain (61-67) → 🌧️ ⛈️
- Snow (71-77, 85-86) → 🌨️ ❄️
- Thunderstorm (95-99) → ⛈️

## Browser Compatibility

Works in all modern browsers that support:
- ES6+ JavaScript (async/await, arrow functions, template literals)
- CSS backdrop-filter
- CSS Grid and Flexbox
- Geolocation API
- Fetch API

Tested and working on:
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## File Size
- Single HTML file: ~22KB
- No build process required
- No external JavaScript dependencies

## Privacy & Security
- No user data is collected or stored
- All API calls are made directly from the browser to Open-Meteo
- Location data is only used for weather fetching and not transmitted elsewhere
- No cookies or local storage used

## Credits
- Weather data: [Open-Meteo](https://open-meteo.com/)
- Typography: [Google Fonts](https://fonts.google.com/)
- Design: Aurora glassmorphism aesthetic with animated backgrounds

## License
MIT License - Feel free to use and modify as needed.
