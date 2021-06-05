"""
LeetCode :: June 2021 Challenge :: Maximum Performance of a Team
jramaswami
"""


from typing import *
from collections import defaultdict
import heapq


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        edict = defaultdict(list)
        for e, s in zip(efficiency, speed):
            edict[e].append(s)

        team = []
        sum_speed = 0
        soln = 0
        for e in sorted(edict.keys(), reverse=True):
            for s in edict[e]:
                heapq.heappush(team, s)
                sum_speed += s
            while len(team) > k:
                removed = heapq.heappop(team)
                sum_speed -= removed
            soln = max(soln, sum_speed * e)
        
        return soln % (pow(10, 9) + 7)



def test_1():
    n = 6
    speed = [2,10,3,1,5,8]
    efficiency = [5,4,3,9,7,2]
    k = 2
    assert Solution().maxPerformance(n, speed, efficiency, k) == 60


def test_2():
    n = 6
    speed = [2,10,3,1,5,8]
    efficiency = [5,4,3,9,7,2]
    k = 3
    assert Solution().maxPerformance(n, speed, efficiency, k) == 68


def test_3():
    n = 6
    speed = [2,10,3,1,5,8]
    efficiency = [5,4,3,9,7,2]
    k = 4
    assert Solution().maxPerformance(n, speed, efficiency, k) == 72


def test_4():
    """RTE"""
    n = 5
    speed = [10,10,7,9,8]
    efficiency = [9,8,3,6,9]
    k = 1
    assert Solution().maxPerformance(n, speed, efficiency, k) == 90


