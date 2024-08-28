# EDA for Benin, Sierra leon & togo
   
## Objective of the EDA: 
To analyze environmental data and provide a data-driven strategy for identifying high-potential regions for solar installation, ensuring alignment with MoonLight Energy Solutions' goals of enhancing operational efficiency and achieving long-term sustainability.
    
## Data Understanding:
- the dataset contains solar farm data found in Benin, Sierra Leone, and Togo.
- each dataset was analyzed separately. 
- the datasets have same shape(525600,19). 
- each table has the following columns:

    - Timestamp (yyyy-mm-dd hh:mm): Date and time of each observation.
    - GHI (W/m²): Global Horizontal Irradiance, the total solar radiation received per square meter on a horizontal surface.
    - DNI (W/m²): Direct Normal Irradiance, the amount of solar radiation received per square meter on a surface perpendicular to the rays of thesun.
    - DHI (W/m²): Diffuse Horizontal Irradiance, solar radiation received per square meter on a horizontal surface that does not arrive on a direct  path from the sun.
    - ModA (W/m²): Measurements from a module or sensor (A), similar to irradiance.
    - ModB (W/m²): Measurements from a module or sensor (B), similar to irradiance.
    - Tamb (°C): Ambient Temperature in degrees Celsius.
    - RH (%): Relative Humidity as a percentage of moisture in the air.
    - WS (m/s): Wind Speed in meters per second.
    - WSgust (m/s): Maximum Wind Gust Speed in meters per second.
    - WSstdev (m/s): Standard Deviation of Wind Speed, indicating variability.
    - WD (°N (to east)): Wind Direction in degrees from north.
    - WDstdev: Standard Deviation of Wind Direction, showing directional variability.
    - BP (hPa): Barometric Pressure in hectopascals.
    - Cleaning (1 or 0): Signifying whether cleaning (possibly of the modules or sensors) occurred.
    - Precipitation (mm/min): Precipitation rate measured in millimeters per minute.
    - TModA (°C): Temperature of Module A in degrees Celsius.
    - TModB (°C): Temperature of Module B in degrees Celsius.
    - Comments: This column is designed for any additional notes.

## Outliers and error values found:

1. negative values entered in GHI,DNI,DHI which is an error for positive valued attribute.
2. comments attribute was found NaN

## Data ceaning measurements:
1. the negative valued numbers were too many to drop and to many to take absolute value. so the method used is that the negative numbers  in the tree coulumns were found and replaced with absolute value of 75% of them. this results a minimum data bias for further analysis. 
2. column comments was droped.

Let's take a look at the datasets separately

### Benin Data:

1. **Global Horizontal Irradiance (GHI):**
Mean: 240.56 W/m², indicating moderate sunlight exposure on a horizontal plane.
Standard Deviation (std): 331.13 W/m², showing significant variability in solar exposure.
Min/Max: The minimum value is -12.9 W/m² (likely indicating night or incorrect data), and the maximum is 1413 W/m², suggesting high solar potential at peak times.
2. **Direct Normal Irradiance (DNI):**
Mean: 167.19 W/m², indicating direct sunlight exposure, critical for solar panel efficiency.
Std: 261.71 W/m², with similar variability as GHI.
Min/Max: Ranges from -7.8 W/m² (again, possibly indicating night or data errors) to 952.3 W/m², showing good potential for concentrated solar power systems.
3. **Diffuse Horizontal Irradiance (DHI):**
Mean: 115.36 W/m², representing scattered sunlight, which is still usable for solar energy.
Std: 158.69 W/m², indicating variability but also significant potential.
Min/Max: Ranges from -12.6 W/m² to 759.2 W/m², showing a wide range in diffuse radiation.
4. **Air Temperature (Tamb):**
Mean: 28.18°C, with a low standard deviation of 5.92°C, indicating relatively stable temperatures.
Min/Max: Temperatures range from 11°C to 43.3°C, which is generally favorable for solar panel efficiency, though high temperatures may slightly reduce efficiency.
5. **Relative Humidity (RH):**
Mean: 54.49%, indicating moderate humidity levels.
Std: 28.07%, showing variability in humidity, which can affect solar efficiency (e.g., cloud formation).
Min/Max: Ranges from 2.1% to 100%, indicating varying atmospheric conditions.

### Sieraleon Data:

