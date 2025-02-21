from typing import List, Dict

from hike import Hike


class HikeManager:
    def __init__(self, hikes: List[Hike]):
        """Initialize HikeManager with a list of hikes."""
        self.hikes = hikes
    
    def suggest_hike(self, preferences: Dict[str, str]) -> List[str]:
        """
        Suggest hikes based on user preferences.

        :param preferences: A dictionary containing user preferences such as 'difficulty', 'weather', and 'time_of_day'
        :return: A list of hike names that match the user's preferences
        """
        suggested_hikes = []
        for hike in self.hikes:
            if all(preferences[key] == getattr(hike, key) for key in preferences):
                suggested_hikes.append(hike.name)
        return suggested_hikes