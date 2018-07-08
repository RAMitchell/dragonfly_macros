from dragonfly import *


class TelephonyRule(MappingRule):
    exported = True
    mapping = {
        'alpha': Key('a', static=True),
        'bat': Key('b', static=True),
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

        'up alpha': Key('A', static=True),
        'up bat': Key('B', static=True),
        'up charlie': Key('C', static=True),
        'up delta': Key('D', static=True),
        'up echo': Key('E', static=True),
        'up foxtrot': Key('F', static=True),
        'up golf': Key('G', static=True),
        'up hotel': Key('H', static=True),
        'up india': Key('I', static=True),
        'up juliet': Key('J', static=True),
        'up kilo': Key('K', static=True),
        'up lima': Key('L', static=True),
        'up mike': Key('M', static=True),
        'up november': Key('N', static=True),
        'up oscar': Key('O', static=True),
        'up papa': Key('P', static=True),
        'up queen': Key('Q', static=True),
        'up romeo': Key('R', static=True),
        'up suk': Key('S', static=True),
        'up tango': Key('T', static=True),
        'up uniform': Key('U', static=True),
        'up venous': Key('V', static=True),
        'up whiskey': Key('W', static=True),
        'up x-ray': Key('X', static=True),
        'up yankee': Key('Y', static=True),
        'up zulu': Key('Z', static=True),

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
        '(raip|right)': Key('rparen'),
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
        'exit|exerpt': Key('a-f4'),
        "desktop": Key("w-d"),
        "cuda": Text("cuda "),
        "lard": Key("c-c"),
        "card": Key("c-v"),
        "pop": Key("shift:down/2, insert, shift:up"),
        "menu": Key("s-f10"),
        "task": Key("w-tab"),
    }
    extras = [
        Integer('n', 0, 30),

    ]


grammar = Grammar('Global')
grammar.add_rule(RepeatTelephony())
grammar.add_rule(GlobalMappings())
grammar.load()


def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
