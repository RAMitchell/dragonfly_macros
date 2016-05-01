
from dragonfly import (Grammar, AppContext, MappingRule, Integer, Key, Dictation, Text, Alternative, Repetition, RuleRef, CompoundRule)


class  GlobalIntelliJMappings(MappingRule):
    mapping = {
        #ide shortcuts
        "helper": Key("a-enter"),
        "reformat": Key("ctrl:down, a-l, ctrl:up"),
        "project": Key("ctrl:down, tab:down/10,1/10,tab:up,ctrl:up"), 
	"rename":   Key("shift:down,f6/10, shift:up"),
	"run": Key("s-f10"),
	"debug": Key("s-f9"),
	"stop": Key("c-f2"),

        }
    extras = [
        Dictation("text"),
        Integer("n", 0, 50),
        Integer("line", 1, 10000)
        ]

context = AppContext(executable='idea64')
grammar=Grammar('IntelliJ',context=context)
grammar.add_rule(GlobalIntelliJMappings())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None


