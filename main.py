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
