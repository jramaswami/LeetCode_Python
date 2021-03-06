"""
LeetCode :: July 2021 Challenge :: Word Ladder II
jramaswami
"""


from string import ascii_lowercase
from collections import defaultdict
from math import inf


def neighbor_generator(word):
    """
    Generator for words that are one letter different than word.
    """
    for i, c in enumerate(word):
        for p in ascii_lowercase:
            if p == c:
                continue
            yield word[:i] + p + word[i+1:]


def build_graph(words):
    """
    Build a graph from the words where an edge exists between a word
    and any word in words that is different by a single letter.
    """
    adj = defaultdict(list)
    for wd in words:
        for wd0 in neighbor_generator(wd):
            if wd0 in words:
                adj[wd].append(wd0)
    return adj


def bfs(begin_word, end_word, adj):
    """
    Use BFS to form a new graph where there is an adjacency list for each level
    of the original graph, where a level is the distance from begin_word.
    """
    parent = []
    queue = set([begin_word])
    level = 0
    while queue:
        level_parent = defaultdict(set)
        new_queue = set()
        for wd in queue:
            if wd == end_word:
                # Stop here
                new_queue = []
                level_children = []
                break

            for wd0 in adj[wd]:
                if parent and wd0 in parent[-1][wd]:
                    continue
                level_parent[wd0].add(wd)
                new_queue.add(wd0)

        queue = new_queue
        level += 1
        parent.append(level_parent)

    # The last entry in parent was from the level after cog was found,
    # so we can get rid of it.
    parent.pop()
    return parent


class Solution():
    def findLadders(self, begin_word, end_word, word_list):
        # Build a graph from the words.
        word_list0 = set(word_list)
        word_list0.add(begin_word)
        adj = build_graph(word_list0)
        # Build a leveled graph from the words.
        level_adj = bfs(begin_word, end_word, adj)

        # Make sure there is a path between begin_word and end_word.
        if not level_adj or end_word not in level_adj[-1]:
            return []

        # Build all the possible paths from end_word to begin_word using
        # the leveled graph.
        queue = [[end_word]]
        new_queue = []
        for level in reversed(level_adj):
            for path in queue:
                child = path[-1]
                for parent in level[child]:
                    path0 = list(path)
                    path0.append(parent)
                    new_queue.append(path0)
            queue, new_queue = new_queue, []

        # Reverse all the paths.
        return [p[::-1] for p in queue]


def test_1():
    begin_word = "hit"
    end_word = "cog"
    word_list = ["hot","dot","dog","lot","log","cog"]
    expected = [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
    result = Solution().findLadders(begin_word, end_word, word_list)
    assert sorted(result) == sorted(expected)


def test_2():
    begin_word = "hit"
    end_word = "cog"
    word_list = ["hot","dot","dog","lot","log"]
    expected = []
    result = Solution().findLadders(begin_word, end_word, word_list)
    assert sorted(result) == sorted(expected)


def test_3():
    """TLE"""
    begin_word = "qa"
    end_word = "sq"
    word_list = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
    expected = [["qa","ba","be","se","sq"],["qa","ba","bi","si","sq"],["qa","ba","br","sr","sq"],["qa","ca","cm","sm","sq"],["qa","ca","co","so","sq"],["qa","la","ln","sn","sq"],["qa","la","lt","st","sq"],["qa","ma","mb","sb","sq"],["qa","pa","ph","sh","sq"],["qa","ta","tc","sc","sq"],["qa","fa","fe","se","sq"],["qa","ga","ge","se","sq"],["qa","ha","he","se","sq"],["qa","la","le","se","sq"],["qa","ma","me","se","sq"],["qa","na","ne","se","sq"],["qa","ra","re","se","sq"],["qa","ya","ye","se","sq"],["qa","ca","ci","si","sq"],["qa","ha","hi","si","sq"],["qa","la","li","si","sq"],["qa","ma","mi","si","sq"],["qa","na","ni","si","sq"],["qa","pa","pi","si","sq"],["qa","ta","ti","si","sq"],["qa","ca","cr","sr","sq"],["qa","fa","fr","sr","sq"],["qa","la","lr","sr","sq"],["qa","ma","mr","sr","sq"],["qa","fa","fm","sm","sq"],["qa","pa","pm","sm","sq"],["qa","ta","tm","sm","sq"],["qa","ga","go","so","sq"],["qa","ha","ho","so","sq"],["qa","la","lo","so","sq"],["qa","ma","mo","so","sq"],["qa","na","no","so","sq"],["qa","pa","po","so","sq"],["qa","ta","to","so","sq"],["qa","ya","yo","so","sq"],["qa","ma","mn","sn","sq"],["qa","ra","rn","sn","sq"],["qa","ma","mt","st","sq"],["qa","pa","pt","st","sq"],["qa","na","nb","sb","sq"],["qa","pa","pb","sb","sq"],["qa","ra","rb","sb","sq"],["qa","ta","tb","sb","sq"],["qa","ya","yb","sb","sq"],["qa","ra","rh","sh","sq"],["qa","ta","th","sh","sq"]]
    result = Solution().findLadders(begin_word, end_word, word_list)
    assert sorted(result) == sorted(expected)


def test_4():
    """TLE"""
    begin_word = "cet"
    end_word = "ism"
    word_list = ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"]
    expected = [["cet","get","gee","gte","ate","ats","its","ito","ibo","ibm","ism"],["cet","cat","can","ian","inn","ins","its","ito","ibo","ibm","ism"],["cet","cot","con","ion","inn","ins","its","ito","ibo","ibm","ism"]]
    result = Solution().findLadders(begin_word, end_word, word_list)
    assert sorted(result) == sorted(expected)


def test_5():
    """WA"""
    begin_word = "hot"
    end_word = "dog"
    word_list = ["hot","dog"]
    expected = []
    result = Solution().findLadders(begin_word, end_word, word_list)
    assert sorted(result) == sorted(expected)


def test_6():
    begin_word = "hit"
    end_word = "zzz"
    word_list = ["hot","dot","dog","lot","log"]
    expected = []
    result = Solution().findLadders(begin_word, end_word, word_list)
    assert sorted(result) == sorted(expected)
