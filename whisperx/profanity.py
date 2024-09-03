from profanity_check import predict, predict_prob
import string
import re


set_comp = {'gooks', 'footjob', 'dyke', 'pedophile', 'dumbasses', 'knobjokey', 'testicle', 'cuntlicker', 'mthrfucker', 'nazi', 'schizo', 'transsexual', 'niggers', 'orgasm', 'vulgar', 'fukwit', 'rumprammer', 'wazoo', 'dummy', 'tubgirl', 'gey', 'howtokill', 'lezbian', 'molest', 'stupid', 'fecker', 'whorehopper', 'shag', 'injun', 'gae', 'schlong', 'pisser', 'fuckwad', 'dlck', 'mams', 'nad', 'stripclub', 'douchey', 'jiz', 'cummer', 'phukked', 'thrust', 'cokmuncher', 'fingerfucker', 'shithead', 'fuckhead', 'slutbucket', 'orgasim', 'fingerfucking', 'fuckwit', 'penial', 'shagging', 'reefer', 'erect', 'cockmunch', 'fanyy', 'motherfucking', 'titwank', 'motherfuckka', 'sleazy', 'fuckers', 'kikes', 'hebe', 'horny', 'felch', 'foad', 'pisses', 'rectus', 'muther', 'fudgepacker', 'fuckmeat', 'scroat', 'spunk', 'viagra', 'bondage', 'pornos', 'pusse', 'dildo', 'feltcher', 'junky', 'assbanged', 'cockface', 'mutherfucker', 'japs', 'pron', 'shittings', 'skank', 'cunts', 'tush', 'bdsm', 'fistfucker', 'fart', 'sodom', 'prostitute', 'arse', 'clits', 'motherfucker', 'mothafuckers', 'yaoi', 'carpet muncher', 'pecker', 'sucked', 'fisting', 'wench', 'tittyfuck', 'gook', 'knobead', 'smegma', 'hiv', 'pedo', 'fuckyomama', 'pussi', 'xx', 'shitty', 'fuker', 'femdom', 'weenie', 'puto', 'nob', 'lezzie', 'fuckface', 'booobs', 'muffpuff', 'hore', 'wank', 'ejaculating', 'ejakulate', 'fucked', 'flogthelog', 'phuks', 'testee', 'fuckings', 'phuking', 'fucka', 'fuckingshitmotherfucker', 'penetrate', 'jizz', 'shits', 'cawk', 'goddamned', 'hooker', 'pinko', 'slutdumper', 'snatch', 'rape', 'orgasmic', 'dumbass', 'muthrfucking', 'queero', 'twunter', 'dog-fucker', 'pissflaps', 'lezzy', 'suck', 'needthedick', 'incest', 'orgasims', 'faggitt', 'pussy', 'shit', 'tittiefucker', 'nazism', 'pornography', 'pastie', 'cuntlicking', 'fanny', 'kock', 'smut', 'homo', 'masterbations', 'muthafuckaz', 'clitoris', 'shiting', 'niggaz', 'boobs', 'strip', 'knob', 'meth', 'motherfucka', 'pubic', 'turd', 'omg', 'son-of-a-bitch', 'skag', 'gays', 'shitfucker', 'menstruate', 'rectal', 'masterbate', 'vodka', 'cunt', 'doofus', 'gaylord', 'kondums', 'nobjocky', 'blowjobs', 'fucker', 'herpes', 'smutty', 'goatse', 'scum', 'cumshot', 'vag', 'assbang', 'orgasms', 'mothafuck', 'assfuck', 'doggiestyle', 'shibary', 'urine', 'fubar', 'gokkun', 'gonads', 'fucktrophy', 'wigger', 'gangbangs', 'moron', 'mofo', 'knobhead', 'cocksucked', 'ninny', 'nympho', 'beastiality', 'cocksuck', 'slave', 'reich', 'uzi', 'orally', 'assfucker', 'howtomurdep', 'cum', 'fagot', 'nipple', 'titi', 'glans', 'scantily', 'blue waffle', 'pubis', 'crap', 'racy', 'tawdry', 'teste', 'pissin', 'hoar', 'rump', 'arian', 'cunnilingus', 'areole', 'fucknut', 'kums', 'wanky', 'loins', 'whoar', 'fukking', 'gay', 'faggs', 'orgies', 'scag', 'phuq', 'fcuk', 'quicky', 'boooobs', 'pee', 'orgy', 'pigfucker', 'fukkin', 'poontang', 'asshole', 'crotch', 'fannyfucker', 'ghey', 'urinal', 'muthafecker', 'dumass', 'tampon', 'penis', 'muffdiver', 'opium', 'arrse', 'nads', 'retarded', 'masterbating', 'vagina', 'fucktoy', 'twat', 'cunilingus', 'phuck', 'fuckoff', 'titties', 'lusting', 'faggit', 'kraut', 'gonad', 'fistfuckers', 'twunt', 'oral', 'tosser', 'masterb8', 'motherfuckings', 'punky', 'raunch', 'hamflap', 'toke', 'pedophilia', 'willy', 'faig', 'douchebag', 'mtherfucker', 'spik', 'cocksucks', 'bestiality', 'fuckup', 'masturbating', 'rimjob', 'hookah', 'jerk', 'steamy', 'cock', 'sucking', 'goddamn', 'raper', 'screw', 'fux', 'knobed', 'booty call', 'virgin', 'eatadick', 'eathairpie', 'nobjokey', 'frigga', 'perversion', 'jizm', 'lezbo', 'anus', 'vomit', 'gangbang', 'slutkiss', 'godamnit', 'nigger', 'asanchez', 'cunillingus', 'stiffy', 'hotsex', 'herpy', 'fxck', 'godamn', 'mothafucked', 'lesbo', 'whorehouse', 'shemale', 'cocks', 'fellate', 'vixen', 'bitch', 'm-fucking', 'fingerfuck', 'undies', 'gangbanged', 'guido', 'ovary', 'pussies', 'pussypounder', 'fistfuck', 'mothafucking', 'fucking', 'fagots', 'homoey', 'pasty', 'phuk', 'cumming', 'doggystyle', 'weed', 'hymen', 'jackoff', 'mthrfucking', 'fucks', 'lesbos', 'polack', 'blowjob', 'numbnuts', 'cowgirl', 'bimbo', 'seaman', 'bastard', 'hooters', 'l3itch', 'penile', 'bukake', 'butthole', 'kondum', 'pillowbiter', 'pussyfart', 'womb', 'x-rated2g1c', 'wang', 'jackass', 'knobjocky', 'goldenshower', 'fook', 'fag', 'mutha', 'kooches', 'labia', 'screwed', 'titt', 'gtfo', 'pussys', 'lech', 'god', 'woody', 'ejaculated', 'floozy', 'slut', 'hussy', 'opiate', 'piss', 'dong', 'stroke', 'terd', 'shite', 'whorealicious', 'shiz', 'fucktard', 'shited', 'aryan', 'coon', 'fondle', 'hobag', 'throating', 'pollock', 'ruski', 'shota', 'felcher', 'whoring', 'sob', 'gaysex', 'heeb', 'bitchin', 'homoerotic', 'fuckhole', 'bitches', 'hoor', 'ugly', 'lmfao', 'mothafuckas', 'nappy', 'felching', 'phuked', 'dick', 'gigolo', 'hump', 'len', 'nutbutter', 'bestial', 'panty', 'penetration', 'sumofabiatch', 'testis', 'wop', 'pcp', 'hentai', 'hoer', 'dogging', 'fcuker', 'teets', 'essohbee', 'mothafuckin', 'mothafucka', 'nigga', 'foreskin', 'dickhead', 'nigg', 'kill', 'autoerotic', 'lust', 'shithole', 'motherfucked', 'fannyflaps', 'vulva', 'booooobs', 'nude', 'kooch', 'gai', 'milf', 'douche', 'honky', 'rum', 'shitter', 'testical', 'ghay', 'beastial', 'jap', 'heroin', 'masterbation', '2 girls 1 cup', 'pissed', 'titty', 'seduce', 'cipa', 'erotism', 'shibari', 'asswhole', 'xxx', 'wetback', 'damn', 'dykes', 'jism', 'cocksucker', 'whore', 'brown showers', 'cums', 'twats', 'kike', 'mutherfucking', 'fcuking', 'shitters', 'clit', 'bimbos', 'pms', 'prick', 'pot', 'shaggin', 'sluts', 'asses', 'seamen', 'fukwhit', 'moolie', 'phonesex', 'raped', 'shamedame', 'twathead', 'facial', 'whores', 'lube', 'fisty', 'lezbians', 'queaf', 'screwing', 'hoare', 'naked', 'spic', 'faggot', 'puss', 'heshe', 'teez', 'fagged', 'potty', 'punkass', 'voyeur', 'nudes', 'arsehole', 'sex', 'mafugly', 'nig', 'peyote', 'boner', 'whoreface', 'sexual', 'wedgie', 'shitted', 'niggas', 'spac', 'masturbation', 'niggle', 'menses', 'drunk', 'slope', 'pussypalace', 'extacy', 'stfu', 'enlargement', 'rectum', 'weewee', 'flange', 'sissy', 'weirdo', 'nobhead', 'niggah', 'frigg', 'gassyass', 'soused', 'fingering', 'fartknocker', 'fingerfuckers', 'paddy', 'poop', 'tittywank', 'nipples', 'ejaculate', 'muff', 'futanari', 'rtard', 'gringo', 'klan', 'bellend', 'hooter', 'jerked', 'uterus', 'sniper', 'fat', 'boob', 'ejaculates', 'sadism', 'shagger', 'fistfucked', 'shitfuck', 'shitey', 'erotic', 'herp', 'quim', 'whiz', 'phalli', 'queer', 'sausagequeen', 'cockhead', 'sleaze', 'threesome', 'cocksucking', 'hooch', 'assmunch', 'dog style', 'jackhole', 'prig', 'busty', 'panties', 'tard', 'fistfuckings', 'penisfucker', 'woose', 'inbred', 'douchebags', 'semen', 'souse', 'knobend', 'scrotum', 'fuck', 'pube', 'fuckass', 'strip club', 'handjob', 'fucknugget', 'organ', 'loin', 'ejaculatings', 'nutsack', 'fagging', 'kummer', 'pimpis', 'twatty', 'sandbar', 'prude', 'lusty', 'kinbaku', 'assfukka', 'porn', 'ganja', 'trashy', 'ejaculation', 'motherfuckers', 'murder', 'pimp', 'fingerfucked', 'fistfucks', 'fooker', 'homey', 'brown shower', 'ritard', 'booooooobs', 'pricks', 'queers', 'shitfull', 'shitface', 'kawk', 'dink', 'humping', 'ovums', 'phallic', 'sadist', 'scrote', 'lezzies', 'fingerfucks', 'fannybandit', 'fuxor', 'kkk', 'napalm', 'buceta', 'kinky', 'thug', 'whored', 'bitching', 'wtf', 'lez', 'maxi', 'poon', 'testes', 'titfuck', 'mothafucks', 'tittyfucker', 'unwed', 'fatass', 'massa', 'tramp', 'futanary', 'bukkake', 'stoned', 'hootch', 'fags', 'dildos', 'fuckwhit', 'teat', 'anal', 'whitey', 'breasts', 'kyke', 'gspot', 'deepthroat', 'ass', 'tits', 'cowgirls', 'pissing', 'cockmuncher', 'lezbos', 'pedophiliac', 'paki', 'jizzed', 'tit', 'fukker', 'junkie', 'doggin', 'ovum', 'weiner', 'masochist', 'duche', 'fellatio', 'goddam', 'dinks', 'humped', 'kunilingus', 'nooky', 'wad', 'bullshit', 'fuckpuppet', 'leper', 'shiteater', 'phukking', 'spiks', 'shitt', 'fuckbitch', 'jerkoff', 'peepee', 'lesbians', 'queef', 'scrud', 'feltch', 'fuckme', 'hemp', 'kootch', 'raping', 'revue', 'willies', 'donkeyribber', 'kinkyjesus', 'kwif', 'scrog', 'cnut', 'mothafuckings', 'kumming', 'shitting', 'hardon', 'chink', 'menstruation', 'shithouse', 'reetard', 'fisted', 'scrot', 'nimrod', 'cuming', 'ballsack', 'retard', 'pissoff', 'feck', 'wanker', 'pantie', 'rapist', 'doosh', 'spick', 'rimjaw', 'vigra', 'mothafuckaz', 'spooge', 'tinkle', 'motherfuck', 'muthafuckker', 'pawn', 'yury', 'sperm', 'fack', 'pissers', 'masturbate', 'teabagging', 'rimming', 'fuckheads', 'toots', 'porno', 'horniest', 'lmao', 'motherfucks', 'motherfuckin', 'foobar', 'erection', 'fuckin', 'faigt', 'kum', 'hardcoresex', 'negro', 'shitdick', 'snuff', 'muthafucker', 'goddammit', 'gfy', 'dopey', 'whoralicious', 'fuks', 'fistfucking', 'mothafucker', 'valium', 'fagg', 'hitler', 'freex', 'niglet', 'hell', 'playboy', 'extasy', 'fuk', 'shitings'}
def remove_compounds(segments, compound_words):
    # Convert compound words to lowercase and remove punctuation
    compound_words_cleaned = compound_words.lower().translate(str.maketrans('', '', string.punctuation))
    compound_words_set = set(compound_words_cleaned.split())
    
    # Sort compound words by length (longest first) to handle overlapping cases
    sorted_compound_words = sorted(compound_words_set, key=len, reverse=True)
    
    # Compile a regex pattern for efficient matching
    pattern = re.compile(r'\b(' + '|'.join(map(re.escape, sorted_compound_words)) + r')\b', re.IGNORECASE)
    
    def split_word(word):
        # Find all non-overlapping matches
        matches = list(pattern.finditer(word))
        if not matches:
            return [word]
        
        parts = []
        last_end = 0
        for match in matches:
            start, end = match.span()
            if start > last_end:
                parts.append(word[last_end:start])
            parts.append(match.group())
            last_end = end
        
        if last_end < len(word):
            parts.append(word[last_end:])
        
        return parts

    # Iterate over each segment and replace compounded words
    for segment in segments:
        # Convert text to lowercase and remove punctuation
        text = segment['text']
        text_no_punct = text.lower().translate(str.maketrans('', '', string.punctuation))
        
        words = text_no_punct.split()
        new_words = []
        for word in words:
            # Check if the word is in the compounded swearing set or predicted as profanity
            if word in set_comp or predict([word])[0]:
                print('profanity', word)
                # Split the word based on compound words
                split_parts = split_word(word)
                new_words.extend(split_parts)
            else:
                new_words.append(word)
        
        # Join the words back together
        text_no_punct = ' '.join(new_words)
        
        # Update the segment text with the modified version
        segment['text'] = text_no_punct
    
    return segments