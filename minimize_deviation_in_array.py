"""
LeetCode :: February 2022 Challenge :: 1675. Minimize Deviation in Array
jramaswami
"""


import collections
import heapq
import math


Item = collections.namedtuple('Item', ['curr_n', 'top_n'])

class Solution:

    def minimumDeviation(self, nums):

        def reduce(n):
            # Reduce n to the first odd number.
            while n % 2 == 0:
                n //= 2
            return n


        # TODO: You only have to keep track of the smallest top_n for
        #       a given reduction.
        active = []
        max_n = -math.inf
        min_n = math.inf
        for n in nums:
            if n % 2:
                active.append(Item(n, n * 2))
            else:
                active.append(Item(reduce(n), n))
            max_n = max(active[-1].curr_n, max_n)
            min_n = min(active[-1].curr_n, min_n)

        heapq.heapify(active)

        while active:
            print(f"{active=}")
            item = heapq.heappop(active)
            if item.curr_n != item.top_n:
                n0 = 2 * item.curr_n
                min_n0 = min_n
                if (min_n == item.curr_n):
                    min_n0 = min(active[0].curr_n if active else n0, n0)
                max_n0 = max(max_n, n0)
                if abs(max_n0 - min_n0) < abs(max_n - min_n):
                    print(f"{item=} {item.curr_n}->{n0} {min_n}->{min_n0} {max_n}->{max_n0} {max_n-min_n} {max_n0-min_n0}")
                    min_n, max_n = min_n0, max_n0
                    heapq.heappush(active, Item(n0, item.top_n))

        return max_n - min_n


def test_1():
    nums = [1,2,3,4]
    expected = 1
    assert Solution().minimumDeviation(nums) == expected


def test_2():
    nums = [4,1,5,20,3]
    expected = 3
    assert Solution().minimumDeviation(nums) == expected


# def test_3():
#     nums = [2,10,8]
#     expected = 3
#     assert Solution().minimumDeviation(nums) == expected


# def test_4():
#     "RTE"
#     nums = [3,5]
#     expected = 1
#     assert Solution().minimumDeviation(nums) == expected


