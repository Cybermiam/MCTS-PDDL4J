import os
import subprocess
import platform
import re
import matplotlib.pyplot as plt

# Détecte le système d'exploitation pour choisir le séparateur correct
classpath_separator = ";" if platform.system() == "Windows" else ":"

# Chemins des fichiers
pathBlocks = "./pddl/blocks/"
pathDepots = "./pddl/depots/"
pathGripper = "./pddl/gripper/"
pathLogistics = "./pddl/logistics/"

domainBlocks = pathBlocks + "domain/domain.pddl"
pathPBlocks = pathBlocks + "problems/"
domainDepots = pathDepots + "domain/domain.pddl"
pathPDepots = pathDepots + "problems/"
domainGripper = pathGripper + "domain/domain.pddl"
pathPGripper = pathGripper + "problems/"
domainLogistics = pathLogistics + "domain/domain.pddl"
pathPLogistics = pathLogistics + "problems/"
classpath = f"classes{classpath_separator}lib/pddl4j-4.0.0.jar"

with open("./results/resultBlocksASP.txt", "w") as f:

    for problem in os.listdir(pathPBlocks) :
        print(problem)
        p = subprocess.Popen(
            ["java", "-cp", classpath, "fr.uga.pddl4j.examples.asp.ASP", domainBlocks, pathPBlocks + problem, "-e", "FAST_FORWARD", "-w", "1.2", "-t", "300"],
            stdout=f,
            shell=False
        )
        try:
            p.wait(300)  # Timeout de 300 secondes
        except subprocess.TimeoutExpired:
            print("Timeout reached. Killing the process.")
            p.kill()
            with open("timeout_log.txt", "a") as log_file:
                log_file.write(f"{problem} timed out, duration = 5 minutes\n")

with open("./results/resultBlocksMCRW.txt", "w") as f:
    for problem in os.listdir(pathPBlocks) :
        # Lance la commande Java avec subprocess
        print(problem)
        p = subprocess.Popen(
            ["java", "-cp", classpath, "fr.uga.pddl4j.examples.asp.MCRW", domainBlocks, pathPBlocks + problem, "-e", "FAST_FORWARD", "-w", "1.2", "-t", "300"],
            stdout=f,
            shell=False
        )
        try:
            p.wait(300)  # Timeout de 300 secondes
        except subprocess.TimeoutExpired:
            print("Timeout reached. Killing the process.")
            p.kill()
            with open("timeout_log.txt", "a") as log_file:
                log_file.write(f"{problem} timed out, duration = 5 minutes\n")

with open("./results/resultDepotsASP.txt", "w") as f:

    for problem in os.listdir(pathPDepots) :
        print(problem)
        p = subprocess.Popen(
            ["java", "-cp", classpath, "fr.uga.pddl4j.examples.asp.ASP", domainDepots, pathPDepots + problem, "-e", "FAST_FORWARD", "-w", "1.2", "-t", "300"],
            stdout=f,
            shell=False
        )
        try:
            p.wait(300)  # Timeout de 300 secondes
        except subprocess.TimeoutExpired:
            print("Timeout reached. Killing the process.")
            p.kill()
            with open("timeout_log.txt", "a") as log_file:
                log_file.write(f"{problem} timed out, duration = 5 minutes\n")

with open("./results/resultDepotsMCRW.txt", "w") as f:
    for problem in os.listdir(pathPDepots) :
        # Lance la commande Java avec subprocess
        print(problem)
        p = subprocess.Popen(
            ["java", "-cp", classpath, "fr.uga.pddl4j.examples.asp.MCRW", domainDepots, pathPDepots + problem, "-e", "FAST_FORWARD", "-w", "1.2", "-t", "300"],
            stdout=f,
            shell=False
        )
        try:
            p.wait(300)  # Timeout de 300 secondes
        except subprocess.TimeoutExpired:
            print("Timeout reached. Killing the process.")
            p.kill()
            with open("timeout_log.txt", "a") as log_file:
                log_file.write(f"{problem} timed out, duration = 5 minutes\n")

