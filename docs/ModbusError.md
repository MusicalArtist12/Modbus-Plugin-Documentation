# ModbusError

Re-Export of [nmbs_error](https://debevv.github.io/nanoMODBUS/nanomodbus_8h.html#a1cb1b1b4b26001764e36a1df4335f7f0).

"*nanoMODBUS errors. Values <= 0 are \[nanoModbus\] errors, > 0 are modbus exceptions*"

| Enum | Value | Source | Description |
| --- | --- | --- | --- |
| `ERROR_INVALID_REQUEST` | -8 | nanoModbus | Received invalid request from client |
| `ERROR_INVALID_UNIT_ID` | -7 | nanoModbus | Received invalid unit ID in response from server |
| `ERROR_INVALID_TCP_MBAP` | -6 | nanoModbus | Received invalid TCP MBAP |
| `ERROR_CRC` |-5 | nanoModbus | Received invalid CRC |
| `ERROR_TRANSPORT` | -4 | nanoModbus | Transport error |
| `ERROR_TIMEOUT` | -3 | nanoModbus | Read/write timeout occurred |
| `ERROR_INVALID_RESPONSE` | -2 | nanoModbus | Received invalid response from server |
| `ERROR_INVALID_ARGUMENT` | -1 | nanoModbus | Invalid argument provided |
| `ERROR_NONE` | 0 | nanoModbus | No error |
| `EXCEPTION_ILLEGAL_FUNCTION` | 1 | Modbus | Illegal Function |
| `EXCEPTION_ILLEGAL_DATA_ADDRESS` | 2 | Modbus | Illegal Data Address |
| `EXCEPTION_ILLEGAL_DATA_VALUE` | 3 | Modbus | Illegal Data Value |
| `EXCEPTION_SERVER_DEVICE_FAILURE` | 4 | Modbus | Server Device Failure |