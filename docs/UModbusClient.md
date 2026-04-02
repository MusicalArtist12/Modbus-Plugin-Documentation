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
<p class="mono-title"><mark>UModbusClient*</mark> Create(<mark>UModbusTcpSocket*</mark> InPort, <mark>int32</mark> TimeoutMs)</p>

<hr id="init"></hr>
<p class="mono-title"><mark>bool</mark> Init(<mark>UModbusTcpSocket*</mark> InPort, <mark>int32</mark> TimeoutMs)</p>

<hr id="disconnect"></hr>
<p class="mono-title"><mark>void</mark> Disconnect()</p>

<hr id="read_holding_register"></hr>
<p class="mono-title"><mark>int32</mark> ReadHoldingRegister(<mark>int32</mark> Address)</p>

<hr id="read_many_holding_registers"></hr>
<p class="mono-title"><mark>TArray\<<mark>int32</mark>\></mark> ReadManyHoldingRegisters(<mark>int32</mark> Address, <mark>int32</mark> Count)</p>

<hr id="write_holding_register"></hr>
<p class="mono-title"><mark>bool</mark> WriteHoldingRegister(<mark>int32</mark> Address, <mark>int32</mark> Value)</p>

<hr id="write_many_holding_registers"></hr>
<p class="mono-title"><mark>bool</mark> WriteManyHoldingRegisters(<mark>int32</mark> Address, TArray<<mark>int32</mark>\> Values)</p>

<hr id="read_coil"></hr>
<p class="mono-title"><mark>int32</mark> ReadCoil(<mark>int32</mark> Address)</p>

<hr id="read_many_coils"></hr>
<p class="mono-title"><mark>TArray&lt;int32&gt;</mark> ReadManyCoils(<mark>int32</mark> Address, <mark>int32</mark> Count)</p>

<hr id="write_coil"></hr>
<p class="mono-title"><mark>bool</mark> WriteCoil(<mark>int32</mark> Address, <mark>bool</mark> Value)</p>

<hr id="write_many_coils"></hr>
<p class="mono-title"><mark>bool</mark> WriteManyCoils(<mark>int32</mark> Address, <mark>TArray&lt;bool&gt;</mark> Values)</p>

<hr id="client_debug_print"></hr>
<p class="mono-title"><mark>void</mark> Client_DebugPrint()</p>

<hr id="begin_destroy"></hr>
<p class="mono-title"><mark>void</mark> BeginDestroy() <i>virtual override</i></p>
