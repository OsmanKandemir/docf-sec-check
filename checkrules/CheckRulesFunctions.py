#Checker Rules Functions
from .log import msg,bcolors
from .functions import IsVersionTag,SecretKeys


def CheckUserCommand(DockerFileContent:list) -> None:
    try:
        if DockerFileContent:
            for line in DockerFileContent:
                Clist = [x for x in line.split(" ") if x]
                if Clist[0] == "USER":
                    if Clist[1].strip() != "root":
                        msg(f"{bcolors.GOOD}GOOD{bcolors.ENDC} Non-root user '{Clist[1].strip()}' is specified.")
                    else:
                        msg(f"{bcolors.LOG}ALERT{bcolors.ENDC} The root user is specified. Consider using a non-root user for better security.")
                else:
                    continue
        else:
            msg(f"App Error - Dockerfile empty.")

    except Exception as Error:
        msg(f"An Error Occurred: {Error}")

def CheckImageUpdate(DockerFileContent:list) -> None:
    try:
        if DockerFileContent:
            for line in DockerFileContent:
                if line.split(" ")[0] == "FROM":
                    image_version = line.split(" ")[1].strip()
                    if not IsVersionTag(image_version):
                        msg(f"{bcolors.GOOD}GOOD{bcolors.ENDC}  The version of the Docker image named '{image_version}' has not been detected. However, there may be a possibility of failures in your application during the changes that will be made.")
                    else:
                        msg(f"{bcolors.LOG}ALERT{bcolors.ENDC} The version of the Docker image named '{image_version}' has been detected. You should check your updates. Be careful about being affected by changes.")                   
                else:
                    continue
        else:
            msg(f"App Error - Dockerfile empty.")

    except Exception as Error:
        msg(f"An Error Occurred: {Error}")


def CheckDownloadedPackageFiles(DockerFileContent:list) -> None:
    try:
        if DockerFileContent:
            for line in DockerFileContent:
                if "apt-get update" in line:
                    msg(f"""{bcolors.LOG}ALERT{bcolors.ENDC} the apt-get update command has been detected. To reduce the attack surface, you can use the following commands 
                                                RUN apt-get update && apt-get install -y
                                                package1
                                                package2
                                                && apt-get purge --auto-remove -y
                                                && apt-get clean
                                                && rm -rf /var/lib/apt/lists/*"""
                        )
                else:
                    continue
        else:
            msg(f"App Error - Dockerfile empty.")
    except Exception as Error:
        msg(f"An Error Occurred: {Error}")


def CheckOpenPorts(DockerFileContent:list) -> None:
    try:
        if DockerFileContent:
            for line in DockerFileContent:
                if "EXPOSE" in line:
                    msg(f"{bcolors.LOG}ALERT{bcolors.ENDC} EXPOSE command detected. If exposed to the outside, be careful about open ports. Ports : {line.split(' ')[1]}")
                else:
                    continue
        else:
            msg(f"App Error - Dockerfile empty.")
    except Exception as Error:
        msg(f"An Error Occurred: {Error}")

def CheckAddCopyCommands(DockerFileContent:list) -> None:
    try:
        if DockerFileContent:
            for line in DockerFileContent:
                if line.split(" ")[0] == "ADD":
                    msg(f"""{bcolors.LOG}ALERT{bcolors.ENDC} 
                            The ADD command has been detected in the Dockerfile. Both the ADD and COPY instructions provide similar functions. However, COPY is more explicit.
                            Use COPY unless you really need the ADD functionality, such as adding files from an URL or from a tar file. COPY is more predictable and less error prone.
                            In some cases, it is preferred to use the RUN instruction over ADD to download a package using curl or wget, extract it, and then remove the original file in a single step, reducing the number of layers.
                        """)
                else:
                    continue
        else:
            msg(f"App Error - Dockerfile empty.")
            
    except Exception as Error:
        msg(f"An Error Occurred: {Error}")

def CheckChmod(DockerFileContent:list) -> None:
    try:
        if DockerFileContent:
            for line in DockerFileContent:
                try:
                    if line.split(" ")[1] == "chmod":
                        msg(f"{bcolors.LOG}ALERT{bcolors.ENDC} The chmod command has been detected. Keep the permissions of the files you upload and the files you run as minimal as possible. ")
                    else:
                        continue
                except:
                    continue
        else:
            msg(f"App Error - Dockerfile empty.")
            
    except Exception as Error:
        msg(f"An Error Occurred: {Error}")


def CheckSecretKeys(DockerFileContent:list) -> None:
    try:
        if DockerFileContent:
            SecretKeys_ = SecretKeys()
            for line in DockerFileContent:
                if line.split(" ")[0] == "ENV":
                    for keys in SecretKeys_:
                        if keys in line:
                            msg(f"{bcolors.LOG}ALERT{bcolors.ENDC} Sensitive information has been detected with the ENV command. If possible, store this information in a separate file and access it with the RUN command, or consider using Docker Secrets. Command : {line}")
                        else:
                            continue
                else:
                    continue
        else:
            msg(f"App Error - Dockerfile empty.")
    except Exception as Error:
        msg(f"An Error Occurred: {Error}")

def CheckCurlWgetCommands(DockerFileContent:list) -> None:
    try:
        if DockerFileContent:
            for line in DockerFileContent:
                if line.split(" ")[0] == "RUN":
                    if "wget" and "curl" in line:
                        msg(f"{bcolors.LOG}ALERT{bcolors.ENDC} Wget and curl commands have been detected. If there are fixed links and package managers, use them instead. Using a direct URL can be risky. Command : {line}")
                    else:
                        continue
                else:
                    continue
        else:
            msg(f"App Error - Dockerfile empty.")
    except Exception as Error:
        msg(f"An Error Occurred: {Error}")

def CheckMultipleRunCommands(DockerFileContent:list) -> None:

    try:
        if DockerFileContent:
            count = 0 
            for line in DockerFileContent:
                if line.split(" ")[0] == "RUN":
                    count += 1
                else:
                    continue
            if count >= 3:
                msg(f"{bcolors.LOG}ALERT{bcolors.ENDC} More than 3 RUN commands detected. Using fewer layers can indirectly improve security. Fewer layers means less code that attackers can potentially exploit. You can combine commands with the '&&' operator.")
            else:
                msg(f"{bcolors.GOOD}GOOD{bcolors.ENDC} The number of layers is in good condition.")
        else:
            msg(f"App Error - Dockerfile empty.")
    except Exception as Error:
        msg(f"An Error Occurred: {Error}")