# def test_4():
#     nums = [3732877, 36907992, 13018214, 91469246, 31916112, 38006032, 63860671, 55461500, 72023724, 58517881, 24455492, 52173628, 57171061, 31098316, 63519388, 85556330, 33853542, 11267319, 9928002, 42249395, 2591121, 64832274, 6350845, 31116229, 30714681, 54919686, 99321532, 37168665, 39030971, 73853982, 85704770, 25632502, 42243400, 43382466, 62953262, 53319268, 38449384, 10543558, 36346022, 84325508, 53864002, 64673782, 71285907, 32703592, 17598075, 54332905, 25525049, 97947952, 43291904, 62064683, 57156227, 70998448, 39048906, 81106967, 71133095, 18985913, 1164853, 30215088, 5911086, 86701305, 86000681, 69603229, 22636777, 45700208, 82930367, 88203007, 66969851, 49457910, 96137972, 18044212, 16308264, 71281429, 35733583, 44042049, 69212444, 27403812, 69347274, 99453917, 96921162, 20816245, 83640173, 84785924, 5977379, 29523887, 74511326, 27181536, 77520234, 92328886, 22370010, 82360525, 89060681, 24775316, 25852514, 90763247, 37315545, 74515522, 24695311, 84960663, 70893317, 30830153, 61182353, 59680515, 45392680, 2715293, 37966184, 39256648, 54896423, 84966159, 89789406, 23552188, 38366079, 45148781, 3434285, 63996344, 46459260, 51921423, 36195587, 84446545, 13936149, 32399897, 99784295, 37296320, 16315281, 30689154, 2089897, 96190823, 30134159, 80522298, 73235380, 60835155, 22335126, 68076003, 63452593, 81020746, 22798869, 54711491, 75277217, 35442048, 47549042, 56919824, 3550560, 19661939, 31996776, 82852858, 70828616, 18935628, 68743805, 97064489, 65144711, 72875739, 98300870, 31514686, 7104307, 35175153, 44640508, 72445151, 16883877, 49339800, 20299855, 53648793, 22595136, 14902307, 13101095, 81139637, 52148805, 78483867, 82609368, 572747, 80606433, 19165905, 40542876, 98683367, 72760118, 73405283, 49010129, 46173816, 71534059, 23191226, 10581399, 69644145, 31957447, 51133569, 66888599, 86498198, 61543550, 11101772, 10391957, 17895564, 40178248, 26042975, 82910342, 54192010, 79078978, 82836265, 63240963, 31047233, 57847017, 90805381, 71445211, 3038919, 32305922, 94937760, 47182765, 86812005, 81994923, 59672117, 75953302, 36974451, 95375856, 33061163, 34257379, 55221443, 50918600, 49465353, 18231779, 73272183, 19444565, 1819997, 18546786, 86785584, 29214054, 13042309, 69190767, 69554749, 38466951, 4187389, 83150765, 70126438, 17904219, 33481844, 79504764, 57228305, 53916163, 79129621, 64080729, 83118861, 57170647, 73894426, 91212320, 91114348, 48532943, 74378815, 38504106, 33472941, 69082374, 11491264, 20146542, 26759211, 76663301, 7337144, 99208623, 46659687, 82717311, 40994647, 66731541, 88929402, 37772428, 56660851, 51618965, 93499491, 38704005, 24248233, 84892202, 22499794, 69034873, 15956325, 59601813, 2526376, 21440642, 84064555, 58678850, 75532892, 73643544, 91691893, 73494278, 11472275, 58261296, 50869603, 41930636, 52998695, 97589986, 55418166, 47653860, 65426926, 4310117, 62549948, 23155272, 7439295, 74317987, 22707095, 34228577, 15984392, 32699234, 70161260, 5045553, 81725928, 52697453, 35484206, 18945252, 4180216, 23295342, 31965800, 16293691, 21854735, 9976230, 92920198, 16223913, 64032057, 91433360, 81268842, 98992968, 86563155, 5768992, 51755473, 43775562, 98837185, 99918006, 54955681, 53755333, 35210732, 94948785, 96951771, 36066641, 31706378, 26698496, 92982216, 35524848, 57452522, 15275841, 22139083, 35995769, 6371213, 90888107, 59416575, 5000714, 90430632, 30802722, 19605517, 79701421, 5216596, 32051570, 67227032, 71158937, 54096858, 33512184, 92339327, 63619041, 41479168, 10513277, 77357406, 70141432, 17200522, 67529845, 90889613, 54028145, 67775514, 9645782, 45444423, 62020830, 75490297, 74578801, 39954383, 90426880, 64347904, 41179620, 66183458, 45950419, 77738249, 54865291, 84096828, 81095368, 41146448, 4178162, 87555294, 15143589, 1173830, 20327818, 58029453, 43887478, 88693297, 26540209, 17648092, 4998007, 34692182, 54051349, 88856869, 83858982, 72087772, 75843548, 46010167, 79497799, 38104098, 62950258, 33218648, 5555675, 91180343, 1408776, 64315795, 49706905, 41214222, 51313575, 80350536, 58713567, 53446672, 1285001, 66074126, 58161148, 7404051, 54145288, 4778761, 26780379, 96419891, 81232415, 86622481, 48794851, 33155207, 9038346, 98122198, 15969446, 84475395, 87273511, 24371874, 26678430, 36832030, 60854624, 33504649, 71985477, 79030391, 94902128, 64936653, 10267354, 41681060, 12002156, 72755792, 26962341, 97153494, 99579971, 75123215, 25274126, 42720133, 11083717, 49579653, 66322639, 37749182, 52713642, 84775835, 83301790, 92309936, 88452211, 68022985, 10320751, 72411593, 28309806, 9951683, 39927930, 64126906, 12287535, 14995265, 43440970, 32582486, 45633688, 64340566, 13915913, 52113073, 93065732, 46911388, 44002894, 58660634, 67888492, 40440581, 43573132, 6673989, 20457012, 43643016, 55566367, 95836367, 73519389, 34663946, 60292607, 97775481, 68960486, 92852901, 17936301, 78440633, 63998864, 28698946, 82378568, 31010611, 20371474, 49640885, 30091079, 97495705, 97533835, 98950656, 76926882, 99446431, 12751017, 1656939, 46970234, 23427526, 78401945, 72604095, 95238322, 66692335, 86426416, 56896141, 85104325, 48592983, 42666067, 92570272, 52730476, 67744676, 97563557, 13025288, 23516906, 69993450, 95109721, 77688844, 17058738, 29219053, 77936207, 65352884, 99869799, 4768383, 73133617, 30074179, 12035755, 94670873, 70681775, 15461362, 32222597, 99707835, 74637596, 46252577, 53202829, 38390284, 88637258, 52767434, 86946176, 68317921, 35022164, 70080505, 42887247, 96544284, 57918532, 79352088, 95799964, 83182505, 15249283, 34538571, 40754528, 91674230, 63495730, 90074756, 81940479, 51121396, 3794924, 3246092, 3465563, 48428977, 9791416, 29825175, 20075253, 85177976, 59168773, 28324469, 11373546, 14909524, 68865685, 4258068, 61338566, 24215204, 20946120, 52641159, 4861795, 64234725, 33495883, 34659888, 25652108, 89270952, 85830272, 84378626, 56190402, 87738219, 52418790, 21434194, 56675853, 11569316, 99498300, 22082066, 18939692, 41261706, 98119432, 83008806, 29002059, 16024081, 81678402, 96725924, 84722686, 52120165, 15278042, 22618969, 52887403, 59009219, 21759692, 22338043, 38863220, 81933224, 2876886, 42032137, 95096266, 93773418, 73466166, 7279938, 67902202, 7308482, 21005770, 99879126, 91758490, 8146540, 21178296, 31645415, 51702477, 94548066, 76811464, 69154831, 41794843, 67398864, 65918701, 35639773, 25371357, 31286002, 81182425, 65452562, 5246033, 60389676, 93589180, 44801072, 54075980, 12375300, 48312660, 1825696, 17708857, 42554443, 52637129, 14306022, 35756572, 90228727, 71106840, 71650438, 31499299, 32892464, 83433254, 20444981, 16180839, 74746075, 58500234, 53666057, 68717011, 10280816, 39244351, 96473067, 44945131, 87891375, 16653684, 53879230, 22176872, 243536, 34794716, 2904771, 20910102, 36303090, 9104149, 92678129, 29533095, 9059772, 94293443, 17960546, 65450125, 52270625, 9429124, 17934417, 11664088, 55459082, 8925538, 69366505, 55385446, 32333978, 35956642, 5861868, 65695043, 98370543, 90275373, 7336362, 8454545, 93077355, 27438501, 23588661, 86689661, 81905102, 76654699, 24013986, 66631855, 70073054, 60972799, 11079127, 3239338, 7777171, 87219800, 71004768, 55125734, 37496262, 58536094, 85521365, 61565989, 75265972, 45875849, 86376702, 70918736, 79670987, 46011639, 16211229, 64971283, 37739702, 77171627, 46336305, 60267494, 53628155, 41479295, 60047081, 74270015, 41064355, 72874034, 60115347, 6986129, 96189123, 56086214, 83930337, 75603993, 79496330, 23770042, 9726069, 47364857, 49151781, 71735992, 63994232, 5331418, 73250807, 38339249, 55602864, 68307559, 92290940, 68083751, 3999974, 26680133, 51626682, 9917045, 42344668, 21539811, 10207717, 42182853, 99827002, 57350521, 39019874, 30929571, 43344175, 15385842, 58105480, 22191801, 10213194, 99490542, 85622299, 98936616, 93836039, 75441214, 33672750, 49776761, 82833625, 79024010, 14372940, 13696446, 59936573, 4882232, 86607077, 96264601, 83099674, 55625401, 49951934, 99836315, 85763476, 8226886, 57345842, 57099738, 97555575, 78321765, 6128011, 14158219, 60501928, 19452816, 24294928, 8565070, 49726291, 75798930, 49612763, 9892411, 67822265, 84130884, 4125909, 30908484, 31818057, 74413470, 83578695, 48230510, 1807196, 25797575, 90245345, 76326538, 42739232, 35041287, 55033869, 48804637, 58546116, 86007747, 38192385, 79484937, 17571902, 96454184, 39514457, 198935, 25579834, 31871505, 99055275, 92665415, 71510544, 44634241, 16167992, 91562382, 99186718, 57915035, 79445113, 82060786, 38433607, 27118147, 99431604, 43476467, 10810886, 33809972, 36927756, 87718727, 72600412, 35277736, 44572927, 77687272, 69168610, 4896163, 84316822, 54089804, 30143595, 54107428, 41686025, 42328048, 43650195, 96582383, 81016300, 91640679, 67548592, 83364567, 53601315, 35342529, 9771937, 23307693, 85196692, 19706990, 7568742, 2094484, 19472959, 72923122, 48153056, 73860052, 5924403, 9545035, 89485274, 88732124, 66236588, 69620222, 21249975, 37436113, 4516615, 41911955, 79682511, 14420998, 68085073, 92466529, 14776162, 27392183, 14272798, 91180999, 90475160, 31971816, 84469595, 82684309, 77538197, 27153209, 42623984, 29989761, 3302923, 78930099, 62270917, 12530908, 19896819, 67390559, 60512640, 70262280, 24125699, 48019768, 95234823, 51434310, 13214522, 46305892, 10611500, 24835744, 52513301, 53489510, 99640315, 71718134, 47010848, 61652335, 89897732, 47913476, 17057600, 46180908, 1469984, 40744554, 37365354, 52159089, 47967194, 81870324, 61346219, 19692698, 5728608, 80374518, 79973155, 7120991, 70923914, 15017734, 525163, 34004711, 72169092, 97366968, 75678784, 9931970, 53841224, 277750, 3970377, 85688935, 63953779, 43673447, 23682056, 99963426, 57762635, 87787640, 74197733, 68274620, 4474841, 88058174, 83539140, 39682137, 29952489, 75865102, 45514653, 64567054, 42632431, 58395475, 95438302, 11154997, 91487222, 93306407, 89552967, 79824100, 91496726, 21376443, 37318123, 60686652, 11735643, 42816, 6437229, 39780081, 11887202, 60458520, 66622014, 30698464, 64672230, 45890878, 78711173, 15284423, 90294638, 61963962, 32680859, 85616179, 6557274]
#     expected = 99826983
#     assert Solution().minimumDeviation(nums) == expected

