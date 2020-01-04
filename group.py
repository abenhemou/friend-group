"""An example of how to represent a group of acquaintances in Python."""

# This is a friend group 
Jill={
    'Age':26,
    'Job':'biologist',
    'relationships' : {'friend': 'Zalika',
    'partner':'John','cousin':'NA','landlord':'NA'}
    }
Zalika={
    'Age':28,
    'Job':'artist',
    'relationships' : {'friend': 'Jill',
    'partner':'NA','cousin':'NA','landlord':'NA'}
    }
John={
    'Age':27,
    'Job':'writer',
    'relationships' : {'friend': 'NA',
    'partner':'Jill','cousin':'NA','landlord':'NA'}
    }
Nash={
    'Age':34,
    'Job':'chef',
    'relationships' : {'friend': 'NA',
    'partner':'NA','cousin':'Jill','landlord':'Zalika'}
    }

people=[Jill,Zalika,Nash,John] 
