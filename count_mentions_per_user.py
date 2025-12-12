"""
LeetCode
3433. Count Mentions Per User
December 2025 Challenge
jramaswami
"""


import collections
import heapq


class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        ONLINE, MESSAGE, OFFLINE = 0, 2, 1
        Event = collections.namedtuple('Event', ['timestamp', 'type', 'id'])
        events0 = []
        for evt in events:
            t = MESSAGE if evt[0] == 'MESSAGE' else OFFLINE
            events0.append(Event(int(evt[1]), t, evt[2]))
        heapq.heapify(events0)
        here = set(range(numberOfUsers))
        all_mentions = 0
        mentions = collections.Counter()
        while events0:
            evt = heapq.heappop(events0)
            if evt.type == ONLINE:
                here.add(evt.id)
            elif evt.type == MESSAGE:
                if evt.id == 'ALL':
                    all_mentions += 1
                elif evt.id == 'HERE':
                    for uid in here:
                        mentions[uid] += 1
                else:
                    for user in evt.id.split():
                        uid = int(user[2:])
                        mentions[uid] += 1
            elif evt.type == OFFLINE:
                here.remove(int(evt.id))
                evt0 = Event(evt.timestamp + 60, ONLINE, int(evt.id))
                heapq.heappush(events0, evt0)
        return [mentions[x] + all_mentions for x in range(numberOfUsers)]