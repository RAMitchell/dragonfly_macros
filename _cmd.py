from dragonfly import *

class CMDMappings(MappingRule):
	mapping = {
			'change up': Text('cd ..\n'),
			'CD': Text('cd '),
                        'dir': Text('dir\n'),
                        'list': Text('ls\n'),
                        'CD desktop': Text('cd ~/Desktop\n'),
                        'get status': Text('git status\n'),
                        'get add': Text('git add '),
                        'get commit': Text('git commit -m""')  + Key('left'),
                        'get push': Text('git push origin master'),
			}
	extras = [
			Integer('n', 0, 30	),	

			]

context = AppContext(executable='cmd') | AppContext(title='MINGW')
grammar = Grammar('cmd', context=context)
grammar.add_rule(CMDMappings())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
