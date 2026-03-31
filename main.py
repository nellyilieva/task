import argparse
import sys
import notes_logic


def cmd_add(args):
    note = notes_logic.add_note(args.title, args.content or "")
    print(f"Note added (id={note.id}): {note.title}")


def cmd_list(args):
    notes = notes_logic.list_notes()
    if not notes:
        print("No notes yet.")
        return
    for note in notes:
        print(f"[{note.id}] {note.title}")


def cmd_show(args):
    try:
        note = notes_logic.get_note(args.id)
        print(f"[{note.id}] {note.title}")
        print(note.content)
    except KeyError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_delete(args):
    try:
        notes_logic.delete_note(args.id)
        print(f"Note {args.id} deleted.")
    except KeyError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(prog="notes", description="Simple note manager")
    sub = parser.add_subparsers(dest="command")
    sub.required = True
 
    p_add = sub.add_parser("add", help="Add a new note")
    p_add.add_argument("title")
    p_add.add_argument("content", nargs="?", default="")
    p_add.set_defaults(func=cmd_add)
 
    p_list = sub.add_parser("list", help="List all notes")
    p_list.set_defaults(func=cmd_list)
 
    p_show = sub.add_parser("show", help="Show a note by id")
    p_show.add_argument("id", type=int)
    p_show.set_defaults(func=cmd_show)
 
    p_delete = sub.add_parser("delete", help="Delete a note by id")
    p_delete.add_argument("id", type=int)
    p_delete.set_defaults(func=cmd_delete)
 
    args = parser.parse_args()
    args.func(args)
 
 
if __name__ == "__main__":
    main()