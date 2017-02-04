println('|-------------------------------------------- |');
println('| Welcome to the Logical Processing Simulator |');
println('|     Choose a Logical  Gate to Simulate      |');
println('|-------------------------------------------- |');

println('\n');

println('|-----------------------------------------------------|');
println('| 1. AND Gate  2. NAND Gate  3. OR Gate  4. NOR Gate  |');
println('| 5. EX-OR Gate 6. EX-NOR Gatev7. INVERTER  8. BUFFER |');
println('|-----------------------------------------------------|');

println('\n');

var gate = readLine('Choose the gat you want to test: ');

println('\n');
println('\n');

if (gate == '1'){
    println('|----------|');
    println('| AND Gate |');
    println('|----------|');
    
    println('\n');
    
    var in_a = readLine('Input A (use 1 or 0): ');
    var in_b = readLine('Input B (use 1 or 0): ');
    
    println('\n');
    
    println('In A: ' + in_a);
    println('In B: ' + in_b);
    
    println('\n');
    
    if (in_a == '1' && in_b == '1'){
        println('Out: 1');
    }else{
        println('Out: 0');
    }
}else if (gate == '2'){
    println('|-----------|');
    println('| NAND Gate |');
    println('|-----------|');
    
    println('\n');
    
    var in_a = readLine('Input A (use 1 or 0): ');
    var in_b = readLine('Input B (use 1 or 0): ');
    
    println('\n');
    
    println('In A: ' + in_a);
    println('In B: ' + in_b);
    
    println('\n');
    
    if (in_a == '1' && in_b == '1'){
        println('Out: 0');
    }else{
        println('Out: 1');
    }
}else if (gate == '3'){
    println('|---------|');
    println('| OR Gate |');
    println('|---------|');
    
    println('\n');
    
    var in_a = readLine('Input A (use 1 or 0): ');
    var in_b = readLine('Input B (use 1 or 0): ');
    
    println('\n');
    
    println('In A: ' + in_a);
    println('In B: ' + in_b);
    
    println('\n');
    
    if (in_a == '0' && in_b == '0'){
        println('Out: 0');
    }else{
        println('Out: 1');
    }
}else if (gate == '4'){
    
}
