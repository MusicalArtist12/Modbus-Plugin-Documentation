---

functions:
    CreateSocket:
        output: UModbusTcpSocket*
        inputs: []
        annotations:
            - static

    BeginDestroy:
        output: void
        inputs: []
        annotations:
            - override
            - virtual

    Connect:
        output: bool
        inputs:
            - const FString& Host
            - int32 Port

    Read:
        output: int32
        inputs:
            - uint8* Data
            - int32 Length
            - int32 TimeoutMs

    Write:
        output: int32
        inputs:
            - const uint8* Data
            - int32 Length

    Close:
        output: void
        inputs: []
---
# UModbusTcpSocket

**Inherits**: [UObject](https://dev.epicgames.com/documentation/unreal-engine/API/Runtime/CoreUObject/UObject)

## Methods

<HEADER>


## Method Descriptions

<CreateSocket>

Creates a UModbusTcpSocket.

<BeginDestroy>

Ensures that the socket is closed before the object is freed.

<Connect>

Uses [ISocketSubsystem](https://dev.epicgames.com/documentation/unreal-engine/API/Runtime/Sockets/ISocketSubsystem) to create a socket and configure it. `localhost` is replaced with `127.0.0.1`. Returns `true` if the port sucessfully connects.

<Read>

Read data from the socket. Returns the number of bytes read.

<Write>

Writes `Length` bytes from `Data` onto the socket. Returns the number of bytes written if sucessful and `-1` if it fails.

<Close>

Closes the socket.