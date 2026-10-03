from typing import Dict


def generate_basic_plan(project) -> Dict:
    """
    Generate a basic space-planning structure
    from the user's building requirements.
    """

    floors = project.floors
    bedrooms = project.bedrooms or 0
    bathrooms = project.bathrooms or 0
    kitchens = project.kitchen or 0
    parking = project.car_parking or 0

    ground_floor = []
    upper_floor_spaces = []

    # -------------------------
    # Ground Floor
    # -------------------------

    if parking > 0:
        ground_floor.append({
            "space": "Car Parking",
            "quantity": parking
        })

    ground_floor.extend([
        {
            "space": "Drawing Room",
            "quantity": 1
        },
        {
            "space": "TV Lounge",
            "quantity": 1
        }
    ])

    if kitchens > 0:
        ground_floor.append({
            "space": "Kitchen",
            "quantity": kitchens
        })

    # Treat only explicit yes/true values as servant room required
    servant_required = str(project.servant_room).strip().lower() in {
        "yes",
        "true",
        "required"
    }

    if servant_required:
        ground_floor.append({
            "space": "Servant Room",
            "quantity": 1
        })

    # -------------------------
    # Bedrooms
    # -------------------------

    bedrooms_on_ground = min(bedrooms, 1)

    if bedrooms_on_ground > 0:
        ground_floor.append({
            "space": "Bedroom",
            "quantity": bedrooms_on_ground
        })

    remaining_bedrooms = bedrooms - bedrooms_on_ground

    if remaining_bedrooms > 0:
        upper_floor_spaces.append({
            "space": "Bedroom",
            "quantity": remaining_bedrooms
        })

    # -------------------------
    # Bathrooms
    # -------------------------

    bathrooms_on_ground = min(bathrooms, 1)

    if bathrooms_on_ground > 0:
        ground_floor.append({
            "space": "Bathroom",
            "quantity": bathrooms_on_ground
        })

    remaining_bathrooms = bathrooms - bathrooms_on_ground

    if remaining_bathrooms > 0:
        upper_floor_spaces.append({
            "space": "Bathroom",
            "quantity": remaining_bathrooms
        })

    # -------------------------
    # Upper Floors
    # -------------------------

    upper_floors = []

    if floors >= 2:
        upper_floors.append({
            "floor": 2,
            "spaces": upper_floor_spaces
        })

    # Additional floors remain flexible for now.
    # Later we will use actual planning rules
    # and plot dimensions to distribute spaces.

    for floor in range(3, floors + 1):
        upper_floors.append({
            "floor": floor,
            "spaces": [
                {
                    "space": "Flexible Room",
                    "quantity": 1
                }
            ]
        })

    # -------------------------
    # Final Plan
    # -------------------------

    return {
        "planning_type": "basic",
        "ground_floor": {
            "floor": 1,
            "spaces": ground_floor
        },
        "upper_floors": upper_floors,
        "special_requirements": project.special_requirements
    }
