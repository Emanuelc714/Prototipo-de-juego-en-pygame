from os import walk
import pygame

def import_folder(path):
    surface_list = []
    
    for _, __, img_files in walk(path): # walk ya fue importado, nos permite buscar folders dentro de un path, pero tenemos que darle un camino, el tercer elemento nos regresa los archivos dentro del folder encontrado. Los guiones bajos le dicen que ignore los primeros dos elementos
        for image in img_files:
            full_path = path + "/" + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    
    return surface_list