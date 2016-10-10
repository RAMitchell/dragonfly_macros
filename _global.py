from dragonfly import *

class TelephonyRule(MappingRule):
    exported = True 
    mapping = {
        'alpha': Key('a', static=True),
        'bravo': Key('b', static=True),
        'charlie': Key('c', static=True),
        'delta': Key('d', static=True),
        'echo': Key('e', static=True),
        'foxtrot': Key('f', static=True),
        'golf': Key('g', static=True),
        'hotel': Key('h', static=True),
        'India': Key('i', static=True),
        'juliet': Key('j', static=True),
        'kilo': Key('k', static=True),
        'lima': Key('l', static=True),
        'mike': Key('m', static=True),
        'november': Key('n', static=True),
        'oscar': Key('o', static=True),
        'papa': Key('p', static=True),
        'queen': Key('q', static=True),
        'romeo': Key('r', static=True),
        'suk': Key('s', static=True),
        'tango': Key('t', static=True),
        'uniform': Key('u', static=True),
        'venous': Key('v', static=True),
        'whiskey': Key('w', static=True),
        'x-ray': Key('x', static=True),
        'yankee': Key('y', static=True),
        'zulu': Key('z', static=True),

        'upper alpha': Key('A', static=True),
        'upper bravo': Key('B', static=True),
        'upper charlie': Key('C', static=True),
        'upper delta': Key('D', static=True),
        'upper echo': Key('E', static=True),
        'upper foxtrot': Key('F', static=True),
        'upper golf': Key('G', static=True),
        'upper hotel': Key('H', static=True),
        'upper india': Key('I', static=True),
        'upper juliet': Key('J', static=True),
        'upper kilo': Key('K', static=True),
        'upper lima': Key('L', static=True),
        'upper mike': Key('M', static=True),
        'upper november': Key('N', static=True),
        'upper oscar': Key('O', static=True),
        'upper papa': Key('P', static=True),
        'upper queen': Key('Q', static=True),
        'upper romeo': Key('R', static=True),
        'upper suk': Key('S', static=True),
        'upper tango': Key('T', static=True),
        'upper uniform': Key('U', static=True),
        'upper venous': Key('V', static=True),
        'upper whiskey': Key('W', static=True),
        'upper x-ray': Key('X', static=True),
        'upper yankee': Key('Y', static=True),
        'upper zulu': Key('Z', static=True),

        'zero': Key('0'),
        'one': Key('1'),
        'two': Key('2'),
        'three': Key('3'),
        'four': Key('4'),
        'five': Key('5'),
        'six': Key('6'),
        'seven': Key('7'),
        'eight': Key('8'),
        'nine': Key('9'),

        'space': Key('space'),
        'tab': Key('tab'),

        'ampersand': Key('ampersand'),
        'apostrophe': Key('apostrophe'),
        'asterisk': Key('asterisk'),
        'at': Key('at'),
        'backslash': Key('backslash'),
        'backtick': Key('backtick'),
        'bar': Key('bar'),
        'caret': Key('caret'),
        'colon': Key('colon'),
        'comma': Key('comma'),
        'dollar': Key('dollar'),
        '(dot|period)': Key('dot'),
        'quote': Key('dquote'),
        'equal': Key('equal'),
        'bang': Key('exclamation'),
        'hash': Key('hash'),
        'hyphen': Key('hyphen'),
        'minus': Key('minus'),
        'percent': Key('percent'),
        'plus': Key('plus'),
        'question': Key('question'),
        'slash': Key('slash'),
        'single quote': Key('squote'),
        'tilde': Key('tilde'),
        'underscore': Key('underscore'),

        'langle': Key('langle'),
        'lace': Key('lbrace'),
        'lack': Key('lbracket'),
        'laip': Key('lparen'),
        'rangle': Key('rangle'),
        'race': Key('rbrace'),
        'rack': Key('rbracket'),
        'raip': Key('rparen'),
    }

telephony_single = Alternative([RuleRef(rule=TelephonyRule())])
telephony_sequence = Repetition(telephony_single, min=1, max=10, name="telephony_sequence")

class RepeatTelephony(CompoundRule):
    spec = '<telephony_sequence>'
    extras = [telephony_sequence]

    def _process_recognition(self, node, extras):
        for action in extras['telephony_sequence']:
            action.execute()

class GlobalMappings(MappingRule):
	mapping = {

			'slap': Key('enter'),
			'flip <n>': Key('w-t/5, right:%(n)d/10, enter'),
			'flip': Key('a-tab'),
			'jump <n>': Key('win:down, alt:down, %(n)d, win:up, alt:up, down'), 
			'exit|exerpt': Key('a-f4'),
			"desktop": Key("w-d"),
			"cuda": Text("cuda "),

                        "menu": Key("s-f10"),
                        "task": Key("w-tab"),
			}
	extras = [
			Integer('n', 0, 30	),	

			]
grammar = Grammar('Global')
grammar.add_rule(RepeatTelephony())
grammar.add_rule(GlobalMappings())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
