from par import parser
from scheduler import schedule
data = '''
INPUT a, b, c
OUTPUT s, r
VAR
  _l_1, _l_3, _l_4, _l_5, a, b, c, r, s
IN
r = OR _l_3 _l_5
s = XOR _l_1 c
_l_1 = XOR a b
_l_3 = AND a b
_l_4 = XOR a b
_l_5 = AND _l_4 c
'''

program = parser.parse(data)

scheduled_program = schedule(program)
print("lol")