def test_5():
    """WA"""
    n = 378
    speed = [48842,98221,44112,59789,63403,18966,19433,22555,48204,77278,54122,67344,96931,90613,56821,63675,93778,52679,55722,8447,27020,30046,3426,33191,62887,52315,94832,393,56058,6668,28611,55297,6165,13523,72462,55002,97141,34778,36537,62877,6249,88711,11429,16226,58628,89386,65269,15225,62809,19548,80431,26372,68255,54606,70349,64550,71408,99571,44183,13482,99324,86152,92904,7398,81980,39304,29958,35988,92572,53955,17066,25600,73512,78446,69833,66764,54238,36673,91151,35004,28102,48194,61676,44355,79395,96890,90987,70093,7624,42731,90454,84550,41336,64715,43260,16768,91534,29495,83266,92134,73804,89754,29655,26137,74394,40353,42945,2629,80659,11085,29428,89220,44706,78793,67952,3032,43233,18277,32876,89287,5377,10142,95018,39320,32631,69420,47417,10266,52341,94379,90611,12303,43100,1044,42183,46185,94918,79451,53106,88999,81349,69172,73983,70224,39466,82934,71975,7070,66654,22957,28184,35979,2620,70626,69488,62028,52860,13600,48953,85777,47598,72809,66501,76130,81140,58391,17330,9745,18603,28347,43971,38319,20396,57635,15449,19025,38705,90041,79127,70423,84271,49743,13258,3981,78455,55349,48516,53233,60554,13001,4904,92293,78,14566,18295,66595,72225,74479,46717,91420,81500,13834,46887,15258,92282,55365,45385,86188,7297,57000,49323,38527,57806,31203,79908,18924,44761,14877,22571,84246,63890,99284,15923,2840,27423,82786,52068,29859,32553,43130,32136,60465,61757,64570,86925,25398,57751,71045,74899,34926,19646,49299,14284,85512,23982,49417,65804,20384,68761,33370,60874,83074,96479,70482,51222,71320,55440,86805,44889,31346,70302,21096,49242,2828,28425,30889,67589,24936,66065,80199,70354,32495,60942,74320,6337,11756,12399,62774,67958,1595,40896,36448,54469,77984,73619,41723,83428,65745,72591,91604,91560,26309,36495,19856,74302,22959,81533,95819,44056,33878,33067,50367,74118,1766,17074,29612,9236,70459,26007,56259,31435,18245,60360,93262,10823,10113,87464,3967,50152,89446,77465,16932,70583,9722,50027,37444,86739,52059,98181,29505,92974,45577,70172,11611,39183,92456,2871,81537,13506,48842,33410,7635,41367,17350,13539,57055,76874,97606,66092,52013,92781,50309,67823,93881,33372,477,15846,73756,86908,71434,30235,4943,21991,87897,65912,53798,86722,52239,64747,87725,24465,2081,98801,64023,51635,70604,31914,10108]
    efficiency = [85340554,64615150,52138061,15637635,47579750,55726454,2437874,34927889,17061584,38539937,34617517,38557657,56472622,36732050,45084193,28919126,65951443,96124045,12264446,17377187,20079421,98001151,13859996,20899422,13281162,87195934,25157099,11967124,82126748,73765523,71737521,46533628,87454907,98585727,91142944,90146822,15924482,91879339,24030573,94511177,28752098,86472701,52306941,89751613,39493269,68158232,52758668,81350878,14204219,51856957,94272953,22430927,34575768,99747536,38734238,85048717,28806472,83692369,65226377,1149160,97882637,46557257,35907764,72549511,59089521,13523596,68184457,36284107,33064450,19909434,34402173,54722966,84560664,7842329,81736015,19978947,36260559,64444234,41043386,65944722,66942187,80397320,32435395,23643634,24320745,77919701,60547448,20056095,67638547,70931586,18128433,28612643,83556934,64479131,15892331,18806198,34422747,11815021,72319939,6715049,23096679,15587710,75599525,67513770,88570890,56675389,568633,40977289,29563666,99730571,37604126,83973651,36114537,96471047,50905636,16328441,46576671,15220369,19230588,77042078,46573777,12323886,13852572,42549703,36149885,6679549,4183564,18660933,49936672,85681662,32488878,91220299,36726426,69154076,15060854,86059463,16898002,36383718,12223613,77395850,97358092,63832019,56199793,52851012,29446367,40623874,17867592,80542907,14746298,32290302,58332672,73277085,33609748,36364197,35130804,16921265,95143294,99980902,9271061,73041146,73115472,97061302,91884013,4082053,41356235,91591832,20907469,77750089,90814192,64970975,49001704,21443671,51235544,54444089,80665562,36206014,89507025,85747958,1098547,1301694,17794236,75418789,61676913,57975871,91167299,37052520,54818669,81306298,7150355,63184857,86715795,93598706,5645945,78838329,71194985,47820220,36360027,87894136,63607653,32906622,32186972,75478220,21294878,5446358,42103908,97613499,34022961,83989889,82805943,55691672,48149835,45799918,93850445,85219015,69658436,7520384,90333263,68859521,72884779,84007513,45766176,95351861,78219542,64458866,51437420,23449366,96179296,13381037,45044834,88129442,90838226,99721903,49600144,87433251,97072946,57980878,53533810,16161191,65535524,16806050,1602872,55648957,3519702,10010758,61578716,89552944,38722273,20708273,14191528,2521559,53223702,94580881,30650848,93349486,714578,33483883,21327854,24032050,88906270,10208241,74874240,23569624,78564717,68869569,57368037,5429861,97257498,93993462,92692712,87718896,10364402,53440548,15984451,86421208,51940559,75156901,86092129,6037049,32103948,2798584,62603087,97031016,22373843,17877988,94962356,71764646,60221548,56050424,22497289,53080973,52222655,66490664,48317164,34823147,37512283,96765366,11229123,48388659,19154408,34226818,46889453,37464701,62781874,20002781,33920024,26374280,77758473,83003806,72881842,96114639,77525791,74345113,52521823,26284857,83940450,20546147,7720856,54410190,56002897,18448857,80115109,90286695,73329803,32375774,18713584,27167244,96490146,47897142,23931473,39975573,19300785,66051547,39160576,69026120,28029378,62203576,38962842,79536719,82568725,59538046,82994865,6987977,21461666,84448620,15101873,85017284,33004033,27900112,68145202,16316292,28477627,88698230,17979105,77624625,97316974,96329487,27050784,50741007,64697058,82353560,35924768,85689106,90136859,74406074,31288485,36734043,56531412,36504511,13117351,17394621,75096551,60925550,6019185,28767929,97995501,45130696,12620166,91015298]
    k = 22
    assert Solution().maxPerformance(n, speed, efficiency, k) == 728685483
