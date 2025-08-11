#!/usr/bin/env python3
import sys, json, os
from datetime import datetime

DATA_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(desc):
    tasks = load_tasks()
    new = {
        "id": (max([t["id"] for t in tasks]) + 1) if tasks else 1,
        "description": desc,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(new)
    save_tasks(tasks)
    print(f"Added (ID {new['id']}): {desc}")

def list_tasks(status=None):
    tasks = load_tasks()
    filtered = [t for t in tasks if status is None or t["status"] == status]
    for t in filtered:
        print(f"{t['id']}. [{t['status']}] {t['description']} (created: {t['createdAt']})")

def update_status(task_id, new_status):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["status"] = new_status
            t["updatedAt"] = datetime.now().isoformat()
            break
    save_tasks(tasks)
    print(f"Task {task_id} marked {new_status}")

def update_desc(task_id, desc):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["description"] = desc
            t["updatedAt"] = datetime.now().isoformat()
            break
    save_tasks(tasks)
    print(f"Task {task_id} updated")

def delete_task(task_id):
    tasks = load_tasks()
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)
    print(f"Task {task_id} deleted")

def usage():
    print("Usage: task.py add/list/mark-in-progress/mark-done/update/delete ...")

def main():
    if len(sys.argv) < 2:
        usage(); return
    cmd = sys.argv[1]
    if cmd == "add" and len(sys.argv) >= 3:
        add_task(" ".join(sys.argv[2:]))
    elif cmd == "list":
        status = sys.argv[2] if len(sys.argv) > 2 else None
        list_tasks(status)
    elif cmd == "mark-in-progress":
        update_status(int(sys.argv[2]), "in-progress")
    elif cmd == "mark-done":
        update_status(int(sys.argv[2]), "done")
    elif cmd == "update":
        update_desc(int(sys.argv[2]), " ".join(sys.argv[3:]))
    elif cmd == "delete":
        delete_task(int(sys.argv[2]))
    else:
        usage()

if __name__ == "__main__":
    main()
