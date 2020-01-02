import warnings

dict = {}

if dict:
    print(True)
else:
    warnings.warn(
        'It is empty'
    )
    dict = {}
