from dragonfly import (Grammar, AppContext, MappingRule, Integer, Key, Dictation, Text, Alternative, Repetition, RuleRef, CompoundRule)


class GlobalChromeMappings(MappingRule):
    mapping = {
        'close tab': Key('c-w'),
	'new tab': Key('c-t'),
        'reopen tab': Key('cs-t'),
        'next': Key('c-pgdown'),
        'previous': Key('c-pgup'),
        'tab <tab>': Key('c-%(tab)d'),
        'first tab': Key('c-1'),
        'last tab': Key('c-9'),
        'back': Key('a-left'),
        'forward': Key('a-right'),
        'address': Key('c-l'),
        'reload page': Key('f5'),
        'labels': Key('f'),                         # vimium

        '[go to] label <number>': Text('%(number)d'),    # vimium
	'find': Key('c-f'),
	'search <text>': Key('c-l') + Text('%(text)s\r'),
        }
    extras=[
        Integer('tab', 1, 30	),
        Integer('number', 1, 9999),
		Dictation("text"),
    ]

context = AppContext(executable='chrome',  title='Google Chrome')
grammar=Grammar('Google Chrome',context=context)
grammar.add_rule(GlobalChromeMappings())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
