

temp_c = float(input("Enter the temperature in °C: "))

if temp_c < 20:
    status = "Cold"
elif 20 <= temp_c <= 30:
    status = "Normal"
else:
    status = "Hot"


temp_f = (temp_c * 9/5) + 32

print("Temperature:", temp_c, "°C")
print("Status:", status)
print("Temperature in Fahrenheit:", round(temp_f, 2), "°F")

