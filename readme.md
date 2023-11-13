# M14 - UF1 - SIMULACRE Prova escrita 1

La WHO (OMS) ha quedat impressionada amb les pràctiques que heu realitzat a DAWBIO2 aquest curs i és per això 
que us encarrega realitzar un estudi amb un portal web sobre el dataset adjunt **incidence-rate-2021-raw.csv**
, que recopila la incidència de les enfermetats en tot el món.

Si extraieu gràfics, coneixement i un servei web (una API REST) i sobretot, conclusions rellevants segur que voldran contractar-vos. 

## Explicació del context. Què son aquestes dades? Posar referències.

Representen els ratios d'incidencia de casos de diferents enfermedades contagioses en molts països. 
Aquest ratio està representat pel camp **INCIDENCE_RATE.**

S'utilitzen diverses maneres de calcular aquestes ratios, ho indica el camp **DENOMINATOR.**
No és el mateix mesurar 'per 1,000,000 total population' que ';per 1,000,000 <15 population'

**GROUP** Pot ser un país, una agrupació de països o un estat.

**CODE** és la abreviatura del nom del país/estat/grup en format iso3, útil per crear mapes.

**NAME** el nom complet del país.

**DISEASE** és el nom de la enfermetat. 

Per traduïr alguns cal diccionari:
1. Numps = Paperes
2. Measles = Xarampió
3. Pertussis = tos ferina

**YEAR**: Des de 1980 a 2021

## Estrucuta de l'examen:

### Les 4 primeres preguntes es fan sobre el codi Python:

### Les 3 últimes s'han de fer sobre el projecte web en Flask

### La pregunta 1 compta 1 punt i les altres 1.5 punts

### La nota màxima és de 10 punts.

## Altres Observacions:

#### Cal respectar la estructura del projecte; cada apartat té la seva pròpia funció. Si voleu posar nous fitxers i classes endavant sempre que es respecti.

#### Consulta al professor quan hagis aconseguit cada gràfic que es demana.

#### En casos d'errors excepcionals en el sistema es podrà fer algun apartat amb Jupyter Notebook, previa autorització dels professors.

### Molts ànims!

### Referència:

Dataset extret del portal Inmunization Data, de la WHO (la OMS)

https://immunizationdata.who.int/listing.html?topic=&location=