from dragonfly import *

class GlobalBashMappings(MappingRule):
    mapping = {
		'CD' : Key("c, d, space"),		   
		'change up': Key("c, d, space, dot, dot, enter"),
		'make directory' : Key("m, k, d, i, r, space"),		    
		 'slap': Key("enter"),
		 'list': Key("l,s, enter"),
		 'git|get': Key("g,i,t,space"),
		 'git|get update': Text("git add -u\r"),
		 'git|get status': Text("git status\r"),
		 'git|get commit': Text('git commit -m ""') + Key('left'),
 		 'git|get commit modified': Text('git commit -a -m ""') + Key('left'),
		 'git|get push': Text("git push\r"),
		 'git|get pull': Text("git pull\r"),
		 'git|get clone': Text("git clone "),
		 'paste': Key("a-space, e, p"),
		 'make': Text("make\r"),
		 }
    extras=[

        Integer('number', 1, 9999),
		Dictation("text"),
    ]

context = AppContext(executable='sh', title='bash')
grammar=Grammar('bash',context=context)
grammar.add_rule(GlobalBashMappings())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
