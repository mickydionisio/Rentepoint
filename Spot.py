from SpotDataEngine import SpotDataEngine


class Spot:

    spot_engine = None

    ratings = []
    dates = []

    def __init__(self, init_data):
        self.id = init_data['_id']
        self.name = init_data['name']
        self.url = init_data['url']
        self.lat = init_data['lat']
        self.lon = init_data['lon']
        self.country = init_data['country']['iso']

    def init_engine(self):
        #TODO: Should return None if no internet or data unable to read
        self.spot_engine = SpotDataEngine(self.url)

    def initialize(self):
        self.set_dates()
        self.set_ratings()

    def set_dates(self):
        if self.spot_engine.initialized is True:
            self.dates = self.spot_engine.get_dates()

    def set_ratings(self):
        if self.spot_engine.initialized is True:
            self.ratings = self.spot_engine.get_ratings()

    # Sort this better out!
    def get_pretty_properties(self):
        pretty_prop = [self.id,
                       self.url,
                       #self.name,
                       self.country,
                       self.lat,
                       self.lon,
                       ]
        return pretty_prop

    def get_pretty_ratings(self):
        if len(self.ratings) > 0:
            return [rating for rating in self.ratings]

    def get_pretty_day_rating(self, day=0):
        pretty = self.get_pretty_properties()
        pretty.append(self.ratings[day])

    def get_pretty_all(self):
        pretty = self.get_pretty_properties()
        pretty.append(self.get_pretty_ratings())
        return pretty

    def get_pretty_all_long(self):
        pretty = []
        for day_rating in self.ratings:
            day = self.get_pretty_properties()
            day.append(day_rating)
            pretty.append(day)
        return pretty



