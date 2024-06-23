import os,sys,threading
import argparse, unittest
from checkrules.log import bcolors,msg
from checkrules.CheckRulesFunctions import (
                                            CheckUserCommand,
                                            CheckImageUpdate,
                                            CheckDownloadedPackageFiles,
                                            CheckOpenPorts,
                                            CheckAddCopyCommands,
                                            CheckChmod,
                                            CheckSecretKeys,
                                            CheckCurlWgetCommands,
                                            CheckMultipleRunCommands,
                                           )


print(f"""{bcolors.OKGREEN}

     ____             _____    ____                  ____ _               _    
    |  _ \  ___   ___|  ___|  / ___|  ___  ___      / ___| |__   ___  ___| | __
    | | | |/ _ \ / __| |_ ____\___ \ / _ \/ __|____| |   | '_ \ / _ \/ __| |/ /
    | |_| | (_) | (__|  _|_____|__) |  __/ (_|_____| |___| | | |  __/ (__|   <
    |____/ \___/ \___|_|      |____/ \___|\___|     \____|_| |_|\___|\___|_|\_\ v1.0
      
                                                                                        
    Author : OsmanKandemir

{bcolors.ENDC}""")


class DocFCheckerException(Exception):
    """
    DocFChecker exception class
    """

    def __init__(self, information):
        """
        DocFCheckerException class constructor
        :param information: string
        """
        self.information:str = information

        Exception.__init__(self, '%s' % (self.information))

class DocFCheckerClass:

    """

        Dockerfile Check Main class
        :param file_: file


    """


    def __init__(self,file) -> None:

        self.file_:list = file

    def OpenFile(self) -> None:
        try:
            with open(self.file_[0], 'r') as file:
                return file.readlines()
        except Exception as Error:
            msg(f"An File Error Occurred: {Error}")
            sys.exit()
            


    def Run(self) -> None:

        DockerFiles = self.OpenFile()

        threads = [
            threading.Thread(target=lambda: CheckUserCommand(DockerFiles,)),
            threading.Thread(target=lambda: CheckImageUpdate(DockerFiles,)),
            threading.Thread(target=lambda: CheckDownloadedPackageFiles(DockerFiles,)),
            threading.Thread(target=lambda: CheckOpenPorts(DockerFiles,)),
            threading.Thread(target=lambda: CheckAddCopyCommands(DockerFiles,)),
            threading.Thread(target=lambda: CheckChmod(DockerFiles,)),
            threading.Thread(target=lambda: CheckSecretKeys(DockerFiles,)),
            threading.Thread(target=lambda: CheckCurlWgetCommands(DockerFiles,)),
            threading.Thread(target=lambda: CheckMultipleRunCommands(DockerFiles,)),
        ]
        
        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()
    

    @property
    def file(self) -> str:
        return self.file_
    
    def __str__(self):
        return f"DocFChecker"

    def __repr__(self):
        return 'DocFCheckerClass(file_=' + str(self.file_)




def DocFChecker(file:str) -> None:
    DocFCheckerClass(file).Run()



def MAIN():

    """
        Argument Function.
    
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--DOCKERFILE", nargs='+', required="True", help="DockerFile Path. --file Dockerfile")
    args = parser.parse_args()

    proxy = set()

    file = args.DOCKERFILE if args.DOCKERFILE else None
    
    DocFChecker(file)

if __name__ == "__main__":
    """
        Start Here. 

        ⠟⠭⠃⠛⠛⠈⠁⠈⠜⠼⠚⠼⠁⠈⠎⠼⠋
    
    """
    MAIN()