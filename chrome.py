from dragonfly import (Grammar, AppContext, MappingRule, Integer, Key, Dictation, Text, Alternative, Repetition, RuleRef, CompoundRule)

class TelephonyRule(MappingRule):
    exported = False

    mapping = {
        "alpha": Key("a"),
        "bravo": Key("b"),
        "charlie": Key("c"),
        "delta": Key("d"),
        "echo": Key("e"),
        "foxtrot": Key("f"),
        "golf": Key("g"),
        "hotel": Key("h"),
        "india": Key("i"),
        "juliet": Key("j"),
        "kilo": Key("k"),
        "lima": Key("l"),
        "mike": Key("m"),
        "november": Key("n"),
        "oscar": Key("o"),
        "papa": Key("p"),
        "quebec": Key("q"),
        "romeo": Key("r"),
        "sierra": Key("s"),
        "tango": Key("t"),
        "uniform": Key("u"),
        "victor": Key("v"),
        "whiskey": Key("w"),
        "xray": Key("x"),
        "yankee": Key("y"),
        "zulu": Key("z"),
        "zero": Key("0"),
        "one": Key("1"),
        "two": Key("2"),
        "tree": Key("3"),
        "four": Key("4"),
        "fife": Key("5"),
        "six": Key("6"),
        "seven": Key("7"),
        "eight": Key("8"),
        "niner": Key("9"),
    }

telephony_single = Alternative([RuleRef(rule=TelephonyRule())])
telephony_sequence = Repetition(telephony_single, min=1, max=10, name="telephony_sequence")

class RepeatTelephony(CompoundRule):
    spec = '<telephony_sequence>'
    extras = [telephony_sequence]

    def _process_recognition(self, node, extras):
        for action in extras['telephony_sequence']:
            action.execute()

class GlobalChromeMappings(MappingRule):
    mapping = {
        'close tab': Key('c-w'),
	'new tab': Key('c-t'),
        'reopen tab': Key('cs-t'),
        'next tab': Key('c-pgdown'),
        'previous tab': Key('c-pgup'),
        'tab <tab>': Key('c-%(tab)d'),
        'first tab': Key('c-1'),
        'last tab': Key('c-9'),
        'back': Key('a-left'),
        'forward': Key('a-right'),
        'address': Key('c-l'),
        'reload page': Key('f5'),
        'labels': Key('f'),                         # vimium

        '[go to] label <number>': Text('%(number)d'),    # vimium
	'[<number>] down': Key('pgdown/2:%(number)d'),
	'[<number>] up': Key('pgup/2:%(number)d'),
	'find': Key('c-f'),
	'search <text>': Key('c-l') + Text('%(text)s\r'),
        }
    extras=[
        Integer('tab', 1, 30	),
        Integer('number', 1, 9999),
		Dictation("text"),
    ]

context = AppContext(executable='chrome')
grammar=Grammar('Google Chrome',context=context)
grammar.add_rule(GlobalChromeMappings())
#grammar.add_rule(RepeatTelephony())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
