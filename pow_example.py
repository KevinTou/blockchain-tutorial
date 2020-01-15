from hashlib import sha256

x = 5
y = 0  # We don't know what y should be yet

# Find the hash of x * y and check the last character for '0'
while sha256(f'{x * y}'.encode()).hexdigest()[-1] != '0':
    y += 1

print(f'The solution is y = {y}')
'''
print(sha256(f'{5 * 21}'.encode()).hexdigest())

The hash of 5 * 21 is: 1253e9373e781b7500266caa55150e08e210bc8cd8cc70d89985e3600155e860
'''
