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
UModbusTcpSocket\* **CreateSocket**() *static*

<hr id="begindestroy"></hr>
void **BeginDestroy**() *virtual override*

<hr id="connect"></hr>
bool **Connect**(const FString& Host, int32 Port)

<hr id="read"></hr>
int32 **Read**(uint8* Data, int32 Length, int32 TimeoutMs)

<hr id="write"></hr>
int32 **Write**(const uint8* Data, int32 Length)

<hr id="close"></hr>
void **Close**()
