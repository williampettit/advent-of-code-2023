# day1 p2
with open('1.in') as f:
  lines = f.readlines()
ans = 0
for line in lines:
  line_digs = []
  for pos, ch in enumerate(line):
    if ch.isdigit():
      line_digs.append(ch)
    for dig_val, dig_name in enumerate(('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')):
      if line[pos:pos+len(dig_name)] == dig_name:
        line_digs.append(str(dig_val+1))
  ans += int(line_digs[0] + line_digs[-1])
print(ans)
