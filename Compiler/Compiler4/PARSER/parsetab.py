
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD ASSIGN BOOLEAN CHAR CHARACTER CLASS CLOSEAKOL CLOSEBRACKET CLOSEPAR COMMA DIVIDE DOT DOUBLE ELSE EQUALS FALSE FLOAT FOR GREATEREQUAL GREATERTHAN ID IF INT LESSEQUAL LESSTHAN MEQUAL MINUS MULT NEW NOTEQUAL NULL NUMBER OPENAKOL OPENBRACKET OPENPAR PEQUAL PLUSPLUS PRIVATE PUBLIC RETURN SEMI STATIC STRING THIS TRUE VOID WHILEPROGRAM : ZZ : CLASSDECLARATION Z\n       Z : EMPTYCLASSDECLARATION : CLASS ID OPENAKOL A CLOSEAKOLA : FIELDDECLARATION A\n         | METHODDECLARATION A\n         | EMPTYFIELDDECLARATION : DECLARATORS ID SEMI\n       FIELDDECLARATION : STATEMENTMETHODDECLARATION : DECLARATORS ID OPENPAR PARAMERERLIST CLOSEPAR OPENAKOL B RETURN EXPRESSION SEMI CLOSEAKOL\n       METHODDECLARATION : DECLARATORS ID OPENPAR CLOSEPAR OPENAKOL B RETURN EXPRESSION SEMI CLOSEAKOL\n       METHODDECLARATION : DECLARATORS ID OPENPAR PARAMERERLIST CLOSEPAR OPENAKOL B CLOSEAKOL\n       METHODDECLARATION : DECLARATORS ID OPENPAR  CLOSEPAR OPENAKOL B CLOSEAKOLB : STATEMENT B\n         | EMPTYDECLARATORS : C STATIC TYPE\n       DECLARATORS : STATIC TYPE\n       DECLARATORS : C TYPE\n       DECLARATORS : TYPEC : PUBLIC\n       C : PRIVATEEMPTY :TYPE : PRIMTYPE\n       TYPE : CLASSTYPE\n       TYPE : ARRTYPEPRIMTYPE : INT\n       PRIMTYPE : BOOLEAN\n       PRIMTYPE : STRING\n       PRIMTYPE : DOUBLE\n       PRIMTYPE : CHARACTER\n       PRIMTYPE : FLOAT\n       PRIMTYPE : VOIDCLASSTYPE : ID ARRTYPE : INT OPENBRACKET CLOSEBRACKET\n       ARRTYPE : CLASSTYPE OPENBRACKET CLOSEBRACKETPARAMERERLIST : TYPE ID DD : COMMA TYPE ID D\n       D : EMPTYARGUMENTLIST : EXPRESSION EE : COMMA EXPRESSION\n       E : EMPTYREFERENCE : THIS G\n       REFERENCE : ID G G : DOT ID G\n       G : EMPTYSTATEMENT : OPENAKOL H CLOSEAKOL\n       STATEMENT : EXPRESSION\n       STATEMENT : REFERENCE OPENBRACKET EXPRESSION CLOSEBRACKET ASSIGN EXPRESSION SEMI\n       STATEMENT : REFERENCE ASSIGN EXPRESSION SEMI\n       STATEMENT : REFERENCE OPENPAR CLOSEPAR SEMI\n       STATEMENT : REFERENCE OPENPAR ARGUMENTLIST CLOSEPAR SEMI\n       STATEMENT : IF OPENPAR EXPRESSION CLOSEPAR STATEMENT ELSE STATEMENT\n       STATEMENT : IF OPENPAR EXPRESSION CLOSEPAR STATEMENT\n       STATEMENT : FOR OPENPAR EXPRESSION CLOSEPAR STATEMENT\n       STATEMENT : WHILE OPENPAR EXPRESSION CLOSEPAR STATEMENTH : STATEMENT H\n       H : EMPTYEXPRESSION : EXPRESSION1\n                  | EXPRESSION2\n                  | EXPRESSION3\n                  | EXPRESSION4\n                  | EXPRESSION5\n                  | EXPRESSION6EXPRESSION1 : ID ASSIGN ID OP ID SEMIEXPRESSION2 : TYPE ID ASSIGN ID OP ID SEMIEXPRESSION3 : TYPE ID SEMIEXPRESSION4 : TYPE ID ASSIGN VALUE SEMIEXPRESSION5 : ID ASSIGN VALUE SEMIVALUE : VALUE1\n             | VALUE2VALUE1 : NUMBERVALUE2 : CHAREXPRESSION6 : TRUE\n       EXPRESSION6 : FALSE\n       EXPRESSION6 : NULL\n       EXPRESSION6 : ID\n       EXPRESSION6 : VALUE\n       EXPRESSION6 : TYPE ID ASSIGN EXPRESSION OP EXPRESSION SEMI\n       EXPRESSION6 : ID ASSIGN ID OP ID OP ID SEMI\n       EXPRESSION6 : EMPTY\n       EXPRESSION6 : REFERENCE ASSIGN NUMBER SEMI REFERENCE OP REFERENCE SEMI IOP : LESSEQUAL\n          | ASSIGN\n          | EQUALS\n          | GREATEREQUAL\n          | GREATERTHAN\n          | LESSTHAN\n          | ADD\n          | MINUS\n          | MULT\n          | NOTEQUAL\n          | DIVIDE\n          | PEQUAL\n          | MEQUAL\n          | PLUSPLUSI : REFERENCE OP\n       | REFERENCE OP NUMBER\n       | REFERENCE OP REFERENCE'
    
