
from dragonfly import (Grammar, AppContext, MappingRule, Integer, Key, Dictation, Text, Alternative, Repetition, RuleRef, CompoundRule)


class  GlobalVSMappings(MappingRule):
    mapping = {
        #ide shortcuts
	"run": Key("c-f5"),
	"build": Key("ctrl:down,shift:down/1,b/1,shift:up,ctrl:up"),
	"device vector": Text("thrust::device_vector<"),
	"thrust": Text("thrust::"),
	"reformat":Key("alt:down,shift:down/1,k/1,shift:up,alt:up"),
	"code": Key("ctrl:down,alt:down/1,0/1,alt:up,ctrl:up"),
	"output": Key("a-2"),
	"rename": Key("c-r,r/1"),

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


