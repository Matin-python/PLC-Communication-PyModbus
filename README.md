# PLC Communication using PyModbus

A Python project that communicates with a PLC using the **PyModbus** library over the **Modbus ASCII** protocol. This project demonstrates how to read from and write to PLC registers and coils using a high-level Modbus library, making industrial communication simpler and more maintainable.

## Features

* Communicate with PLCs using the Modbus ASCII protocol
* Read Holding Registers
* Read Coils
* Write Single Coil
* Write Single Register
* Write Multiple Coils
* Write Multiple Registers
* Convert register values into Python data types
* Configurable serial communication settings
* Simple and well-documented code

## Technologies Used

* Python 3
* PyModbus
* Modbus ASCII Protocol

## Project Structure

```text
PLC-Communication-PyModbus/
│
├── PLC Communication PyModbus.py
├── requirements.txt
├── README.md
└── LICENSE

```

## Requirements

Install the required packages:

```bash
pip install pymodbus pyserial
```

or

```bash
pip install -r requirements.txt
```

## Hardware Requirements

* PLC supporting the Modbus ASCII protocol
* USB-to-Serial (RS-232 / RS-485) converter (if required)
* Python 3

## Serial Configuration

The project uses the following serial settings:

| Parameter | Value        |
| --------- | ------------ |
| Protocol  | Modbus ASCII |
| Baud Rate | 9600         |
| Data Bits | 7            |
| Parity    | Even         |
| Stop Bits | 1            |
| Timeout   | 1 second     |

Adjust these settings according to your PLC configuration.

## Supported Functions

### Read Operations

* Read Coils (Function Code 01)
* Read Holding Registers (Function Code 03)

### Write Operations

* Write Single Coil (Function Code 05)
* Write Single Register (Function Code 06)
* Write Multiple Coils (Function Code 15)
* Write Multiple Registers (Function Code 16)

## Usage

Run the program:

```bash
python main.py
```

Example:

```python
read_data(function=READ_HOLDING_REGISTERS, address=0x100A, count=2)

send_data(function=WRITE_SINGLE_REGISTER,
          address=0x1000,
          value=1)
```

## Example Output

```text
connect to server

get and verify data

Got int32: 12345

close connection
```

## Project Workflow

The program performs the following steps:

1. Connect to the PLC.
2. Send a Modbus request.
3. Receive and verify the response.
4. Convert register data into Python data types (when applicable).
5. Display the received data.
6. Close the serial connection.

## Related Project

This project uses the **PyModbus** library for Modbus communication.

If you are interested in learning how the Modbus ASCII protocol works internally, including manual frame construction, LRC checksum calculation, serial communication, and response parsing without using external libraries, check out my companion project:

**PLC Communication – Manual Modbus ASCII**

https://github.com/Matin-python/PLC-Communication-Manual-Modbus-ASCII

## Future Improvements

* Support additional Modbus function codes
* Automatic serial port detection
* Communication retry mechanism
* Better exception handling
* Logging communication to a file
* Graphical User Interface (GUI)
* Support for Modbus RTU and Modbus TCP

## License

This project is licensed under the MIT License.

## Author

**Mohammad Reza Bakhshandeh**

Electrical Engineering (Electronics) Graduate

Interested in Industrial Automation, Embedded Systems, PLC Programming, Python Development, Computer Vision, Machine Learning, and Artificial Intelligence.
