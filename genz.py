import re
import sys
import subprocess

var_func_name_pattern = r'[a-zA-Z_]{1}\w*'
indexing_pattern = r'\['+var_func_name_pattern+r'\]'
str_lit_pattern = r'[\'"]{1}.*[\'"]{1}'
comment_sl_pattern = r'(lowkey )'
comment_ml_pattern = r'(highkey)((?:\s{0,1})(?:.*\n)*?(?:\s{0,1}))(on god)'
'''
(highkey\s?)(\s?on god)
'''

def transpile(code: str) -> str:
	'''converts genz code into python code'''

	replacements = [
		# commenting
		
		# lowkey --> #
		(r'(lowkey)', r'#'),
		# highkey _ on god --> """ _ """
		# (comment_ml_pattern, r'"""\2"""'),
		(r'(highkey)', '"""'),
		(r'(on god)', '"""'),

		# other basic stuff

		# spill ? tea --> print(?)
		(r'(spill )(.*)( tea)', r'print(\2)'),
		# sip ? tea --> input(?)
		(r'(sip )(.*)( tea)', r'input(\2)'),
		# is giving --> =
		(r'( is giving )', ' = '),
		# <val> is <type>-core --> <type>(<val>)
		(r'(\w*)( is )(\w*)(-core)', r'\3(\1)'),

		# literal values

		# mid --> None
		(r'(mid)', 'None'),
		# green flag --> True
		(r'(green flag)', 'True'),
		# red flag --> False
		(r'(red flag)', 'False'),

		# if stuff

		# POV --> if
		(r'(POV)', 'if'),
		# we're so back --> elif
		(r"(we're so back)", 'elif'),
		# it's so over --> else
		(r"(it's so over)", 'else'),
		# bet --> :
		(r'( bet)', ':'),

		# assertions

		# be fucking for real ? --> assert(?)
		(r'(be fucking for real )(.*)', r'assert(\2)'),

		# loop stuff

		# cooking with --> while
		(r'(cooking with)', 'while'),
		# say less --> continue
		(r'(say less)', 'continue'),
		# crash out --> break
		(r'(crash out)', 'break'),

		# bestie _ aura farming _ --> for _ in _
		(r'(bestie )(.*?)( aura farming )(.*)', r'for \2 in \4'),

		# comparison ops

		# A vibes with B --> A == B
		(r'( vibes with )', ' == '),
		# A vibe checks B --> A != B
		(r'( vibe checks )', ' != '),
		# A ate B and left no crumbs --> A > B
		(r'(.*)( ate )(.*)( and left no crumbs)', r'\1 > \3'),
		# A ate B --> A >= B
		(r'(.*)( ate )(.*)', r'\1 >= \3'),
		# A got cancelled and ratioed by B --> A < B
		(r'(.*)( got cancelled and ratioed by )(.*)', r'\1 < \3'),
		# A got cancelled by B --> A <= B
		(r'(.*)( got cancelled by )(.*)', r'\1 <= \3'),
		# _ in _
		(r'( aura farming )', ' in '),

		# list stuff

		# gyatt --> []
		(r'(gyatt)', '[]'),
		# pulled --> .append
		(r'( pulled )(.*)', r'.append(\2)'),
		# pull up _ --> [_]
		(r'( pull up )([\d+\w+])', r'[\2]'),
		# fit check <list> --> len(<list>)
		(r'(fit check )((?:'+var_func_name_pattern+r')(?:'+indexing_pattern+r')*)', r'len(\2)'),

		# function stuff

		# finna --> def
		(r'([\t ]*)(finna)', r'\1def'),
		# clapback with --> return
		(r'(clapback with )', 'return '),
	]

	python_code = code

	for pattern, replacement in replacements:
		python_code = re.sub(pattern, replacement, python_code)

	return python_code

def main():
	if len(sys.argv) < 2:
		print('Usage: python genz.py <genz.txt>')
		return
	
	input_file = sys.argv[1]

	with open(input_file, 'r', encoding='utf-8') as f:
		genz_code = f.read()

	python_code = transpile(genz_code)
	output_fname = 'output.py'

	with open(output_fname, 'w', encoding='utf-8') as f:
		f.write(python_code)

	print(f'✨ Transpiled to {output_fname}')

	# automatically run the python file
	print(f'🏃 Running {output_fname}...\n')
	subprocess.run(['python', output_fname])

if __name__ == "__main__":
	main()