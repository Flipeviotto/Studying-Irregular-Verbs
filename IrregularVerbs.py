from random import choice
from random import randint

vida = 3
p = 0

words = ['abide', 'alight', 'arise', 'awake', 'backbite', 'backslide', 'be', 'bear', 'beat', 'become', 'befall',
         'beget', 'begin', 'behold', 'bend', 'bereave', 'beseech', 'beset', 'bestrew', 'bet', 'betake', 'bethink',
         'bid (farewell)', 'bid (offer amount)', 'bind', 'bite', 'bleed', 'blow', 'break', 'breed', 'bring',
         'broadcast', 'browbeat', 'build', 'burn', 'burst', 'bust', 'buy', 'cast', 'catch', 'chide', 'choose', 'clap',
         'cling', 'clothe', 'colorbreed', 'come', 'cost', 'creep', 'crossbreed', 'cut', 'dare', 'daydream', 'deal',
         'dig', 'dight', 'disprove', 'dive (jump head-first)', 'dive (scuba diving)', 'do', 'draw', 'dream', 'drink',
         'drive', 'dwell', 'eat', 'enwind', 'fall', 'feed', 'feel', 'fight', 'find', 'fit (tailor, chege size)',
         'fit (be right size)', 'flee', 'fling', 'fly', 'forbear', 'forbid', 'fordo', 'forecast',
         'forego (also forgo in British English)', 'foreknow', 'forerun', 'foresee', 'foreshow', 'forespeak',
         'foretell', 'forget', 'forgive', 'forsake', 'forswear', 'fraught', 'freeze', 'frostbite', 'gainsay', 'get',
         'gild', 'give', 'go', 'grind', 'grow', 'hagride', 'halterbreak', 'hamstring', 'hand-feed', 'handwrite', 'hang',
         'hang (kill by hanging)', 'have', 'hear', 'heave', 'hew', 'hide', 'hit', 'hold', 'hurt', 'inbreed', 'inlay',
         'input', 'inset', 'interbreed', 'intercut', 'interlay', 'interset', 'interweave', 'interwind', 'inweave',
         'jerry-build', 'keep', 'kneel', 'knit', 'know', 'lade', 'landslide', 'lay', 'lead', 'lean', 'leap', 'learn',
         'leave', 'lend', 'let', 'lie (deitar)', 'lie (not tell truth)', 'light', 'lip-read', 'lose', 'make', 'mean',
         'meet', 'misbecome', 'miscast', 'miscut', 'misdeal', 'misdo', 'mishear', 'mishit', 'mislay', 'mislead',
         'mislearn', 'misread', 'missay', 'missend', 'misset', 'misspeak', 'misspell', 'misspend', 'misswear',
         'mistake', 'misteach', 'mistell', 'misthink', 'misunderstand', 'miswear', 'miswed', 'miswrite', 'mow',
         'offset', 'outbid', 'outbreed', 'outdo', 'outdraw', 'outdrink', 'outdrive', 'outfight', 'outfly', 'outgrow',
         'outlay', 'outleap', 'output', 'outride', 'outrun', 'outsee', 'outsell', 'outshine', 'outshoot', 'outsing',
         'outsit', 'outsleep', 'outsmell', 'outspeak', 'outspeed', 'outspend', 'outspin', 'outspring', 'outstand',
         'outswear', 'outswim', 'outtell', 'outthink', 'outthrow', 'outtwear', 'outwind', 'outwrite', 'overbear',
         'overbid', 'overbreed', 'overbuild', 'overbuy', 'overcast', 'overcome', 'overcut', 'overdo', 'overdraw',
         'overdrink', 'overeat', 'overfeed', 'overhang', 'overhear', 'overlay', 'overleap', 'overlie', 'overpay',
         'override', 'overrun', 'oversee', 'oversell', 'overset', 'oversew', 'overshoot', 'oversleep', 'oversow',
         'overspeak', 'overspend', 'overspill', 'overspin', 'overspread', 'overspring', 'overstand', 'overstrew',
         'overtride', 'overstrike', 'overtake', 'overthink', 'overthrow', 'overwear', 'overwind', 'overwrite',
         'partake', 'pay', 'plead', 'prebuild', 'predo', 'premake', 'prepay', 'presell', 'preset', 'preshrink',
         'presplit', 'proofread', 'prove', 'put', 'quick-freeze', 'quit', 'read', 'reawake', 'rebid', 'rebind',
         'rebroadcast', 'rebuild', 'recast', 'recut', 'redeal', 'redo', 'redraw', 'reeve', 'refit (replace parts)',
         'refit (reailor)', 'regrind', 'regrow', 'rehang', 'rehear', 'reknit', 'relay (for example tiles)',
         'replay (pass along message)', 'relearn', 'relight', 'remake', 'rend', 'repay', 'reread', 'rerun', 'resell',
         'resend', 'reset', 'resew', 'retake', 'reteach', 'retear', 'retell', 'rethink', 'retread', 'retrofit',
         'rewake', 'rewear', 'reweave', 'rewed', 'rewet', 'rewin', 'rewind', 'rewrite', 'rid', 'ride', 'ring', 'rise',
         'rive', 'roughcast', 'run', 'sand-cast', 'saw', 'say', 'see', 'seek', 'self-feed', 'self-sow', 'sell', 'send',
         'set', 'sew', 'shake', 'shave', 'shear', 'shed', 'shine', 'shit', 'shoe', 'shoot', 'show', 'shrink', 'shrive',
         'shut', 'sight-read', 'sing', 'sink', 'sit', 'skywrite', 'slay (kill)', 'slay (amuse)', 'sleep', 'slide',
         'sling', 'slink', 'slit', 'smell', 'smite', 'sneak', 'sow', 'speak', 'speed', 'spell', 'spend', 'spill',
         'spin', 'spit', 'split', 'spoil', 'spoon-feed', 'spread', 'spring', 'stall-feed', 'stand', 'stave', 'steal',
         'stick', 'sting', 'stink', 'strew', 'stride', 'strike', 'string', 'strip', 'strive', 'sublet', 'sunburn',
         'swear', 'sweat', 'sweep', 'swell', 'swim', 'swing', 'take', 'trach', 'tear', 'telecast', 'tell', 'test-drive',
         'test-fly', 'think', 'thrive', 'throw', 'thrust', 'tread', 'troubleshoot', 'typecast', 'typeset', 'typewrite',
         'unbear', 'unbend', 'unbind', 'unbuild', 'unclothe', 'underbid', 'underbuy', 'undercut', 'underfeed',
         'undergo', 'underlay', 'underlet', 'underlie', 'underrun', 'undersell', 'undershoot', 'underspend',
         'understand', 'understake', 'underthrust', 'underwrite', 'undo', 'undraw', 'unfreeze', 'unhang', 'unhide',
         'unhold', 'unknit', 'unlade', 'unlay', 'unlearn', 'unmake', 'unreeve', 'unsay', 'unsew', 'unsling', 'unspin',
         'unstick', 'unstring', 'unswear', 'unteach', 'unthink', 'unweave', 'unwind', 'unwrite', 'uphold', 'upset',
         'vex', 'wake', 'waylay', 'wear', 'weave', 'wed', 'weep', 'wet', 'whet', 'win', 'wind', 'withdraw', 'withhold',
         'withstand', 'wring', 'write']
