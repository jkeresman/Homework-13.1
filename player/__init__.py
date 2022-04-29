import constants
from exceptions import NotPositiveNumberError


class Player:

    def __init__(self, first_name: str, last_name: str, height_cm: float, weight_kg: float):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        return self.weight_kg * constants.KG_TO_LBS

    def height_to_inches(self):
        return self.height_cm * constants.CM_INCHES

    def __repr__(self):
        return f"{self.__class__.__name__} -> Name: {self.first_name} {self.last_name}," \
               f" height: {self.height_cm}, weight: {self.weight_kg}"

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    @property
    def height_cm(self):
        return self.__height_cm

    @height_cm.setter
    def height_cm(self, height_cm):
        if height_cm <= 0:
            raise NotPositiveNumberError(height_cm)
        self.__height_cm = height_cm

    @property
    def weight_kg(self):
        return self.__weight_kg

    @weight_kg.setter
    def weight_kg(self, weight_kg):
        if weight_kg <= 0:
            raise NotPositiveNumberError(weight_kg)
        self.__weight_kg = weight_kg


class BasketballPlayer(Player):
    def __init__(self, player: Player, points: int, rebounds: int, assists: int):
        super().__init__(player.first_name, player.last_name, player.height_cm, player.weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

    def __repr__(self):
        return super().__repr__() + f", points: {self.points}, rebounds: {self.rebounds}, assists: {self.assists}"

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, points):
        if points < 0:
            raise NotPositiveNumberError(points)
        self.__points = points

    @property
    def rebounds(self):
        return self.__rebounds

    @rebounds.setter
    def rebounds(self, rebounds):
        if rebounds < 0:
            raise NotPositiveNumberError(rebounds)
        self.__rebounds = rebounds

    @property
    def assists(self):
        return self.__assists

    @assists.setter
    def assists(self, assists):
        if assists < 0:
            raise NotPositiveNumberError(assists)
        self.__assists = assists


class FootballPlayer(Player):

    def __init__(self, player: Player, goals: int, yellow_cards: int, red_cards: int):
        super().__init__(player.first_name, player.last_name, player.height_cm, player.weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards

    def __repr__(self):
        return super().__repr__() + f", goals: {self.goals}, yellow cards: {self.yellow_cards}," \
                                    f" red cards: {self.red_cards}"

    @property
    def goals(self):
        return self.__goals

    @goals.setter
    def goals(self, goals):
        if goals < 0:
            raise NotPositiveNumberError(goals)
        self.__goals = goals

    @property
    def yellow_cards(self):
        return self.__yellow_cards

    @yellow_cards.setter
    def yellow_cards(self, yellow_cards):
        if yellow_cards < 0:
            raise NotPositiveNumberError(yellow_cards)
        self.__yellow_cards = yellow_cards

    @property
    def red_cards(self):
        return self.__red_cards

    @red_cards.setter
    def red_cards(self, red_cards):
        if red_cards < 0:
            raise NotPositiveNumberError(red_cards)
        self.__red_cards = red_cards
