from .depot_map import depot_finder, _normalise


class DepotService:

    @staticmethod
    def get_depot_from_area(area: str) -> dict:

        normalised = _normalise(area)
        depot_number = depot_finder(area)

        return {
            "query": area,
            "normalised": normalised,
            "depot_number": depot_number
        }