with open("./results/resultGripperASP.txt", "w") as f:

    for problem in os.listdir(pathPGripper) :
        print(problem)
        p = subprocess.Popen(
            ["java", "-cp", classpath, "fr.uga.pddl4j.examples.asp.ASP", domainGripper, pathPGripper + problem, "-e", "FAST_FORWARD", "-w", "1.2", "-t", "300"],
            stdout=f,
            shell=False
        )
        try:
            p.wait(300)  # Timeout de 300 secondes
        except subprocess.TimeoutExpired:
            print("Timeout reached. Killing the process.")
            p.kill()
            with open("timeout_log.txt", "a") as log_file:
                log_file.write(f"{problem} timed out, duration = 5 minutes\n")

with open("./results/resultGripperMCRW.txt", "w") as f:
    for problem in os.listdir(pathPGripper) :
        # Lance la commande Java avec subprocess
        print(problem)
        p = subprocess.Popen(
            ["java", "-cp", classpath, "fr.uga.pddl4j.examples.asp.MCRW", domainGripper, pathPGripper + problem, "-e", "FAST_FORWARD", "-w", "1.2", "-t", "300"],
            stdout=f,
            shell=False
        )
        try:
            p.wait(300)  # Timeout de 300 secondes
        except subprocess.TimeoutExpired:
            print("Timeout reached. Killing the process.")
            p.kill()
            with open("timeout_log.txt", "a") as log_file:
                log_file.write(f"{problem} timed out, duration = 5 minutes\n")

with open("./results/resultLogisticsASP.txt", "w") as f:

    for problem in os.listdir(pathPLogistics) :
        print(problem)
        p = subprocess.Popen(
            ["java", "-cp", classpath, "fr.uga.pddl4j.examples.asp.ASP", domainLogistics, pathPLogistics + problem, "-e", "FAST_FORWARD", "-w", "1.2", "-t", "300"],
            stdout=f,
            shell=False
        )
        try:
            p.wait(300)  # Timeout de 300 secondes
        except subprocess.TimeoutExpired:
            print("Timeout reached. Killing the process.")
            p.kill()
            with open("timeout_log.txt", "a") as log_file:
                log_file.write(f"{problem} timed out, duration = 5 minutes\n")

with open("./results/resultLogisticsMCRW.txt", "w") as f:
    for problem in os.listdir(pathPLogistics) :
        # Lance la commande Java avec subprocess
        print(problem)
        p = subprocess.Popen(
            ["java", "-cp", classpath, "fr.uga.pddl4j.examples.asp.MCRW", domainLogistics, pathPLogistics + problem, "-e", "FAST_FORWARD", "-w", "1.2", "-t", "300"],
            stdout=f,
            shell=False
        )
        try:
            p.wait(300)  # Timeout de 300 secondes
        except subprocess.TimeoutExpired:
            print("Timeout reached. Killing the process.")
            p.kill()
            with open("timeout_log.txt", "a") as log_file:
                log_file.write(f"{problem} timed out, duration = 5 minutes\n")



def parse_file(filename):
    """Parse the file to extract problem names, execution times, and step counts."""
    problem_data = []

    with open(filename, 'r') as file:
        content = file.read()
        # Split each problem by the keyword "parsing problem file"
        problems = content.split("parsing problem file")[1:]

        for problem in problems:
            # Extract problem name
            problem_name_match = re.search(r'\"(p\d+\.pddl)\"', problem)
            if problem_name_match:
                problem_name = problem_name_match.group(1)
            else:
                continue
            
            # Extract total execution time
            lines = problem.split('\n')

            # Chercher la ligne qui contient 'total time' et extraire le temps
            for line in lines:
                if 'total time' in line:
                    # Split la ligne en parties et récupère le temps en secondes
                    parts = line.split()
                    total_time = parts[0]  # C'est l'avant-dernier élément qui contient le temps
                    print("Temps d'exécution total:", total_time)
            
            # Count the steps in the plan
            steps = re.findall(r'\d+:\s\(.+\)', problem)
            num_steps = len(steps)

            # Store the parsed data
            problem_data.append((problem_name, total_time, num_steps))
    
    return problem_data


