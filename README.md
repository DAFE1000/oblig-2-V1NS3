[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/tKFkieDb)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=23035753)
﻿# DAFE1000-oblig-template

# Vincent Jake Dalisay de los Reyes
## vidal2966@oslomet.no

### Hvordan jeg løste oppgaven:
Så for å se hvor ekstremalpunktene til funskjonen (la oss kalle den F) ligger, må vi derivere den. Utregningen for derivasjonen ligger i Utregning1.png

Så se når F' blir 0 og tegne en fortegnslinje (eller plotte funskjonen og se på når den krysser y = 0)

Deretter plotte uttrykket som viser til punktet (vi kan kalle denne for G)

Jeg brukte python for å plotte både F(x), F'(x) og G(x).

Ifølge grafene (og evt ved å tegne fortegnslinje) ser jeg at F'(x) og G(x) krysser y = 0 på samme sted.

Så det betyr at verdien til x når grafene krysser y = 0, er der toppunktet til F(x) ligger. Det betyr også at punktet er faktisk bestemt ved likningen atan(x) - 4/(x^2-1) = 0.

Siden det er meget upraktisk å vise at både F'(x) og G(x) viser til samme punkt når de krysser y = 0 for hånd, er det best å gjøre dette numerisk eller grafisk.

Jeg valgte grafisk siden det er enklere og mer praktisk.
Siden vi vet at den deriverte må være 0 for at det skal være en ekstremalpunkt (eller terrassepunkt) så kan vi lage en likning f'(x) = 0 og sette toppunktets x-verdi inn. hvis vi vår 0 (eller en tilnærming) er x-verdien korrekt. Samme med g(x) = 0.

For å verifisere at f'(x) og g(x) viser til samme punkt brukte jeg geogebra.

Hvis man ser på geogebra_image.png har jeg satt inn alle tre grafene og man kan da se at graf F'(x) og G(x) krysser hverandre og bytter fortegn på samme sted, 1.69.