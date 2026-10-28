import unittest

from src.spell_book import SpellBook


class TestSpellBook(unittest.TestCase):
    def setUp(self):
        self.book = SpellBook("Harry")

    def test_starts_empty(self):
        self.assertEqual(self.book.get_spell_count(), 0)

    def test_adds_a_spell(self):
        self.book.add_spell("Expelliarmus")
        self.assertTrue(self.book.has_spell("Expelliarmus"))
        self.assertEqual(self.book.get_spell_count(), 1)

    def test_does_not_add_duplicates(self):
        self.book.add_spell("Lumos")
        self.book.add_spell("Lumos")
        self.assertEqual(self.book.get_spell_count(), 1)

    def test_removes_a_spell(self):
        self.book.add_spell("Alohomora")
        self.assertTrue(self.book.has_spell("Alohomora"))
        self.assertTrue(self.book.remove_spell("Alohomora"))
        self.assertFalse(self.book.has_spell("Alohomora"))
        self.assertEqual(self.book.get_spell_count(), 0)

    def test_returns_false_when_removing_nonexistent_spell(self):
        self.assertFalse(self.book.remove_spell("NonExistentSpell"))


if __name__ == "__main__":
    unittest.main()
