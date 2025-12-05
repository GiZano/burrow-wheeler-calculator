# FastAPI BWT Service

## Description

Here you can find the FastAPI version of the application. You can simply execute the server script on the machine and then access the api endpoint to receive back the transformed thanks to the client script.

Check out more:
- <a href='#start'>Quick Start</a>
- <a href='#endp'>Avaiable Endpoints</a>

## <p id='start'> Quick Start </p>

### <p >API App</p>

Navigate in correct folder ... 

```bash
cd .\app\FastAPI
```

#### Server

Navigate in correct folder ...

```bash
cd '.\API Server'
```

- <i>venv opening refers only to windows</i>

```bash
# Open virtual environment
.\.venv\Scripts\activate
# Start Server
fastapi dev .\api.py
```

##### Docker
```bash
# Pull Docker image
docker pull ghcr.io/gizano/burrow-wheeler-transform-server:v1.0.0
# Start Server
docker run -d --name burrow-wheeler-transform-server ghcr.io/gizano/burrow-wheeler-transform-server:v1.0.0
```

#### Client

Navigate in correct folder ...

```bash
cd '.\Client Tester'
```

... and then run the client ...

```bash
# Open virtual environment
.\.venv\Scripts\activate
# Run client
python '.\app\Client Tester\client.py'
```

## <p id='endp'> Avaiable Endpoints </p>

### /calculator/{value}

<strong> Endpoint to calculate the Burrows Wheeler Transformed. </strong>

- <strong>Method</strong>: <i>GET</i>
- <strong>Input</strong>: <i>value</i>
    - String to transform
- <strong>Output</strong>:
    - <i>original</i>: received string
    - <i>encoded</i>: encoded string

### (root) /

<strong> Endpoint to check avaiability of service. </strong>

- <strong>Method</strong>: <i>GET</i>
- <strong>Output</strong>:
    - <i>original</i>: received string
    - <i>encoded</i>: encoded string

### /health

<strong> Endpoint to check service health status. </strong>

- <strong>Method</strong>: <i>GET</i>
- <strong>Output</strong>:
    - <i>original</i>: received string
    - <i>encoded</i>: encoded string