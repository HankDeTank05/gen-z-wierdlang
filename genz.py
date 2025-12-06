import re
import sys
import subprocess

def transpile(code: str) -> str:
	'''converts genz code into python code'''

	replacements = [
		# commenting
		
		# lowkey --> #
		(r'(lowkey )(.*)', r'# \2'),

		# other basic stuff

		# spill ? tea --> print(?)
		(r'(spill )(.*)( tea)', r'print(\2)'),
		# sip ? tea --> input(?)
		(r'(sip )(.*)( tea)', r'input(\2)'),
		# is giving --> =
		(r'(\w*)( is giving )(.*)', r'\1 = \3'),
		# <val> is <type>-core --> <type>(<val>)
		(r'(\w*)( is )(\w*)(-core)', r'\3(\1)'),

		# literal values

		# mid --> None
		(r'(mid)', 'None'),
		# green flag --> True
		(r'(green flag)', 'True'),

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

		# comparison ops

		# A ate B and left no crumbs --> A > B
		(r'(.*)( ate )(.*)( and left no crumbs)', r'\1 > \3'),
		# A ate B --> A >= B
		(r'(.*)( ate )(.*)', r'\1 >= \3'),
		# A got cancelled and ratioed by B --> A < B
		(r'(.*)( got cancelled and ratioed by )(.*)', r'\1 < \3'),
		# A got cancelled by B --> A <= B
		(r'(.*)( got cancelled by )(.*)', r'\1 <= \3')
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