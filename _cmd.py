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
        'get stash': Text('git stash\n'),
        'get fetch': Text('git fetch '),
        'get clone': Text('git clone '),
        'get checkout': Text('git checkout '),
        'get commit': Text('git commit -m""') + Key('left'),
        'get commit amend': Text('git commit --amend --no-edit -a'),
        'get push': Text('git push origin HEAD'),
        'python': Text('python '),
        'run': Key('up, enter'),
        'run second': Text('!-2\n'),
        'go': Key('tab, enter'),
    }
    extras = [
        Integer('n', 0, 30),

    ]


context = AppContext(executable='cmd') | AppContext(title='MINGW') | AppContext(executable='putty') | AppContext(
    executable='mintty') | AppContext(executable='MobaXterm')
grammar = Grammar('cmd', context=context)
grammar.add_rule(CMDMappings())
grammar.load()


def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