answer = {'abide': ['abided', 'abode'], 'alight': ["alighted", "alit"], 'arise': ["arose"],
          'awake': ['awakened', 'awoke'], 'backbite': ['backbit'], 'backslide': ['backslid'], 'be': ['was', 'were'],
          'bear': ['bore'], 'beat': ['beat'], 'become': ['became'], 'befall': ['befell'], 'beget': ['begat', 'begot'],
          'begin': ['began'], 'behold': ['beheld'], 'bend': ['bent'], 'bereave': ['bereaved', 'bereft'],
          'beseech': ['besought', 'beseeche'], 'beset': ['beset'], 'bestrew': ["bestrewed"], 'bet': ['bet', 'betted'],
          'betake': ['betook'], 'bethink': ['bethought'], 'bid (farewell)': ['bid', 'bade'],
          'bid (offer amount)': ['bid'], 'bind': ['bound'], 'bite': ['bit'], 'bleed': ['bled'], 'blow': ['blew'],
          'break': ['broke'], 'breed': ['bred'], 'bring': ['brought'], 'broadcast': ['broadcast', 'broadcasted'],
          'browbeat': ['browbeat'], 'build': ['built'], 'burn': ['burned', 'burnt'], 'burst': ['burst'],
          'bust': ['busted', 'bust'], 'buy': ['bought'], 'cast': ['cast'], 'catch': ['caught'],
          'chide': ['chided', 'chid'], 'choose': ['chose'], 'clap': ['clapped', 'clapt'], 'cling': ['clung'],
          'clothe': ['clothed', 'clad'], 'colorbreed': ['colorbred'], 'come': ['came'], 'cost': ['cost'],
          'creep': ['crept'], 'crossbreed': ['crossbred'], 'cut': ['cut'], 'dare': ['dared', 'durst'],
          'daydream': ['daydreamed', 'daydreamt'], 'deal': ['dealt'], 'dig': ['dug'], 'dight': ['dighted', 'dight'],
          'disprove': ['disproved'], 'dive (jump head-first)': ['dove', 'dived'],
          'dive (scuba diving)': ['dived', 'dove'], 'do': ['did'], 'draw': ['drew'], 'dream': ['dreamed', 'dreamt'],
          'drink': ['drank'], 'drive': ['drove'], 'dwell': ['dwelt', 'dwelled'], 'eat': ['ate'], 'enwind': ['enwound'],
          'fall': ['fell'], 'feed': ['fed'], 'feel': ['felt'], 'fight': ['fought'], 'find': ['found'],
          'fit (tailor, chege size)': ['fitted', 'fit'], 'fit (be right size)': ['fit', 'fitted'], 'flee': ['fled'],
          'fling': ['flung'], 'fly': ['flew'], 'forbear': ['forbore'], 'forbid': ['forbade'], 'fordo': ['fordid'],
          'forecast': ['forecast'], 'forego (also forgo in British English)': ['forewent'], 'foreknow': ['foreknew'],
          'forerun': ['foreran'], 'foresee': ['foresaw'], 'foreshow': ['foreshowed'], 'forespeak': ['forespoke'],
          'foretell': ["foretold"], 'forget': ['forgot'], 'forgive': {'forgave'}, 'forsake': ['forsook'],
          'forswear': ['forswore'], 'fraught': ['fraught'], 'freeze': ['froze'], 'frostbite': ['frostbit'],
          'gainsay': ['gainsaid'], 'get': ['got'], 'gild': ['gilded', 'gilt'], 'give': ['gave'], 'go': ['went'],
          'grind': ['ground'], 'grow': ['grew'], 'hagride': ['hagrode'], 'halterbreak': ['halterbroke'],
          'hamstring': ['hamstrung'], 'hand-feed': ['hand-fed'], 'handwrite': ['handwrote'], 'hang': ['hung'],
          'hang (kill by hanging)': ['hanged', 'hung'], 'have': ['had'], 'hear': ['heard'], 'heave': ['heaved', 'hove'],
          'hew': ['hewed'], 'hide': ['hid'], 'hit': ['hit'], 'hold': ['held'], 'hurt': ['hurt'], 'inbreed': ['inbred'],
          'inlay': ['inlaid'], 'input': ['input', 'inputted'], 'inset': ['inset'], 'interbreed': ['interbred'],
          'intercut': ['intercut'], 'interlay': ['interlaid'], 'interset': ['interset'],
          'interweave': ['interwove', 'interweaved'], 'interwind': ['interwound'], 'inweave': ['inwove', 'inweaved'],
          'jerry-build': ['jerry-built'], 'keep': ['kept'], 'kneel': ['knelt', 'kneeled'], 'knit': ['knitted', 'knit'],
          'know': ['knew'], 'lade': ['laded'], 'landslide': ['landslid'], 'lay': ['laid'], 'lead': ['led'],
          'lean': ['leaned', 'leant'], 'leap': ['leaped', 'leapt'], 'learn': ['learned', 'learnt'], 'leave': ['left'],
          'lend': ['lent'], 'let': ['let'], 'lie (deitar)': ['lay'], 'lie (not tell truth)': ['lied'],
          'light': ['lit', 'lighted'], 'lip-read': ['lip-read'], 'lose': ['lost'], 'make': ['made'], 'mean': ['meant'],
          'meet': ['met'], 'misbecome': ['misbecame'], 'miscast': ['miscast'], 'miscut': ['miscut'],
          'misdeal': ['misdealt'], 'misdo': ['misdid'], 'mishear': ['misheard', 'houvir mal'], 'mishit': ['mishit'],
          'mislay': ['mislaid'], 'mislead': ['misled'], 'mislearn': ['mislearned', 'mislearnt'], 'misread': ['misread'],
          'missay': ['missaid'], 'missend': ['missent'], 'misset': ['misset'], 'misspeak': ['misspoke'],
          'misspell': ['misspelled', 'misspelt'], 'misspend': ['misspent'], 'misswear': ['misswore'],
          'mistake': ['mistook'], 'misteach': ['mistaught'], 'mistell': ['mistold'], 'misthink': ['misthought'],
          'misunderstand': ['misunderstood'], 'miswear': ['miswore'], 'miswed': ['miswed', 'miswedded'],
          'miswrite': ['miswrote'], 'mow': ['mowed'], 'offset': ['offset'], 'outbid': ['outbid'],
          'outbreed': ['outbred'], 'outdo': ['outdid'], 'outdraw': ['outdrew'], 'outdrink': ['outdrank'],
          'outdrive': ['outdrove'], 'outfight': ['outfought'], 'outfly': ['outflew'], 'outgrow': ['outgrew'],
          'outlay': ['outlaid'], 'outleap': ['outleaped', 'outleapt'], 'output': ['output', 'outputted'],
          'outride': ['outrode'], 'outrun': ['outran'], 'outsee': ['outsaw'], 'outsell': ['outsold'],
          'outshine': ['outshined', 'outshone'], 'outshoot': ['outshot'], 'outsing': ['outsang'], 'outsit': ['outsat'],
          'outsleep': ['outslept'], 'outsmell': ['outsmelled', 'outsmelt'], 'outspeak': ['outspoke'],
          'outspeed': ['outsped'], 'outspend': ['outspun'], 'outspin': ['outspun'],
          'outspring': ['outsprang', 'outsprung'], 'outstand': ['outstood'], 'outswear': ['outwore'],
          'outswim': ['outswam'], 'outtell': ['outtold'], 'outthink': ['outthought'], 'outthrow': ['outthrew'],
          'outwear': ['outwore'], 'outwind': ['outwound'], 'outwrite': ['outwrote'], 'overbear': ['overbore'],
          'overbid': ['overbid'], 'overbreed': ['overbred'], 'overbuild': ['overbuilt'], 'overbuy': ['overbought'],
          'overcast': ['overcast'], 'overcome': ['overcame'], 'overcut': ['overcut'], 'overdo': ['overdid'],
          'overdraw': ['overdrew'], 'overdrink': ['overdrank'], 'overeat': ['overate'], 'overfeed': ['overfed'],
          'overhang': ['overhung'], 'overhear': ['overheard'], 'overlay': ['overlaid'],
          'overleap': ['overleaped', 'overleapt'], 'overlie': ['overlay'], 'overpay': ['overpaid'],
          'override': ['overrode'], 'overrun': ['overran'], 'oversee': ['oversaw'], 'oversell': ['oversold'],
          'overset': ['overset'], 'oversew': ['oversewed'], 'overshoot': ['overshot'], 'oversleep': ['overslept'],
          'oversow': ['oversowed'], 'overspeak': ['overspoke'], 'overspend': ['overspent'],
          'overspill': ['overspilled', 'overspilt'], 'overspin': ['overspun'], 'overspread': ['overspread'],
          'overspring': ['oversprang', 'oversprung'], 'overstand': ['overstood'], 'overstrew': ['overstrewed'],
          'overtride': ['ovestrode'], 'overstrike': ['overstruck'], 'overtake': ['overstook'],
          'overthink': ['overthought'], 'overthrow': ['overthrew'], 'overwear': ['overwore'], 'overwind': ['overwound'],
          'overwrite': ['overwrote'], 'partake': ['partook', 'estar envolvido com alguma coisa; comer/beber de algo'],
          'pay': ['paid'], 'plead': ['pleaded', 'pled'], 'prebuild': ['prebuilt'], 'predo': ['predid'],
          'premake': ['premade'], 'prepay': ['prepaid'], 'presell': ['presold'], 'preset': ['preset'],
          'preshrink': ['preshrank'], 'presplit': ['presplit'], 'proofread': ['proofread'], 'prove': ['proved'],
          'put': ['put'], 'quick-freeze': ['quick-froze'], 'quit': ['quit', 'quitted'], 'read': ['read'],
          'reawake': ['reawoke'], 'rebid': ['rebid'], 'rebind': ['rebound'],
          'rebroadcast': ['rebroadcast', 'rebroadcasted'], 'rebuild': ['rebuilt'], 'recast': ['recast'],
          'recut': ['recut'], 'redeal': ['redealt'], 'redo': ['redid'], 'redraw': ['redrew'],
          'reeve': ['reeved', 'rove'], 'refit (replace parts)': ['refit', 'refitted'],
          'refit (reailor)': ['refitted', 'refit'], 'regrind': ['reground'], 'regrow': ['regrew'], 'rehang': ['rehung'],
          'rehear': ['reheard'], 'reknit': ['reknitted', 'reknit'], 'relay (for example tiles)': ['relaid'],
          'replay (pass along message)': ['relayed'], 'relearn': ['relearned', 'relearnt'],
          'relight': ['relit', 'relighted'], 'remake': ['remade'], 'rend': ['rent', 'rended'], 'repay': ['repaid'],
          'reread': ['reread'], 'rerun': ['reran'], 'resell': ['resold'], 'resend': ['resent'], 'reset': ['reset'],
          'resew': ['resewed'], 'retake': ['retook'], 'reteach': ['retaught'], 'retear': ['retore'],
          'retell': ['retold'], 'rethink': ['rethought'], 'retread': ['retread'],
          'retrofit': ['retrofitted', 'retrofit'], 'rewake': ['rewoke', 'rewaked'], 'rewear': ['rewore'],
          'reweave': ['rewove', 'reweaved'], 'rewed': ['rewed', 'rewedded'], 'rewet': ['rewet', 'rewetted'],
          'rewin': ['rewon'], 'rewind': ['rewound'], 'rewrite': ['rewrote'], 'rid': ['rid'], 'ride': ['rode'],
          'ring': ['rang'], 'rise': ['rose'], 'rive': ['rived'], 'roughcast': ['roughcast'], 'run': ['ran'],
          'sand-cast': ['sand-cast'], 'saw': ['sawed'], 'say': ['said'], 'see': ['saw'], 'seek': ['sought'],
          'self-feed': ['self-fed'], 'self-sow': ['self-sowed'], 'sell': ['sold'], 'send': ['sent'], 'set': ['set'],
          'sew': ['sewed'], 'shake': ['shook'], 'shave': ['shaved'], 'shear': ['sheared'], 'shed': 
          ['shed'],
          'shine': ['shined', 'shone'], 'shit': ['shit', 'shat', 'shitted'], 'shoe': ['shoed', 'shod'],
          'shoot': ['shot'], 'show': ['showed'], 'shrink': ['shrank', 'shrunk'], 'shrive': ['shrived', 'shrove'],
          'shut': ['shut'], 'sight-read': ['sight-read'], 'sing': ['sang'], 'sink': ['sank', 'sunk'], 'sit': ['sat'],
          'skywrite': ['skywrote'], 'slay (kill)': ['slew', 'slayed'], 'slay (amuse)': ['slayed'], 'sleep': ['slept'],
          'slide': ['slid'], 'sling': ['slung'], 'slink': ['slinked', 'slunk'], 'slit': ['slit'],
          'smell': ['smelled', 'smelt'], 'smite': ['smote'], 'sneak': ['sneaked', 'snuck'], 'sow': ['sowed'],
          'speak': ['spoke'], 'speed': ['sped', 'speeded'], 'spell': ['spelled', 'spelt'], 'spend': ['spent'],
          'spill': ['spilled', 'spilt'], 'spin': ['spun'], 'spit': ['spit', 'spat'], 'split': ['split'],
          'spoil': ['spoiled', 'spoilt'], 'spoon-feed': ['spoon-fed'], 'spread': ['spread'],
          'spring': ['sprang', 'sprung'], 'stall-feed': ['stall-fed'], 'stand': ['stood'], 'stave': ['staved', 'stove'],
          'steal': ['stole'], 'stick': ['stuck'], 'sting': ['stung'], 'stink': ['stunk', 'stank'], 'strew': ['strewed'],
          'stride': ['strode'], 'strike': ['struck'], 'string': ['strung'], 'strip': ['stripped', 'stript'],
          'strive': ['strove', 'strived'], 'sublet': ['sublet'], 'sunburn': ['sunburned', 'sunburnt'],
          'swear': ['swore'], 'sweat': ['sweat','sweated'], 'sweep': ['swept'], 'swell': ['swelled'], 'swim': ['swam'],
          'swing': ['swung'], 'take': ['took'], 'trach': ['taught'], 'tear': ['tore'], 'telecast': ['telecast'],
          'tell': ['told'], 'test-drive': ['test-drove'], 'test-fly': ['test-flew'], 'think': ['thought'],
          'thrive': ['thrived', 'throve'], 'throw': ['threw'], 'thrust': ['thrust'], 'tread': ['trod'],
          'troubleshoot': ['troubleshot'], 'typecast': ['typecast'], 'typeset': ['typeset'], 'typewrite': ['typewrote'],
          'unbear': ['unbore'], 'unbend': ['unbent'], 'unbind': ['unbound'], 'unbuild': ['unbuilt'],
          'unclothe': ['unclothed', 'unclad'], 'underbid': ['underbid'], 'underbuy': ['underbought'],
          'undercut': ['undercut'], 'underfeed': ['underfed'], 'undergo': ['underwent'], 'underlay': ['underlaid'],
          'underlet': ['underlet'], 'underlie': ['underlay'], 'underrun': ['underran'], 'undersell': ['undersold'],
          'undershoot': ['undershot'], 'underspend': ['underspent'], 'understand': ['understood'],
          'understake': ['understook'], 'underthrust': ['understhrust'], 'underwrite': ['underwrote'],
          'undo': ['undid'], 'undraw': ['undraw'], 'unfreeze': ['unfroze'], 'unhang': ['unhung'], 'unhide': ['unhid'],
          'unhold': ['unheld'], 'unknit': ['unknitted', 'unknit'], 'unlade': ['unladed'], 'unlay': ['unlaid'],
          'unlearn': ['unlearned', 'unlearnt'], 'unmake': ['unmade'], 'unreeve': ['unreeved', 'unrove'],
          'unsay': ['unsaid'], 'unsew': ['unsewed'], 'unsling': ['unslung'], 'unspin': ['unspun'],
          'unstick': ['unstuck'], 'unstring': ['unstrung'], 'unswear': ['unswore'], 'unteach': ['untaught'],
          'unthink': ['unthought'], 'unweave': ['unwove', 'unweaved'], 'unwind': ['unwound'], 'unwrite': ['unwrote'],
          'uphold': ['upheld'], 'upset': ['upset'], 'vex': ['vexed', 'vext'], 'wake': ['woke', 'waked'],
          'waylay': ['waylaid'], 'wear': ['wore'], 'weave': ['wove', 'weaved'], 'wed': ['wed', 'wedded'],
          'weep': ['wept'], 'wet': ['wet', 'wetted'], 'whet': ['whetted'], 'win': ['won'], 'wind': ['wound'],
          'withdraw': ['withdrew'], 'withhold': ['withheld'], 'withstand': ['withstood'], 'wring': ['wrung'],
          'write': ['wrote']}
