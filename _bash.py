from dragonfly import *

class LetterRule(MappingRule):
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
        'sierra': Key('s', static=True),
        'tango': Key('t', static=True),
        'uniform': Key('u', static=True),
        'victor': Key('v', static=True),
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
        'upper sierra': Key('S', static=True),
        'upper tango': Key('T', static=True),
        'upper uniform': Key('U', static=True),
        'upper victor': Key('V', static=True),
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
        'double quote': Key('dquote'),
        'equal': Key('equal'),
        'bang': Key('exclamation'),
        'hash': Key('hash'),
        'hyphen': Key('hyphen'),
        'minus': Key('minus'),
        'percent': Key('percent'),
        'plus': Key('plus'),
        'question': Key('question'),
        # Getting Invalid key name: 'semicolon'
        #'semicolon': Key('semicolon'),
        'slash': Key('slash'),
        '[single] quote': Key('squote'),
        'tilde': Key('tilde'),
        'underscore | score': Key('underscore'),

        'langle': Key('langle'),
        'lace': Key('lbrace'),
        'lack': Key('lbracket'),
        'lapen': Key('lparen'),
        'rangle': Key('rangle'),
        'race': Key('rbrace'),
        'rack': Key('rbracket'),
        'rapen': Key('rparen'),
    }


class GlobalBashMappings(MappingRule):
    mapping = {
		'CD' : Key("c, d, space"),		   
		'make dir' : Key("m, k, d, i, r, space"),		    
		 'slap': Key("enter"),
		 'list': Key("l,s, enter"),
        }
    extras=[

        Integer('number', 1, 9999),
		Dictation("text"),
    ]

context = AppContext(executable='bash')
grammar=Grammar('bash',context=context)
grammar.add_rule(GlobalBashMappings())
grammar.add_rule(LetterRule())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
