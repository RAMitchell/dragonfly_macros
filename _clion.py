from dragonfly import *

class InsertModeEnabler(CompoundRule):
    spec = "<command>"
    extras = [Choice("command", {

        "insert": "i",
        "shift insert": "I",

        "change": "c",
        "change whiskey": "c,w",
        "change (echo|end)": "c,e",
        "change a paragraph": "c,a,p",
        "change inner paragraph": "c,i,p",
        "change a (paren|parenthesis|raip|laip)": "c,a,rparen",
        "change inner (paren|parenthesis|raip|laip)": "c,i,rparen",
        "shift change": "C",

        "sub line" : "S",

        "(after | append)": "a",
        "shift (after | append)": "A",

        "oh": "o",
        "shift oh": "O",

	# Jedi vim rename command
	"rename": "backslash,r",
    })]

    def _process_recognition(self, node, extras):
        InsertModeBootstrap.disable()
        normalModeGrammar.disable()
        InsertModeGrammar.enable()
        for string in extras["command"].split(','):
            key = Key(string)
            key.execute()
        print "Available commands:"
        print '  \n'.join(InsertModeCommands.mapping.keys())
        print "\n(INSERT)"



class InsertModeDisabler(CompoundRule):
    # spoken command to exit InsertMode
    spec = "<command>"
    extras = [Choice("command", {
        "done": "okay",
        "cancel": "cancel",
    })]

    def _process_recognition(self, node, extras):
        InsertModeGrammar.disable()
        InsertModeBootstrap.enable()
        normalModeGrammar.enable()
        Key("escape").execute()
        if extras["command"] == "cancel":
		Key("u:2").execute()
		print "Insert command canceled"
        else:
            print "Insert command accepted"
        print "\n(NORMAL)"


# handles InsertMode control structures
class InsertModeCommands(MappingRule):
    mapping  = {
	"slap": Key("enter"),
        "[<n>] (scratch|delete)": Key("c-w:%(n)d"),
        "[<n>] tab": Key("tab:%(n)d"),
        "[<n>] backspace": Key("backspace:%(n)d"),
        "(scratch|delete) line": Key("c-u"),
        "[<n>] left": Key("left:%(n)d"),
        "[<n>] right": Key("right:%(n)d"),

	"assign": Key("space,equal,space"),
	"plus": Key("space,plus,space"),
	"minus": Key("space,minus,space"),
	"times": Key("space,asterisk,space"),
	"equals": Key("space,equal,equal,space"),
	"not equals": Key("space,exclamation,equal,space"),
	"triple quote": Key("dquote,dquote,dquote"),
	"ref": Key("asterisk"),

	#C++
	"int": Text("int "),
	"for loop": Text("for(int i = 0; i < y; i++)"),
	"include": Text("#include <>") + Key("left"),
	"include local": Text('#include ""') + Key("left"),
	"pragma once": Text("#pragma once"),

    }
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 50),
    ]
    defaults = {
        "n": 1,
    }


#---------------------------------------------------------------------------
# Here we globally defined the release action which releases all
#  modifier-keys used within this grammar.  It is defined here
#  because this functionality is used in many different places.
#  Note that it is harmless to release ("...:up") a key multiple
#  times or when that key is not held down at all.

release = Key("shift:up, ctrl:up")