answer2 = {'abide': ['abided'], 'alight': ["alighted", "alit"], 'arise': ["arisen"], 'awake': ['awakened', 'awoken'],
           'backbite': ['backbitten'], 'backslide': ['backslidden', 'backslid'], 'be': ['been'],
           'bear': ['born', 'borne'], 'beat': ['beat', 'beaten'], 'become': ['become'], 'befall': ['befellen'],
           'beget': ['begotten'], 'begin': ['begun'], 'behold': ['beheld'], 'bend': ['bent'],
           'bereave': ['bereaved', 'bereft'], 'beseech': ['besought', 'beseeche'], 'beset': ['beset'],
           'bestrew': ["bestrewed", 'bestrewn'], 'bet': ['bet', 'betted'], 'betake': ['betaken'],
           'bethink': ['bethought'], 'bid (farewell)': ['bidden'], 'bid (offer amount)': ['bid'], 'bind': ['bound'],
           'bite': ['bitten'], 'bleed': ['bled'], 'blow': ['blown'], 'break': ['broken'], 'breed': ['bred'],
           'bring': ['brought'], 'broadcast': ['broadcast', 'broadcasted'], 'browbeat': ['browbeat', 'browbeaten'],
           'build': ['built'], 'burn': ['burned', 'burnt'], 'burst': ['burst'], 'bust': ['busted', 'bust'],
           'buy': ['bought'], 'cast': ['cast'], 'catch': ['caught'], 'chide': ['chided', 'chidden'],
           'choose': ['chosen'], 'clap': ['clapped', 'clapt'], 'cling': ['clung'], 'clothe': ['clothed', 'clad'],
           'colorbreed': ['colorbred'], 'come': ['come'], 'cost': ['cost'], 'creep': ['crept'],
           'crossbreed': ['crossbred'], 'cut': ['cut'], 'dare': ['dared', 'durst'],
           'daydream': ['daydreamed', 'daydreamt'], 'deal': ['dealt'], 'dig': ['dug'], 'dight': ['dighted', 'dight'],
           'disprove': ['disproved', 'disproven'], 'dive (jump head-first)': ['dived'],
           'dive (scuba diving)': ['dived'], 'do': ['done'], 'draw': ['drawn'], 'dream': ['dreamed', 'dreamt'],
           'drink': ['drunk'], 'drive': ['driven'], 'dwell': ['dwelt', 'dwelled'], 'eat': ['eaten'],
           'enwind': ['enwound'], 'fall': ['fallen'], 'feed': ['fed'], 'feel': ['felt'], 'fight': ['fought'],
           'find': ['found'], 'fit (tailor, chege size)': ['fitted', 'fit'], 'fit (be right size)': ['fit', 'fitted'],
           'flee': ['fled'], 'fling': ['flung'], 'fly': ['flown'], 'forbear': ['forborne'], 'forbid': ['forbidden'],
           'fordo': ['fordone'], 'forecast': ['forecast'], 'forego (also forgo in British English)': ['foregone'],
           'foreknow': ['foreknown'], 'forerun': ['forerun'], 'foresee': ['foreseen'],
           'foreshow': ['foreshowed', 'foreshown'], 'forespeak': ['forespoken'], 'foretell': ["foretold"],
           'forget': ['forgot', 'forgotten'], 'forgive': {'forgiven'}, 'forsake': ['forsaken'],
           'forswear': ['forswore'], 'fraught': ['fraught'], 'freeze': ['frozen'], 'frostbite': ['frostbitten'],
           'gainsay': ['gainsaid'], 'get': ['got', 'gotten'], 'gild': ['gilded', 'gilt'], 'give': ['gaven'],
           'go': ['gone'], 'grind': ['ground'], 'grow': ['grown'], 'hagride': ['hagridden'],
           'halterbreak': ['halterbroken'], 'hamstring': ['hamstrung'], 'hand-feed': ['hand-fed'],
           'handwrite': ['handwritten'], 'hang': ['hung'], 'hang (kill by hanging)': ['hanged', 'hung'],
           'have': ['had'], 'hear': ['heard'], 'heave': ['heaved', 'hove'], 'hew': ['hewed', 'hewn'],
           'hide': ['hidden'], 'hit': ['hit'], 'hold': ['held'], 'hurt': ['hurt'], 'inbreed': ['inbred'],
           'inlay': ['inlaid'], 'input': ['input', 'inputted'], 'inset': ['inset'], 'interbreed': ['interbred'],
           'intercut': ['intercut'], 'interlay': ['interlaid'], 'interset': ['interset'],
           'interweave': ['interwoven', 'interweaved'], 'interwind': ['interwound'], 'inweave': ['inwoven', 'inweaved'],
           'jerry-build': ['jerry-built'], 'keep': ['kept'], 'kneel': ['knelt', 'kneeled'], 'knit': ['knitted', 'knit'],
           'know': ['known'], 'lade': ['laded', 'laden'], 'landslide': ['landslid'], 'lay': ['laid'], 'lead': ['led'],
           'lean': ['leaned', 'leant'], 'leap': ['leaped', 'leapt'], 'learn': ['learned', 'learnt'], 'leave': ['left'],
           'lend': ['lent'], 'let': ['let'], 'lie (deitar)': ['lain'], 'lie (not tell truth)': ['lied'],
           'light': ['lit', 'lighted'], 'lip-read': ['lip-read'], 'lose': ['lost'], 'make': ['made'], 'mean': ['meant'],
           'meet': ['met'], 'misbecome': ['misbecome'], 'miscast': ['miscast'], 'miscut': ['miscut'],
           'misdeal': ['misdealt'], 'misdo': ['misdone'], 'mishear': ['misheard'], 'mishit': ['mishit'],
           'mislay': ['mislaid'], 'mislead': ['misled'], 'mislearn': ['mislearned', 'mislearnt'],
           'misread': ['misread'], 'missay': ['missaid'], 'missend': ['missent'], 'misset': ['misset'],
           'misspeak': ['misspoken'], 'misspell': ['misspelled', 'misspelt'], 'misspend': ['misspent'],
           'misswear': ['missworn'], 'mistake': ['mistaken'], 'misteach': ['mistaught'], 'mistell': ['mistold'],
           'misthink': ['misthought'], 'misunderstand': ['misunderstood'], 'miswear': ['misworn'],
           'miswed': ['miswed', 'miswedded'], 'miswrite': ['miswritten'], 'mow': ['mowed', 'mown'],
           'offset': ['offset'], 'outbid': ['outbid'], 'outbreed': ['outbred'], 'outdo': ['outdone'],
           'outdraw': ['outdrawn'], 'outdrink': ['outdrunk'], 'outdrive': ['outdriven'], 'outfight': ['outfought'],
           'outfly': ['outflown'], 'outgrow': ['outgrown'], 'outlay': ['outlaid'], 'outleap': ['outleaped', 'outleapt'],
           'output': ['output', 'outputted'], 'outride': ['outridden'], 'outrun': ['outrun'], 'outsee': ['outseen'],
           'outsell': ['outsold'], 'outshine': ['outshined', 'outshone'], 'outshoot': ['outshot'],
           'outsing': ['outsung'], 'outsit': ['outsat'], 'outsleep': ['outslept'],
           'outsmell': ['outsmelled', 'outsmelt'], 'outspeak': ['outspoke'], 'outspeed': ['outsped'],
           'outspend': ['outspun'], 'outspin': ['outspun'], 'outspring': ['outsprung'], 'outstand': ['outstood'],
           'outswear': ['outsworn'], 'outswim': ['outswum'], 'outtell': ['outtold'], 'outthink': ['outthought'],
           'outthrow': ['outthrown'], 'outwear': ['outworn'], 'outwind': ['outwound'], 'outwrite': ['outwritten'],
           'overbear': ['overborn', 'overborne'], 'overbid': ['overbid'], 'overbreed': ['overbred'],
           'overbuild': ['overbuilt'], 'overbuy': ['overboght'], 'overcast': ['overcast'], 'overcome': ['overcome'],
           'overcut': ['overcut'], 'overdo': ['overdone'], 'overdraw': ['overdrawn'], 'overdrink': ['overdrunk'],
           'overeat': ['overeaten'], 'overfeed': ['overfed'], 'overhang': ['overhung'], 'overhear': ['overheard'],
           'overlay': ['overlain'], 'overleap': ['overleaped', 'overleapt'], 'overlie': ['overlain'],
           'overpay': ['overpaid'], 'override': ['overridden'], 'overrun': ['overrun'], 'oversee': ['overseen'],
           'oversell': ['oversold'], 'overset': ['overset'], 'oversew': ['oversewed', 'oversewn'],
           'overshoot': ['overshot'], 'oversleep': ['overslept'], 'oversow': ['oversowed', 'oversown'],
           'overspeak': ['overspoken'], 'overspend': ['overspent'], 'overspill': ['overspilled', 'overspilt'],
           'overspin': ['overspun'], 'overspread': ['overspread'], 'overspring': ['oversprung'],
           'overstand': ['overstood'], 'overstrew': ['overstrewed', 'overstrewn'], 'overtride': ['overstridden'],
           'overstrike': ['overstruck'], 'overtake': ['overtaken'], 'overthink': ['overthought'],
           'overthrow': ['overthrew'], 'overwear': ['overworn'], 'overwind': ['overwound'],
           'overwrite': ['overwritten'],
           'partake': ['partaken', 'estar envolvido com alguma coisa; comer/beber de algo'], 'pay': ['paid'],
           'plead': ['pleaded', 'pled'], 'prebuild': ['prebuilt'], 'predo': ['predone'], 'premake': ['premade'],
           'prepay': ['prepaid'], 'presell': ['presold'], 'preset': ['preset'], 'preshrink': ['preshrunk'],
           'presplit': ['presplit'], 'proofread': ['proofread'], 'prove': ['proved', 'proven'], 'put': ['put'],
           'quick-freeze': ['quick-froze'], 'quit': ['quit', 'quitted'], 'read': ['read'],
           'reawake': ['reawoke', 'reawaken'], 'rebid': ['rebid'], 'rebind': ['rebound'],
           'rebroadcast': ['rebroadcast', 'rebroadcasted'], 'rebuild': ['rebuilt'], 'recast': ['recast'],
           'recut': ['recut'], 'redeal': ['redealt'], 'redo': ['redone'], 'redraw': ['redrawn'],
           'reeve': ['reeved', 'rove'], 'refit (replace parts)': ['refit', 'refitted'],
           'refit (reailor)': ['refitted', 'refit'], 'regrind': ['reground'], 'regrow': ['regrown'],
           'rehang': ['rehung'], 'rehear': ['reheard'], 'reknit': ['reknitted', 'reknit'],
           'relay (for example tiles)': ['relaid'], 'replay (pass along message)': ['relayed'],
           'relearn': ['relearned', 'relearnt'], 'relight': ['relit', 'relighted'], 'remake': ['remade'],
           'rend': ['rent', 'rended'], 'repay': ['repaid'], 'reread': ['reread'], 'rerun': ['rerun'],
           'resell': ['resold'], 'resend': ['resent'], 'reset': ['reset'], 'resew': ['resewed', 'resewn'],
           'retake': ['retaken'], 'reteach': ['retaught'], 'retear': ['retorn'], 'retell': ['retold'],
           'rethink': ['rethought'], 'retread': ['retread'], 'retrofit': ['retrofitted', 'retrofit'],
           'rewake': ['rewaken', 'rewaked'], 'rewear': ['reworn'], 'reweave': ['rewoven', 'reweaved'],
           'rewed': ['rewed', 'rewedded'], 'rewet': ['rewet', 'rewetted'], 'rewin': ['rewon'], 'rewind': ['rewound'],
           'rewrite': ['rewritten'], 'rid': ['rid'], 'ride': ['ridden'], 'ring': ['rung'], 'rise': ['risen'],
           'rive': ['rived', 'riven'], 'roughcast': ['roughcast'], 'run': ['run'], 'sand-cast': ['sand-cast'],
           'saw': ['sawed', 'sawn'], 'say': ['said'], 'see': ['sawn'], 'seek': ['sought'], 'self-feed': ['self-fed'],
           'self-sow': ['self-sowed', 'self-sown'], 'sell': ['sold'], 'send': ['sent'], 'set': ['set'],
           'sew': ['sewed', 'sewn'], 'shake': ['shaken'], 'shave': ['shaved', 'shaven'], 'shear': ['sheared', 'shorn'],
           'shed': ['shed'], 'shine': ['shined', 'shone'], 'shit': ['shit', 'shat', 'shitted'],
           'shoe': ['shoed', 'shod'], 'shoot': ['shot'], 'show': ['showed', 'shown'], 'shrink': ['shrunk'],
           'shrive': ['shriven'], 'shut': ['shut'], 'sight-read': ['sight-read'], 'sing': ['sung'], 'sink': ['sunk'],
           'sit': ['sat'], 'skywrite': ['skywritten'], 'slay (kill)': ['slain', 'slayed'], 'slay (amuse)': ['slayed'],
           'sleep': ['slept'], 'slide': ['slid'], 'sling': ['slung'], 'slink': ['slinked', 'slunk'], 'slit': ['slit'],
           'smell': ['smelled', 'smelt'], 'smite': ['smote', 'mitten'], 'sneak': ['sneaked', 'snuck'],
           'sow': ['sowed', 'sown'], 'speak': ['spoken'], 'speed': ['sped', 'speeded'], 'spell': ['spelled', 'spelt'],
           'spend': ['spent'], 'spill': ['spilled', 'spilt'], 'spin': ['spun'], 'spit': ['spit', 'spat'],
           'split': ['split'], 'spoil': ['spoiled', 'spoilt'], 'spoon-feed': ['spoon-fed'], 'spread': ['spread'],
           'spring': ['sprung'], 'stall-feed': ['stall-fed'], 'stand': ['stood'], 'stave': ['staved', 'stove'],
           'steal': ['stolen'], 'stick': ['stuck'], 'sting': ['stung'], 'stink': ['stunk'],
           'strew': ['strewed', 'strewn'], 'stride': ['stridden'], 'strike': ['struck', 'stricken'],
           'string': ['strung'], 'strip': ['stripped', 'stript'], 'strive': ['striven', 'strived'],
           'sublet': ['sublet'], 'sunburn': ['sunburned', 'sunburnt'], 'swear': ['sworn'], 'sweat': ['sweat', 'sweated'],
           'sweep': ['swept'], 'swell': ['swelled', 'swollen'], 'swim': ['swum'], 'swing': ['swung'], 'take': ['taken'],
           'trach': ['taught'], 'tear': ['torn'], 'telecast': ['telecast'], 'tell': ['told'],
           'test-drive': ['test-driven'], 'test-fly': ['test-flown'], 'think': ['thought'],
           'thrive': ['thrived', 'thriven'], 'throw': ['thrown'], 'thrust': ['thrust'], 'tread': ['trod', 'trodden'],
           'troubleshoot': ['troubleshot'], 'typecast': ['typecast'], 'typeset': ['typeset'],
           'typewrite': ['typewritten'], 'unbear': ['unborn', 'unborne'], 'unbend': ['unbent'], 'unbind': ['unbound'],
           'unbuild': ['unbuilt'], 'unclothe': ['unclothed', 'unclad'], 'underbid': ['underbid'],
           'underbuy': ['underbought'], 'undercut': ['undercut'], 'underfeed': ['underfed'], 'undergo': ['undergone'],
           'underlay': ['underlaid'], 'underlet': ['underlet'], 'underlie': ['underlain'], 'underrun': ['underrun'],
           'undersell': ['undersold'], 'undershoot': ['undershot'], 'underspend': ['underspent'],
           'understand': ['understood'], 'understake': ['undertaken'], 'underthrust': ['understhrust'],
           'underwrite': ['underwritten'], 'undo': ['undone'], 'undraw': ['undrawn'], 'unfreeze': ['unfrozen'],
           'unhang': ['unhung'], 'unhide': ['unhidden'], 'unhold': ['unheld'],
           'unknit': ['unknitted', 'unknit'], 'unlade': ['unladed', 'unladen'], 'unlay': ['unlaid'],
           'unlearn': ['unlearned', 'unlearnt'], 'unmake': ['unmade'], 'unreeve': ['unreeved', 'unrove'],
           'unsay': ['unsaid'], 'unsew': ['unsewed', 'unsewn'], 'unsling': ['unslung'], 'unspin': ['unspun'],
           'unstick': ['unstuck'], 'unstring': ['unstrung'], 'unswear': ['unsworn'], 'unteach': ['untaught'],
           'unthink': ['unthought'], 'unweave': ['unwove', 'unweaved'], 'unwind': ['unwound'], 'unwrite': ['unwritten'],
           'uphold': ['upheld'], 'upset': ['upset'], 'vex': ['vexed', 'vext'], 'wake': ['woken', 'waked'],
           'waylay': ['waylaid'], 'wear': ['worn'], 'weave': ['woven', 'weaved'], 'wed': ['wed', 'wedded'],
           'weep': ['wept'], 'wet': ['wet', 'wetted'], 'whet': ['whetted'], 'win': ['won'], 'wind': ['wound'],
           'withdraw': ['withdrawn'], 'withhold': ['withheld'], 'withstand': ['withstood'], 'wring': ['wrung'],
           'write': ['written']}

