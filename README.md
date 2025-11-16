# Burrow Wheeler Transform Calculator

## Description

Python code to calculate the burrow wheeler transform equivalent of a given string.

## Quick Start

#### Clone repository in local

```bash
git clone https://github.com/GiZano/burrow-wheeler-calculator.git
```

#### Go in project directory

```bash
cd burrow-wheeler-calculator
```

### BWT Debug

```bash
python ./app/Components/bwt_calculator.py
```

### Terminal App

```bash
python ./app/Terminal/main.py
```

### API App

- Windows

```bash
# Open virtual environment
.venv\Scripts\activate
# Run app
fastapi dev app/API/api.py

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


