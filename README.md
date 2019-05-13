# Binary ancestor

Given a binary tree, find the nearest common ancestor.

```
                  70
         .--------+-------.
         49               84
    .----+---.        .----+---.
   37        54      78        85
 .--+--.    .+    .---+---.
22     40  51    76       80

```

For example.

Ancestor (40, 78) = 70 <br />
Ancestor (51, 37) = 49


## How to run

Create venv and install dependencies:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run the server

```
python src/server
```

Run the test

```
export PYTHONPATH=src/

```
