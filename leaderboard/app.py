import collections
from datetime import datetime
import json
import os
import urllib
from flask import Flask, render_template, request

os.environ["TZ"] = "Europe/Stockholm"
app = Flask(__name__)


def get_data(token, calendar, leaderboard, dummy_data=True):
    if dummy_data:
        with open("leaderboard.json") as lb:
            data = lb.read()
    else:
        try:
            url = f"https://adventofcode.com/{calendar}/leaderboard/private/view/{leaderboard}.json"
            headers = {"Cookie": f"session={token}"}
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as response:
                data = response.read()
        except TypeError:
            data = "[]"
        except urllib.error.HTTPError:
            data = "[]"

    return json.loads(data)


@app.route("/")
def hello_world():
    calendar = request.args.get("calendar", datetime.now().year)
    leaderboard = request.args.get("board")
    token = os.environ.get("AOC_TOKEN")
    if not token:
        return "Missing AOC_TOKEN environment variable. Use the session cookie on adventofcode.com"
    if not leaderboard:
        return "Missing board get parameter."
    data = get_data(token, calendar, leaderboard, False)
    if len(data) == 0:
        return "Token expired or no access to board"
    leaderboard = sorted(
        [
            (int(member["local_score"]), int(member["stars"]), member["name"])
            for _, member in data["members"].items()
            if int(member["stars"]) > 0
        ],
        key=lambda x: x[0],
        reverse=True,
    )
    timeline = collections.defaultdict(lambda: [])
    for _id, m in data["members"].items():
        for d, stars in m["completion_day_level"].items():
            for p, tsd in stars.items():
                ts = datetime.fromtimestamp(tsd["get_star_ts"])

                timeline[d].append(
                    (datetime.strftime(ts, "%Y-%m-%dT%H:%M:%S"), d, p, m["name"])
                )
    timeline = sorted(timeline.items(), key=lambda x: int(x[0]), reverse=True)
    timeline = [
        (
            d,
            sorted(
                tl, key=lambda entry: datetime.strptime(entry[0], "%Y-%m-%dT%H:%M:%S")
            ),
        )
        for d, tl in timeline
    ]
    timeline = [
        (
            d,
            [
                te + (get_score(time_entries, te, len(data["members"])),)
                for te in time_entries
            ],
        )
        for d, time_entries in timeline
    ]
    return render_template("main.jinja2", leaderboard=leaderboard, timeline=timeline)


def get_score(time_entries, current_te, nr_competitors):
    list_for_current_star = [te for te in time_entries if te[2] == current_te[2]]
    pos = [i for i, te in enumerate(list_for_current_star) if te[3] == current_te[3]][0]
    return nr_competitors - pos
