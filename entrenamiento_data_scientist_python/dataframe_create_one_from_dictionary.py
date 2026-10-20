"""Create a DataFrame from the dictionary example."""
import pandas as pd

# Create a dictionary with data for the DataFrame
datos = {
    "nombre": ["María", "Luis", "Carmen", "Antonio"],
    "edad": [18, 22, 20, 21],
    "grado": ["Economía", "Medicina", "Arquitectura", "Economía"],
    "correo": [
        "maria@gmail.com",
        "luis@yahoo.es",
        "carmen@gmail.com",
        "antonio@gmail.com",
    ],
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(datos)

# Print the DataFrame
print(df)
