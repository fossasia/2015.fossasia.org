#!/usr/bin/env python3
import os
from pathlib import Path
from itertools import count, cycle
from os.path import abspath, dirname

dir_proj = Path(abspath(__file__)).parent.parent
dir_include = dir_proj / '_includes'
dir_asset = dir_proj / 'assets'
dir_speaker = dir_asset / 'images' / 'speakers'

TEMPLATE = """
<div class='col-md-2'>
	<img src='/{}'>
</div>"""

WRAP = """
<div class='row'>{}
</div>
"""

if __name__ == '__main__':
	lines = []
	rows = []
	t = cycle(range(6))
	for i, p in zip(t, dir_speaker.glob('*')):
		rel = p.relative_to(dir_proj)
		line = TEMPLATE.format(rel)
		print(rel.name)
		lines.append(line)
		if i == 5:
			rows.append(WRAP.format(''.join(lines)))
			lines = []

	out = dir_include / 'speaker_list.html'
	with out.open('w') as fl:
		fl.write(''.join(rows))