
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ATTRIBUTE COMPARE DATE EXCLUDE MEASURE TOKEN statement : MEASURE TOKEN\n                | ATTRIBUTE TOKEN  statement : TOKEN MEASURE\n                | TOKEN ATTRIBUTE  statement : MEASURE TOKEN EXCLUDE\n                | ATTRIBUTE TOKEN EXCLUDE  statement : MEASURE EXCLUDE TOKEN\n                | ATTRIBUTE EXCLUDE TOKEN  statement : EXCLUDE MEASURE TOKEN\n                | EXCLUDE ATTRIBUTE TOKEN  statement : MEASURE EXCLUDE ATTRIBUTE TOKEN\n                | ATTRIBUTE EXCLUDE MEASURE TOKEN\n                | ATTRIBUTE EXCLUDE ATTRIBUTE TOKEN\n                | MEASURE EXCLUDE MEASURE TOKEN  statement : ATTRIBUTE TOKEN MEASURE\n                | MEASURE TOKEN ATTRIBUTE\n                | ATTRIBUTE TOKEN ATTRIBUTE  statement : ATTRIBUTE MEASURE TOKEN\n                | MEASURE ATTRIBUTE TOKEN\n                | ATTRIBUTE ATTRIBUTE TOKEN  statement : ATTRIBUTE TOKEN MEASURE TOKEN\n                | MEASURE TOKEN ATTRIBUTE TOKEN\n                | ATTRIBUTE TOKEN ATTRIBUTE TOKEN statement : ATTRIBUTE COMPARE MEASURE\n                | MEASURE COMPARE ATTRIBUTE\n                | ATTRIBUTE COMPARE ATTRIBUTE statement : ATTRIBUTE DATEstatement : ATTRIBUTE ATTRIBUTE DATE\n                | MEASURE ATTRIBUTE DATEstatement : ATTRIBUTE DATE DATEstatement : ATTRIBUTE ATTRIBUTE DATE DATE\n                | MEASURE ATTRIBUTE DATE DATE'
    
_lr_action_items = {'COMPARE':([1,4,],[6,14,]),'ATTRIBUTE':([0,1,2,4,5,6,8,11,14,16,17,],[1,7,12,15,18,20,24,29,32,36,38,]),'TOKEN':([0,1,4,7,9,11,15,17,18,19,24,25,29,31,36,38,39,],[2,8,16,23,27,30,34,37,40,41,43,44,45,46,48,49,50,]),'MEASURE':([0,1,2,5,6,8,11,17,],[4,9,13,19,21,25,31,39,]),'DATE':([1,7,10,15,22,33,],[10,22,28,33,42,47,]),'EXCLUDE':([0,1,4,8,16,],[5,11,17,26,35,]),'$end':([3,8,10,12,13,16,20,21,22,23,24,25,26,27,28,30,32,33,34,35,36,37,40,41,42,43,44,45,46,47,48,49,50,],[0,-2,-27,-4,-3,-1,-26,-24,-28,-20,-17,-15,-6,-18,-30,-8,-25,-29,-19,-5,-16,-7,-10,-9,-31,-23,-21,-13,-12,-32,-22,-11,-14,]),}

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
  ('statement -> MEASURE TOKEN','statement',2,'p_statement_single','grammar.py',46),
  ('statement -> ATTRIBUTE TOKEN','statement',2,'p_statement_single','grammar.py',47),
  ('statement -> TOKEN MEASURE','statement',2,'p_statement_single_second','grammar.py',53),
  ('statement -> TOKEN ATTRIBUTE','statement',2,'p_statement_single_second','grammar.py',54),
  ('statement -> MEASURE TOKEN EXCLUDE','statement',3,'p_statement_exclude','grammar.py',59),
  ('statement -> ATTRIBUTE TOKEN EXCLUDE','statement',3,'p_statement_exclude','grammar.py',60),
  ('statement -> MEASURE EXCLUDE TOKEN','statement',3,'p_statement_exclude_middle','grammar.py',65),
  ('statement -> ATTRIBUTE EXCLUDE TOKEN','statement',3,'p_statement_exclude_middle','grammar.py',66),
  ('statement -> EXCLUDE MEASURE TOKEN','statement',3,'p_statement_exclude_first','grammar.py',71),
  ('statement -> EXCLUDE ATTRIBUTE TOKEN','statement',3,'p_statement_exclude_first','grammar.py',72),
  ('statement -> MEASURE EXCLUDE ATTRIBUTE TOKEN','statement',4,'p_statement_exclude_large','grammar.py',77),
  ('statement -> ATTRIBUTE EXCLUDE MEASURE TOKEN','statement',4,'p_statement_exclude_large','grammar.py',78),
  ('statement -> ATTRIBUTE EXCLUDE ATTRIBUTE TOKEN','statement',4,'p_statement_exclude_large','grammar.py',79),
  ('statement -> MEASURE EXCLUDE MEASURE TOKEN','statement',4,'p_statement_exclude_large','grammar.py',80),
  ('statement -> ATTRIBUTE TOKEN MEASURE','statement',3,'p_statement_multiple_token_second','grammar.py',85),
  ('statement -> MEASURE TOKEN ATTRIBUTE','statement',3,'p_statement_multiple_token_second','grammar.py',86),
  ('statement -> ATTRIBUTE TOKEN ATTRIBUTE','statement',3,'p_statement_multiple_token_second','grammar.py',87),
  ('statement -> ATTRIBUTE MEASURE TOKEN','statement',3,'p_statement_multiple_token_third','grammar.py',93),
  ('statement -> MEASURE ATTRIBUTE TOKEN','statement',3,'p_statement_multiple_token_third','grammar.py',94),
  ('statement -> ATTRIBUTE ATTRIBUTE TOKEN','statement',3,'p_statement_multiple_token_third','grammar.py',95),
  ('statement -> ATTRIBUTE TOKEN MEASURE TOKEN','statement',4,'p_statement_multiple_token_four','grammar.py',101),
  ('statement -> MEASURE TOKEN ATTRIBUTE TOKEN','statement',4,'p_statement_multiple_token_four','grammar.py',102),
  ('statement -> ATTRIBUTE TOKEN ATTRIBUTE TOKEN','statement',4,'p_statement_multiple_token_four','grammar.py',103),
  ('statement -> ATTRIBUTE COMPARE MEASURE','statement',3,'p_statement_compare','grammar.py',109),
  ('statement -> MEASURE COMPARE ATTRIBUTE','statement',3,'p_statement_compare','grammar.py',110),
  ('statement -> ATTRIBUTE COMPARE ATTRIBUTE','statement',3,'p_statement_compare','grammar.py',111),
  ('statement -> ATTRIBUTE DATE','statement',2,'p_statement_time','grammar.py',117),
  ('statement -> ATTRIBUTE ATTRIBUTE DATE','statement',3,'p_statement_attribute_time','grammar.py',124),
  ('statement -> MEASURE ATTRIBUTE DATE','statement',3,'p_statement_attribute_time','grammar.py',125),
  ('statement -> ATTRIBUTE DATE DATE','statement',3,'p_statement_time_time','grammar.py',132),
  ('statement -> ATTRIBUTE ATTRIBUTE DATE DATE','statement',4,'p_statement_attribute_time_time','grammar.py',140),
  ('statement -> MEASURE ATTRIBUTE DATE DATE','statement',4,'p_statement_attribute_time_time','grammar.py',141),
]