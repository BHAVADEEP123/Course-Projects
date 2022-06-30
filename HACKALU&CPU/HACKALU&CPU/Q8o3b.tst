load HackComputer.hdl,
output-file Q8o3b.out,
compare-to Q8o3b.cmp,
output-list time%S1.4.1 reset%B2.1.2 ARegister[0]%D1.7.1 DRegister[0]%D1.7.1 PC[]%D0.4.0 RAM16K[16]%D2.6.2 RAM16K[17]%D2.6.2 RAM16K[18]%D2.6.2;

//Loading the program in Hack machine language
ROM32K load Q8o3b.hack,
output;

set RAM16K[16] 27,
set RAM16K[17] 5,
repeat 14
{
tick, tock;
}
output;

// Reset the PC
set reset 1,
set RAM16K[16] 0;
set RAM16K[17] 0;
set RAM16K[18] 0;
tick, tock;

set reset 0;
set RAM16K[16] 45,
set RAM16K[17] 56,
repeat 14
{
tick, tock;
}
output;

// Reset the PC
set reset 1,
set RAM16K[16] 0;
set RAM16K[17] 0;
set RAM16K[18] 0;
tick, tock;

set reset 0;
set RAM16K[16] 68,
set RAM16K[17] 68,
repeat 14
{
tick, tock;
}
output;

// Reset the PC
set reset 1,
set RAM16K[16] 0;
set RAM16K[17] 0;
set RAM16K[18] 0;
tick, tock;