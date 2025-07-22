from datetime import datetime

LOG_PATH = "logs/keylog.txt"

def load_logs(path):
    with open(path, "r") as f:
        lines = f.readlines()
    return [parse_line(line) for line in lines if parse_line(line)]

def parse_line(line):
    try:
        timestamp_str, key = line.strip().split(" - ", 1)
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        return {"timestamp": timestamp, "key": key}
    except ValueError:
        return None

def detect_phrases(events, keywords):
    sequence = "".join([e["key"].lower() if len(e["key"]) == 1 else " " for e in events])
    found = []
    for word in keywords:
        if word in sequence:
            found.append(word)
    return found

def detect_typing_speed(events):
    speeds = []
    for i in range(1, len(events)):
        delta = (events[i]["timestamp"] - events[i-1]["timestamp"]).total_seconds()
        if 0 < delta < 5:
            speeds.append(delta)
    avg = sum(speeds) / len(speeds) if speeds else 0
    return round(avg, 2)

if __name__ == "__main__":
    logs = load_logs(LOG_PATH)

    keywords = ["login", "password", "admin", "secret"]
    found = detect_phrases(logs, keywords)
    typing_speed = detect_typing_speed(logs)

    print("\n🔍 Keylog Analysis Summary\n" + "-"*30)
    print(f"Total keystrokes captured: {len(logs)}")
    print(f"Average typing delay (sec): {typing_speed}")
    print(f"Suspicious keywords detected: {found if found else 'None'}")
