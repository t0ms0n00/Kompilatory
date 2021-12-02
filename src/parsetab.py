
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocIFXnonassocELSEnonassoc=ADDASSIGNSUBASSIGNMULASSIGNDIVASSIGNnonassoc<>LESSEQUALGREATEREQUALEQUALNOTEQUALleft+-leftDOTADDDOTSUBleft*/leftDOTMULDOTDIVrightUMINUSADDASSIGN BREAK CONTINUE DIVASSIGN DOTADD DOTDIV DOTMUL DOTSUB ELSE EQUAL EYE FLOAT FOR GREATEREQUAL ID IF INTEGER LESSEQUAL MULASSIGN NOTEQUAL ONES PRINT RETURN STRING SUBASSIGN WHILE ZEROS program : instructions\n                |  instructions : instructions instruction\n                     | instruction  instruction : block\n                    | if\n                    | for\n                    | while\n                    | break\n                    | continue\n                    | return\n                    | print\n                    | assign  block : \'{\' instructions \'}\'  if : IF \'(\' condition \')\' instruction %prec IFX\n           | IF \'(\' condition \')\' instruction ELSE instruction  for : FOR ID \'=\' range instruction  range : expression \':\' expression  while : WHILE \'(\' condition \')\' instruction  break : BREAK \';\'  continue : CONTINUE \';\'  return : RETURN \';\'\n               | RETURN expression \';\'  print : PRINT expressions \';\'  expression : singleton\n                   | vector\n                   | matrix\n                   | variable  expressions : expressions \',\' expression\n                    | expression  singleton : STRING\n                  | INTEGER\n                  | FLOAT   vector : \'[\' expressions \']\'\n                | \'[\' \']\'  vectors : vectors \',\' vector\n                | vector  matrix : \'[\' vectors \']\'  assign : variable \'=\' expression \';\'\n               | variable calculation_assign expression \';\'  calculation_assign : ADDASSIGN\n                           | SUBASSIGN\n                           | MULASSIGN\n                           | DIVASSIGN  variable : ID\n               | ID \'[\' INTEGER \']\'\n               | ID \'[\' INTEGER \',\' INTEGER \']\'  comparator : \'<\'\n                   | \'>\'\n                   | EQUAL\n                   | NOTEQUAL\n                   | LESSEQUAL\n                   | GREATEREQUAL  condition : expression comparator expression  expression : expression \'+\' expression\n                   | expression \'-\' expression\n                   | expression \'*\' expression\n                   | expression \'/\' expression  expression : expression DOTADD expression\n                   | expression DOTSUB expression\n                   | expression DOTMUL expression\n                   | expression DOTDIV expression  expression : \'-\' expression %prec UMINUS  expression : \'(\' expression \')\'  expression : expression "\'"  expression : matrix_func \'(\' INTEGER \')\' \n                   | matrix_func \'(\' INTEGER \',\' INTEGER \')\'  matrix_func : EYE\n                    | ONES\n                    | ZEROS '
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,7,8,9,10,11,12,23,29,30,31,55,61,78,109,110,111,113,116,125,],[-2,0,-1,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-3,-20,-21,-22,-14,-23,-24,-39,-40,-15,-17,-19,-16,]),'{':([0,2,3,4,5,6,7,8,9,10,11,12,13,16,23,24,29,30,31,33,34,35,36,40,41,42,55,61,70,71,75,78,82,90,92,94,95,96,97,98,99,100,101,102,103,105,106,109,110,111,113,116,117,121,122,123,125,126,],[13,13,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,13,-45,-3,13,-20,-21,-22,-25,-26,-27,-28,-32,-31,-33,-14,-23,-65,-63,-35,-24,13,13,-46,13,-55,-56,-57,-58,-59,-60,-61,-62,-64,-34,-38,-39,-40,-15,-17,-19,-66,13,-18,-47,-16,-67,]),'IF':([0,2,3,4,5,6,7,8,9,10,11,12,13,16,23,24,29,30,31,33,34,35,36,40,41,42,55,61,70,71,75,78,82,90,92,94,95,96,97,98,99,100,101,102,103,105,106,109,110,111,113,116,117,121,122,123,125,126,],[14,14,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,14,-45,-3,14,-20,-21,-22,-25,-26,-27,-28,-32,-31,-33,-14,-23,-65,-63,-35,-24,14,14,-46,14,-55,-56,-57,-58,-59,-60,-61,-62,-64,-34,-38,-39,-40,-15,-17,-19,-66,14,-18,-47,-16,-67,]),'FOR':([0,2,3,4,5,6,7,8,9,10,11,12,13,16,23,24,29,30,31,33,34,35,36,40,41,42,55,61,70,71,75,78,82,90,92,94,95,96,97,98,99,100,101,102,103,105,106,109,110,111,113,116,117,121,122,123,125,126,],[15,15,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,15,-45,-3,15,-20,-21,-22,-25,-26,-27,-28,-32,-31,-33,-14,-23,-65,-63,-35,-24,15,15,-46,15,-55,-56,-57,-58,-59,-60,-61,-62,-64,-34,-38,-39,-40,-15,-17,-19,-66,15,-18,-47,-16,-67,]),'WHILE':([0,2,3,4,5,6,7,8,9,10,11,12,13,16,23,24,29,30,31,33,34,35,36,40,41,42,55,61,70,71,75,78,82,90,92,94,95,96,97,98,99,100,101,102,103,105,106,109,110,111,113,116,117,121,122,123,125,126,],[17,17,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,17,-45,-3,17,-20,-21,-22,-25,-26,-27,-28,-32,-31,-33,-14,-23,-65,-63,-35,-24,17,17,-46,17,-55,-56,-57,-58,-59,-60,-61,-62,-64,-34,-38,-39,-40,-15,-17,-19,-66,17,-18,-47,-16,-67,]),'BREAK':([0,2,3,4,5,6,7,8,9,10,11,12,13,16,23,24,29,30,31,33,34,35,36,40,41,42,55,61,70,71,75,78,82,90,92,94,95,96,97,98,99,100,101,102,103,105,106,109,110,111,113,116,117,121,122,123,125,126,],[18,18,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,18,-45,-3,18,-20,-21,-22,-25,-26,-27,-28,-32,-31,-33,-14,-23,-65,-63,-35,-24,18,18,-46,18,-55,-56,-57,-58,-59,-60,-61,-62,-64,-34,-38,-39,-40,-15,-17,-19,-66,18,-18,-47,-16,-67,]),'CONTINUE':([0,2,3,4,5,6,7,8,9,10,11,12,13,16,23,24,29,30,31,33,34,35,36,40,41,42,55,61,70,71,75,78,82,90,92,94,95,96,97,98,99,100,101,102,103,105,106,109,110,111,113,116,117,121,122,123,125,126,],[19,19,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,19,-45,-3,19,-20,-21,-22,-25,-26,-27,-28,-32,-31,-33,-14,-23,-65,-63,-35,-24,19,19,-46,19,-55,-56,-57,-58,-59,-60,-61,-62,-64,-34,-38,-39,-40,-15,-17,-19,-66,19,-18,-47,-16,-67,]),'RETURN':([0,2,3,4,5,6,7,8,9,10,11,12,13,16,23,24,29,30,31,33,34,35,36,40,41,42,55,61,70,71,75,78,82,90,92,94,95,96,97,98,99,100,101,102,103,105,106,109,110,111,113,116,117,121,122,123,125,126,],[20,20,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,20,-45,-3,20,-20,-21,-22,-25,-26,-27,-28,-32,-31,-33,-14,-23,-65,-63,-35,-24,20,20,-46,20,-55,-56,-57,-58,-59,-60,-61,-62,-64,-34,-38,-39,-40,-15,-17,-19,-66,20,-18,-47,-16,-67,]),'PRINT':([0,2,3,4,5,6,7,8,9,10,11,12,13,16,23,24,29,30,31,33,34,35,36,40,41,42,55,61,70,71,75,78,82,90,92,94,95,96,97,98,99,100,101,102,103,105,106,109,110,111,113,116,117,121,122,123,125,126,],[21,21,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,21,-45,-3,21,-20,-21,-22,-25,-26,-27,-28,-32,-31,-33,-14,-23,-65,-63,-35,-24,21,21,-46,21,-55,-56,-57,-58,-59,-60,-61,-62,-64,-34,-38,-39,-40,-15,-17,-19,-66,21,-18,-47,-16,-67,]),'ID':([0,2,3,4,5,6,7,8,9,10,11,12,13,15,16,20,21,23,24,25,28,29,30,31,33,34,35,36,37,38,40,41,42,43,49,50,51,52,53,54,55,58,61,62,63,64,65,66,67,68,69,70,71,75,78,79,82,83,84,85,86,87,88,89,90,92,94,95,96,97,98,99,100,101,102,103,105,106,109,110,111,113,114,116,117,120,121,122,123,125,126,],[16,16,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,16,26,-45,16,16,-3,16,16,16,-20,-21,-22,-25,-26,-27,-28,16,16,-32,-31,-33,16,16,16,-41,-42,-43,-44,-14,16,-23,16,16,16,16,16,16,16,16,-65,-63,-35,-24,16,16,16,-48,-49,-50,-51,-52,-53,16,-46,16,-55,-56,-57,-58,-59,-60,-61,-62,-64,-34,-38,-39,-40,-15,-17,16,-19,-66,16,16,-18,-47,-16,-67,]),'}':([3,4,5,6,7,8,9,10,11,12,23,24,29,30,31,55,61,78,109,110,111,113,116,125,],[-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-3,55,-20,-21,-22,-14,-23,-24,-39,-40,-15,-17,-19,-16,]),'ELSE':([4,5,6,7,8,9,10,11,12,29,30,31,55,61,78,109,110,111,113,116,125,],[-5,-6,-7,-8,-9,-10,-11,-12,-13,-20,-21,-22,-14,-23,-24,-39,-40,121,-17,-19,-16,]),'(':([14,17,20,21,25,28,37,38,39,43,44,45,46,49,50,51,52,53,54,58,62,63,64,65,66,67,68,69,79,83,84,85,86,87,88,89,114,120,],[25,28,38,38,38,38,38,38,73,38,-68,-69,-70,38,38,-41,-42,-43,-44,38,38,38,38,38,38,38,38,38,38,38,-48,-49,-50,-51,-52,-53,38,38,]),'=':([16,22,26,92,123,],[-45,49,58,-46,-47,]),'ADDASSIGN':([16,22,92,123,],[-45,51,-46,-47,]),'SUBASSIGN':([16,22,92,123,],[-45,52,-46,-47,]),'MULASSIGN':([16,22,92,123,],[-45,53,-46,-47,]),'DIVASSIGN':([16,22,92,123,],[-45,54,-46,-47,]),';':([16,18,19,20,32,33,34,35,36,40,41,42,47,48,70,71,75,80,81,92,95,96,97,98,99,100,101,102,103,105,106,108,117,123,126,],[-45,29,30,31,61,-25,-26,-27,-28,-32,-31,-33,78,-30,-65,-63,-35,109,110,-46,-55,-56,-57,-58,-59,-60,-61,-62,-64,-34,-38,-29,-66,-47,-67,]),'+':([16,32,33,34,35,36,40,41,42,48,57,70,71,72,75,77,80,81,91,92,95,96,97,98,99,100,101,102,103,105,106,108,112,117,122,123,126,],[-45,62,-25,-26,-27,-28,-32,-31,-33,62,62,-65,-63,62,-35,-26,62,62,62,-46,-55,-56,-57,-58,-59,-60,-61,-62,-64,-34,-38,62,62,-66,62,-47,-67,]),'-':([16,20,21,25,28,32,33,34,35,36,37,38,40,41,42,43,48,49,50,51,52,53,54,57,58,62,63,64,65,66,67,68,69,70,71,72,75,77,79,80,81,83,84,85,86,87,88,89,91,92,95,96,97,98,99,100,101,102,103,105,106,108,112,114,117,120,122,123,126,],[-45,37,37,37,37,63,-25,-26,-27,-28,37,37,-32,-31,-33,37,63,37,37,-41,-42,-43,-44,63,37,37,37,37,37,37,37,37,37,-65,-63,63,-35,-26,37,63,63,37,-48,-49,-50,-51,-52,-53,63,-46,-55,-56,-57,-58,-59,-60,-61,-62,-64,-34,-38,63,63,37,-66,37,63,-47,-67,]),'*':([16,32,33,34,35,36,40,41,42,48,57,70,71,72,75,77,80,81,91,92,95,96,97,98,99,100,101,102,103,105,106,108,112,117,122,123,126,],[-45,64,-25,-26,-27,-28,-32,-31,-33,64,64,-65,-63,64,-35,-26,64,64,64,-46,64,64,-57,-58,64,64,-61,-62,-64,-34,-38,64,64,-66,64,-47,-67,]),'/':([16,32,33,34,35,36,40,41,42,48,57,70,71,72,75,77,80,81,91,92,95,96,97,98,99,100,101,102,103,105,106,108,112,117,122,123,126,],[-45,65,-25,-26,-27,-28,-32,-31,-33,65,65,-65,-63,65,-35,-26,65,65,65,-46,65,65,-57,-58,65,65,-61,-62,-64,-34,-38,65,65,-66,65,-47,-67,]),'DOTADD':([16,32,33,34,35,36,40,41,42,48,57,70,71,72,75,77,80,81,91,92,95,96,97,98,99,100,101,102,103,105,106,108,112,117,122,123,126,],[-45,66,-25,-26,-27,-28,-32,-31,-33,66,66,-65,-63,66,-35,-26,66,66,66,-46,66,66,-57,-58,-59,-60,-61,-62,-64,-34,-38,66,66,-66,66,-47,-67,]),'DOTSUB':([16,32,33,34,35,36,40,41,42,48,57,70,71,72,75,77,80,81,91,92,95,96,97,98,99,100,101,102,103,105,106,108,112,117,122,123,126,],[-45,67,-25,-26,-27,-28,-32,-31,-33,67,67,-65,-63,67,-35,-26,67,67,67,-46,67,67,-57,-58,-59,-60,-61,-62,-64,-34,-38,67,67,-66,67,-47,-67,]),'DOTMUL':([16,32,33,34,35,36,40,41,42,48,57,70,71,72,75,77,80,81,91,92,95,96,97,98,99,100,101,102,103,105,106,108,112,117,122,123,126,],[-45,68,-25,-26,-27,-28,-32,-31,-33,68,68,-65,-63,68,-35,-26,68,68,68,-46,68,68,68,68,68,68,-61,-62,-64,-34,-38,68,68,-66,68,-47,-67,]),'DOTDIV':([16,32,33,34,35,36,40,41,42,48,57,70,71,72,75,77,80,81,91,92,95,96,97,98,99,100,101,102,103,105,106,108,112,117,122,123,126,],[-45,69,-25,-26,-27,-28,-32,-31,-33,69,69,-65,-63,69,-35,-26,69,69,69,-46,69,69,69,69,69,69,-61,-62,-64,-34,-38,69,69,-66,69,-47,-67,]),"'":([16,32,33,34,35,36,40,41,42,48,57,70,71,72,75,77,80,81,91,92,95,96,97,98,99,100,101,102,103,105,106,108,112,117,122,123,126,],[-45,70,-25,-26,-27,-28,-32,-31,-33,70,70,-65,-63,70,-35,-26,70,70,70,-46,-55,-56,-57,-58,-59,-60,-61,-62,-64,-34,-38,70,70,-66,70,-47,-67,]),',':([16,33,34,35,36,40,41,42,47,48,59,70,71,74,75,76,77,92,95,96,97,98,99,100,101,102,103,104,105,106,108,117,119,123,126,],[-45,-25,-26,-27,-28,-32,-31,-33,79,-30,93,-65,-63,79,-35,107,-26,-46,-55,-56,-57,-58,-59,-60,-61,-62,-64,118,-34,-38,-29,-66,-36,-47,-67,]),'<':([16,33,34,35,36,40,41,42,57,70,71,75,92,95,96,97,98,99,100,101,102,103,105,106,117,123,126,],[-45,-25,-26,-27,-28,-32,-31,-33,84,-65,-63,-35,-46,-55,-56,-57,-58,-59,-60,-61,-62,-64,-34,-38,-66,-47,-67,]),'>':([16,33,34,35,36,40,41,42,57,70,71,75,92,95,96,97,98,99,100,101,102,103,105,106,117,123,126,],[-45,-25,-26,-27,-28,-32,-31,-33,85,-65,-63,-35,-46,-55,-56,-57,-58,-59,-60,-61,-62,-64,-34,-38,-66,-47,-67,]),'EQUAL':([16,33,34,35,36,40,41,42,57,70,71,75,92,95,96,97,98,99,100,101,102,103,105,106,117,123,126,],[-45,-25,-26,-27,-28,-32,-31,-33,86,-65,-63,-35,-46,-55,-56,-57,-58,-59,-60,-61,-62,-64,-34,-38,-66,-47,-67,]),'NOTEQUAL':([16,33,34,35,36,40,41,42,57,70,71,75,92,95,96,97,98,99,100,101,102,103,105,106,117,123,126,],[-45,-25,-26,-27,-28,-32,-31,-33,87,-65,-63,-35,-46,-55,-56,-57,-58,-59,-60,-61,-62,-64,-34,-38,-66,-47,-67,]),'LESSEQUAL':([16,33,34,35,36,40,41,42,57,70,71,75,92,95,96,97,98,99,100,101,102,103,105,106,117,123,126,],[-45,-25,-26,-27,-28,-32,-31,-33,88,-65,-63,-35,-46,-55,-56,-57,-58,-59,-60,-61,-62,-64,-34,-38,-66,-47,-67,]),'GREATEREQUAL':([16,33,34,35,36,40,41,42,57,70,71,75,92,95,96,97,98,99,100,101,102,103,105,106,117,123,126,],[-45,-25,-26,-27,-28,-32,-31,-33,89,-65,-63,-35,-46,-55,-56,-57,-58,-59,-60,-61,-62,-64,-34,-38,-66,-47,-67,]),')':([16,33,34,35,36,40,41,42,56,60,70,71,72,75,92,95,96,97,98,99,100,101,102,103,104,105,106,112,117,123,124,126,],[-45,-25,-26,-27,-28,-32,-31,-33,82,94,-65,-63,103,-35,-46,-55,-56,-57,-58,-59,-60,-61,-62,-64,117,-34,-38,-54,-66,-47,126,-67,]),']':([16,33,34,35,36,40,41,42,43,48,59,70,71,74,75,76,77,92,95,96,97,98,99,100,101,102,103,105,106,108,115,117,119,120,123,126,],[-45,-25,-26,-27,-28,-32,-31,-33,75,-30,92,-65,-63,105,-35,106,-26,-46,-55,-56,-57,-58,-59,-60,-61,-62,-64,-34,-38,-29,123,-66,-36,75,-47,-67,]),':':([16,33,34,35,36,40,41,42,70,71,75,91,92,95,96,97,98,99,100,101,102,103,105,106,117,123,126,],[-45,-25,-26,-27,-28,-32,-31,-33,-65,-63,-35,114,-46,-55,-56,-57,-58,-59,-60,-61,-62,-64,-34,-38,-66,-47,-67,]),'[':([16,20,21,25,28,37,38,43,49,50,51,52,53,54,58,62,63,64,65,66,67,68,69,79,83,84,85,86,87,88,89,107,114,120,],[27,43,43,43,43,43,43,43,43,43,-41,-42,-43,-44,43,43,43,43,43,43,43,43,43,43,43,-48,-49,-50,-51,-52,-53,120,43,43,]),'STRING':([20,21,25,28,37,38,43,49,50,51,52,53,54,58,62,63,64,65,66,67,68,69,79,83,84,85,86,87,88,89,114,120,],[41,41,41,41,41,41,41,41,41,-41,-42,-43,-44,41,41,41,41,41,41,41,41,41,41,41,-48,-49,-50,-51,-52,-53,41,41,]),'INTEGER':([20,21,25,27,28,37,38,43,49,50,51,52,53,54,58,62,63,64,65,66,67,68,69,73,79,83,84,85,86,87,88,89,93,114,118,120,],[40,40,40,59,40,40,40,40,40,40,-41,-42,-43,-44,40,40,40,40,40,40,40,40,40,104,40,40,-48,-49,-50,-51,-52,-53,115,40,124,40,]),'FLOAT':([20,21,25,28,37,38,43,49,50,51,52,53,54,58,62,63,64,65,66,67,68,69,79,83,84,85,86,87,88,89,114,120,],[42,42,42,42,42,42,42,42,42,-41,-42,-43,-44,42,42,42,42,42,42,42,42,42,42,42,-48,-49,-50,-51,-52,-53,42,42,]),'EYE':([20,21,25,28,37,38,43,49,50,51,52,53,54,58,62,63,64,65,66,67,68,69,79,83,84,85,86,87,88,89,114,120,],[44,44,44,44,44,44,44,44,44,-41,-42,-43,-44,44,44,44,44,44,44,44,44,44,44,44,-48,-49,-50,-51,-52,-53,44,44,]),'ONES':([20,21,25,28,37,38,43,49,50,51,52,53,54,58,62,63,64,65,66,67,68,69,79,83,84,85,86,87,88,89,114,120,],[45,45,45,45,45,45,45,45,45,-41,-42,-43,-44,45,45,45,45,45,45,45,45,45,45,45,-48,-49,-50,-51,-52,-53,45,45,]),'ZEROS':([20,21,25,28,37,38,43,49,50,51,52,53,54,58,62,63,64,65,66,67,68,69,79,83,84,85,86,87,88,89,114,120,],[46,46,46,46,46,46,46,46,46,-41,-42,-43,-44,46,46,46,46,46,46,46,46,46,46,46,-48,-49,-50,-51,-52,-53,46,46,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'instructions':([0,13,],[2,24,]),'instruction':([0,2,13,24,82,90,94,121,],[3,23,3,23,111,113,116,125,]),'block':([0,2,13,24,82,90,94,121,],[4,4,4,4,4,4,4,4,]),'if':([0,2,13,24,82,90,94,121,],[5,5,5,5,5,5,5,5,]),'for':([0,2,13,24,82,90,94,121,],[6,6,6,6,6,6,6,6,]),'while':([0,2,13,24,82,90,94,121,],[7,7,7,7,7,7,7,7,]),'break':([0,2,13,24,82,90,94,121,],[8,8,8,8,8,8,8,8,]),'continue':([0,2,13,24,82,90,94,121,],[9,9,9,9,9,9,9,9,]),'return':([0,2,13,24,82,90,94,121,],[10,10,10,10,10,10,10,10,]),'print':([0,2,13,24,82,90,94,121,],[11,11,11,11,11,11,11,11,]),'assign':([0,2,13,24,82,90,94,121,],[12,12,12,12,12,12,12,12,]),'variable':([0,2,13,20,21,24,25,28,37,38,43,49,50,58,62,63,64,65,66,67,68,69,79,82,83,90,94,114,120,121,],[22,22,22,36,36,22,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,22,36,22,22,36,36,22,]),'expression':([20,21,25,28,37,38,43,49,50,58,62,63,64,65,66,67,68,69,79,83,114,120,],[32,48,57,57,71,72,48,80,81,91,95,96,97,98,99,100,101,102,108,112,122,48,]),'singleton':([20,21,25,28,37,38,43,49,50,58,62,63,64,65,66,67,68,69,79,83,114,120,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'vector':([20,21,25,28,37,38,43,49,50,58,62,63,64,65,66,67,68,69,79,83,107,114,120,],[34,34,34,34,34,34,77,34,34,34,34,34,34,34,34,34,34,34,34,34,119,34,34,]),'matrix':([20,21,25,28,37,38,43,49,50,58,62,63,64,65,66,67,68,69,79,83,114,120,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'matrix_func':([20,21,25,28,37,38,43,49,50,58,62,63,64,65,66,67,68,69,79,83,114,120,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'expressions':([21,43,120,],[47,74,74,]),'calculation_assign':([22,],[50,]),'condition':([25,28,],[56,60,]),'vectors':([43,],[76,]),'comparator':([57,],[83,]),'range':([58,],[90,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> instructions','program',1,'p_program','Mparser.py',28),
  ('program -> <empty>','program',0,'p_program','Mparser.py',29),
  ('instructions -> instructions instruction','instructions',2,'p_instructions','Mparser.py',37),
  ('instructions -> instruction','instructions',1,'p_instructions','Mparser.py',38),
  ('instruction -> block','instruction',1,'p_instruction','Mparser.py',46),
  ('instruction -> if','instruction',1,'p_instruction','Mparser.py',47),
  ('instruction -> for','instruction',1,'p_instruction','Mparser.py',48),
  ('instruction -> while','instruction',1,'p_instruction','Mparser.py',49),
  ('instruction -> break','instruction',1,'p_instruction','Mparser.py',50),
  ('instruction -> continue','instruction',1,'p_instruction','Mparser.py',51),
  ('instruction -> return','instruction',1,'p_instruction','Mparser.py',52),
  ('instruction -> print','instruction',1,'p_instruction','Mparser.py',53),
  ('instruction -> assign','instruction',1,'p_instruction','Mparser.py',54),
  ('block -> { instructions }','block',3,'p_block','Mparser.py',59),
  ('if -> IF ( condition ) instruction','if',5,'p_if','Mparser.py',64),
  ('if -> IF ( condition ) instruction ELSE instruction','if',7,'p_if','Mparser.py',65),
  ('for -> FOR ID = range instruction','for',5,'p_for','Mparser.py',73),
  ('range -> expression : expression','range',3,'p_range','Mparser.py',78),
  ('while -> WHILE ( condition ) instruction','while',5,'p_while','Mparser.py',83),
  ('break -> BREAK ;','break',2,'p_break','Mparser.py',88),
  ('continue -> CONTINUE ;','continue',2,'p_continue','Mparser.py',93),
  ('return -> RETURN ;','return',2,'p_return','Mparser.py',98),
  ('return -> RETURN expression ;','return',3,'p_return','Mparser.py',99),
  ('print -> PRINT expressions ;','print',3,'p_print','Mparser.py',107),
  ('expression -> singleton','expression',1,'p_expression','Mparser.py',112),
  ('expression -> vector','expression',1,'p_expression','Mparser.py',113),
  ('expression -> matrix','expression',1,'p_expression','Mparser.py',114),
  ('expression -> variable','expression',1,'p_expression','Mparser.py',115),
  ('expressions -> expressions , expression','expressions',3,'p_expressions','Mparser.py',120),
  ('expressions -> expression','expressions',1,'p_expressions','Mparser.py',121),
  ('singleton -> STRING','singleton',1,'p_singleton','Mparser.py',129),
  ('singleton -> INTEGER','singleton',1,'p_singleton','Mparser.py',130),
  ('singleton -> FLOAT','singleton',1,'p_singleton','Mparser.py',131),
  ('vector -> [ expressions ]','vector',3,'p_vector','Mparser.py',150),
  ('vector -> [ ]','vector',2,'p_vector','Mparser.py',151),
  ('vectors -> vectors , vector','vectors',3,'p_vectors','Mparser.py',159),
  ('vectors -> vector','vectors',1,'p_vectors','Mparser.py',160),
  ('matrix -> [ vectors ]','matrix',3,'p_matrix','Mparser.py',168),
  ('assign -> variable = expression ;','assign',4,'p_assign','Mparser.py',173),
  ('assign -> variable calculation_assign expression ;','assign',4,'p_assign','Mparser.py',174),
  ('calculation_assign -> ADDASSIGN','calculation_assign',1,'p_calculation_assign','Mparser.py',179),
  ('calculation_assign -> SUBASSIGN','calculation_assign',1,'p_calculation_assign','Mparser.py',180),
  ('calculation_assign -> MULASSIGN','calculation_assign',1,'p_calculation_assign','Mparser.py',181),
  ('calculation_assign -> DIVASSIGN','calculation_assign',1,'p_calculation_assign','Mparser.py',182),
  ('variable -> ID','variable',1,'p_variable','Mparser.py',187),
  ('variable -> ID [ INTEGER ]','variable',4,'p_variable','Mparser.py',188),
  ('variable -> ID [ INTEGER , INTEGER ]','variable',6,'p_variable','Mparser.py',189),
  ('comparator -> <','comparator',1,'p_comparator','Mparser.py',199),
  ('comparator -> >','comparator',1,'p_comparator','Mparser.py',200),
  ('comparator -> EQUAL','comparator',1,'p_comparator','Mparser.py',201),
  ('comparator -> NOTEQUAL','comparator',1,'p_comparator','Mparser.py',202),
  ('comparator -> LESSEQUAL','comparator',1,'p_comparator','Mparser.py',203),
  ('comparator -> GREATEREQUAL','comparator',1,'p_comparator','Mparser.py',204),
  ('condition -> expression comparator expression','condition',3,'p_condition','Mparser.py',209),
  ('expression -> expression + expression','expression',3,'p_expression_binop','Mparser.py',214),
  ('expression -> expression - expression','expression',3,'p_expression_binop','Mparser.py',215),
  ('expression -> expression * expression','expression',3,'p_expression_binop','Mparser.py',216),
  ('expression -> expression / expression','expression',3,'p_expression_binop','Mparser.py',217),
  ('expression -> expression DOTADD expression','expression',3,'p_expression_matrixop','Mparser.py',222),
  ('expression -> expression DOTSUB expression','expression',3,'p_expression_matrixop','Mparser.py',223),
  ('expression -> expression DOTMUL expression','expression',3,'p_expression_matrixop','Mparser.py',224),
  ('expression -> expression DOTDIV expression','expression',3,'p_expression_matrixop','Mparser.py',225),
  ('expression -> - expression','expression',2,'p_expression_uminus','Mparser.py',230),
  ('expression -> ( expression )','expression',3,'p_expression_parentheses','Mparser.py',235),
  ("expression -> expression '",'expression',2,'p_expression_transpose','Mparser.py',240),
  ('expression -> matrix_func ( INTEGER )','expression',4,'p_expression_matrix_functions','Mparser.py',245),
  ('expression -> matrix_func ( INTEGER , INTEGER )','expression',6,'p_expression_matrix_functions','Mparser.py',246),
  ('matrix_func -> EYE','matrix_func',1,'p_matrix_function','Mparser.py',254),
  ('matrix_func -> ONES','matrix_func',1,'p_matrix_function','Mparser.py',255),
  ('matrix_func -> ZEROS','matrix_func',1,'p_matrix_function','Mparser.py',256),
]
