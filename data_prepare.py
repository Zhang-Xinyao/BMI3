import sys
import os

print("This is our program finding gRNAs")
print("You are currently in the directory:", os.getcwd())
# /Your_path_to/bat1K
target_dir = input("Please enter the full path to the folder where your data is placed: ")


if os.path.isdir(target_dir):
    os.chdir(target_dir)  # change to the target dictionary
    print(f"Changed directory to: {os.getcwd()}")
else:
    print("The directory you entered does not exist. Please restart the program and try again.")
    exit()

# the phylogeny tree of our species are stored in the following dictionary
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

# we use HLrhiTri2 as example
print("Here are the bat species you can choose:")
species = []
for key,val in clusters.items():
    for v in val:
        print(v)
        species.append(v)
species_name=input("Please choose a species: ")
if species_name not in species:
    sys.exit("Can't find the species. Please try again.")

def get_members(input_element):
    neighbor_cluster=0
    for cluster_name, elements in clusters.items():
        if input_element in elements:
            if len(elements) > 1:
                return [e for e in elements if e != input_element], neighbor_cluster
            else:
                # if there is no other members in its own cluster, we will search its neighboring cluster
                neighbors = cluster_neighbors.get(cluster_name, [])
                members = []
                for neighbor in neighbors:
                    neighbor_cluster += 1
                    members.extend(clusters.get(neighbor, []))
                return members,neighbor_cluster
    return [], 0

similar_member, neighbors = get_members(species_name)
if similar_member:
    if neighbors > 0:
        print("There is no members in its own cluster. The members in its neighboring clusters will be listed.")
    print(f"Similar members are shown as follows: {', '.join(similar_member)}")
    # example
    # Similar members are shown as follows: HLrhiSed2, HLrhiLuc4
else:
    print("No similar members found. You can choose other species.")
    sys.exit()


target_path = os.path.join(target_dir, species_name)

# read the fasta and gtf file
genome_fasta = os.path.join(target_path, f"{species_name}.fa")
if os.path.exists(genome_fasta):
    print("Genome fasta file already exists")
else:
    sys.exit("Genome fasta file does not exist")

genome_gtf1 = os.path.join(target_path, f"{species_name}_annotation.sorted.gtf")
genome_gtf2 = os.path.join(target_path, f"{species_name}.gtf")
if os.path.exists(genome_gtf1):
    print("Genome gtf file already exists")
    genome_gtf = genome_gtf1
elif os.path.exists(genome_gtf2):
    print("Genome gtf file already exists")
    genome_gtf = genome_gtf2
else:
    sys.exit("Genome gtf file does not exist")
