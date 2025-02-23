import folium

# Coordinates for the major locations along the route
locations = [
    {"name": "Srinagar", "lat": 34.0836, "lon": 74.7973},
    {"name": "Jammu", "lat": 32.7266, "lon": 74.8570},
    {"name": "Amritsar", "lat": 31.5497, "lon": 74.3436},
    {"name": "Delhi", "lat": 28.6139, "lon": 77.2090},
    {"name": "Chennai", "lat": 13.0827, "lon": 80.2707},
    {"name": "Kanyakumari", "lat": 8.0883, "lon": 77.5385},
]

# Create a map centered around the midpoint of the locations
mymap = folium.Map(location=[20.0, 77.0], zoom_start=5)

# Add markers for each location along the route
for loc in locations:
    folium.Marker([loc["lat"], loc["lon"]]).add_to(mymap)
    folium.Marker([loc["lat"], loc["lon"]], icon=folium.DivIcon(icon_size=(150, 36), icon_anchor=(7, 25), html=f'<div style="font-size: 15pt; color: black">{loc["name"]}</div>')).add_to(mymap)

# Add PolyLine to connect all the markers (Srinagar to Kanyakumari)
folium.PolyLine(
    locations=[(loc["lat"], loc["lon"]) for loc in locations],  # List of (lat, lon) pairs
    color="blue",  # Line color
    weight=2.5,    # Line thickness
    opacity=1      # Line opacity
).add_to(mymap)

# Save the map to an HTML file
mymap.save("route.html")
