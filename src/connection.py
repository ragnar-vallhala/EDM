import serial
import serial.tools.list_ports

# Get a list of available ports
ports = serial.tools.list_ports.comports()

# Print information about each port
for port in ports:
    print(f"Device: {port.device}")
    print(f"Name: {port.name}")
    print(f"Description: {port.description}")
    print(f"Hardware ID: {port.hwid}")
    print(f"Manufacturer: {port.manufacturer}")
    print(f"Product: {port.product}")
    print(f"Serial Number: {port.serial_number}")
    print(f"Location: {port.location}")
    print(f"Interface: {port.interface}")
    print("=" * 20)

port=ports[0]
print(type(port.name))

# Create a serial object
ser = serial.Serial(port.name, 115200)  # Replace 'COM1' with the appropriate port name and 9600 with the baud rate

# Read and print data from the serial port



while True:
    
    a = input("entre something ")
    a+='\n'
    ser.write(a.encode('latin-1'))
    if ser.in_waiting > 0:
        data = ser.readline().decode('latin-1').strip()

        print("Received:", data)





