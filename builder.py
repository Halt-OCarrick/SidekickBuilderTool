class AbilityScore:
    def __init__(self, name: str, score: int, prof_save: bool=False):
        self.name = name
        self.score = score
        self.prof_save = prof_save
        self.mod: int = self.set_modifier()

    def increase_score(self):
        self.score += 1
        self.mod = self.set_modifier()

    def set_modifier(self):
        modifier_dict = {
            1: -5,
            2: -4,
            3: -4,
            4: -3,
            5: -3,
            6: -2,
            7: -2,
            8: -1,
            9: -1,
            10: 0,
            11: 0,
            12: 1,
            13: 1,
            14: 2,
            15: 2,
            16: 3,
            17: 3,
            18: 4,
            19: 4,
            20: 5
        }
        return modifier_dict[self.score]

    def add_save_proficiency(self):
        self.prof_save = True


class Skill:
    def __init__(self, name: str, prof: bool, prof_bonus: int, score: AbilityScore):
        self.name = name
        self.proficient = prof
        self.expert = False
        self.bonus = self.set_bonus(prof_bonus, score)

    def set_bonus(self, prof_bonus, score):
        if self.proficient:
            return prof_bonus + score.mod
        if self.expert:
            return 2 * prof_bonus + score.mod
        return score.mod

    def add_proficiency(self):
        self.proficient = True

    def add_expertise(self):
        self.expert = True


class Sidekick:
    def __init__(self, name: str, class_: str, type_: str, race: str, level: int, speed: int, scores: dict):
        self.name = name
        self.class_ = class_
        self.type_ = type_
        self.race = race
        self.level = level
        self.speed = speed
        self.armor_class = self.set_armor_class()  # TODO: reference inventory somehow
        self.proficiency_bonus = self.set_proficiency_bonus()
        self.initiative = self.set_initiative()
        self.scores: dict[str, AbilityScore] = self.set_ability_scores(scores)

    @staticmethod
    def set_ability_scores(scores):
        scores_dict = {}
        for name, score in scores:
            scores_dict[name] = (AbilityScore(name, score))
        return scores_dict

    def set_armor_class(self):
        return None

    def set_proficiency_bonus(self):
        if self.level <= 4:
            return 2
        elif 5 <= self.level <= 8:
            return 3
        elif 9 <= self.level <= 12:
            return 4
        elif 13 <= self.level <= 16:
            return 5
        else:
            return 6

    def set_initiative(self):
        return self.scores['DEX'].mod
