# UModbusClient

**Inherits**: UObject

## Methods

| Return | Call |
| --- | --- |
| UModbusClient\* | [Create](#create)(UModbusTcpSocket* InPort, int32 TimeoutMs) |
| bool | [Init](#init)(UModbusTcpSocket* InPort, int32 TimeoutMs) |
| void | [Disconnect](#disconnect)() |
| int32 | [ReadHoldingRegister](#read_holding_register)(int32 Address) |
| TArray<int32\> | [ReadManyHoldingRegisters](#read_many_holding_registers)(int32 Address, int32 Count) |
| bool | [WriteHoldingRegister](#write_holding_register)(int32 Address, int32 Value) |
| bool | [WriteManyHoldingRegisters](#write_many_holding_registers)(int32 Address, TArray<int32\> Values) |
| int32 | [ReadCoil](#read_coil)(int32 Address) |
| TArray<int32\> | [ReadManyCoils](#read_many_coils)(int32 Address, int32 Count) |
| bool | [WriteCoil](#write_coil)(int32 Address, bool Value) |
| bool | [WriteManyCoils](#write_many_coils)(int32 Address, TArray<bool\> Values) |
| void | [Client_DebugPrint](#client_debug_print)() |
| void | [BeginDestroy](#begin_destroy)() *virtual override* |

***

<hr id="create"></hr>
UModbusClient\* **Create**(UModbusTcpSocket* InPort, int32 TimeoutMs)

<hr id="init"></hr>
bool **Init**(UModbusTcpSocket* InPort, int32 TimeoutMs)

<hr id="disconnect"></hr>
void **Disconnect**()

<hr id="read_holding_register"></hr>
int32 **ReadHoldingRegister**(int32 Address)

<hr id="read_many_holding_registers"></hr>
TArray<int32\> **ReadManyHoldingRegisters**(int32 Address, int32 Count)

<hr id="write_holding_register"></hr>
bool **WriteHoldingRegister**(int32 Address, int32 Value)

<hr id="write_many_holding_registers"></hr>
bool **WriteManyHoldingRegisters**(int32 Address, TArray<int32\> Values)

<hr id="read_coil"></hr>
int32 **ReadCoil**(int32 Address)

<hr id="read_many_coils"></hr>
TArray<int32\> **ReadManyCoils**(int32 Address, int32 Count)

<hr id="write_coil"></hr>
bool **WriteCoil**(int32 Address, bool Value)

<hr id="write_many_coils"></hr>
bool **WriteManyCoils**(int32 Address, TArray<bool\> Values)

<hr id="client_debug_print"></hr>
void **Client_DebugPrint**()

<hr id="begin_destroy"></hr>
void **BeginDestroy**() *virtual override*
