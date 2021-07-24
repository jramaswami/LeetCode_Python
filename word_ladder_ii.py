"""
LeetCode :: July 2021 Challenge :: Word Ladder II
jramaswami
"""


from collections import defaultdict, deque
from math import inf


def adjacent(wd1, wd2):
    """
    Return True if wd1 and wd2 differ by only a single letter.
    """
    delta = 0
    for a, b in zip(wd1, wd2):
        if a != b:
            delta += 1
    return delta == 1


def build_graph(word_list):
    """
    Build a graph of words that differ by 1 letter.
    """
    adj = defaultdict(list)
    for i, wd1 in enumerate(word_list):
        for wd2 in word_list[i+1:]:
            if adjacent(wd1, wd2):
                adj[wd1].append(wd2)
                adj[wd2].append(wd1)
    return adj


def bfs(begin_word, end_word, adj):
    """
    BFS to determine the shortest path length from begin_word to end_word.
    """
    distance = defaultdict(lambda: inf)
    queue = deque()
    distance[begin_word] = 0
    visited = set()
    queue.append(begin_word)
    visited.add(begin_word)
    while queue:
        wd = queue.popleft()
        for wd0 in adj[wd]:
            if wd0 not in visited:
                visited.add(wd0)
                distance[wd0] = 1 + distance[wd]
                queue.append(wd0)
    return distance[end_word]



def dfs(begin_word, end_word, path_limit, adj):

    soln = []
    visited = defaultdict(int)

    def dfs_visit(u, path, path_limit):
        if len(path) > path_limit:
            return

        if u == end_word:
            path.append(u)
            soln.append(list(path))
            path.pop()
            return


        visited[u] = 1
        path.append(u)

        for v in adj[u]:
            if not visited[v]:
                dfs_visit(v, path, path_limit)

        path.pop()
        visited[u] = 0

    dfs_visit(begin_word, [], path_limit)
    return soln


class Solution():
    def findLadders(self, begin_word, end_word, word_list):
        # Make sure begin_word gets into the graph.
        if begin_word not in word_list:
            word_list.append(begin_word)
        # Build the graph.
        adj = build_graph(word_list)
        # Use a BFS to find the shortest length path between begin_word
        # and end_word.  It will be used to limit the DFS done later.
        path_length = bfs(begin_word, end_word, adj)
        # Use a DFS to find all the paths.
        return dfs(begin_word, end_word, path_length, adj)


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
    expected = []
    result = Solution().findLadders(begin_word, end_word, word_list)
    assert sorted(result) == sorted(expected)