class LetterRule(MappingRule):
    exported = True
    mapping = {
        'alpha': Key('a', static=True),
        'bravo': Key('b', static=True),
        'charlie': Key('c', static=True),
        'delta': Key('d', static=True),
        'echo': Key('e', static=True),
        'foxtrot': Key('f', static=True),
        'golf': Key('g', static=True),
        'hotel': Key('h', static=True),
        'India': Key('i', static=True),
        'juliet': Key('j', static=True),
        'kilo': Key('k', static=True),
        'lima': Key('l', static=True),
        'mike': Key('m', static=True),
        'november': Key('n', static=True),
        'oscar': Key('o', static=True),
        'papa': Key('p', static=True),
        'queen': Key('q', static=True),
        'romeo': Key('r', static=True),
        'sierra': Key('s', static=True),
        'tango': Key('t', static=True),
        'uniform': Key('u', static=True),
        'victor': Key('v', static=True),
        'whiskey': Key('w', static=True),
        'x-ray': Key('x', static=True),
        'yankee': Key('y', static=True),
        'zulu': Key('z', static=True),

        'upper alpha': Key('A', static=True),
        'upper bravo': Key('B', static=True),
        'upper charlie': Key('C', static=True),
        'upper delta': Key('D', static=True),
        'upper echo': Key('E', static=True),
        'upper foxtrot': Key('F', static=True),
        'upper golf': Key('G', static=True),
        'upper hotel': Key('H', static=True),
        'upper india': Key('I', static=True),
        'upper juliet': Key('J', static=True),
        'upper kilo': Key('K', static=True),
        'upper lima': Key('L', static=True),
        'upper mike': Key('M', static=True),
        'upper november': Key('N', static=True),
        'upper oscar': Key('O', static=True),
        'upper papa': Key('P', static=True),
        'upper queen': Key('Q', static=True),
        'upper romeo': Key('R', static=True),
        'upper sierra': Key('S', static=True),
        'upper tango': Key('T', static=True),
        'upper uniform': Key('U', static=True),
        'upper victor': Key('V', static=True),
        'upper whiskey': Key('W', static=True),
        'upper x-ray': Key('X', static=True),
        'upper yankee': Key('Y', static=True),
        'upper zulu': Key('Z', static=True),

        'zero': Key('0'),
        'one': Key('1'),
        'two': Key('2'),
        'three': Key('3'),
        'four': Key('4'),
        'five': Key('5'),
        'six': Key('6'),
        'seven': Key('7'),
        'eight': Key('8'),
        'nine': Key('9'),

        'space': Key('space'),
        'tab': Key('tab'),

        'ampersand': Key('ampersand'),
        'apostrophe': Key('apostrophe'),
        'asterisk': Key('asterisk'),
        'at': Key('at'),
        'backslash': Key('backslash'),
        'backtick': Key('backtick'),
        'bar': Key('bar'),
        'caret': Key('caret'),
        'colon': Key('colon'),
        'comma': Key('comma'),
        'dollar': Key('dollar'),
        '(dot|period)': Key('dot'),
        'quote': Key('dquote'),
        'equal': Key('equal'),
        'bang': Key('exclamation'),
        'hash': Key('hash'),
        'hyphen': Key('hyphen'),
        'minus': Key('minus'),
        'percent': Key('percent'),
        'plus': Key('plus'),
        'question': Key('question'),
        # Getting Invalid key name: 'semicolon'
        #'semicolon': Key('semicolon'),
        'slash': Key('slash'),
        'single quote': Key('squote'),
        'tilde': Key('tilde'),
        'underscore': Key('underscore'),

        'langle': Key('langle'),
        'lace': Key('lbrace'),
        'lack': Key('lbracket'),
        'lapen': Key('lparen'),
        'rangle': Key('rangle'),
        'race': Key('rbrace'),
        'rack': Key('rbracket'),
        'rapen': Key('rparen'),
    }

letter = RuleRef(rule=LetterRule(), name='letter')
letter_sequence = Repetition(letter, min=1, max=32, name='letter_sequence')

def executeLetter(letter):
    letter.execute()

def executeLetterSequence(letter_sequence):
    for letter in letter_sequence:
        letter.execute()


#---------------------------------------------------------------------------
# Here we define the keystroke rule.

