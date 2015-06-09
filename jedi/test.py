import jedi

src = """
class Test(object):
    @defer.inlineCallbacks
    def method(a):
        defer.returnValue(Test())

Test().method(1).<>
"""

line_number = 0
col_number = 0
for line in src.split('\n'):
    line_number += 1

    if line.find('<>') > -1:
        col_number = line.find('<>')
        src = src.replace('<>', '')
        break

completions = jedi.Script(src, line_number, col_number, 'example.py').completions()
print(completions)