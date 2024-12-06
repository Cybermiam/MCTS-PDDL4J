from matplotlib import pyplot as plt
import re
import subprocess
import os

# On définit les commandes à exécuter pour chaque solveur
commands = {
    "SAT4JPlanner": "java -cp \"classes;lib/pddl4j-4.0.0.jar;lib/org.sat4j.core.jar\" fr.uga.pddl4j.examples.asp.SATV2",
    "HSP": "java -cp \"classes;lib/pddl4j-4.0.0.jar;lib/org.sat4j.core.jar\" fr.uga.pddl4j.examples.asp.HSP"
}

# On définit les domaines et les problèmes à résoudre
domains = ["logistics", "blocks"]
problems = []

# Pour les problèmes, on selectionne 10 problèmes de chaque domaine
for domain in domains:
    for i in range(1, 11):
        problems.append((f"pddl/{domain}/domain/domain.pddl", f"pddl/{domain}/problems/p{i:02}.pddl"))

# Fonction pour vérifier la validité du plan
def check_plan_validity(full_path_file_domain: str, full_path_file_problem: str, full_path_file_plan: str) -> bool:
    print("Checking plan validity")
    command = "wsl ./VAL/bin/Validate " + full_path_file_domain + " " + full_path_file_problem + " " + full_path_file_plan

    print("Command used for validation: " + "\n")
    print(command + "\n")

    try:
        output = subprocess.run(
            command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

        if "Plan valid" in output.stdout:
            return True
        else:
            return False
    except subprocess.CalledProcessError as e:
        return False


# Fonction pour créer le fichier du plan et appeler la validation
def validate(output, domain, problem_file) -> bool:
    print("Constructing plan")
    plan = ""
    pattern = r"(\d+):\s*\(([^)]+)\)\s*\[(\d+)\]"
    matches = re.findall(pattern, output)
    plan_file = "./plan/plan.txt"

    with open(plan_file, "w") as file:
        for match in matches:
            plan += f"{match[0]}: ({match[1]}) [{match[2]}]\n"
        file.write(plan)

    return check_plan_validity(domain, problem_file, plan_file)
        

# Fonction qui execute les commandes java, max 5 minutes
def execute_command(command, timeout=30):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
        return result.stdout
    except subprocess.TimeoutExpired:
        return "TimeoutExpired"

# Fonction pour parser le résultat d'une commande
def parse_output(output):
    if output == "TimeoutExpired":
        time_spent = 5000
        steps = 0
        return time_spent, steps

    # On a ajouté dans le résultat des commandes un pattern type |time|steps| 
    patern = r"\|(\d+)\|(\d+)\|" # On récupère le temps et le nombre d'étapes
    match = re.search(patern, output)

    if match:
        time_spent = match.group(1)
        steps = int(match.group(2))
        print(f"time_spent: {time_spent}, steps: {steps}")
        if time_spent:
            time_spent = float(time_spent) / 1000  # Convert ms to seconds
        else:
            time_spent = 0.0
        return time_spent, steps

# On initialise la liste des résultats
results = []

# Boucle pour exécuter les commandes pour chaque problème
for problem in problems:
    domain, problem_file = problem
    for solver, command in commands.items():
        full_command = f"{command} {domain} {problem_file}"
        print(f"Executing: {full_command}")
        output = execute_command(full_command)
        time_spent, steps = parse_output(output)
        
        if not validate(output, domain, problem_file):
            # Si le plan est invalide, on met le temps à infini et les pas a 0 pour le calcul du score
            time_spent, steps = 5000, 0
            print("Plan is invalid")
        else:
            print("Plan is valid")
        
        results.append((solver, problem_file, time_spent, steps))


# Création du dossier xplot pour stocker les graphes si il n'existe pas
if not os.path.exists("xplot"):
    os.makedirs("xplot")


# Calcul des scores pour chaque solveur
def calculate_scores(results, domains, commands):
    scores = {solver: {domain: 0 for domain in domains} for solver in commands.keys()}
    for domain in domains:
        domain_results = [result for result in results if domain in result[1]]
        for i in range(1, 11):
            problem_results = [result for result in domain_results if f"p{i:02}" in result[1]]
            if len(problem_results) == 2:
                solver1, solver2 = problem_results
                time1, steps1 = solver1[2], solver1[3]
                time2, steps2 = solver2[2], solver2[3]
                if time1 == 5000 and time2 == 5000:
                    continue
                elif time1 == 5000:
                    scores[solver2[0]][domain] += 2
                elif time2 == 5000:
                    scores[solver1[0]][domain] += 2
                else:
                    if time1 < time2:
                        scores[solver1[0]][domain] += 1
                        scores[solver2[0]][domain] += time1 / time2
                    else:
                        scores[solver2[0]][domain] += 1
                        scores[solver1[0]][domain] += time2 / time1
                    if steps1 < steps2:
                        scores[solver1[0]][domain] += 1
                        scores[solver2[0]][domain] += steps1 / steps2
                    else:
                        scores[solver2[0]][domain] += 1
                        scores[solver1[0]][domain] += steps2 / steps1
    return scores

# Génération du fichier markdown des résultats
with open("SATResults10Problems.md", "w") as md_file:
    md_file.write("# Comparison of SAT4JPlanner and HSP\n\n")
    md_file.write("| Solver | Problem | Time Spent (s) | Steps |\n")
    md_file.write("|--------|---------|----------------|-------|\n")
    for result in results:
        md_file.write(f"| {result[0]} | {result[1]} | {result[2]:.2f} | {result[3]} |\n")

    scores = calculate_scores(results, domains, commands)

    for domain in domains:
        domain_times = {solver: sum(result[2] for result in results if result[0] == solver and domain in result[1]) for solver in commands.keys()}
        domain_steps = {solver: sum(result[3] for result in results if result[0] == solver and domain in result[1]) for solver in commands.keys()}

        plt.figure(figsize=(10, 5))
        plt.title(f"Total Time for {domain.capitalize()}")
        plt.bar(commands.keys(), [domain_times[solver] for solver in commands.keys()], color=['blue', 'orange'])
        plt.ylabel('Time (s)')
        domain_time_plot_filename = f"xplot/{domain}_total_time.png"
        plt.savefig(domain_time_plot_filename)
        plt.close()

        plt.figure(figsize=(10, 5))
        plt.title(f"Total Steps for {domain.capitalize()}")
        plt.bar(commands.keys(), [domain_steps[solver] for solver in commands.keys()], color=['blue', 'orange'])
        plt.ylabel('Steps')
        domain_steps_plot_filename = f"xplot/{domain}_total_steps.png"
        plt.savefig(domain_steps_plot_filename)
        plt.close()

        plt.figure(figsize=(10, 5))
        plt.title(f"Scores for {domain.capitalize()}")
        plt.bar(commands.keys(), [scores[solver][domain] for solver in commands.keys()], color=['blue', 'orange'])
        plt.ylabel('Score')
        domain_scores_plot_filename = f"xplot/{domain}_scores.png"
        plt.savefig(domain_scores_plot_filename)
        plt.close()

        md_file.write(f"## {domain.capitalize()} Results\n\n")
        md_file.write(f"![Scores for {domain.capitalize()}]({domain_scores_plot_filename})\n")
        md_file.write(f"![Total Time for {domain.capitalize()}]({domain_time_plot_filename})\n")
        md_file.write(f"![Total Steps for {domain.capitalize()}]({domain_steps_plot_filename})\n")

    overall_scores = {solver: sum(scores[solver][domain] for domain in domains) for solver in commands.keys()}
    overall_steps = {solver: sum(result[3] for result in results if result[0] == solver) for solver in commands.keys()}
    overall_time = {solver: sum(result[2] for result in results if result[0] == solver) for solver in commands.keys()}

    plt.figure(figsize=(10, 5))
    plt.title("Overall Total Time")
    plt.bar(commands.keys(), [overall_time[solver] for solver in commands.keys()], color=['blue', 'orange'])
    plt.ylabel('Time (s)')
    overall_time_plot_filename = "xplot/overall_total_time.png"
    plt.savefig(overall_time_plot_filename)
    plt.close()

    plt.figure(figsize=(10, 5))
    plt.title("Overall Total Steps")
    plt.bar(commands.keys(), [overall_steps[solver] for solver in commands.keys()], color=['blue', 'orange'])
    plt.ylabel('Steps')
    overall_steps_plot_filename = "xplot/overall_total_steps.png"
    plt.savefig(overall_steps_plot_filename)
    plt.close()

    plt.figure(figsize=(10, 5))
    plt.title("Overall Scores")
    plt.bar(commands.keys(), [overall_scores[solver] for solver in commands.keys()], color=['blue', 'orange'])
    plt.ylabel('Score')
    overall_scores_plot_filename = "xplot/overall_scores.png"
    plt.savefig(overall_scores_plot_filename)
    plt.close()

    md_file.write("## Overall Results\n\n")
    md_file.write(f"![Overall Total Time]({overall_time_plot_filename})\n")
    md_file.write(f"![Overall Total Steps]({overall_steps_plot_filename})\n")
    md_file.write(f"![Overall Scores]({overall_scores_plot_filename})\n")