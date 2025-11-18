# Burrow Wheeler Transform Calculator

## Description

Python code to calculate the burrow wheeler transform equivalent of a given string.
There are three main ways to use this code:
- <a href="#debug">Debug</a>
- <a href="#terminal">Terminal</a>
- <a href="#api">API server - client</a>

## Quick Start

#### Clone repository in local

```bash
git clone https://github.com/GiZano/burrow-wheeler-calculator.git
```

#### Go in project directory

```bash
cd burrow-wheeler-calculator
```

### <p id="debug">BWT Debug</p>

```bash
python ./app/Components/bwt_calculator.py
```

### <p id="terminal">Terminal App</p>

```bash
python ./app/Terminal/main.py
```

### <p id="api">API App</p>

#### Server

##### Terminal

- <i>venv opening refers only to windows</i>

```bash
# Open virtual environment
.\.venv\Scripts\activate
# Start Server
fastapi dev .\app\API\api.py
```

##### Docker
```bash
# Pull Docker image
docker pull ghcr.io/gizano/burrow-wheeler-transform-server:v1.0.0
# Start Server
docker run -d --name burrow-wheeler-transform-server ghcr.io/gizano/burrow-wheeler-transform-server:v1.0.0
```

#### Client

```bash
# Open virtual environment
.\.venv\Scripts\activate
# Run client
python '.\app\Client Tester\client.py'
```

## Burrow Wheeler Transform Algorithm

Algorithm to make similar character be near to each other,
making it easier to compress the strings afterwhile with other algorithms.

Steps:
1. Concatenate $ character at the end
2. Calculate rotations to the left
3. Sort rotations
4. Build bwt using the last character of each sorted rotation

### Example: "BANANA"

#### 1. Concatenate $ at the end:

BANANA --> BANANA$

#### 2. Calculate rotations to the left

BANANA$:

- BANANA$ 
- ANANA$B
- NANA$BA
- ANA$BAN
- NA$BANA 
- A$BANAN$
- $BANANA

#### 3. Sort rotations

<i>Sorting previous list...</i> :

- $BANANA
- A$BANAN
- ANA$BAN
- ANANA$B
- BANANA$
- NA$BANA
- NANA$BA

#### 4. Build BWT using the last character of each sorted rotation

- $BANAN<strong>A</strong>
- A$BANA<strong>N</strong>
- ANA$BA<strong>N</strong>
- ANANA$<strong>B</strong>
- BANANA<strong>$</strong>
- NA$BAN<strong>A</strong>
- NANA$B<strong>A</strong>

<strong>Transformed: ANNB$AA </strong>

## Mock Data

The mock data, present in "data/input.txt" can be found <a href="https://rest.uniprot.org/uniprotkb/O95905.fasta">here</a>


