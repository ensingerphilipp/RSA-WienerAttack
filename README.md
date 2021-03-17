# Wiener´s Attack on RSA
This tool aims to crack RSA private Keys implementing the Attack by Michael J. Wiener.
Tested with Python 3.8

## CommandLine Arguments:
Define the Console Parameters by specifing the RSA public key using its parameters:  
  
  **-n** The RSA - Modulus   
  **-e** public Exponent
    
  More Information on Wiener´s Attack:  
  https://en.wikipedia.org/wiki/Wiener%27s_attack  
  
## Example Usage:
----------------------------------
```python WienerAttackRSA.py -n 90581 -e 17993```  

  Solution:  
  p = 379, q = 239  
  d = 5

----------------------------------

Some more Examples in examples.txt
