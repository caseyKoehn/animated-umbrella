import minimalmodbus

mb_address = 1

sensy_boi = minimalmodbus.Instrument('/dev/ttyACM0',mb_address)

sensy_boi.serial.baudrate = 9600
sensy_boi.serial.bytesize = 8
sensy_boi.serial.parity = minimalmodbus.serial.PARITY_NONE
sensy_boi.serial.stopbits = 1
sensy_boi.serial.timeout  = 0.5
sensy_boi.mode = minimalmodbus.MODE_RTU
sensy_boi.clear_buffers_before_each_transaction = True
sensy_boi.close_port_after_each_call = True

print(sensy_boi) 

data =sensy_boi.read_registers(0, 2, 3)

print(f"Raw data is {data}")

sensy_boi.serial.close()
