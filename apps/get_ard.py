from fido.bear import return_scenelist

def run_get_files():
    """ gets a list of files from ../work/x.csv

    """
    file = "../work/ARD_TILE_286919.csv"

    scene_list = return_scenelist(file)

    [ print("HI",item) for item in scene_list ]


run_get_files()
    
