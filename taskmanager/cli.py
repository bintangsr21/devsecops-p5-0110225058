import argparse

from .manager import TaskManager
from .storage import JsonStorage


def build_parser():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="Tambah tugas")
    p_add.add_argument("title")
    p_add.add_argument("--priority", default="medium")

    sub.add_parser("list", help="Daftar tugas")

    p_done = sub.add_parser("done", help="Tandai selesai")
    p_done.add_argument("id", type=int)

    p_rm = sub.add_parser("remove", help="Hapus tugas")
    p_rm.add_argument("id", type=int)

    return parser


def run(argv=None):
    args = build_parser().parse_args(argv)
    manager = TaskManager(JsonStorage())

    if args.command == "add":
        t = manager.add(args.title, args.priority)
        print(f"Ditambahkan: [{t.id}] {t.title} ({t.priority})")
    elif args.command == "list":
        for t in manager.list():
            mark = "x" if t.done else " "
            print(f"[{mark}] {t.id}. {t.title} ({t.priority})")
    elif args.command == "done":
        t = manager.complete(args.id)
        print(f"Selesai: {t.title}")
    elif args.command == "remove":
        manager.remove(args.id)
        print("Tugas dihapus")