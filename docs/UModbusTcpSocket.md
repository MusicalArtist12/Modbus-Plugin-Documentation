# UModbusTcpSocket

**Inherits**: UObject

## Methods


| Return | Call |
| --- | --- |
| UModbusTcpSocket* | [CreateSocket](#createsocket)() *static* |
| void | [BeginDestroy](#begindestroy)() *virtual override* |
| bool | [Connect](#connect)(const FString& Host, int32 Port) |
| int32 | [Read](#read)(uint8* Data, int32 Length, int32 TimeoutMs) |
| int32 | [Write](#write)(const uint8* Data, int32 Length) |
| void | [Close](#close)() |

***

<hr id="createsocket"></hr>

<p class="mono-title"><mark>UModbusTcpSocket*</mark> <strong>CreateSocket</strong>() <i>static</i></p>

Creates a new UModbusTcpSocket

<hr id="begindestroy"></hr>

<p class="mono-title"><mark>void</mark> <strong>BeginDestroy</strong>() <i>virtual override</i></p>

Closes the socket before destroying the object.

<hr id="connect"></hr>

<p class="mono-title"><mark>bool</mark> <strong>Connect</strong>(<mark>const FString&</mark> Host, <mark>int32</mark> Port)</p>


Connect to a Modbus Host, returns the connection status.

<hr id="read"></hr>

<p class="mono-title"><mark>int32</mark> <strong>Read</strong>(<mark>uint8*</mark> Data, <mark>int32</mark> Length, <mark>int32</mark> TimeoutMs)</p>

Read data from the socket and writes max Length bytes into Data. Waits TimeoutMs before timing out.

<hr id="write"></hr>

<p class="mono-title"><mark>int32</mark> <strong>Write</strong>(<mark>const uint8*</mark> Data, <mark>int32</mark> Length)</p>

Write Length bytes into the socket from Data

<hr id="close"></hr>

<p class="mono-title"><mark>void</mark> <strong>Close</strong>()</p>

Closes the socket.