# This rule maps spoken-forms to actions.  Some of these
#  include special elements like the number with name "n"
#  or the dictation with name "text".  This rule is not
#  exported, but is referenced by other elements later on.
#  It is derived from MappingRule, so that its "value" when
#  processing a recognition will be the right side of the
#  mapping: an action.
# Note that this rule does not execute these actions, it
#  simply returns them when it's value() method is called.
#  For example "up 4" will give the value Key("up:4").
# More information about Key() actions can be found here:
#  http://dragonfly.googlecode.com/svn/trunk/dragonfly/documentation/actionkey.html
class NormalModeKeystrokeRule(MappingRule):

    exported = False

    mapping = {

        "[<n>] up": Key("k:%(n)d"),
        "[<n>] down": Key("j:%(n)d"),
        "[<n>] down": Key("j:%(n)d"),
        "[<n>] left": Key("h:%(n)d"),
        "[<n>] right": Key("l:%(n)d"),
        "[<n>] go up": Key("c-b:%(n)d"),
        "[<n>] go down": Key("c-f:%(n)d"),

	"home": Key("home"),
	"end": Key("end"),

        "lower case": Key("g,u"),
        "upper case": Key("g,U"),
        "swap case": Key("tilde"),

        "visual": Key("v"),
        "visual line": Key("s-v"),
        "visual block": Key("c-v"),

        "next": Key("n"),
        "previous": Key("N"),
        "[<n>] back": Key("b:%(n)d"),
        "[<n>] whiskey": Key("w:%(n)d"),
        "[<n>] end": Key("e:%(n)d"),

        "Center": Key("z,dot"),
        "format": Key("g,q"),

		"indent": Key("g, g, equal, G"),
		
        "next paragraph": Key("rbrace"),
        "previous paragraph": Key("lbrace"),
        "a paragraph": Key("a,p"),
        "inner paragraph": Key("i,p"),

        "[<n>] X.": Key("x:%(n)d"),
        "[<n>] backspace": Key("backspace:%(n)d"),


        "[<n>] Pete macro": Key("at,at:%(n)d"),

        "[<n>] join": Key("J:%(n)d"),

        "(delete | D.)": Key("d"),
        "[<n>] (delete | D.) (whiskey|word)": Text("%(n)ddw"),
        "(delete | D.) a (whiskey | word)": Key("d,a,w"),
        "(delete | D.) inner (whiskey | word)": Key("d,i,w"),
        "(delete | D.) a paragraph": Key("d,a,p"),
        "(delete | D.) inner paragraph": Key("d,i,p"),
        "(delete | D.) a (paren|parenthesis|raip|laip)": Key("d,a,rparen"),
        "(delete | D.) inner (paren|parenthesis|raip|laip)": Key("d,i,rparen"),
        "(delete | D.) a (bracket|rack|lack)": Key("d,a,rbracket"),
        "(delete | D.) inner (bracket|rack|lack)": Key("d,i,rbracket"),
        "(delete | D.) a (bracket|race|lace)": Key("d,a,rbrace"),
        "(delete | D.) inner (bracket|race|lace)": Key("d,i,rbrace"),

        "[<n>] (increment|increase)": Key("c-a:%(n)d"),
        "[<n>] (decrement|decrease)": Key("c-x:%(n)d"),

        "shift (delete | D.)": Key("s-d"),

        "[<n>] undo": Key("u:%(n)d"),
        "[<n>] redo": Key("c-r:%(n)d"),

	"mistake": Key("escape, u:2"),

        '[<n>] find <letter>': Text('%(n)df') + Function(executeLetter),
        '[<n>] shift find <letter>': Text('%(n)dF') + Function(executeLetter),
        'find [<n>] <letter>': Text('%(n)df') + Function(executeLetter),
        'shift find [<n>] <letter>': Text('%(n)dF') + Function(executeLetter),

	'remove <letter>': Text("df") + Function(executeLetter),

        '[<n>] again': Text('%(n)d;'),
        '[<n>] shift again': Text('%(n)d,'),

        "(yank | copy)": Key("y"),
        "(yank | copy) a paragraph": Key("y,a,p"),
        "(yank | copy) inner paragraph": Key("y,i,p"),
        "(yank | copy) a (paren|parenthesis|raip|laip)": Key("y,a,rparen"),
        "(yank | copy) inner (paren|parenthesis|raip|laip)": Key("y,i,rparen"),
        
        "copy line": Key("y,y"),

        "paste": Key("p"),
        "shift paste": Key("P"),

        "replace": Key("r"),
        "shift replace": Key("R"),

        "shift left": Key("langle,langle"),
        "shift right": Key("rangle,rangle"),

        "fuzzy find": Key("backslash,t"),


	#shortcuts
	"save": Key("colon/3, w, enter"),
	"run": Key("s-f10"),

    }
    extras   = [
        letter,
        letter_sequence,
        IntegerRef("n", 1, 100),
        Dictation("text"),
        Dictation("text2"),
    ]
    defaults = {
        "n": 1,
    }
    # Note: when processing a recognition, the *value* of
    #  this rule will be an action object from the right side
    #  of the mapping given above.  This is default behavior
    #  of the MappingRule class' value() method.  It also
    #  substitutes any "%(...)." within the action spec
    #  with the appropriate spoken values.


#---------------------------------------------------------------------------
# Here we create an element which is the sequence of keystrokes.

