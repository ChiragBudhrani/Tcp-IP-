
dest = format(8095, 'x')
source = hex(int('5424'))


ackNumber = '00000000'
seqNumber = '00000000'

Offset = '51020010'

print(source + dest + seqNumber + ackNumber + Offset)
