grammar URL;

url: protocolo? '://' dominio (':' porta)? caminho? query? fragmento?;

protocolo: 'http' | 'https' | 'ftp';

dominio: HOST;

porta: DIGITO+;

caminho: '/' CAMINHO_SEGMENTO+;

query: '?' PARAMETRO ('&' PARAMETRO)*;

fragmento: '#' FRAGMENTO;

HOST: [a-zA-Z0-9.-]+;
DIGITO: [0-9];
CAMINHO_SEGMENTO: [a-zA-Z0-9./_-]+;
PARAMETRO: [a-zA-Z0-9_]+ '=' [a-zA-Z0-9_]+;
FRAGMENTO: [a-zA-Z0-9_]+;
