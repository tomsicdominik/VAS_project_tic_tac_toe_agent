# VAS_project_tic_tac_toe_agent


Za pokretanje programa potrebno je imati instaliran Python verziju 3.7. i slijedeće pakete: "spade", "random",
"time", "sys" i "json" (samo spade treba posebno instalirati).

Za pokretanje agenata koji će igrati igru treba se s 2 različita command prompta pozicionirati na lokaciju samog programa
i zatim u svakom od njih pokrenuti Pythong skriptu main.py s parametrima za svakog agenta:
• svoju adresu
• svoju lozinku
• startni potez (je li agent prvi ili drugi na redu)
• oznaku taktike kojom ce igrati ´
• adresu suparnika

Važna napomena jest da se agent koji igra drugi mora pokrenuti prvi.
Primjer komandi za pokretanje agenata:
Agent koji igra drugi: 
python main.py dtomsic@rec.foi.hr lozinka123 2 4 dtomsic2@rec.foi.hr
Agent koji igra prvi:
python main.py dtomsic2@rec.foi.hr lozinka123 1 5 dtomsic@rec.foi.hr
