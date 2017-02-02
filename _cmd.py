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
                        'get clone': Text('git clone '),
                        'get checkout': Text('git checkout '),
                        'get commit': Text('git commit -m""')  + Key('left'),
                        'get push': Text('git push origin master'),
                        'python': Text('python '),
                        'run': Key('up, enter'),
			}
	extras = [
			Integer('n', 0, 30	),	

			]

context = AppContext(executable='cmd') | AppContext(title='MINGW') | AppContext(executable='putty')
grammar = Grammar('cmd', context=context)
grammar.add_rule(CMDMappings())
grammar.load()

def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
