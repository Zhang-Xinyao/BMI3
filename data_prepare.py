import sys
import os

print("This is our program finding gRNAs")
print("You are currently in the directory:", os.getcwd())
target_dir = input("Please enter the full path to the folder where your data is placed: ")


if os.path.isdir(target_dir):
    os.chdir(target_dir)  # change to the target dictionary
    print(f"Changed directory to: {os.getcwd()}")
else:
    print("The directory you entered does not exist. Please restart the program and try again.")
    exit()


clusters={"cluster1":["HLhipCyc2","HLaseSto2","HLhipLar2"],
          "cluster2":["HLrhiAff2","HLrhiSin3"],
          "cluster3":["HLrhiSed2","HLrhiLuc4","HLrhiTri2"],
          "cluster4":["HLrhiFer5"],
          "cluster5":["HLpipKuh2","HLmyoMyo6"],
          "cluster6":["HLmolMol2"],
          "cluster7":["HLphyDis3"],
          "cluster8":["HLrouAeg4"],}

cluster_neighbors = {
    "cluster1": [],
    "cluster2": ["cluster3", "cluster4"],
    "cluster3": ["cluster2", "cluster4"],
    "cluster4": ["cluster2", "cluster3"],
    "cluster5": ["cluster6"],
    "cluster6": ["cluster5"],
    "cluster7": [],
    "cluster8": []
}

print("Here are the bat species you can choose:")
species = []
for key,val in clusters.items():
    for v in val:
        print(v)
        species.append(v)
species_name=input("Please choose a species: ")
if species_name not in species:
    sys.exit("Can't find the species. Please try again.")

def get_cluster_members(input_element):
    for cluster_name, elements in clusters.items():
        if input_element in elements:
            if len(elements) > 1:
                return [e for e in elements if e != input_element]
            else:
                neighbors = cluster_neighbors.get(cluster_name, [])
                members = []
                for neighbor in neighbors:
                    members.extend(clusters.get(neighbor, []))
                return members
    return None

similar_member = get_cluster_members(species_name)
if similar_member:
    print(f"Similar members are shown as follows: {', '.join(similar_member)}")
else:
    print("No similar members found. You can choose other species.")
    sys.exit()


target_path = os.path.join(target_dir, species_name)

genome_fasta = os.path.join(target_path, f"{species_name}.fa")
if os.path.exists(genome_fasta):
    print("Genome fasta file already exists")
else:
    print("Genome fasta file does not exist")

genome_gtf = os.path.join(target_path, f"{species_name}_annotation.sorted.gtf")
if os.path.exists(genome_gtf):
    print("Genome gtf file already exists")
else:
    print("Genome gtf file does not exist")
