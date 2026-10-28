class SpellBook:
    def __init__(self, owner: str):
        self.owner = owner
        self._spells: set[str] = set()

    def add_spell(self, spell: str) -> None:
        self._spells.add(spell)

    def has_spell(self, spell: str) -> bool:
        return spell in self._spells

    def get_spell_count(self) -> int:
        return len(self._spells)

    def remove_spell(self, spell: str) -> bool:
        if spell not in self._spells:
            return False

        self._spells.remove(spell)
        return True
