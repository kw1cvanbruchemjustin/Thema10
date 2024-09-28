import pymssql
import time
from gpiozero import CPUTemperature

sensorDevice = 1  # Specify your sensor device ID

# Infinite loop to record sensor data periodically
while True:
    # Establish the database connection
    conn = pymssql.connect(
        host='justinvanbruchemserver.database.windows.net',
        port=1433,
        database='justinvanbruchemserver',
        user='justinvanbruchem@justinvanbruchemserver',
        password='m5a6zodc8sHA&Pho'
    )
    cursor = conn.cursor()
    
    # Get the current CPU temperature
    cpu_temp = round(CPUTemperature().temperature)  # Get and round the CPU temperature
    
    # Execute the SQL query with parameterized inputs
    cursor.execute('INSERT INTO dbo.Opdracht21 (sensorDevice, sensorValue) VALUES (%s, %s)', 
                   (sensorDevice, cpu_temp))
    
    # Commit the transaction to save the data in the database
    conn.commit()
    
    # Print the temperature to the console
    print(f"Inserted: SensorDevice {sensorDevice}, Temperature: {cpu_temp}")
    
    cursor.close()
    conn.close()
    print("Database connection closed.")
    
    # Wait for 10 secondsbefore sending next value
    time.sleep(10)