while True:
    game = int(input('''1 - simple past\n2 - past participle\n3 - toggle\noption: '''))
    if game == 1:
        while True:
            word = choice(words)
            while True:
                print('')
                print(f'''The word is   \033[0;31m {word} \033[m''')
                r = str(input('The simple past is:  ')).strip().lower()
                print('')
                print('----------------------------')
                print('')
                if r in answer[word]:
                    p += 1
                    words.remove(word)
                    break
                elif r == 'help':
                    print(f'{answer[word]}')
                    p -= 1
                else:
                    vida -= 1
                    print(f'Wrong!   \033[0;33mlife = {vida}\033[m')
                    print('')
                if vida == 0:
                    print(f'The answer was {answer[word]}')
                    print('GAME OVER!')
                    print(f'Punctuation: {p}')
                    exit()
                elif words == 0:
                    print('CONGRATULATIONS, You won the game!')
    elif game == 2:
        while True:
            word = choice(words)
            while True:
                print('')
                print(f'''The word is   \033[0;31m {word} \033[m''')
                r = str(input('The past participle is:  ')).strip().lower()
                print('')
                print('----------------------------')
                print('')
                if r in answer2[word]:
                    p += 1
                    words.remove(word)
                    break
                elif r == 'help':
                    print(f'{answer2[word]}')
                    p -= 1
                else:
                    vida -= 1
                    print(f'Wrong!   \033[0;33mlife = {vida}\033[m')
                    print('')
                if vida == 0:
                    print(f'The answer was {answer2[word]}')
                    print('GAME OVER!')
                    print(f'Punctuation: {p}')
                    exit()
                elif words == 0:
                    print('CONGRATULATIONS, You won the game!')
    elif game == 3:
        while True:
            tp = randint(1, 2)
            word = choice(words)
            while True:
                if tp == 1:
                    print(f'''acertos {vida-3} erros {p}''')
                    print('')
                    print(f'''\33[0;33mSimple past\033[m\nThe word is \033[0;31m{word}\033[m''')
                    r = str(input('Your answer: ').strip().lower())
                    print('')
                    if r in answer[word]:
                        print('certo')
                        vida += 1
                        break
                    elif r == 'help':
                        print(f'{answer[word]}')
                        print('')
                    else:
                        p += 1
                        print('Wrong')
                elif tp == 2:
                    print(f'''acertos {vida - 3} erros {p}''')
                    print('')
                    print(f'''\33[0;33mPast participle\033[m\nThe word is \033[0;31m{word}\033[m''')
                    r = str(input('Your answer: ').strip().lower())
                    print('')
                    if r in answer2[word]:
                        print('')
                        print('certo')
                        vida += 1
                        break
                    elif r == 'help':
                        print(f'{answer2[word]}')
                        print('')
                    else:
                        p += 1
                        print('Wrong')
    else:
        print(f'{game} não é um valor válido. Write again.')
