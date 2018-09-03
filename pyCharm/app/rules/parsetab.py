
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DIMENSION EXCLUDE MEASURE METRIC TOKEN statement : METRIC TOKEN\n                | DIMENSION TOKEN  statement : TOKEN METRIC\n                | TOKEN DIMENSION  statement : METRIC TOKEN EXCLUDE\n                | DIMENSION TOKEN EXCLUDE  statement : EXCLUDE METRIC TOKEN\n                | EXCLUDE DIMENSION TOKEN  statement : DIMENSION TOKEN METRIC\n                | METRIC TOKEN DIMENSION\n                | DIMENSION TOKEN DIMENSION  statement : DIMENSION METRIC TOKEN\n                | METRIC DIMENSION TOKEN\n                | DIMENSION DIMENSION TOKEN  statement : DIMENSION MEASURE METRIC\n                | METRIC MEASURE DIMENSION '
    
_lr_action_items = {'METRIC':([0,2,4,5,14,16,],[1,9,11,13,24,28,]),'TOKEN':([0,1,5,8,11,12,13,15,],[2,7,14,20,21,22,23,27,]),'MEASURE':([1,5,],[6,16,]),'EXCLUDE':([0,7,14,],[4,18,25,]),'DIMENSION':([0,1,2,4,5,6,7,14,],[5,8,10,12,15,17,19,26,]),'$end':([3,7,9,10,14,17,18,19,20,21,22,23,24,25,26,27,28,],[0,-1,-3,-4,-2,-16,-5,-10,-13,-7,-8,-12,-9,-6,-11,-14,-15,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[3,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> METRIC TOKEN','statement',2,'p_statement_single','grammar.py',45),
  ('statement -> DIMENSION TOKEN','statement',2,'p_statement_single','grammar.py',46),
  ('statement -> TOKEN METRIC','statement',2,'p_statement_single_second','grammar.py',52),
  ('statement -> TOKEN DIMENSION','statement',2,'p_statement_single_second','grammar.py',53),
  ('statement -> METRIC TOKEN EXCLUDE','statement',3,'p_statement_exclude','grammar.py',59),
  ('statement -> DIMENSION TOKEN EXCLUDE','statement',3,'p_statement_exclude','grammar.py',60),
  ('statement -> EXCLUDE METRIC TOKEN','statement',3,'p_statement_exclude_first','grammar.py',66),
  ('statement -> EXCLUDE DIMENSION TOKEN','statement',3,'p_statement_exclude_first','grammar.py',67),
  ('statement -> DIMENSION TOKEN METRIC','statement',3,'p_statement_multiple_token_second','grammar.py',73),
  ('statement -> METRIC TOKEN DIMENSION','statement',3,'p_statement_multiple_token_second','grammar.py',74),
  ('statement -> DIMENSION TOKEN DIMENSION','statement',3,'p_statement_multiple_token_second','grammar.py',75),
  ('statement -> DIMENSION METRIC TOKEN','statement',3,'p_statement_multiple_token_third','grammar.py',81),
  ('statement -> METRIC DIMENSION TOKEN','statement',3,'p_statement_multiple_token_third','grammar.py',82),
  ('statement -> DIMENSION DIMENSION TOKEN','statement',3,'p_statement_multiple_token_third','grammar.py',83),
  ('statement -> DIMENSION MEASURE METRIC','statement',3,'p_statement_measure','grammar.py',89),
  ('statement -> METRIC MEASURE DIMENSION','statement',3,'p_statement_measure','grammar.py',90),
]