"""
LeetCode :: October 2021 Challenge :: 1044. Longest Duplicate Substring
jramaswami
"""


import collections


class Solution:
    def longestDupSubstring(self, S):

        def lds(i, j):
            result = 0
            while i < len(S) and j < len(S):
                if S[i] != S[j]:
                    return result
                result += 1
                i += 1
                j += 1
            return result

        # Optimize so that when you start looking for repeated substrings,
        # you only start on matching letters.
        locations = collections.defaultdict(list)
        for i, c in enumerate(S):
            locations[c].append(i)

        soln_length = 0
        soln = ""
        for c in locations:
            for p, i in enumerate(locations[c]):
                for _, j in enumerate(locations[c][p+1:], start=p+1):
                    # If we reach a point where the right substring is not
                    # large enough to beat our current winner, then stop.
                    if len(S) - j < soln_length:
                        break
                    k = lds(i, j)
                    if k > soln_length:
                        soln_length = k
                        soln = S[i:i+k]
        return soln


def test_1():
    S = "banana"
    expected = "ana"
    assert Solution().longestDupSubstring(S) == expected


def test_2():
    S = "abcd"
    expected = ""
    assert Solution().longestDupSubstring(S) == expected


def test_3():
    S = "a" * pow(10, 4) * 3
    expected = "a" * ((pow(10, 4) * 3) - 1)
    result = Solution().longestDupSubstring(S)
    assert result == expected