# GRAPHES

# Blocks
file1_data = parse_file('results/resultBlocksASP.txt')
file2_data = parse_file('results/resultBlocksMCRW.txt')

file1_sorted = sorted(file1_data, key=lambda x: x[1])
file2_sorted = sorted(file2_data, key=lambda x: x[1])
file1_problems = [data[0] for data in file1_sorted]
file1_times = [data[1] for data in file1_sorted]
file2_times = [next(data[1] for data in file2_sorted if data[0] == prob) for prob in file1_problems]
plt.figure(figsize=(12, 6))
plt.plot(file1_problems, file1_times, label="ASP", marker='o')
plt.plot(file1_problems, file2_times, label="MCRW", marker='o')
plt.xticks(rotation=90)
plt.xlabel("Problèmes")
plt.ylabel("Temps d'exécution")
plt.title("Comparaison Temps d'exécution ASP vs RW (Blocks)")
plt.legend()
plt.tight_layout()
plt.show()

file1_sorted_steps = sorted(file1_data, key=lambda x: x[2])
file2_sorted_steps = sorted(file2_data, key=lambda x: x[2])
file1_steps_problems = [data[0] for data in file1_sorted_steps]
file1_steps = [data[2] for data in file1_sorted_steps]
file2_steps = [next(data[2] for data in file2_sorted_steps if data[0] == prob) for prob in file1_steps_problems]
plt.figure(figsize=(12, 6))
plt.plot(file1_steps_problems, file1_steps, label="ASP", marker='o')
plt.plot(file1_steps_problems, file2_steps, label="MCRW", marker='o')
plt.xticks(rotation=90)
plt.xlabel("Problèmes")
plt.ylabel("Nombre d'étapes")
plt.title("Comparaison Nombre d'étapes ASP vs RW(Blocks)")
plt.legend()
plt.tight_layout()
plt.show()

# Depots
file1_data = parse_file('results/resultDepotsASP.txt')
file2_data = parse_file('results/resultDepotsMCRW.txt')

file1_sorted = sorted(file1_data, key=lambda x: x[1])
file2_sorted = sorted(file2_data, key=lambda x: x[1])
file1_problems = [data[0] for data in file1_sorted]
file1_times = [data[1] for data in file1_sorted]
file2_times = [next(data[1] for data in file2_sorted if data[0] == prob) for prob in file1_problems]
plt.figure(figsize=(12, 6))
plt.plot(file1_problems, file1_times, label="ASP", marker='o')
plt.plot(file1_problems, file2_times, label="MCRW", marker='o')
plt.xticks(rotation=90)
plt.xlabel("Problèmes")
plt.ylabel("Temps d'exécution")
plt.title("Comparaison Temps d'exécution ASP vs RW (Depots)")
plt.legend()
plt.tight_layout()
plt.show()

file1_sorted_steps = sorted(file1_data, key=lambda x: x[2])
file2_sorted_steps = sorted(file2_data, key=lambda x: x[2])
file1_steps_problems = [data[0] for data in file1_sorted_steps]
file1_steps = [data[2] for data in file1_sorted_steps]
file2_steps = [next(data[2] for data in file2_sorted_steps if data[0] == prob) for prob in file1_steps_problems]
plt.figure(figsize=(12, 6))
plt.plot(file1_steps_problems, file1_steps, label="ASP", marker='o')
plt.plot(file1_steps_problems, file2_steps, label="MCRW", marker='o')
plt.xticks(rotation=90)
plt.xlabel("Problèmes")
plt.ylabel("Nombre d'étapes")
plt.title("Comparaison Nombre d'étapes ASP vs RW(Depots)")
plt.legend()
plt.tight_layout()
plt.show()

