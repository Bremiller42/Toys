mode_var = True
SYMBOLS = '%Q/JiV@m8<X:CH2N[DI43a)KPOzF|bvnq?G5cp(09rLwYjdhef!k1yo*x}A7^ug{~;,tWl6+&TUEMSRs-Z]$.#B> '

def handleKey(key):
    key = str(key)
    print(key)
    if mode_var:
        key = key[1:] + key[:2]
    else:
        key = key[-2:] + key[:-2]
    key = [key]
    print(key)
    return key
handleKey(123456)