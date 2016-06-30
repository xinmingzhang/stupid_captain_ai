from random import choice
from itertools import cycle

import pygame as pg


        
class Captain(object):
    def __init__(self, world_info, ship_info, distances):
        self.world = world_info
        self.pos = ship_info['pos']
        self.cargo = ship_info['cargo']
        self.colonists = ship_info['colonists']
        self.home = [name for name in world_info if world_info[name]['resource'] == 'Food'][0]
        self.aim_num = 0
        home_distance = sorted(distances[self.home].items(), key = lambda d: d[1], reverse = True)
        self.route = [i[0] for i in home_distance]
        self.destination = self.route[self.aim_num]
        self.food_num = 0

    def get_orders(self, world_info, ship_info, distances):
        """
        Choose cargo, passengers and destination
        for next trip. This method is called once each day
        while the ship is docked on a planet.
        
        Method should return a dict with the following key, value pairs:
        
        "destination": the name of the planet to travel to
        "cargo": a dict of what cargo should be brought on board
        "colonists": the number of colonists to deliver to the next planet
        
        Parameters
        *********
        world_info: a dict of dicts keyed by planet name
                        each planet

        ship_info: a dict of information about the transport ship

        distances: a dict of distances between each planet        
        """
        if ship_info['pos'] == world_info[self.home]['pos']:
            self.aim_num = (self.aim_num + 1) % len(self.route)
            self.destination = self.route[self.aim_num % len(self.route)]
            self.food_num = world_info[self.home]['inventory']['Food']
            orders = {
                "destination":self.destination ,
                "cargo": {'Food':self.food_num},
                "colonists": 0}
        elif ship_info['pos'] in [world_info[pos]['pos'] for pos in self.route]:
            self.aim_num = (self.aim_num + 1) % len(self.route)
            self.destination = self.route[self.aim_num % len(self.route)]
            orders = {
                "destination":self.destination ,
                "cargo": {'Food':self.food_num/len(self.route)*(len(self.route)-self.aim_num)},
                "colonists": 0}
        return orders