# First we create an element that references the keystroke rule.
#  Note: when processing a recognition, the *value* of this element
#  will be the value of the referenced rule: an action.
normal_mode_alternatives = []
normal_mode_alternatives.append(RuleRef(rule=NormalModeKeystrokeRule()))
#if FormatRule:
    #normal_mode_alternatives.append(RuleRef(rule=FormatRule()))
normal_mode_single_action = Alternative(normal_mode_alternatives)

# Second we create a repetition of keystroke elements.
#  This element will match anywhere between 1 and 16 repetitions
#  of the keystroke elements.  Note that we give this element
#  the name "sequence" so that it can be used as an extra in
#  the rule definition below.
# Note: when processing a recognition, the *value* of this element
#  will be a sequence of the contained elements: a sequence of
#  actions.
normal_mode_sequence = Repetition(normal_mode_single_action,
    min=1, max=16, name="normal_mode_sequence")


#---------------------------------------------------------------------------
# Here we define the top-level rule which the user can say.

# This is the rule that actually handles recognitions.
#  When a recognition occurs, it's _process_recognition()
#  method will be called.  It receives information about the
#  recognition in the "extras" argument: the sequence of
#  actions and the number of times to repeat them.
class NormalModeRepeatRule(CompoundRule):

    # Here we define this rule's spoken-form and special elements.
    spec     = "<normal_mode_sequence> [[[and] repeat [that]] <n> times]"
    extras   = [
            # Sequence of actions defined above.
            normal_mode_sequence,
            # Times to repeat the sequence.
            IntegerRef("n", 1, 100),
        ]
    defaults = {
            # Default repeat count.
            "n": 1,
        }

    # This method gets called when this rule is recognized.
    # Arguments:
    #  - node -- root node of the recognition parse tree.
    #  - extras -- dict of the "extras" special elements:
    #     . extras["sequence"] gives the sequence of actions.
    #     . extras["n"] gives the repeat count.
    def _process_recognition(self, node, extras):
        # A sequence of actions.
        normal_mode_sequence = extras["normal_mode_sequence"]
        # An integer repeat count.
        count = extras["n"]
        for i in range(count):
            for action in normal_mode_sequence:
                action.execute()
        release.execute()


navigation_rule = MappingRule(
    name = "navigation",
    mapping = {
        "go first line": Key("g,g"),
        "go last line": Key("G"),
        "go old": Key("c-o"),

        "cursor top": Key("s-h"),
        "cursor middle": Key("s-m"),
        "cursor (low | bottom)": Key("s-l"),

        # line navigation
        "go <line>": Key("colon/3") + Text("%(line)s\r"),

        "[<n>] next tab": Key("a-right:%(n)d"),
        "next tab": Key("a-right"),
        "previous tab": Key("a-left"),

        # searching
        "search": Key("slash"),
        "search this": Key("asterisk"),
        "back search <text>": Key("question") + Text("%(text)s\n"),

        #ide shortcuts
        "generate": Key("alt:down, insert, alt:up"),
        },
    extras = [
        Dictation("text"),
        IntegerRef("n", 1, 50),
        IntegerRef("line", 1, 10000)
        ]
)



clion_context = AppContext(executable = "clion")

# set up the grammar for vim's normal mode and start normal mode
normalModeGrammar = Grammar("clion", context=clion_context)
normalModeGrammar.add_rule(navigation_rule)
normalModeGrammar.add_rule(NormalModeRepeatRule())	
normalModeGrammar.load()

# set up the grammar for vim's insert mode
InsertModeBootstrap = Grammar("InsertMode bootstrap", context=clion_context)
InsertModeBootstrap.add_rule(InsertModeEnabler())
InsertModeBootstrap.load()
InsertModeGrammar = Grammar("InsertMode grammar", context=clion_context)
InsertModeGrammar.add_rule(InsertModeCommands())
InsertModeGrammar.add_rule(InsertModeDisabler())
#InsertModeGrammar.add_rule(FormatRule())
InsertModeGrammar.load()
InsertModeGrammar.disable()


def unload():
    global normalModeGrammar
    if normalModeGrammar: normalModeGrammar.unload()
    normalModeGrammar = None

    global InsertModeGrammar
    if InsertModeGrammar: InsertModeGrammar.unload()
    InsertModeGrammar = None