_lr_action_items = {'CLASS':([0,3,61,],[5,5,-4,]),'$end':([0,1,2,3,4,6,61,],[-22,0,-1,-22,-3,-2,-4,]),'ID':([5,8,9,10,12,13,14,15,16,17,18,19,20,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,57,58,59,60,65,66,67,68,70,71,72,73,74,75,77,81,82,84,85,86,87,88,91,92,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,122,123,128,129,130,133,135,136,137,140,142,143,144,145,147,149,150,152,153,154,155,156,157,159,160,162,167,168,171,172,174,175,176,177,179,180,181,182,185,190,192,193,194,195,196,],[7,9,-33,59,9,9,-80,64,-9,-47,67,67,69,-20,-21,-23,-24,-25,-58,-59,-60,-61,-62,-63,-22,-26,-27,-28,-29,-30,-31,-32,-77,-73,-74,-75,-71,-69,-70,-72,-43,79,81,-45,59,-80,-33,69,67,-18,-33,-17,91,91,91,91,91,91,-42,-22,-46,-8,67,-16,123,-66,-33,-80,-35,-34,-83,138,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,141,-33,-49,149,-50,91,59,59,59,59,79,164,-67,91,91,-22,-51,-53,-54,-55,169,-64,59,59,-80,67,149,59,91,-13,184,-65,-78,-48,-52,-79,91,-12,149,-81,-11,149,-10,-98,-97,]),'OPENAKOL':([7,8,9,10,12,13,14,16,17,30,31,32,33,34,35,36,44,45,46,47,48,49,50,51,52,55,57,58,59,77,81,82,84,88,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,121,128,130,135,136,137,139,140,144,149,150,152,153,154,156,157,159,160,168,172,175,176,177,179,180,182,190,192,193,194,195,196,],[8,10,-76,10,10,10,-80,-9,-47,-58,-59,-60,-61,-62,-63,-22,-77,-73,-74,-75,-71,-69,-70,-72,-43,-45,10,-80,-76,-42,-22,-46,-8,-66,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,140,-49,-50,10,10,10,157,10,-67,-22,-51,-53,-54,-55,-64,10,10,-80,10,-13,-65,-78,-48,-52,-79,-12,-81,-11,-96,-10,-98,-97,]),'CLOSEAKOL':([8,9,10,11,12,13,14,16,17,30,31,32,33,34,35,36,44,45,46,47,48,49,50,51,52,55,56,57,58,59,62,63,77,81,82,83,84,88,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,128,130,135,136,137,140,144,149,150,152,153,154,156,157,158,159,160,168,170,172,173,175,176,177,179,180,182,187,190,191,192,193,194,195,196,],[-22,-76,-22,61,-22,-22,-7,-9,-47,-58,-59,-60,-61,-62,-63,-22,-77,-73,-74,-75,-71,-69,-70,-72,-43,-45,82,-22,-57,-76,-5,-6,-42,-22,-46,-56,-8,-66,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,-49,-50,-22,-22,-22,-22,-67,-22,-51,-53,-54,-55,-64,-22,172,-22,-15,-22,182,-13,-14,-65,-78,-48,-52,-79,-12,192,-81,194,-11,-96,-10,-98,-97,]),'STATIC':([8,9,12,13,14,16,17,18,25,26,30,31,32,33,34,35,36,44,45,46,47,48,49,50,51,52,55,59,77,81,82,84,88,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,128,130,135,136,137,144,149,150,152,153,154,156,168,172,175,176,177,179,180,182,190,192,193,194,195,196,],[19,-76,19,19,-80,-9,-47,65,-20,-21,-58,-59,-60,-61,-62,-63,-22,-77,-73,-74,-75,-71,-69,-70,-72,-43,-45,-76,-42,-22,-46,-8,-66,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,-49,-50,-22,-22,-22,-67,-22,-51,-53,-54,-55,-64,-22,-13,-65,-78,-48,-52,-79,-12,-81,-11,-96,-10,-98,-97,]),'IF':([8,9,10,12,13,14,16,17,30,31,32,33,34,35,36,44,45,46,47,48,49,50,51,52,55,57,58,59,77,81,82,84,88,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,128,130,135,136,137,140,144,149,150,152,153,154,156,157,159,160,168,172,175,176,177,179,180,182,190,192,193,194,195,196,],[22,-76,22,22,22,-80,-9,-47,-58,-59,-60,-61,-62,-63,-22,-77,-73,-74,-75,-71,-69,-70,-72,-43,-45,22,-80,-76,-42,-22,-46,-8,-66,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,-49,-50,22,22,22,22,-67,-22,-51,-53,-54,-55,-64,22,22,-80,22,-13,-65,-78,-48,-52,-79,-12,-81,-11,-96,-10,-98,-97,]),'FOR':([8,9,10,12,13,14,16,17,30,31,32,33,34,35,36,44,45,46,47,48,49,50,51,52,55,57,58,59,77,81,82,84,88,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,128,130,135,136,137,140,144,149,150,152,153,154,156,157,159,160,168,172,175,176,177,179,180,182,190,192,193,194,195,196,],[23,-76,23,23,23,-80,-9,-47,-58,-59,-60,-61,-62,-63,-22,-77,-73,-74,-75,-71,-69,-70,-72,-43,-45,23,-80,-76,-42,-22,-46,-8,-66,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,-49,-50,23,23,23,23,-67,-22,-51,-53,-54,-55,-64,23,23,-80,23,-13,-65,-78,-48,-52,-79,-12,-81,-11,-96,-10,-98,-97,]),'WHILE':([8,9,10,12,13,14,16,17,30,31,32,33,34,35,36,44,45,46,47,48,49,50,51,52,55,57,58,59,77,81,82,84,88,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,128,130,135,136,137,140,144,149,150,152,153,154,156,157,159,160,168,172,175,176,177,179,180,182,190,192,193,194,195,196,],[24,-76,24,24,24,-80,-9,-47,-58,-59,-60,-61,-62,-63,-22,-77,-73,-74,-75,-71,-69,-70,-72,-43,-45,24,-80,-76,-42,-22,-46,-8,-66,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,-49,-50,24,24,24,24,-67,-22,-51,-53,-54,-55,-64,24,24,-80,24,-13,-65,-78,-48,-52,-79,-12,-81,-11,-96,-10,-98,-97,]),'PUBLIC':([8,9,12,13,14,16,17,30,31,32,33,34,35,36,44,45,46,47,48,49,50,51,52,55,59,77,81,82,84,88,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,128,130,135,136,137,144,149,150,152,153,154,156,168,172,175,176,177,179,180,182,190,192,193,194,195,196,],[25,-76,25,25,-80,-9,-47,-58,-59,-60,-61,-62,-63,-22,-77,-73,-74,-75,-71,-69,-70,-72,-43,-45,-76,-42,-22,-46,-8,-66,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,-49,-50,-22,-22,-22,-67,-22,-51,-53,-54,-55,-64,-22,-13,-65,-78,-48,-52,-79,-12,-81,-11,-96,-10,-98,-97,]),'PRIVATE':([8,9,12,13,14,16,17,30,31,32,33,34,35,36,44,45,46,47,48,49,50,51,52,55,59,77,81,82,84,88,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,128,130,135,136,137,144,149,150,152,153,154,156,168,172,175,176,177,179,180,182,190,192,193,194,195,196,],[26,-76,26,26,-80,-9,-47,-58,-59,-60,-61,-62,-63,-22,-77,-73,-74,-75,-71,-69,-70,-72,-43,-45,-76,-42,-22,-46,-8,-66,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,-49,-50,-22,-22,-22,-67,-22,-51,-53,-54,-55,-64,-22,-13,-65,-78,-48,-52,-79,-12,-81,-11,-96,-10,-98,-97,]),'THIS':([8,9,10,12,13,14,16,17,30,31,32,33,34,35,36,44,45,46,47,48,49,50,51,52,55,57,58,59,70,71,72,73,74,75,77,81,82,84,87,88,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,128,129,130,133,135,136,137,140,144,145,147,149,150,152,153,154,156,157,159,160,167,168,171,172,175,176,177,179,180,181,182,185,190,192,193,194,195,196,],[36,-76,36,36,36,-80,-9,-47,-58,-59,-60,-61,-62,-63,-22,-77,-73,-74,-75,-71,-69,-70,-72,-43,-45,36,-80,-76,36,36,36,36,36,36,-42,-22,-46,-8,36,-66,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,-49,36,-50,36,36,36,36,36,-67,36,36,-22,-51,-53,-54,-55,-64,36,36,-80,36,36,36,-13,-65,-78,-48,-52,-79,36,-12,36,-81,-11,36,-10,-98,-97,]),'INT':([8,9,10,12,13,14,16,17,18,19,25,26,30,31,32,33,34,35,36,44,45,46,47,48,49,50,51,52,55,57,58,59,65,70,71,72,73,74,75,77,81,82,84,85,87,88,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,128,130,133,135,136,137,140,144,145,147,149,150,152,153,154,156,157,159,160,162,168,171,172,175,176,177,179,180,181,182,190,192,193,194,195,196,],[37,-76,37,37,37,-80,-9,-47,37,37,-20,-21,-58,-59,-60,-61,-62,-63,-22,-77,-73,-74,-75,-71,-69,-70,-72,-43,-45,37,-80,-76,37,37,37,37,37,37,37,-42,-22,-46,-8,37,37,-66,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,-49,-50,37,37,37,37,37,-67,37,37,-22,-51,-53,-54,-55,-64,37,37,-80,37,37,37,-13,-65,-78,-48,-52,-79,37,-12,-81,-11,-96,-10,-98,-97,]),'BOOLEAN':([8,9,10,12,13,14,16,17,18,19,25,26,30,31,32,33,34,35,36,44,45,46,47,48,49,50,51,52,55,57,58,59,65,70,71,72,73,74,75,77,81,82,84,85,87,88,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,128,130,133,135,136,137,140,144,145,147,149,150,152,153,154,156,157,159,160,162,168,171,172,175,176,177,179,180,181,182,190,192,193,194,195,196,],[38,-76,38,38,38,-80,-9,-47,38,38,-20,-21,-58,-59,-60,-61,-62,-63,-22,-77,-73,-74,-75,-71,-69,-70,-72,-43,-45,38,-80,-76,38,38,38,38,38,38,38,-42,-22,-46,-8,38,38,-66,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,-49,-50,38,38,38,38,38,-67,38,38,-22,-51,-53,-54,-55,-64,38,38,-80,38,38,38,-13,-65,-78,-48,-52,-79,38,-12,-81,-11,-96,-10,-98,-97,]),'STRING':([8,9,10,12,13,14,16,17,18,19,25,26,30,31,32,33,34,35,36,44,45,46,47,48,49,50,51,52,55,57,58,59,65,70,71,72,73,74,75,77,81,82,84,85,87,88,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,128,130,133,135,136,137,140,144,145,147,149,150,152,153,154,156,157,159,160,162,168,171,172,175,176,177,179,180,181,182,190,192,193,194,195,196,],[39,-76,39,39,39,-80,-9,-47,39,39,-20,-21,-58,-59,-60,-61,-62,-63,-22,-77,-73,-74,-75,-71,-69,-70,-72,-43,-45,39,-80,-76,39,39,39,39,39,39,39,-42,-22,-46,-8,39,39,-66,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,-49,-50,39,39,39,39,39,-67,39,39,-22,-51,-53,-54,-55,-64,39,39,-80,39,39,39,-13,-65,-78,-48,-52,-79,39,-12,-81,-11,-96,-10,-98,-97,]),'DOUBLE':([8,9,10,12,13,14,16,17,18,19,25,26,30,31,32,33,34,35,36,44,45,46,47,48,49,50,51,52,55,57,58,59,65,70,71,72,73,74,75,77,81,82,84,85,87,88,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,128,130,133,135,136,137,140,144,145,147,149,150,152,153,154,156,157,159,160,162,168,171,172,175,176,177,179,180,181,182,190,192,193,194,195,196,],[40,-76,40,40,40,-80,-9,-47,40,40,-20,-21,-58,-59,-60,-61,-62,-63,-22,-77,-73,-74,-75,-71,-69,-70,-72,-43,-45,40,-80,-76,40,40,40,40,40,40,40,-42,-22,-46,-8,40,40,-66,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,-49,-50,40,40,40,40,40,-67,40,40,-22,-51,-53,-54,-55,-64,40,40,-80,40,40,40,-13,-65,-78,-48,-52,-79,40,-12,-81,-11,-96,-10,-98,-97,]),'CHARACTER':([8,9,10,12,13,14,16,17,18,19,25,26,30,31,32,33,34,35,36,44,45,46,47,48,49,50,51,52,55,57,58,59,65,70,71,72,73,74,75,77,81,82,84,85,87,88,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,128,130,133,135,136,137,140,144,145,147,149,150,152,153,154,156,157,159,160,162,168,171,172,175,176,177,179,180,181,182,190,192,193,194,195,196,],[41,-76,41,41,41,-80,-9,-47,41,41,-20,-21,-58,-59,-60,-61,-62,-63,-22,-77,-73,-74,-75,-71,-69,-70,-72,-43,-45,41,-80,-76,41,41,41,41,41,41,41,-42,-22,-46,-8,41,41,-66,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,-49,-50,41,41,41,41,41,-67,41,41,-22,-51,-53,-54,-55,-64,41,41,-80,41,41,41,-13,-65,-78,-48,-52,-79,41,-12,-81,-11,-96,-10,-98,-97,]),'FLOAT':([8,9,10,12,13,14,16,17,18,19,25,26,30,31,32,33,34,35,36,44,45,46,47,48,49,50,51,52,55,57,58,59,65,70,71,72,73,74,75,77,81,82,84,85,87,88,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,128,130,133,135,136,137,140,144,145,147,149,150,152,153,154,156,157,159,160,162,168,171,172,175,176,177,179,180,181,182,190,192,193,194,195,196,],[42,-76,42,42,42,-80,-9,-47,42,42,-20,-21,-58,-59,-60,-61,-62,-63,-22,-77,-73,-74,-75,-71,-69,-70,-72,-43,-45,42,-80,-76,42,42,42,42,42,42,42,-42,-22,-46,-8,42,42,-66,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,-49,-50,42,42,42,42,42,-67,42,42,-22,-51,-53,-54,-55,-64,42,42,-80,42,42,42,-13,-65,-78,-48,-52,-79,42,-12,-81,-11,-96,-10,-98,-97,]),'VOID':([8,9,10,12,13,14,16,17,18,19,25,26,30,31,32,33,34,35,36,44,45,46,47,48,49,50,51,52,55,57,58,59,65,70,71,72,73,74,75,77,81,82,84,85,87,88,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,128,130,133,135,136,137,140,144,145,147,149,150,152,153,154,156,157,159,160,162,168,171,172,175,176,177,179,180,181,182,190,192,193,194,195,196,],[43,-76,43,43,43,-80,-9,-47,43,43,-20,-21,-58,-59,-60,-61,-62,-63,-22,-77,-73,-74,-75,-71,-69,-70,-72,-43,-45,43,-80,-76,43,43,43,43,43,43,43,-42,-22,-46,-8,43,43,-66,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,-49,-50,43,43,43,43,43,-67,43,43,-22,-51,-53,-54,-55,-64,43,43,-80,43,43,43,-13,-65,-78,-48,-52,-79,43,-12,-81,-11,-96,-10,-98,-97,]),'TRUE':([8,9,10,12,13,14,16,17,30,31,32,33,34,35,36,44,45,46,47,48,49,50,51,52,55,57,58,59,70,71,72,73,74,75,77,81,82,84,87,88,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,128,130,133,135,136,137,140,144,145,147,149,150,152,153,154,156,157,159,160,168,171,172,175,176,177,179,180,181,182,190,192,193,194,195,196,],[45,-76,45,45,45,-80,-9,-47,-58,-59,-60,-61,-62,-63,-22,-77,-73,-74,-75,-71,-69,-70,-72,-43,-45,45,-80,-76,45,45,45,45,45,45,-42,-22,-46,-8,45,-66,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,-49,-50,45,45,45,45,45,-67,45,45,-22,-51,-53,-54,-55,-64,45,45,-80,45,45,-13,-65,-78,-48,-52,-79,45,-12,-81,-11,-96,-10,-98,-97,]),'FALSE':([8,9,10,12,13,14,16,17,30,31,32,33,34,35,36,44,45,46,47,48,49,50,51,52,55,57,58,59,70,71,72,73,74,75,77,81,82,84,87,88,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,128,130,133,135,136,137,140,144,145,147,149,150,152,153,154,156,157,159,160,168,171,172,175,176,177,179,180,181,182,190,192,193,194,195,196,],[46,-76,46,46,46,-80,-9,-47,-58,-59,-60,-61,-62,-63,-22,-77,-73,-74,-75,-71,-69,-70,-72,-43,-45,46,-80,-76,46,46,46,46,46,46,-42,-22,-46,-8,46,-66,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,-49,-50,46,46,46,46,46,-67,46,46,-22,-51,-53,-54,-55,-64,46,46,-80,46,46,-13,-65,-78,-48,-52,-79,46,-12,-81,-11,-96,-10,-98,-97,]),'NULL':([8,9,10,12,13,14,16,17,30,31,32,33,34,35,36,44,45,46,47,48,49,50,51,52,55,57,58,59,70,71,72,73,74,75,77,81,82,84,87,88,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,128,130,133,135,136,137,140,144,145,147,149,150,152,153,154,156,157,159,160,168,171,172,175,176,177,179,180,181,182,190,192,193,194,195,196,],[47,-76,47,47,47,-80,-9,-47,-58,-59,-60,-61,-62,-63,-22,-77,-73,-74,-75,-71,-69,-70,-72,-43,-45,47,-80,-76,47,47,47,47,47,47,-42,-22,-46,-8,47,-66,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,-49,-50,47,47,47,47,47,-67,47,47,-22,-51,-53,-54,-55,-64,47,47,-80,47,47,-13,-65,-78,-48,-52,-79,47,-12,-81,-11,-96,-10,-98,-97,]),'NUMBER':([8,9,10,12,13,14,16,17,30,31,32,33,34,35,36,44,45,46,47,48,49,50,51,52,53,55,57,58,59,70,71,72,73,74,75,77,81,82,84,87,88,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,126,128,130,133,135,136,137,140,142,144,145,147,149,150,152,153,154,156,157,159,160,168,171,172,175,176,177,179,180,181,182,190,192,193,194,195,196,],[48,-76,48,48,48,-80,-9,-47,-58,-59,-60,-61,-62,-63,-22,-77,-73,-74,-75,-71,-69,-70,-72,-43,48,-45,48,-80,-76,48,94,48,48,48,48,-42,-22,-46,-8,48,-66,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,146,-49,-50,48,48,48,48,48,48,-67,48,48,-22,-51,-53,-54,-55,-64,48,48,-80,48,48,-13,-65,-78,-48,-52,-79,48,-12,-81,-11,196,-10,-98,-97,]),'CHAR':([8,9,10,12,13,14,16,17,30,31,32,33,34,35,36,44,45,46,47,48,49,50,51,52,53,55,57,58,59,70,71,72,73,74,75,77,81,82,84,87,88,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,128,130,133,135,136,137,140,142,144,145,147,149,150,152,153,154,156,157,159,160,168,171,172,175,176,177,179,180,181,182,190,192,193,194,195,196,],[51,-76,51,51,51,-80,-9,-47,-58,-59,-60,-61,-62,-63,-22,-77,-73,-74,-75,-71,-69,-70,-72,-43,51,-45,51,-80,-76,51,51,51,51,51,51,-42,-22,-46,-8,51,-66,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,-49,-50,51,51,51,51,51,51,-67,51,51,-22,-51,-53,-54,-55,-64,51,51,-80,51,51,-13,-65,-78,-48,-52,-79,51,-12,-81,-11,-96,-10,-98,-97,]),'OPENBRACKET':([9,21,28,36,37,52,55,59,67,77,81,91,119,123,],[-22,70,76,-22,78,-43,-45,-22,-33,-42,-22,-33,-44,-33,]),'ASSIGN':([9,21,30,31,32,33,34,35,36,45,46,47,48,49,50,51,52,55,59,69,77,79,81,87,88,89,91,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,123,124,125,127,138,144,148,149,156,175,176,180,189,190,193,195,196,],[53,71,-58,-59,-60,-61,-62,-63,-22,-73,-74,-75,-71,-69,-70,-72,-43,-45,53,87,-42,103,-22,-22,-66,126,53,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,142,-77,103,147,103,-67,103,-22,-64,-65,-78,-79,103,-81,-96,-98,-97,]),'DOT':([9,36,59,81,91,123,149,],[54,54,54,54,54,54,54,]),'OPENPAR':([9,21,22,23,24,36,52,55,59,64,77,81,119,],[-22,72,73,74,75,-22,-43,-45,-22,85,-42,-22,-44,]),'ELSE':([17,30,31,32,33,34,35,36,44,45,46,47,48,49,50,51,52,55,59,77,81,82,88,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,128,130,135,136,137,144,149,150,152,153,154,156,168,175,176,177,179,180,190,193,195,196,],[-47,-58,-59,-60,-61,-62,-63,-22,-77,-73,-74,-75,-71,-69,-70,-72,-43,-45,-76,-42,-22,-46,-66,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,-49,-50,-22,-22,-22,-67,-22,-51,168,-54,-55,-64,-22,-65,-78,-48,-52,-79,-81,-96,-98,-97,]),'RETURN':([17,30,31,32,33,34,35,36,44,45,46,47,48,49,50,51,52,55,59,77,81,82,88,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,128,130,135,136,137,140,144,149,150,152,153,154,156,157,158,159,160,168,170,173,175,176,177,179,180,190,193,195,196,],[-47,-58,-59,-60,-61,-62,-63,-22,-77,-73,-74,-75,-71,-69,-70,-72,-43,-45,-76,-42,-22,-46,-66,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,-49,-50,-22,-22,-22,-22,-67,-22,-51,-53,-54,-55,-64,-22,171,-22,-15,-22,181,-14,-65,-78,-48,-52,-79,-81,-96,-98,-97,]),'CLOSEBRACKET':([30,31,32,33,34,35,36,44,45,46,47,48,49,50,51,52,55,70,76,77,78,81,88,90,91,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,144,149,156,175,176,180,190,193,195,196,],[-58,-59,-60,-61,-62,-63,-22,-77,-73,-74,-75,-71,-69,-70,-72,-43,-45,-22,101,-42,102,-22,-66,127,-76,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,-67,-22,-64,-65,-78,-79,-81,-96,-98,-97,]),'SEMI':([30,31,32,33,34,35,36,44,45,46,47,48,49,50,51,52,55,64,69,71,77,80,81,88,91,92,93,94,95,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,124,131,138,144,145,146,147,149,156,164,165,166,169,171,175,176,178,180,181,183,186,190,193,195,196,],[-58,-59,-60,-61,-62,-63,-22,-77,-73,-74,-75,-71,-69,-70,-72,-43,-45,84,88,-22,-42,118,-22,-66,-76,-80,128,129,130,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,144,150,156,-67,-22,129,-22,-22,-64,175,176,177,180,-22,-65,-78,185,-79,-22,187,191,-81,-96,-98,-97,]),'COMMA':([30,31,32,33,34,35,36,44,45,46,47,48,49,50,51,52,55,72,77,81,88,91,92,97,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,141,144,149,156,175,176,180,184,190,193,195,196,],[-58,-59,-60,-61,-62,-63,-22,-77,-73,-74,-75,-71,-69,-70,-72,-43,-45,-22,-42,-22,-66,-76,-80,133,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,162,-67,-22,-64,-65,-78,-79,162,-81,-96,-98,-97,]),'CLOSEPAR':([30,31,32,33,34,35,36,44,45,46,47,48,49,50,51,52,55,72,73,74,75,77,81,85,88,91,92,96,97,98,99,100,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,132,133,134,141,144,149,151,156,161,163,175,176,180,184,188,190,193,195,196,],[-58,-59,-60,-61,-62,-63,-22,-77,-73,-74,-75,-71,-69,-70,-72,-43,-45,95,-22,-22,-22,-42,-22,121,-66,-76,-80,131,-22,135,136,137,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,139,-39,-22,-41,-22,-67,-22,-40,-64,-36,-38,-65,-78,-79,-22,-37,-81,-96,-98,-97,]),'LESSEQUAL':([30,31,32,33,34,35,36,45,46,47,48,49,50,51,52,55,77,79,81,87,88,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,123,124,125,138,144,148,149,156,175,176,180,189,190,193,195,196,],[-58,-59,-60,-61,-62,-63,-22,-73,-74,-75,-71,-69,-70,-72,-43,-45,-42,105,-22,-22,-66,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,105,-77,105,105,-67,105,-22,-64,-65,-78,-79,105,-81,-96,-98,-97,]),'EQUALS':([30,31,32,33,34,35,36,45,46,47,48,49,50,51,52,55,77,79,81,87,88,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,123,124,125,138,144,148,149,156,175,176,180,189,190,193,195,196,],[-58,-59,-60,-61,-62,-63,-22,-73,-74,-75,-71,-69,-70,-72,-43,-45,-42,106,-22,-22,-66,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,106,-77,106,106,-67,106,-22,-64,-65,-78,-79,106,-81,-96,-98,-97,]),'GREATEREQUAL':([30,31,32,33,34,35,36,45,46,47,48,49,50,51,52,55,77,79,81,87,88,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,123,124,125,138,144,148,149,156,175,176,180,189,190,193,195,196,],[-58,-59,-60,-61,-62,-63,-22,-73,-74,-75,-71,-69,-70,-72,-43,-45,-42,107,-22,-22,-66,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,107,-77,107,107,-67,107,-22,-64,-65,-78,-79,107,-81,-96,-98,-97,]),'GREATERTHAN':([30,31,32,33,34,35,36,45,46,47,48,49,50,51,52,55,77,79,81,87,88,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,123,124,125,138,144,148,149,156,175,176,180,189,190,193,195,196,],[-58,-59,-60,-61,-62,-63,-22,-73,-74,-75,-71,-69,-70,-72,-43,-45,-42,108,-22,-22,-66,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,108,-77,108,108,-67,108,-22,-64,-65,-78,-79,108,-81,-96,-98,-97,]),'LESSTHAN':([30,31,32,33,34,35,36,45,46,47,48,49,50,51,52,55,77,79,81,87,88,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,123,124,125,138,144,148,149,156,175,176,180,189,190,193,195,196,],[-58,-59,-60,-61,-62,-63,-22,-73,-74,-75,-71,-69,-70,-72,-43,-45,-42,109,-22,-22,-66,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,109,-77,109,109,-67,109,-22,-64,-65,-78,-79,109,-81,-96,-98,-97,]),'ADD':([30,31,32,33,34,35,36,45,46,47,48,49,50,51,52,55,77,79,81,87,88,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,123,124,125,138,144,148,149,156,175,176,180,189,190,193,195,196,],[-58,-59,-60,-61,-62,-63,-22,-73,-74,-75,-71,-69,-70,-72,-43,-45,-42,110,-22,-22,-66,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,110,-77,110,110,-67,110,-22,-64,-65,-78,-79,110,-81,-96,-98,-97,]),'MINUS':([30,31,32,33,34,35,36,45,46,47,48,49,50,51,52,55,77,79,81,87,88,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,123,124,125,138,144,148,149,156,175,176,180,189,190,193,195,196,],[-58,-59,-60,-61,-62,-63,-22,-73,-74,-75,-71,-69,-70,-72,-43,-45,-42,111,-22,-22,-66,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,111,-77,111,111,-67,111,-22,-64,-65,-78,-79,111,-81,-96,-98,-97,]),'MULT':([30,31,32,33,34,35,36,45,46,47,48,49,50,51,52,55,77,79,81,87,88,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,123,124,125,138,144,148,149,156,175,176,180,189,190,193,195,196,],[-58,-59,-60,-61,-62,-63,-22,-73,-74,-75,-71,-69,-70,-72,-43,-45,-42,112,-22,-22,-66,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,112,-77,112,112,-67,112,-22,-64,-65,-78,-79,112,-81,-96,-98,-97,]),'NOTEQUAL':([30,31,32,33,34,35,36,45,46,47,48,49,50,51,52,55,77,79,81,87,88,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,123,124,125,138,144,148,149,156,175,176,180,189,190,193,195,196,],[-58,-59,-60,-61,-62,-63,-22,-73,-74,-75,-71,-69,-70,-72,-43,-45,-42,113,-22,-22,-66,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,113,-77,113,113,-67,113,-22,-64,-65,-78,-79,113,-81,-96,-98,-97,]),'DIVIDE':([30,31,32,33,34,35,36,45,46,47,48,49,50,51,52,55,77,79,81,87,88,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,123,124,125,138,144,148,149,156,175,176,180,189,190,193,195,196,],[-58,-59,-60,-61,-62,-63,-22,-73,-74,-75,-71,-69,-70,-72,-43,-45,-42,114,-22,-22,-66,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,114,-77,114,114,-67,114,-22,-64,-65,-78,-79,114,-81,-96,-98,-97,]),'PEQUAL':([30,31,32,33,34,35,36,45,46,47,48,49,50,51,52,55,77,79,81,87,88,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,123,124,125,138,144,148,149,156,175,176,180,189,190,193,195,196,],[-58,-59,-60,-61,-62,-63,-22,-73,-74,-75,-71,-69,-70,-72,-43,-45,-42,115,-22,-22,-66,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,115,-77,115,115,-67,115,-22,-64,-65,-78,-79,115,-81,-96,-98,-97,]),'MEQUAL':([30,31,32,33,34,35,36,45,46,47,48,49,50,51,52,55,77,79,81,87,88,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,123,124,125,138,144,148,149,156,175,176,180,189,190,193,195,196,],[-58,-59,-60,-61,-62,-63,-22,-73,-74,-75,-71,-69,-70,-72,-43,-45,-42,116,-22,-22,-66,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,116,-77,116,116,-67,116,-22,-64,-65,-78,-79,116,-81,-96,-98,-97,]),'PLUSPLUS':([30,31,32,33,34,35,36,45,46,47,48,49,50,51,52,55,77,79,81,87,88,92,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,123,124,125,138,144,148,149,156,175,176,180,189,190,193,195,196,],[-58,-59,-60,-61,-62,-63,-22,-73,-74,-75,-71,-69,-70,-72,-43,-45,-42,117,-22,-22,-66,-80,-83,-82,-84,-85,-86,-87,-88,-89,-90,-91,-92,-93,-94,-95,-68,-44,117,-77,117,117,-67,117,-22,-64,-65,-78,-79,117,-81,-96,-98,-97,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'PROGRAM':([0,],[1,]),'Z':([0,3,],[2,6,]),'CLASSDECLARATION':([0,3,],[3,3,]),'EMPTY':([0,3,8,9,10,12,13,36,57,59,70,71,72,73,74,75,81,87,91,97,123,133,135,136,137,140,141,145,147,149,157,159,168,171,181,184,],[4,4,14,55,58,14,14,55,58,55,92,92,92,92,92,92,55,92,55,134,55,92,92,92,92,160,163,92,92,55,160,160,92,92,92,163,]),'A':([8,12,13,],[11,62,63,]),'FIELDDECLARATION':([8,12,13,],[12,12,12,]),'METHODDECLARATION':([8,12,13,],[13,13,13,]),'DECLARATORS':([8,12,13,],[15,15,15,]),'STATEMENT':([8,10,12,13,57,135,136,137,140,157,159,168,],[16,57,16,16,57,152,153,154,159,159,159,179,]),'EXPRESSION':([8,10,12,13,57,70,71,72,73,74,75,87,133,135,136,137,140,145,147,157,159,168,171,181,],[17,17,17,17,17,90,93,97,98,99,100,125,151,17,17,17,17,165,166,17,17,17,183,186,]),'C':([8,12,13,],[18,18,18,]),'TYPE':([8,10,12,13,18,19,57,65,70,71,72,73,74,75,85,87,133,135,136,137,140,145,147,157,159,162,168,171,181,],[20,60,20,20,66,68,60,86,60,60,60,60,60,60,122,60,60,60,60,60,60,60,60,60,60,174,60,60,60,]),'REFERENCE':([8,10,12,13,57,70,71,72,73,74,75,87,129,133,135,136,137,140,145,147,157,159,167,168,171,181,185,193,],[21,21,21,21,21,89,89,89,89,89,89,89,148,89,21,21,21,21,89,89,21,21,178,21,89,89,189,195,]),'PRIMTYPE':([8,10,12,13,18,19,57,65,70,71,72,73,74,75,85,87,133,135,136,137,140,145,147,157,159,162,168,171,181,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'CLASSTYPE':([8,10,12,13,18,19,57,65,70,71,72,73,74,75,85,87,133,135,136,137,140,145,147,157,159,162,168,171,181,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'ARRTYPE':([8,10,12,13,18,19,57,65,70,71,72,73,74,75,85,87,133,135,136,137,140,145,147,157,159,162,168,171,181,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'EXPRESSION1':([8,10,12,13,57,70,71,72,73,74,75,87,133,135,136,137,140,145,147,157,159,168,171,181,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'EXPRESSION2':([8,10,12,13,57,70,71,72,73,74,75,87,133,135,136,137,140,145,147,157,159,168,171,181,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'EXPRESSION3':([8,10,12,13,57,70,71,72,73,74,75,87,133,135,136,137,140,145,147,157,159,168,171,181,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'EXPRESSION4':([8,10,12,13,57,70,71,72,73,74,75,87,133,135,136,137,140,145,147,157,159,168,171,181,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'EXPRESSION5':([8,10,12,13,57,70,71,72,73,74,75,87,133,135,136,137,140,145,147,157,159,168,171,181,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'EXPRESSION6':([8,10,12,13,57,70,71,72,73,74,75,87,133,135,136,137,140,145,147,157,159,168,171,181,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'VALUE':([8,10,12,13,53,57,70,71,72,73,74,75,87,133,135,136,137,140,142,145,147,157,159,168,171,181,],[44,44,44,44,80,44,44,44,44,44,44,44,124,44,44,44,44,44,80,44,44,44,44,44,44,44,]),'VALUE1':([8,10,12,13,53,57,70,71,72,73,74,75,87,133,135,136,137,140,142,145,147,157,159,168,171,181,],[49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'VALUE2':([8,10,12,13,53,57,70,71,72,73,74,75,87,133,135,136,137,140,142,145,147,157,159,168,171,181,],[50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'G':([9,36,59,81,91,123,149,],[52,77,52,119,52,52,52,]),'H':([10,57,],[56,83,]),'ARGUMENTLIST':([72,],[96,]),'OP':([79,123,125,138,148,189,],[104,143,145,155,167,193,]),'PARAMERERLIST':([85,],[120,]),'E':([97,],[132,]),'B':([140,157,159,],[158,170,173,]),'D':([141,184,],[161,188,]),'I':([185,],[190,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAM","S'",1,None,None,None),
  ('PROGRAM -> Z','PROGRAM',1,'p_programm','LexAndYacc.py',141),
  ('Z -> CLASSDECLARATION Z','Z',2,'p_Z','LexAndYacc.py',144),
  ('Z -> EMPTY','Z',1,'p_Z','LexAndYacc.py',145),
  ('CLASSDECLARATION -> CLASS ID OPENAKOL A CLOSEAKOL','CLASSDECLARATION',5,'p_classdeclaration','LexAndYacc.py',148),
  ('A -> FIELDDECLARATION A','A',2,'p_A','LexAndYacc.py',151),
  ('A -> METHODDECLARATION A','A',2,'p_A','LexAndYacc.py',152),
  ('A -> EMPTY','A',1,'p_A','LexAndYacc.py',153),
  ('FIELDDECLARATION -> DECLARATORS ID SEMI','FIELDDECLARATION',3,'p_fielddeclaration','LexAndYacc.py',156),
  ('FIELDDECLARATION -> STATEMENT','FIELDDECLARATION',1,'p_fielddeclaration','LexAndYacc.py',157),
  ('METHODDECLARATION -> DECLARATORS ID OPENPAR PARAMERERLIST CLOSEPAR OPENAKOL B RETURN EXPRESSION SEMI CLOSEAKOL','METHODDECLARATION',11,'p_methoddeclaration','LexAndYacc.py',161),
  ('METHODDECLARATION -> DECLARATORS ID OPENPAR CLOSEPAR OPENAKOL B RETURN EXPRESSION SEMI CLOSEAKOL','METHODDECLARATION',10,'p_methoddeclaration','LexAndYacc.py',162),
  ('METHODDECLARATION -> DECLARATORS ID OPENPAR PARAMERERLIST CLOSEPAR OPENAKOL B CLOSEAKOL','METHODDECLARATION',8,'p_methoddeclaration','LexAndYacc.py',163),
  ('METHODDECLARATION -> DECLARATORS ID OPENPAR CLOSEPAR OPENAKOL B CLOSEAKOL','METHODDECLARATION',7,'p_methoddeclaration','LexAndYacc.py',164),
  ('B -> STATEMENT B','B',2,'p_B','LexAndYacc.py',168),
  ('B -> EMPTY','B',1,'p_B','LexAndYacc.py',169),
  ('DECLARATORS -> C STATIC TYPE','DECLARATORS',3,'p_declarators','LexAndYacc.py',172),
  ('DECLARATORS -> STATIC TYPE','DECLARATORS',2,'p_declarators','LexAndYacc.py',173),
  ('DECLARATORS -> C TYPE','DECLARATORS',2,'p_declarators','LexAndYacc.py',174),
  ('DECLARATORS -> TYPE','DECLARATORS',1,'p_declarators','LexAndYacc.py',175),
  ('C -> PUBLIC','C',1,'p_C','LexAndYacc.py',180),
  ('C -> PRIVATE','C',1,'p_C','LexAndYacc.py',181),
  ('EMPTY -> <empty>','EMPTY',0,'p_empty','LexAndYacc.py',186),
  ('TYPE -> PRIMTYPE','TYPE',1,'p_type','LexAndYacc.py',190),
  ('TYPE -> CLASSTYPE','TYPE',1,'p_type','LexAndYacc.py',191),
  ('TYPE -> ARRTYPE','TYPE',1,'p_type','LexAndYacc.py',192),
  ('PRIMTYPE -> INT','PRIMTYPE',1,'p_primetype','LexAndYacc.py',196),
  ('PRIMTYPE -> BOOLEAN','PRIMTYPE',1,'p_primetype','LexAndYacc.py',197),
  ('PRIMTYPE -> STRING','PRIMTYPE',1,'p_primetype','LexAndYacc.py',198),
  ('PRIMTYPE -> DOUBLE','PRIMTYPE',1,'p_primetype','LexAndYacc.py',199),
  ('PRIMTYPE -> CHARACTER','PRIMTYPE',1,'p_primetype','LexAndYacc.py',200),
  ('PRIMTYPE -> FLOAT','PRIMTYPE',1,'p_primetype','LexAndYacc.py',201),
  ('PRIMTYPE -> VOID','PRIMTYPE',1,'p_primetype','LexAndYacc.py',202),
  ('CLASSTYPE -> ID','CLASSTYPE',1,'p_classtype','LexAndYacc.py',207),
  ('ARRTYPE -> INT OPENBRACKET CLOSEBRACKET','ARRTYPE',3,'p_arrtype','LexAndYacc.py',211),
  ('ARRTYPE -> CLASSTYPE OPENBRACKET CLOSEBRACKET','ARRTYPE',3,'p_arrtype','LexAndYacc.py',212),
  ('PARAMERERLIST -> TYPE ID D','PARAMERERLIST',3,'p_parameterlist','LexAndYacc.py',215),
  ('D -> COMMA TYPE ID D','D',4,'p_D','LexAndYacc.py',218),
  ('D -> EMPTY','D',1,'p_D','LexAndYacc.py',219),
  ('ARGUMENTLIST -> EXPRESSION E','ARGUMENTLIST',2,'p_argumentlist','LexAndYacc.py',222),
  ('E -> COMMA EXPRESSION','E',2,'p_E','LexAndYacc.py',225),
  ('E -> EMPTY','E',1,'p_E','LexAndYacc.py',226),
  ('REFERENCE -> THIS G','REFERENCE',2,'p_reference','LexAndYacc.py',229),
  ('REFERENCE -> ID G','REFERENCE',2,'p_reference','LexAndYacc.py',230),
  ('G -> DOT ID G','G',3,'p_G','LexAndYacc.py',233),
  ('G -> EMPTY','G',1,'p_G','LexAndYacc.py',234),
  ('STATEMENT -> OPENAKOL H CLOSEAKOL','STATEMENT',3,'p_statement','LexAndYacc.py',237),
  ('STATEMENT -> EXPRESSION','STATEMENT',1,'p_statement','LexAndYacc.py',238),
  ('STATEMENT -> REFERENCE OPENBRACKET EXPRESSION CLOSEBRACKET ASSIGN EXPRESSION SEMI','STATEMENT',7,'p_statement','LexAndYacc.py',239),
  ('STATEMENT -> REFERENCE ASSIGN EXPRESSION SEMI','STATEMENT',4,'p_statement','LexAndYacc.py',240),
  ('STATEMENT -> REFERENCE OPENPAR CLOSEPAR SEMI','STATEMENT',4,'p_statement','LexAndYacc.py',241),
  ('STATEMENT -> REFERENCE OPENPAR ARGUMENTLIST CLOSEPAR SEMI','STATEMENT',5,'p_statement','LexAndYacc.py',242),
  ('STATEMENT -> IF OPENPAR EXPRESSION CLOSEPAR STATEMENT ELSE STATEMENT','STATEMENT',7,'p_statement','LexAndYacc.py',243),
  ('STATEMENT -> IF OPENPAR EXPRESSION CLOSEPAR STATEMENT','STATEMENT',5,'p_statement','LexAndYacc.py',244),
  ('STATEMENT -> FOR OPENPAR EXPRESSION CLOSEPAR STATEMENT','STATEMENT',5,'p_statement','LexAndYacc.py',245),
  ('STATEMENT -> WHILE OPENPAR EXPRESSION CLOSEPAR STATEMENT','STATEMENT',5,'p_statement','LexAndYacc.py',246),
  ('H -> STATEMENT H','H',2,'p_H','LexAndYacc.py',251),
  ('H -> EMPTY','H',1,'p_H','LexAndYacc.py',252),
  ('EXPRESSION -> EXPRESSION1','EXPRESSION',1,'p_expressin','LexAndYacc.py',256),
  ('EXPRESSION -> EXPRESSION2','EXPRESSION',1,'p_expressin','LexAndYacc.py',257),
  ('EXPRESSION -> EXPRESSION3','EXPRESSION',1,'p_expressin','LexAndYacc.py',258),
  ('EXPRESSION -> EXPRESSION4','EXPRESSION',1,'p_expressin','LexAndYacc.py',259),
  ('EXPRESSION -> EXPRESSION5','EXPRESSION',1,'p_expressin','LexAndYacc.py',260),
  ('EXPRESSION -> EXPRESSION6','EXPRESSION',1,'p_expressin','LexAndYacc.py',261),
  ('EXPRESSION1 -> ID ASSIGN ID OP ID SEMI','EXPRESSION1',6,'p_expressin1','LexAndYacc.py',264),
  ('EXPRESSION2 -> TYPE ID ASSIGN ID OP ID SEMI','EXPRESSION2',7,'p_expressin2','LexAndYacc.py',297),
  ('EXPRESSION3 -> TYPE ID SEMI','EXPRESSION3',3,'p_expressin3','LexAndYacc.py',333),
  ('EXPRESSION4 -> TYPE ID ASSIGN VALUE SEMI','EXPRESSION4',5,'p_expressin4','LexAndYacc.py',341),
  ('EXPRESSION5 -> ID ASSIGN VALUE SEMI','EXPRESSION5',4,'p_expressin5','LexAndYacc.py',355),
  ('VALUE -> VALUE1','VALUE',1,'p_value','LexAndYacc.py',369),
  ('VALUE -> VALUE2','VALUE',1,'p_value','LexAndYacc.py',370),
  ('VALUE1 -> NUMBER','VALUE1',1,'p_value1','LexAndYacc.py',374),
  ('VALUE2 -> CHAR','VALUE2',1,'p_value2','LexAndYacc.py',378),
  ('EXPRESSION6 -> TRUE','EXPRESSION6',1,'p_expressin6','LexAndYacc.py',383),
  ('EXPRESSION6 -> FALSE','EXPRESSION6',1,'p_expressin6','LexAndYacc.py',384),
  ('EXPRESSION6 -> NULL','EXPRESSION6',1,'p_expressin6','LexAndYacc.py',385),
  ('EXPRESSION6 -> ID','EXPRESSION6',1,'p_expressin6','LexAndYacc.py',386),
  ('EXPRESSION6 -> VALUE','EXPRESSION6',1,'p_expressin6','LexAndYacc.py',387),
  ('EXPRESSION6 -> TYPE ID ASSIGN EXPRESSION OP EXPRESSION SEMI','EXPRESSION6',7,'p_expressin6','LexAndYacc.py',388),
  ('EXPRESSION6 -> ID ASSIGN ID OP ID OP ID SEMI','EXPRESSION6',8,'p_expressin6','LexAndYacc.py',389),
  ('EXPRESSION6 -> EMPTY','EXPRESSION6',1,'p_expressin6','LexAndYacc.py',390),
  ('EXPRESSION6 -> REFERENCE ASSIGN NUMBER SEMI REFERENCE OP REFERENCE SEMI I','EXPRESSION6',9,'p_expressin6','LexAndYacc.py',391),
  ('OP -> LESSEQUAL','OP',1,'p_op','LexAndYacc.py',397),
  ('OP -> ASSIGN','OP',1,'p_op','LexAndYacc.py',398),
  ('OP -> EQUALS','OP',1,'p_op','LexAndYacc.py',399),
  ('OP -> GREATEREQUAL','OP',1,'p_op','LexAndYacc.py',400),
  ('OP -> GREATERTHAN','OP',1,'p_op','LexAndYacc.py',401),
  ('OP -> LESSTHAN','OP',1,'p_op','LexAndYacc.py',402),
  ('OP -> ADD','OP',1,'p_op','LexAndYacc.py',403),
  ('OP -> MINUS','OP',1,'p_op','LexAndYacc.py',404),
  ('OP -> MULT','OP',1,'p_op','LexAndYacc.py',405),
  ('OP -> NOTEQUAL','OP',1,'p_op','LexAndYacc.py',406),
  ('OP -> DIVIDE','OP',1,'p_op','LexAndYacc.py',407),
  ('OP -> PEQUAL','OP',1,'p_op','LexAndYacc.py',408),
  ('OP -> MEQUAL','OP',1,'p_op','LexAndYacc.py',409),
  ('OP -> PLUSPLUS','OP',1,'p_op','LexAndYacc.py',410),
  ('I -> REFERENCE OP','I',2,'p_I','LexAndYacc.py',416),
  ('I -> REFERENCE OP NUMBER','I',3,'p_I','LexAndYacc.py',417),
  ('I -> REFERENCE OP REFERENCE','I',3,'p_I','LexAndYacc.py',418),
]
