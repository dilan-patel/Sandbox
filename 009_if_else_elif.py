name = input("Identify yourself: ").lower()
if name == 'dilan':
    print('User recognised.')
elif name in ('ekta', 'ashish'):
    print('Friend of user recognised.')
else:
    print('Unrecognised access!')