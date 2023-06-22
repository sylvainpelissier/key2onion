# ⚙️ key2onion
![Tests Status](https://github.com/sylvainpelissier/key2onion/actions/workflows/ci.yml/badge.svg?branch=master)

Convert private keys to .onion domains.

## Purpose?

When you place your private key to file named `private_key.pem` at Tor hidden service directory, hostname is generated based on that key (or random if not set). This tool allows you to convert RSA private key to onion domain without necessity to paste key to file and restarting Tor hidden service to see what onion domain stands for that key.

## Usage

`python key2onion.py /path/to/private_key.pem`

File `private_key.pem` has to be in following format (PEM):
```
-----BEGIN PRIVATE KEY-----
MC4CAQAwBQYDK2VwBCIEIFKL9sm9nefA8WlUmWK3KnPjlPdTSVjOzqhmC2xV9VVF
-----END PRIVATE KEY-----
```
Example output:

`q6jfbqd6pqddrsmkwq6xwakxfzfpelmxx3jgzzojhlmrkamo5ln6twad.onion`

For version 2 addresses the usage is:
`python2 key2onion.py -v2 /path/to/private_key.pem`

## Installation
Firstly, install Python 3 and python3-pip. Then git clone this repo and `cd` to it:

`git clone https://github.com/sylvainpelissier/key2onion.git && cd key2onion`

And install requirements from file:

`sudo pip install -r requirements.txt`

## How it works

1. Generate public key based on private key.
2. Convert it to DER format.
3. Calculate hash of that value (byte digest, not hex digest).
4. Crop the hash.
5. Encode it to Base32.
6. Add ".onion" to end.
7. Done!
