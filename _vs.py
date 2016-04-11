
from dragonfly import (Grammar, AppContext, MappingRule, Integer, Key, Dictation, Text, Alternative, Repetition, RuleRef, CompoundRule)


class  GlobalVSMappings(MappingRule):
    mapping = {
        #ide shortcuts
	"run": Key("c-f5"),
	"device vector": Text("thrust::device_vector<"),
	"thrust": Text("thrust::"),
	"(<n>) next tab": Key("ctrl:down,alt:down/10,pgdown/10,ctrl:up,alt:up"),

        }
    extras = [
        Dictation("text"),
        Integer("n", 0, 50),
        Integer("line", 1, 10000)
        ]

context = AppContext(  title='Visual Studio')
grammar=Grammar('VS',context=context)
grammar.add_rule(GlobalVSMappings())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None


