#Yaml: Yet Another Markup Languange?
#Nah.
#It's 
#YAML: Yaml Ain't Markup Languange.
#Config File, e.g. Github Action, Gitlab CI/CD, Kubernetes Manifest, Docker Compose File.

#YAML Structure
#Scalar: Simple Values, (Py Variables)
#Sequences: list
#Mappings: Couple of key and value(Dictionary)
#It is defined by identation.
#Value Scalar: str, int, float, bool, seq, map, null
"""
YAML Advanced Features
1. Multi line str:
    - Multi line folded str (>)
    - Multi line literal str (|)
2. Anchor & Alias: Reduce duplicates
    (&) Create anchor
    (*) Reference to anchor
3. Tag (!!dataType)
    Tells the parser, the dataType of yaml instance
    nama: !!str "Andi"
    isMarried: !!bool true
    age: !!int 18
"""

#Python can handle 2 types of YAML:
#1. STR filled with yaml valid format
data = 'nama: "Lanny"'

#2. YAML file: .yaml/ /yml filled with yaml file extention.