1. **Global Horizontal Irradiance (GHI):**
Mean: 201.96 W/m², which is slightly lower than in Benin, but still indicates moderate solar exposure.
Standard Deviation (std): 298.50 W/m², showing substantial variability.
Min/Max: The minimum value is -19.5 W/m² (likely indicating night or erroneous data), and the maximum is 1499 W/m², which suggests significant solar potential during peak sunlight hours.
2. **Direct Normal Irradiance (DNI):**
Mean: 116.38 W/m², which is lower compared to the Benin data, indicating that direct sunlight exposure may be less intense here.
Std: 218.65 W/m², indicating variability in direct sunlight.
Min/Max: Values range from -7.8 W/m² to 946 W/m², with a lower maximum value than Benin, indicating potentially lower peak solar generation capacity.
3. **Diffuse Horizontal Irradiance (DHI):**
Mean: 113.72 W/m², indicating a good level of diffuse sunlight.
Std: 158.95 W/m², similar to the Benin data, showing variability.
Min/Max: Ranges from -17 W/m² to 892 W/m², with the maximum value being somewhat lower than in Benin.
4. **Air Temperature (Tamb):**
Mean: 26.31°C, which is cooler on average than in Benin.
Std: 4.39°C, indicating stable temperatures.
Min/Max: Temperatures range from 12.3°C to 40.3°C, which is generally favorable for solar panel efficiency, with less risk of efficiency loss due to extreme heat compared to the Benin region.
5. **Relative Humidity (RH):**
Mean: 79.45%, which is significantly higher than in Benin, indicating a much more humid climate.
Std: 20.53%, showing variability in humidity levels.
Min/Max: Ranges from 2.9% to 100%, suggesting frequent high humidity, which could affect solar energy efficiency due to increased cloud cover.
6. **Wind Speed (WS):**
Mean: 1.15 m/s, indicating generally lower wind speeds than in Benin.
Min/Max: Ranges from 0.1 m/s to 19.2 m/s, with the maximum wind speed similar to Benin, suggesting the need for wind resilience in solar installations.

### togo Data

1. ***Global Horizontal Irradiance (GHI):***
Mean: 230 W/m², indicating moderate overall sunlight exposure on a horizontal plane, suitable for solar energy generation.
Standard Deviation (Std): 322.55 W/m², showing significant variability in solar exposure.
Min/Max: The minimum value is -12.7 W/m², which likely indicates erroneous data or night conditions, while the maximum of 1413 W/m² points to strong solar potential during peak sunlight hours.
2. ***Direct Normal Irradiance (DNI):***
Mean: 151.26 W/m², indicating moderate direct sunlight, which is essential for the efficiency of solar panels.
Std: 250.95 W/m², showing a wide variability in direct sunlight exposure.
Min/Max: The minimum is 0 W/m², and the maximum is 1004.5 W/m², suggesting periods of both no direct sunlight and very high direct sunlight.
3. ***Diffuse Horizontal Irradiance (DHI):***
Mean: 116.44 W/m², representing a moderate level of scattered sunlight, still useful for solar energy generation.
Std: 156.52 W/m², indicating variability in diffuse radiation.
Min/Max: The minimum is 0 W/m², while the maximum is 805.7 W/m², pointing to periods of high diffuse radiation, likely due to cloud cover or atmospheric scattering.
4. ***ModA (A Modulated Variable, likely Solar-related):***
Mean: 226.14, indicating moderate solar-related activity or measurement.
Std: 317.34, showing a wide range of variation.
Min/Max: Ranges from 0 to 1380, suggesting periods of both inactivity and high activity.


## Key Insights:

Solar Potential: The high values for GHI and DNI indicate strong potential for solar energy production, particularly during peak sunlight hours.
Environmental Considerations: The moderate temperatures and humidity levels suggest favorable conditions for solar installations, though variability in humidity and extreme wind speeds may require additional considerations for maintenance and durability.
Variability in Data: The wide range in values for several variables (e.g., GHI, DNI, DHI) suggests that solar energy potential can vary significantly, necessitating careful site selection and potentially dynamic solar tracking systems to optimize efficiency.

## Recommendations:

Target High DNI and GHI Regions: Prioritize regions with consistently high GHI and DNI values for solar installations.
Consider Local Climate: Ensure that installation designs account for variability in temperature, humidity, and wind speed to maximize efficiency and minimize maintenance costs.
Solar Potential: The solar potential, as indicated by the GHI and DNI, is slightly lower in Sierra Leone compared to Benin and togo, but it is still significant enough to justify solar installations, especially in regions with consistently high GHI and DNI values.
Environmental Considerations: The high humidity levels suggest more cloud cover, which may reduce the efficiency of solar panels. However, the relatively stable and cooler temperatures are favorable for long-term solar efficiency.
Prioritize Regions with Lower Humidity: Given the high average humidity, it may be beneficial to prioritize regions with lower humidity levels or to invest in technologies that perform well in humid conditions.
Leverage Cooler Temperatures: The relatively cooler temperatures in sierra leone compared to Benin suggest that solar panels in Sierra Leone might operate more efficiently over time, with less risk of heat-related efficiency losses.

## Conclusion:

higher solar potential in benin and sieraleon indicate opportunity for higher solar energy production.
While Sierra Leone shows slightly lower solar potential compared to Benin and togo it still offers viable opportunities for solar installations, particularly in regions with lower humidity.
With proper site selection and consideration of the local climate, solar investments in Sierra Leone can contribute to MoonLight Energy Solutions' sustainability goals.