from Elaboration import risoluzioneLabirinto
import os


def checkDirectory(nameDirectory):
    """
    Metodo che consente di svolgere un check per vedere le directory e, quindi, nel caso non ci sia una directory, viene creata
    :param nameDirectory:
    :return:
    """
    isExist = os.path.exists(nameDirectory)
    if not isExist:
        os.makedirs(nameDirectory)

checkDirectory("output")
checkDirectory("json_image")

risoluzioneLabirinto()