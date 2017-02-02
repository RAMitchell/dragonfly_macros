
from dragonfly import (Grammar, AppContext, MappingRule, Integer, Key, Dictation, Text, Alternative, Repetition, RuleRef, CompoundRule)


class  GlobalVSMappings(MappingRule):
    mapping = {
        #ide shortcuts
	"run": Key("c-f5"),
	"build": Key("f7"),
	"device vector": Text("thrust::device_vector<"),
	"thrust": Text("thrust::"),
	"(<n>) next tab": Key("ctrl:down,alt:down/2,pgdown/2,ctrl:up,alt:up"),
	"reformat": Key("ctrl:down,alt:down/10,enter,alt:up,ctrl:up"),
	"code": Key("ctrl:down,alt:down/1,0/1,alt:up,ctrl:up"),
	"output": Key("a-2"),
	"rename": Key("c-r,r/1"),
	"bop": Key("c-pgdown"),
	"doc": Key("ctrl:down, shift:down/2, d/2, ctrl:up, shift:up"),
	"comment": Key("c-k, c-c, escape"),
	"uncomment": Key("c-k, c-u, escape"),

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


