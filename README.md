# valid_MAC_generator
Generate random MAC addresses with a valid manufacturer prefix. The manufacturer prefixes are obtained from *oui.csv* which is available from IEEE at https://regauth.standards.ieee.org/standards-ra-web/pub/view.html#registries

*serializeCSV.py* consumes oui.csv and creates a Python List object, serialized it and saves it to a file. This is to improve the performance of *validMAC.py*

*validMAC.py* picks a random manufacturer prefix and concatinates it to a randomly generated suffix

## Dependencies
The only dependency is Python, the two scripts assume **python3.5** is available, if it is not change the first line of each file to the version of Python available on the system.

## The two files must be made executable with:
```bash
chmod +x serializeCSV.py
chmod +x validMAC.py
```
## This is how you use them:
```
./serializeCSV.py --csv=oui.csv --file=serObj
./validMAC.py --list=serObj
```
## Output
the output is a single MAC address sent to stdout with each octet separated by colons like this **01:23:45:67:89:AB**
