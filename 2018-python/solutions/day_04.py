import heapq
import itertools
import re
from collections import defaultdict
from datetime import datetime, timezone

from solutions import BaseSolution


class Solution(BaseSolution):
    input_file = '04.in'

    def __str__(self):
        return 'Day 4: Repose Record'

    def solve(self, puzzle_input):
        data = self._parse_and_group_data(puzzle_input)
        timelines = self._get_guard_timelines(data)
        sorted_timelines = sorted(timelines, key=lambda kv: sum([len(r) for r in kv[1]]), reverse=True)
        guard_id, rows = sorted_timelines[0]
        most_common_minute, _count = self._get_most_common_minute(rows)
        return guard_id * most_common_minute

    def solve_again(self, puzzle_input):
        data = self._parse_and_group_data(puzzle_input)
        timelines = self._get_guard_timelines(data)
        hiscores = [(guard_id, *self._get_most_common_minute(rows)) for guard_id, rows in timelines]
        guard_id, most_common_minute, _count = heapq.nlargest(1, hiscores, key=lambda hs: hs[2])[0]
        return guard_id * most_common_minute

    def _parse_and_group_data(self, data):
        shift_sep = re.compile(r'\[.+\] Guard #\d+ begins shift')
        sorted_data = '\n'.join(sorted(data.splitlines()))
        entry_heads = shift_sep.findall(sorted_data)
        entry_tails = shift_sep.split(sorted_data)[1:]
        return list(map(lambda s: '\n'.join(map(str.strip, s)), zip(entry_heads, entry_tails)))

    def _get_guard_timelines(self, data):
        id_pattern = re.compile(r'Guard #(\d+)')
        asleep_pattern = re.compile(r'\[(.+)\] f.*\n\[(.+)\] w', re.MULTILINE)
        time_format = '%Y-%m-%d %H:%M'
        rem = 60 * 60 * 24
        timeline = defaultdict(list)
        for entry in data:
            guard_id = int(id_pattern.search(entry).groups()[0])
            for felt_asleep, woke_up in asleep_pattern.findall(entry):
                if guard_id not in timeline:
                    timeline[guard_id] = []
                felt_asleep_dt = datetime.strptime(felt_asleep, time_format)
                felt_asleep_ts = int(felt_asleep_dt.replace(tzinfo=timezone.utc).timestamp())
                felt_asleep_ts = (felt_asleep_ts % rem) // 60
                woke_up_dt = datetime.strptime(woke_up, time_format)
                woke_up_ts = int(woke_up_dt.replace(tzinfo=timezone.utc).timestamp())
                woke_up_ts = (woke_up_ts % rem) // 60
                timeline[guard_id].append(range(felt_asleep_ts, woke_up_ts))
        return timeline.items()

    def _get_most_common_minute(self, rows):
        minutes = defaultdict(int)
        for m in itertools.chain(*rows):
            minutes[m] += 1
        return heapq.nlargest(1, minutes.items(), key=lambda kv: kv[1])[0]


if __name__ == '__main__':
    solution = Solution()
    solution.show_results()
