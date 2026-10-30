# TCP Socket Programming in Python

A small client-server exercise using Python's standard `socket` and `threading` modules. The server sends arithmetic questions, the client calculates answers, and the server returns a completion flag.

## Implemented behavior

- TCP connections on `127.0.0.1:8888`.
- A separate thread for each accepted client connection.
- A simple `HELLO`, `MATH`, `ANSWER`, and `DONE` message exchange.
- Client-side connection and timeout handling.

This is a local learning exercise. Concurrent-client capacity and throughput have not been benchmarked.

## Requirements

Python 3; no third-party packages are required.

## Setup

```bash
git clone https://github.com/Jeevanandh32/SOCKET-PROGRAMMING-IN-PYTHON.git
cd SOCKET-PROGRAMMING-IN-PYTHON
```

## Run

In one terminal, start the server:

```bash
python3 Server.py
```

In another terminal, start the client and enter a username when prompted:

```bash
python3 Client.py
```

The filenames are case-sensitive on Linux. Both scripts currently use loopback, so run them on the same machine. Additional client terminals exercise the server's per-connection threading.

## Files

| File | Purpose |
|---|---|
| `Server.py` | Accept connections, send questions, and issue a completion flag |
| `Client.py` | Introduce the client, solve arithmetic questions, and display the flag |

## Current limits

- The server records submitted answers but does not validate their correctness.
- Division uses integer division.
- Messages rely on individual `recv()` calls; explicit buffering and message framing are future improvements.
- Malformed-input handling and server-side disconnect recovery are incomplete. The current code does not establish production scalability or robustness.