# Gripper
file1_data = parse_file('results/resultGripperASP.txt')
file2_data = parse_file('results/resultGripperMCRW.txt')

file1_sorted = sorted(file1_data, key=lambda x: x[1])
file2_sorted = sorted(file2_data, key=lambda x: x[1])
file1_problems = [data[0] for data in file1_sorted]
file1_times = [data[1] for data in file1_sorted]
file2_times = [next(data[1] for data in file2_sorted if data[0] == prob) for prob in file1_problems]
plt.figure(figsize=(12, 6))
plt.plot(file1_problems, file1_times, label="ASP", marker='o')
plt.plot(file1_problems, file2_times, label="MCRW", marker='o')
plt.xticks(rotation=90)
plt.xlabel("Problèmes")
plt.ylabel("Temps d'exécution")
plt.title("Comparaison Temps d'exécution ASP vs RW (Gripper)")
plt.legend()
plt.tight_layout()
plt.show()

file1_sorted_steps = sorted(file1_data, key=lambda x: x[2])
file2_sorted_steps = sorted(file2_data, key=lambda x: x[2])
file1_steps_problems = [data[0] for data in file1_sorted_steps]
file1_steps = [data[2] for data in file1_sorted_steps]
file2_steps = [next(data[2] for data in file2_sorted_steps if data[0] == prob) for prob in file1_steps_problems]
plt.figure(figsize=(12, 6))
plt.plot(file1_steps_problems, file1_steps, label="ASP", marker='o')
plt.plot(file1_steps_problems, file2_steps, label="MCRW", marker='o')
plt.xticks(rotation=90)
plt.xlabel("Problèmes")
plt.ylabel("Nombre d'étapes")
plt.title("Comparaison Nombre d'étapes ASP vs RW(Gripper)")
plt.legend()
plt.tight_layout()
plt.show()

# Logistics
file1_data = parse_file('results/resultLogisticsASP.txt')
file2_data = parse_file('results/resultLogisticsMCRW.txt')

file1_sorted = sorted(file1_data, key=lambda x: x[1])
file2_sorted = sorted(file2_data, key=lambda x: x[1])
file1_problems = [data[0] for data in file1_sorted]
file1_times = [data[1] for data in file1_sorted]
file2_times = [next(data[1] for data in file2_sorted if data[0] == prob) for prob in file1_problems]
plt.figure(figsize=(12, 6))
plt.plot(file1_problems, file1_times, label="ASP", marker='o')
plt.plot(file1_problems, file2_times, label="MCRW", marker='o')
plt.xticks(rotation=90)
plt.xlabel("Problèmes")
plt.ylabel("Temps d'exécution")
plt.title("Comparaison Temps d'exécution ASP vs RW (Logistics)")
plt.legend()
plt.tight_layout()
plt.show()

file1_sorted_steps = sorted(file1_data, key=lambda x: x[2])
file2_sorted_steps = sorted(file2_data, key=lambda x: x[2])
file1_steps_problems = [data[0] for data in file1_sorted_steps]
file1_steps = [data[2] for data in file1_sorted_steps]
file2_steps = [next(data[2] for data in file2_sorted_steps if data[0] == prob) for prob in file1_steps_problems]
plt.figure(figsize=(12, 6))
plt.plot(file1_steps_problems, file1_steps, label="ASP", marker='o')
plt.plot(file1_steps_problems, file2_steps, label="MCRW", marker='o')
plt.xticks(rotation=90)
plt.xlabel("Problèmes")
plt.ylabel("Nombre d'étapes")
plt.title("Comparaison Nombre d'étapes ASP vs RW(Logistics)")
plt.legend()
plt.tight_layout()
plt.show()