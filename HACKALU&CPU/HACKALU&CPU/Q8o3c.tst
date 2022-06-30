load HackComputer.hdl,
output-file Q8o3c.out,
compare-to Q8o3c.cmp,
output-list time%S1.5.1 reset%B2.1.2 ARegister[0]%D1.7.1 DRegister[0]%D1.7.1 PC[]%D0.4.0 RAM16K[16]%D1.7.1 RAM16K[17]%D1.7.1 RAM16K[18]%D1.7.1;

// Load a program written in the Hack machine language. 
ROM32K load Q8o3c.hack,
output;

set reset 0;
repeat 1415 {
    tick, tock;
}
output;