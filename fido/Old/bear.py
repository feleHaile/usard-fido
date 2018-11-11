import pandas

"""
functions to read csv files
"""

def return_scenelist(filename):
    """ Returns a pruned scenelist as a pandas dataframe.

    Args:
        filename: the csv file from EarthExplorer

    Returns
        scene_list: the pruned pandas list of scenes

    """

    df = pandas.read_csv(filename, encoding='cp1252')

    df_pruned = df['Display ID']
    
    scene_list = df_pruned.tolist()

    return scene_list
