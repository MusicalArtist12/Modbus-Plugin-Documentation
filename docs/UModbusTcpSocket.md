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

<BeginDestroy>

<Connect>

<Read>

<Write>

<Close>