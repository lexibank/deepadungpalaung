<a name="ds-cldfmetadatajson"> </a>

# Wordlist CLDF dataset derived from Deepadung et al.'s "Lexical Comparison of Palaung Dialects" from 2015

**CLDF Metadata**: [cldf-metadata.json](./cldf-metadata.json)

**Sources**: [sources.bib](./sources.bib)

property | value
 --- | ---
[dc:bibliographicCitation](http://purl.org/dc/terms/bibliographicCitation) | Deepadung, Sujaritlak; Buakaw, Supakit; and Rattanapitak, Ampica (2015): A lexical comparison of the Palaung dialects spoken in China, Myanmar, and Thailand. Mon-Khmer Studies 44. 19-38.
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF Wordlist](http://cldf.clld.org/v1.0/terms.rdf#Wordlist)
[dc:format](http://purl.org/dc/terms/format) | <ol><li>http://concepticon.clld.org/contributions/Deepadung-2015-100</li></ol>
[dc:license](http://purl.org/dc/terms/license) | https://creativecommons.org/licenses/by/4.0/
[dcat:accessURL](http://www.w3.org/ns/dcat#accessURL) | https://github.com/lexibank/deepadungpalaung
[prov:wasDerivedFrom](http://www.w3.org/ns/prov#wasDerivedFrom) | <ol><li><a href="https://github.com/lexibank/deepadungpalaung/tree/1f8eb9c">lexibank/deepadungpalaung v1.1-2-g1f8eb9c</a></li><li><a href="https://github.com/glottolog/glottolog/tree/v5.1">Glottolog v5.1</a></li><li><a href="git@github.com:concepticon/concepticon-data/tree/v3.3.0">Concepticon v3.3.0</a></li><li><a href="https://github.com/cldf-clts/clts//tree/v2.3.0">CLTS v2.3.0</a></li></ol>
[prov:wasGeneratedBy](http://www.w3.org/ns/prov#wasGeneratedBy) | <ol><li><strong>lingpy-rcParams</strong>: <a href="./lingpy-rcParams.json">lingpy-rcParams.json</a></li><li><strong>python</strong>: 3.13.2</li><li><strong>python-packages</strong>: <a href="./requirements.txt">requirements.txt</a></li></ol>
[rdf:ID](http://www.w3.org/1999/02/22-rdf-syntax-ns#ID) | deepadungpalaung
[rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | http://www.w3.org/ns/dcat#Distribution


## <a name="table-formscsv"></a>Table [forms.csv](./forms.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF FormTable](http://cldf.clld.org/v1.0/terms.rdf#FormTable)
[dc:extent](http://purl.org/dc/terms/extent) | 1584


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Local_ID](http://purl.org/dc/terms/identifier) | `string` | 
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | References [languages.csv::ID](#table-languagescsv)
[Parameter_ID](http://cldf.clld.org/v1.0/terms.rdf#parameterReference) | `string` | References [parameters.csv::ID](#table-parameterscsv)
[Value](http://cldf.clld.org/v1.0/terms.rdf#value) | `string` | 
[Form](http://cldf.clld.org/v1.0/terms.rdf#form) | `string` | 
[Segments](http://cldf.clld.org/v1.0/terms.rdf#segments) | list of `string` (separated by ` `) | 
[Comment](http://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | 
[Source](http://cldf.clld.org/v1.0/terms.rdf#source) | list of `string` (separated by `;`) | References [sources.bib::BibTeX-key](./sources.bib)
`Cognacy` | `string` | 
`Loan` | `boolean` | 
`Graphemes` | `string` | 
`Profile` | `string` | 
`Partial_Cognacy` | `string` | 

## <a name="table-languagescsv"></a>Table [languages.csv](./languages.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF LanguageTable](http://cldf.clld.org/v1.0/terms.rdf#LanguageTable)
[dc:extent](http://purl.org/dc/terms/extent) | 16


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Glottocode](http://cldf.clld.org/v1.0/terms.rdf#glottocode) | `string` | 
`Glottolog_Name` | `string` | 
[ISO639P3code](http://cldf.clld.org/v1.0/terms.rdf#iso639P3code) | `string` | 
[Macroarea](http://cldf.clld.org/v1.0/terms.rdf#macroarea) | `string` | 
[Latitude](http://cldf.clld.org/v1.0/terms.rdf#latitude) | `decimal`<br>&ge; -90<br>&le; 90 | 
[Longitude](http://cldf.clld.org/v1.0/terms.rdf#longitude) | `decimal`<br>&ge; -180<br>&le; 180 | 
`Family` | `string` | 
`SubGroup` | `string` | 
`Location` | `string` | 
`EthnicName` | `string` | 
`Abbreviation` | `string` | 

## <a name="table-parameterscsv"></a>Table [parameters.csv](./parameters.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF ParameterTable](http://cldf.clld.org/v1.0/terms.rdf#ParameterTable)
[dc:extent](http://purl.org/dc/terms/extent) | 100


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Concepticon_ID](http://cldf.clld.org/v1.0/terms.rdf#concepticonReference) | `string` | 
`Concepticon_Gloss` | `string` | 
`Number` | `string` | 

## <a name="table-cognatescsv"></a>Table [cognates.csv](./cognates.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF CognateTable](http://cldf.clld.org/v1.0/terms.rdf#CognateTable)
[dc:extent](http://purl.org/dc/terms/extent) | 1584


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Form_ID](http://cldf.clld.org/v1.0/terms.rdf#formReference) | `string` | References [forms.csv::ID](#table-formscsv)
[Form](http://linguistics-ontology.org/gold/2010/FormUnit) | `string` | 
[Cognateset_ID](http://cldf.clld.org/v1.0/terms.rdf#cognatesetReference) | `string` | 
`Doubt` | `boolean` | 
`Cognate_Detection_Method` | `string` | 
[Source](http://cldf.clld.org/v1.0/terms.rdf#source) | list of `string` (separated by `;`) | References [sources.bib::BibTeX-key](./sources.bib)
[Alignment](http://cldf.clld.org/v1.0/terms.rdf#alignment) | list of `string` (separated by ` `) | 
`Alignment_Method` | `string` | 
`Alignment_Source` | `string` | 

