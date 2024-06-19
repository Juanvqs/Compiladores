grammar Html;

html
    : element+ EOF
    ;

element
    : menu
    | button
    ;

menu
    : 'MENU' ID ':' LABEL '{' menuOption+ '}'
    ;

menuOption
    : 'OPTION' ID ':' LABEL
    ;

button
    : 'BOTAO' LABEL ':' 'ALERT' '(' STRING ')'
    ;

ID
    : [a-zA-Z_][a-zA-Z0-9_]*
    ;

LABEL
    : '"' .*? '"'
    ;

STRING
    : '\'' .*? '\''
    ;

WS
    : [ \t\n\r]+ -> skip
    ;
