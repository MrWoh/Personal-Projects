from estate_project.models.building import Building
from estate_project.models.building import House
import pickle as pkl


def get_list():
    try:
        with open("list.pkl", 'rb') as file:
            house_list = pkl.load(file)
    except:
        house_list = []
    return house_list


def list_append(house_list):
    try:
        with open("list.pkl", 'wb') as file:
            pkl.dump(house_list, file)
    except:
        print("Failed to write")
