from pymodbus.client import ModbusSerialClient
from pymodbus import (
    FramerType,
    ModbusException,
    pymodbus_apply_logging_config,
)


READ_COILS = 1
READ_HOLDING_REGISTERS = 3

WRITE_SINGLE_COILS = 5
WRITE_SINGLE_REGISTER = 6

WRITE_MULTIPLE_COILS = 15
WRITE_MULTIPLE_REGISTERS = 16


pymodbus_apply_logging_config("DEBUG")

client = ModbusSerialClient(
                            framer= FramerType.ASCII,
                            port="COM8",
                            baudrate= 9600,
                            bytesize= 7,
                            parity= 'E',
                            stopbits= 1,
                            timeout= 1
                            )

def read_data(function:int = READ_HOLDING_REGISTERS, address= int, count=int, device_id: int=1):
    """
    Read data from the PLC using Modbus ASCII.

    Parameters
    ----------
    function : int
        Modbus function code.
    address : int
        Register address.
    count : int
        Number of registers.

    Returns
    -------
    ModbusResponse
    """

    print("connect to server")
    client.connect()

    print("get and verify data")
    if function == READ_COILS:
        try:
            rr = client.read_coils(address= address, count= count, device_id=device_id)
            print(rr)
        except ModbusException as exc:  # pragma: no cover
            print(f"1: Received ModbusException({exc}) from library")
            client.close()
            return
        if rr.isError():  # pragma: no cover
            print(f"1: Received exception from device ({rr})")
            # THIS IS NOT A PYTHON EXCEPTION, but a valid modbus message
            client.close()
            return
    elif function == READ_HOLDING_REGISTERS:
        try:
            # See all calls in client_calls.py
            rr = client.read_holding_registers(address=address, count= count, device_id=device_id)
            value_int32 = client.convert_from_registers(registers=rr.registers, 
                                                        data_type=client.DATATYPE.INT32, 
                                                        word_order="little")
            print(f"Got int32: {value_int32}")
        except ModbusException as exc:  # pragma: no cover
            print(f"2: Received ModbusException({exc}) from library")
            client.close()
            return
        if rr.isError():  # pragma: no cover
            print(f"2: Received exception from device ({rr})")
            # THIS IS NOT A PYTHON EXCEPTION, but a valid modbus message
            client.close()
            return
    

    print("close connection")
    client.close()

def send_data(function:int = WRITE_SINGLE_REGISTER, address= int, value=int, device_id: int=1):
    print("connect to server")
    client.connect()

    if function == WRITE_SINGLE_COILS:
        result = client.write_coil(address= address, value= value, device_id= device_id, no_response_expected=False)
    elif function == WRITE_SINGLE_REGISTER:
        result = client.write_register(address= address, value= value, device_id= device_id, no_response_expected=False)
    elif function == WRITE_MULTIPLE_COILS:
        result = client.write_coils(address= address, values= value, device_id= device_id, no_response_expected=False)
    elif function == WRITE_MULTIPLE_REGISTERS:
        result = client.write_registers(address= address, values= value, device_id= device_id, no_response_expected=False)

    print(result)


    print("close connection")
    client.close()

if __name__ == "__main__":
    read_data(function= READ_HOLDING_REGISTERS , address=0x100A, count= 2)
    
    send_data(function= WRITE_SINGLE_COILS, address=0x505, value= 1)
    send_data(function= WRITE_SINGLE_REGISTER, address=0x1000, value= 1)
    send_data(function= WRITE_MULTIPLE_COILS, address=0x500, value= [True,True,True,False,True,False])
    # send_data(function= WRITE_MULTIPLE_REGISTERS, address=0x1000, value= [7])
