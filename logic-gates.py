print '|---------------------------------------------|'
print '| Welcome to the Logical Processing Simulator |'
print '|     Choose a Logical  Gate to Simulate      |'
print '|---------------------------------------------|'

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
    print '|----------|'
    print '| AND Gate |'
    print '|----------|'
    
    print '\n'
    
    in_a = input('Input A (use 1 or 0): ')
    in_b = input('Input B (use 1 or 0): ')
    
    print '\n'
    
    print 'In A: {0}'.format(in_a)
    print 'In B: {0}'.format(in_b)
    
    print'\n'
    
    if in_a == '1' and in_b == '1':
        print 'Out: 1'
    else:
        print 'Out: 0'
    
elif gate == '2':
    print '|-----------|'
    print '| NAND Gate |'
    print '|-----------|'
    
    print '\n'
    
    in_a = input('Input A (use 1 or 0): ')
    in_b = input('Input B (use 1 or 0): ')
    
    print '\n'
    
    print 'In A: {0}'.format(in_a)
    print 'In B: {0}'.format(in_b)
    
    print'\n'
    
    if in_a == '1' and in_b == '1':
        print 'Out: 0'
    else:
        print 'Out: 1'
elif gate == '3':
    print '|---------|'
    print '| OR Gate |'
    print '|---------|'
    
    print '\n'
    
    in_a = input('Input A (use 1 or 0): ')
    in_b = input('Input B (use 1 or 0): ')
    
    print '\n'
    
    print 'In A: {0}'.format(in_a)
    print 'In B: {0}'.format(in_b)
    
    print'\n'
    
    if in_a == '0' and in_b == '0':
        print 'Out: 0'
    else:
        print 'Out: 1'
elif gate == '4':
    print '|----------|'
    print '| NOR Gate |'
    print '|----------|'
    
    print '\n'
    
    in_a = input('Input A (use 1 or 0): ')
    in_b = input('Input B (use 1 or 0): ')
    
    print '\n'
    
    print 'In A: {0}'.format(in_a)
    print 'In B: {0}'.format(in_b)
    
    print'\n'
    
    if in_a == '0' and in_b == '0':
        print 'Out: 1'
    else:
        print 'Out: 0'
elif gate == '5':
    print '|------------|'
    print '| EX-OR Gate |'
    print '|------------|'
    
    print '\n'
    
    in_a = input('Input A (use 1 or 0): ')
    in_b = input('Input B (use 1 or 0): ')
    
    print '\n'
    
    print 'In A: {0}'.format(in_a)
    print 'In B: {0}'.format(in_b)
    
    print'\n'
    
    if in_a =='0' and in_b == '0' or in_a == '1' and in_b =='1':
        print 'Out: 0'
    else:
        print 'Out: 1'
elif gate == '6':
    print '|-------------|'
    print '| EX-NOR Gate |'
    print '|-------------|'
    
    print '\n'
    
    in_a = input('Input A (use 1 or 0): ')
    in_b = input('Input B (use 1 or 0): ')
    
    print '\n'
    
    print 'In A: {0}'.format(in_a)
    print 'In B: {0}'.format(in_b)
    
    print'\n'
    
    if in_a =='0' and in_b == '0' or in_a == '1' and in_b == '1':
        print 'Out: 0'
    else:
        print 'Out: 1'
elif gate == '7':
    print '|---------------|'
    print '| INVERTER Gate |'
    print '|---------------|'
    
    print '\n'
    
    in_a = input('Input A (use 1 or 0): ')
    
    print '\n'
    
    print 'In A: {0}'.format(in_a)
    
    print'\n'
    
    if in_a == '1':
        print 'Out: 0'
    else:
        print 'Out: 1'
elif gate == '8':
    print '|-------------|'
    print '| BUFFER Gate |'
    print '|-------------|'
    
    print '\n'
    
    in_a = input('Input A (use 1 or 0): ')
    
    print '\n'
    
    print 'In A: {0}'.format(in_a)
    
    print'\n'
    
    in in_a == '1':
        print 'Out: 1'
    elif in_b == '0':
        print 'Out: 0'
else:
    print 'No such gate exsists.'
