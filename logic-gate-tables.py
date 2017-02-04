print '|---------------------------------------------------|'
print '| Welcome to the Logical Processing Table Generator |'
print '|        Choose a Logical   Gate to view it         |'
print '|---------------------------------------------------|'

print'\n'

print '|-----------------------------------------------------|'
print '| 1. AND Gate  2. NAND Gate  3. OR Gate  4. NOR Gate  |'
print '| 5. EX-OR Gate 6. EX-NOR Gatev7. INVERTER  8. BUFFER |'
print '|-----------------------------------------------------|'

print '\n'

gate = input('Choose the gate you want to test: ')

print '\n'
print '\n'

if gate == '1':
    print '|-------------|'
    print '|  AND  Gate  |'
    print '|-------------|'
    print '| A | B | OUT |'
    print '|-------------|'
    print '| 0 | 0 |  0  |'
    print '|-------------|'
    print '| 0 | 1 |  0  |'
    print '|-------------|'
    print '| 1 | 0 |  0  |'
    print '|-------------|'
    print '| 1 | 1 |  1  |'
    print '|-------------|'
    
elif gate == '2':
    print '|-----------|'
    print '| NAND Gate |'
    print '|-----------|'
    
    print '\n'
    
    
elif gate == '3':
    print '|---------|'
    print '| OR Gate |'
    print '|---------|'
    
    print '\n'
    
    
elif gate == '4':
    print '|----------|'
    print '| NOR Gate |'
    print '|----------|'
    
    print '\n'
    
    
elif gate == '5':
    print '|------------|'
    print '| EX-OR Gate |'
    print '|------------|'
    
    print '\n'
    
    
elif gate == '6':
    print '|-------------|'
    print '| EX-NOR Gate |'
    print '|-------------|'
    
    print '\n'
    
    
elif gate == '7':
    print '|---------------|'
    print '| INVERTER Gate |'
    print '|---------------|'
    
    print '\n'
    
    
elif gate == '8':
    print '|-------------|'
    print '| BUFFER Gate |'
    print '|-------------|'
    
    print '\n'
    
    
else:
    print 'No such logic gate table exsists.'
