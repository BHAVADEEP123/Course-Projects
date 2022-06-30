load HackComputer.hdl,
output-file Q8o3a.out,
compare-to Q8o3a.cmp,
output-list time%S1.4.1 reset%B2.1.2 ARegister[0]%D1.7.1 DRegister[0]%D1.7.1 PC[]%D0.4.0 RAM16K[16]%D1.7.1 RAM16K[17]%D1.7.1 RAM16K[18]%D1.7.1 RAM16K[19]%D1.7.1;

//Loading the program in Hack machine language
ROM32K load Q8o3a.hack,
output;

set reset 0;
set RAM16K[16] 5,
set RAM16K[17] 6,
set RAM16K[18] 7;
repeat 10
{
  tick, tock;
}
output;

// Reset the PC
set reset 1,
set RAM16K[16] 0;
set RAM16K[17] 0;
set RAM16K[18] 0;
set RAM16K[19] 0;
tick, tock;

set reset 0,
set RAM16K[16] 17,
set RAM16K[17] 87,
set RAM16K[18] 25;
repeat 10
{
tick, tock;
}
output;

// Reset the PC
set reset 1,
set RAM16K[16] 0;
set RAM16K[17] 0;
set RAM16K[18] 0;
set RAM16K[19] 0;
tick, tock;

set reset 0,
set RAM16K[16] 237,
set RAM16K[17] 187,
set RAM16K[18] 57;
repeat 10
{
tick, tock;
}
output;

// Reset the PC
set reset 1,
set RAM16K[16] 0;
set RAM16K[17] 0;
set RAM16K[18] 0;
set RAM16K[19] 0;
tick, tock;