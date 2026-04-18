---
functions:
    Create:
        output: UModbusClient*
        inputs:
            - UModbusTcpSocket* InPort
            - int32 TimeoutMs
        annotations:
            - static

    Init:
        output: bool
        inputs:
            - UModbusTcpSocket* InPort
            - int32 TimeoutMs

    Connect:
        output: bool
        inputs:
            - const FString& Host
            - int32 Port

    Disconnect:
        output: void

    ReadHoldingRegister:
        output: int32
        inputs:
            - int32 Address
            - int32& OutValue

    ReadManyHoldingRegisters:
        output: int32
        inputs:
            - int32 Address
            - int32 Count
            - TArray<int32>& OutValue

    WriteHoldingRegister:
        output: int32
        inputs:
            - int32 Address
            - int32 Value

    WriteManyHoldingRegisters:
        output: int32
        inputs:
            - int32 Address
            - TArray<int32> Values

    ReadCoil:
        output: int32
        inputs:
            - int32 Address
            - bool& OutValue

    ReadManyCoils:
        output: int32
        inputs:
            - int32 Address
            - int32 Count
            - TArray<bool>& OutValue

    WriteCoil:
        output: int32
        inputs:
            - int32 Address
            - bool Value

    WriteManyCoils:
        output: int32
        inputs:
            - int32 Address
            - TArray<bool> Values

    ReadInputRegister:
        output: int32
        inputs:
            - int32 Address
            - int32& OutValue

    ReadManyInputRegisters:
        output: int32
        inputs:
            - int32 Address
            - int32 Count
            - TArray<int32>& OutValue

    ReadDiscreteInput:
        output: int32
        inputs:
            - int32 Address
            - bool& OutValue

    ReadManyDiscreteInputs:
        output: int32
        inputs:
            - int32 Address
            - int32 Count
            - TArray<bool>& OutValue

    Client_DebugPrint:
        output: void
        inputs: []

    BeginDestroy:
        output: void
        inputs: []
        annotations:
            - override
            - virtual
---
# UModbusClient

**Inherits**: [UObject](https://dev.epicgames.com/documentation/unreal-engine/API/Runtime/CoreUObject/UObject)

## Methods

<HEADER>

[UModbusClient](/UModbusClient#bweh)

## Method Descriptions

<Create>

Constructor. Creates a UModbusTcpSocket if the input pointer `InPort` is null.

<Init>

Attaches InPort and initializes the socket. Called by the constructor.

<Connect>

Calls [UModbusTcpSocket.Connect()](UModbusTcpSocket#Connect) on its attached socket.

<Disconnect>

Calls [UModbusTcpSocket.Close()](UModbusTcpSocket#Close) on its attached socket if it was attached.

<ReadHoldingRegister>

Writes the contents of the Modbus register at `address` to `OutValue`. Returns a [nmbs_error](https://debevv.github.io/nanoMODBUS/nanomodbus_8h.html#a1cb1b1b4b26001764e36a1df4335f7f0) code.

<ReadManyHoldingRegisters>

Writes the contents of the registers starting from `address` and ending at `address + count` to `OutValue`. Returns a [nmbs_error](https://debevv.github.io/nanoMODBUS/nanomodbus_8h.html#a1cb1b1b4b26001764e36a1df4335f7f0) code.

<WriteHoldingRegister>

Writes `Value` to the register at the `address`. Returns a [nmbs_error](https://debevv.github.io/nanoMODBUS/nanomodbus_8h.html#a1cb1b1b4b26001764e36a1df4335f7f0) code.

<WriteManyHoldingRegisters>

Writes `Values` to the registers between `address` and `address + Values.size()`. Returns a [nmbs_error](https://debevv.github.io/nanoMODBUS/nanomodbus_8h.html#a1cb1b1b4b26001764e36a1df4335f7f0) code.

<ReadCoil>

Writes the contents of the Modbus coil at `address` to `OutValue`. Returns a [nmbs_error](https://debevv.github.io/nanoMODBUS/nanomodbus_8h.html#a1cb1b1b4b26001764e36a1df4335f7f0) code.

<ReadManyCoils>

Writes the contents of the coils starting from `address` and ending at `address + count` to `OutValue`. Returns a [nmbs_error](https://debevv.github.io/nanoMODBUS/nanomodbus_8h.html#a1cb1b1b4b26001764e36a1df4335f7f0) code.

<WriteCoil>

Writes `Value` to the coil at the `address`. Returns a [nmbs_error](https://debevv.github.io/nanoMODBUS/nanomodbus_8h.html#a1cb1b1b4b26001764e36a1df4335f7f0) code.

<WriteManyCoils>

Writes `Values` to the coils between `address` and `address + Values.Num()`. Returns a [nmbs_error](https://debevv.github.io/nanoMODBUS/nanomodbus_8h.html#a1cb1b1b4b26001764e36a1df4335f7f0) code.

<ReadInputRegister>

Writes the contents of the Modbus input register at `address` to `OutValue`. Returns a [nmbs_error](https://debevv.github.io/nanoMODBUS/nanomodbus_8h.html#a1cb1b1b4b26001764e36a1df4335f7f0) code.


<ReadManyInputRegisters>

Writes the contents of the input registers starting from `address` and ending at `address + count` to `OutValue`. Returns a [nmbs_error](https://debevv.github.io/nanoMODBUS/nanomodbus_8h.html#a1cb1b1b4b26001764e36a1df4335f7f0) code.

<ReadDiscreteInput>

Writes the contents of the Modbus discrete input (or "contact") register at `address` to `OutValue`. Returns a [nmbs_error](https://debevv.github.io/nanoMODBUS/nanomodbus_8h.html#a1cb1b1b4b26001764e36a1df4335f7f0) code.

<ReadManyDiscreteInputs>

Writes the contents of the Modbus discrete input (or "contact") registers starting from `address` and ending at `address + count` to `OutValue`. Returns a [nmbs_error](https://debevv.github.io/nanoMODBUS/nanomodbus_8h.html#a1cb1b1b4b26001764e36a1df4335f7f0) code.

<Client_DebugPrint>

Debug Function that outputs to [LogTemp](https://dev.epicgames.com/documentation/unreal-engine/logging-in-unreal-engine) whether the socket is valid (NULL) or not.

<BeginDestroy>

Ensures that the socket is disconnected before destroying this object. Overrides [UObject.BeginDestroy()](https://dev.epicgames.com/documentation/unreal-engine/API/Runtime/CoreUObject/UClassProperty/BeginDestroy)