def test_4():
    """TLE"""
    S = "dcecccaedebdcedcbaaddbbdbccbcbdcecbddaaedecbeccdeabdceebcaaeccbbcdcdaceceeacedadcdddbbbaedeaebbbecbeebdcdebadabaecacdeeeabeaaaeacbdacedabbadcbeddebbbcebedeecdbebbdbcebacebdaaceabdbdcaebddeaeccaccbcebdacddbdddbadecbadaacaadcdececadeebbacedebeddcaacedacbcaadecdeecddbdbbbcccedeaaeecededdaccddbdccdcdddddcdacceabbcebdebddbcbbaaababceebdaaeababeacaeddccecadebeceeddaddbdbdebcbceceeacedcaedcebeeeadbbecdecaeabaeedbdddaececeebcaddbcaaeebcbeccbedcdeccebeebdbaceddebddabebbabbcedbbedacecbaebaaedbeaeaebbaaeeeebbbbeecdecdcedbcdbbbdcaecdbbcadbeebaebcaebccadecdccabbddbddeaeeaecccbeacdcbeadadadacbceaaeceebcdcddceeebebedececacadbedeeebdecadbebebebecaeeecbdceecdcacadceadcceaebcbaceeceeaaedecaddbaacacdbedebeeccadbccdeccdcadcdaadbabddbbdaacbaaaceeecaadcabadbeecadeebbdcebabedcddbebdcbaccdaabebcbacbedadeacbbcacadbdabbaccadadddeabdcbbdeacdbeededdecebceacabdceaeaaeaacbbbacabccedddeceadceedacccedaaceadeabccbdaeadcabbccadaecddebbadeecadccbacebdaabbeacdccaedeeeaaadaaaddebeadcbbdcebeeaebecdbacccbaeadcbacabbbeedeaaccaebddaaceadebeedebabdbbecebeabddeeecaeedddabacbbdbddebbadadcbeacecdaabcaeddceebceebaecccadeecbbdbeaeedcdeaabadcdeaebaaaadbdadeeaadadcabeceadbbdedadaaaecdacdbcedbeabcbeaeacaecebdeaedacbcbeaebcabdaabaddecadbeaecdcbebbbccbbddbccdebaaeecccddaaeccedebabacdeecbbbbccdedcbcebeceedcaacbeaacabdbbeeebdcddbceebdaddacadadceaaeecabaecadcdabbccaabcdbeededadcbecbebcdceabccecbebbbccbcddccebdeacbebabeecbebacceecbdddeeeeabeaabcdbecbbdacdccadbeeaccecdbcddcdacbaddcacdacdbebeaabdadeaadcacedcccdcdbddaaebacecbdccdbaabdecadddedcbbaaacdeaddcdcebcaeccbcbcdaaeceabaedeeeadebcaadbbedbccbaabdbdccbabceabeeccbbadbaecedddccedaeaabcbaaeabcdbdbdaabcedbbbdbeabaedcbdabeeabbadecadeadabcbdaebdbcbecccaaeadcaaebcccdacabdbecebbedaaeebcadbeeeebebccdaceedecdedceaceaeabccbebaccebdceabbdadcdccbeeebbbbaedebecbbbeabebdabdcdcbcbedaedcbcaebbccdbacdccbbcbadcbbaccbebaaabaaaedccdceecababeacddacceeabeaabaaeccceccecddeecdadedeaadabaccabbadaaecbebccbabaadcbecebedbaececeabdebcadaddcaebeeabbebedeadcdccbadabcecbacecbdbccebcbbaadceadbacadeeebcddcdddccaeaababdcddeebaaddcbcaaddceedacdaaeaadcedeeaeaddebdabaddddbadccbdbebcecdccebeebdcccbeedbcceebbadcdebaeedbecccdbaedcdbcbbaaaaabbbdaddabdbbeebdeabedededbdbcecedadbaebddcabbbabecacdedccbeaacaeaccadcbeebaadceddbdacbbadccacbadcdddabcccaababebdceeddcaebbaebeeedabdbcacabdcbaceabcccdcacacbbaeeaaddedaabccaabbeaccaceecbaacbeebcbeaecdbcaeaaaedcdbebcaaaaacaabbbbccbceebbbaaaceccabdeceeeddbabadddeeaaebbabbeaadaacacdebbaadbaeebbdebbabbbbbeadbebadacdcdbaccaebaadccbabcadccbeaacadeabcadebbcadabaaaaeccaddbbebcdabdededddeadcbceacebaeeddeaebedbebaeabebcadcdbccdbdbdeccaebddeaabccdaecebdededddcbbcacdcbaedcebdedaaceebccbcdababaeaacabcddaadacaadbadcdbbedaebddebedceddddceadeaebbebbaabdeabdcdabccdcedaddeaeddecdecbeebeedaadbcbbebcbeecedaabcacaabdbaecaeebeaedadbabecbaabbebadaccadeebeeebbecdcaecaeacadeabbadceaeccbcdbebaaabebaacdebbcaaeadccbebcebebebbedddacbbccbedbecbeaebecedacdcdbbebdaedeabcabaaaeebbdbbaddadcebbacecbaacddecbddeecbbedecedbbaebddeeacbcdedbdaddbbaecdccaedcebeeebaacaaabcbddccacbccbacdbebaeadbeaacacbceddbaeabaaaadaabbcddaabcabeeccabcebacdacbadbdebddaddeaabeebbbbbbacbdddecbaddcdeaaaeecbbcedcbecddbebeccaacaedabdacabdaabdbadccddedecdebadcdcadbedeecbdddaacdbdcadddacaedceacaecaebcecedeaeadbabccdbdeacebaccaabccccdcecaecadeaddeaeddabcbadedceebdaacdadebbeebdeedcecebdeecaaeccbcdddddadbbbcbaabccabebabdcdcaacadaaeebbbedbdecabcceeccabadbbaddcdbeaaeeadaddeebaecaedecccaadbdeddbbbeeceeaaccaedadddbaecacccadaeecdecabccabbebcacedbeadccddeaadacdcbeedeaeabcbccbbdcdaeedbcabaaccaccbdaacebacaecdacbebddbbbdddebacadaaadbdcbcaccdddeedbecbcdcbaeaacbabbeaeebbadadaebbccaebebdeeceecbabdebcebeaadebdbbddcaeddbcadeadaabdccdecdcaccaecccdeaaacdbdccadacbdbaaccdbddbecaacbcbbdbedecedecbaacadccaedbacabddaeccdecaaeeecadddeaaadcdaedeadedbeeccccabeadaebcaaecacebdcdaaadedccacdceaeededcaaedceccedccebdacbececeeaebaecbdeecdbaeeeeeadececcdcabbddadecdddabdeeedccabbaebddedecccacdbdcbbcddcaecbdaddcadacbbccceccecacddcbaedcbbeecedbeecdeaaeeeecdcabcebecbcebbceabaddeacaedaabadebcecdadbebcbbeeaceaacbdcaabacadaebebcdceeeacaacaddeaadabaceeecbccbecbdabebebccdadeedaadaecceacaabeacdaebeecbdcbbdeddbeebdadbabbeaddbcdccdbcebddaebeddcaecdededebebdaabdddaecedddabbeeebadbbbdebeeecbbebaebdeebceaeaedbecbbcadadbeacceeecbabaeadbdedccbbbbaabeabbbdadceedaaddcbbceadbbaebebebbdeadcaabdeebaaebbeecaddecccbddcdebadcebbaacddbbeecadbcaebdebaaeeaadbaeeeedbcabebceccebabbeebcddebcdbdabcbcbbcadecbdacedadacdbbebeebaddecbccaeaeccedbcddededdecbcecdeaabeceeadbcbeaaccaeccceadecaaacbaaccaccbeeeceddadaabdeeaedbcceabeabbbcaeededdcdcbdbbedecbbdbeeeccadcadedeacbbcdbebcbeaedbcbdbdabbdcacacadeedbebddeddccaeebceddeeebdbbabcaebdbdbedeeadbabaadddcaabbbbcabeeddbbadabacceabcbceddeceadcdbaeadaedebecdecbdbabdcacddbccbaedcceabbecabdacbdcbaeaeccceecabbaeaecdeadabaeeedeeadeebbacdaceadedecedebbbcbaccaacebbebadaeaecbeebadaaceaabebdbddeecedcbcbcdbcdaccacbbbdaddacbcaaaebdcadbcaeeaacacebeebaeeecbdeedddcebcbeaabdedbaddabcadbbaeadccdbcebddadebaaabcaeadcedaadcaeedcbbcdbcdbcdcbdcebaaadededdccebebbedcadeadeeadeebbdceebdddacebdedbbcdabbcdacbbdcccacdbacbbaeeeacbedceaedebbacdbeebaebbaeacaccaecdeacbbaacaceebedaacdcebaaacadcdeceaeeadcadceaeeabeecaabbabbebdecdcadadebabddbabebdbadeabcdadbbcaadcdbdbabddebcbcbeddabbcabaebcbccddbbbbebdbdabcdcddbdbceecadbadadbdcbadedecdcbaebcaaddbeebceaceeaacceabcacaccddcebcabbebddecddbedbddaeadebbcdccddeebebbaceaaeeebcdceeebdccbaababcdcbdcebbbbcaeccecaadcaeabababbcdaeaecdcbaddbacbaeecdcdecccabcddbbbcdcadadabcbcedaadaacceaededbaecaeadabdcd"
    expected = "dccdbcebdda"
    assert Solution().longestDupSubstring(S) == expected
