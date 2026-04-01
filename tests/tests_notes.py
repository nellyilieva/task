import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import unittest
from unittest.mock import patch
import notes_logic


class TestAddNote(unittest.TestCase):

    def test_add_note_returns_correct_note(self):
        store = {"next_id": 1, "notes": []}

        with patch("notes_logic.load_notes", return_value=store), \
             patch("notes_logic.save_notes"):

            note = notes_logic.add_note("Meeting", "Discuss Q3")

            self.assertEqual(note.id, 1)
            self.assertEqual(note.title, "Meeting")
            self.assertEqual(note.content, "Discuss Q3")

    def test_add_note_increments_id(self):
        store = {"next_id": 5, "notes": []}

        with patch("notes_logic.load_notes", return_value=store), \
             patch("notes_logic.save_notes"):

            note = notes_logic.add_note("Second note", "")

            self.assertEqual(note.id, 5)

    def test_add_note_saves_to_store(self):
        store = {"next_id": 1, "notes": []}

        with patch("notes_logic.load_notes", return_value=store), \
             patch("notes_logic.save_notes") as mock_save:

            notes_logic.add_note("Meeting", "Discuss Q3")

            mock_save.assert_called_once()
            saved = mock_save.call_args[0][0]
            self.assertEqual(len(saved["notes"]), 1)
            self.assertEqual(saved["notes"][0]["title"], "Meeting")


class TestGetNote(unittest.TestCase):

    def test_get_existing_note(self):
        store = {
            "next_id": 2,
            "notes": [{"id": 1, "title": "Meeting", "content": "Discuss Q3"}],
        }

        with patch("notes_logic.load_notes", return_value=store):
            note = notes_logic.get_note(1)

            self.assertEqual(note.id, 1)
            self.assertEqual(note.title, "Meeting")

    def test_get_note_not_found_raises_key_error(self):
        store = {"next_id": 1, "notes": []}

        with patch("notes_logic.load_notes", return_value=store):
            with self.assertRaises(KeyError):
                notes_logic.get_note(99)


class TestDeleteNote(unittest.TestCase):

    def test_delete_existing_note(self):
        store = {
            "next_id": 2,
            "notes": [{"id": 1, "title": "Meeting", "content": "Discuss Q3"}],
        }

        with patch("notes_logic.load_notes", return_value=store), \
             patch("notes_logic.save_notes") as mock_save:

            notes_logic.delete_note(1)

            mock_save.assert_called_once()
            saved = mock_save.call_args[0][0]
            self.assertEqual(saved["notes"], [])

    def test_delete_note_not_found_raises_key_error(self):
        store = {"next_id": 1, "notes": []}

        with patch("notes_logic.load_notes", return_value=store), \
             patch("notes_logic.save_notes"):

            with self.assertRaises(KeyError):
                notes_logic.delete_note(99)


class TestListNotes(unittest.TestCase):

    def test_list_returns_all_notes(self):
        store = {
            "next_id": 3,
            "notes": [
                {"id": 1, "title": "First", "content": "AAA"},
                {"id": 2, "title": "Second", "content": "BBB"},
            ],
        }

        with patch("notes_logic.load_notes", return_value=store):
            notes = notes_logic.list_notes()

            self.assertEqual(len(notes), 2)
            self.assertEqual(notes[0].title, "First")
            self.assertEqual(notes[1].title, "Second")

    def test_list_returns_empty_when_no_notes(self):
        store = {"next_id": 1, "notes": []}

        with patch("notes_logic.load_notes", return_value=store):
            notes = notes_logic.list_notes()

            self.assertEqual(notes, [])


if __name__ == "__main__":
    unittest.main()