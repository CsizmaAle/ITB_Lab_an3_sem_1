#include "merkle_tree.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// doar il facem sa mearga

// parcurgem fiecare nume, cream tree
// generam proof
// trimitem proof
// video :)))


int main() {
    const char *path = "students_2026.txt";
    FILE *f = fopen(path, "r");
    if (!f) {
        printf("ERROR: fisierul nu a fost gasit");
        return 1;
    }

    MerkleTree *tree = create_merkle_tree();
    char line[256];
    while (fgets(line, sizeof(line), f)) {
        line[strcspn(line, "\r\n")] = 0;
        if (line[0] == 0) continue;
        add_element(tree, line);
    }
    fclose(f);

    print_tree(tree);
    unsigned char *root=hash_to_string(get_root_hash(tree));
    printf("\nRoot: %s \n", root);

    const char *query = "\"Csizmadia Alexandra\"";
    MerkleProof *proof=generate_proof(tree, query);
    printf("Proof:\n");
    for (int i=0; i<get_proof_count(proof); i++){
        printf("%d : %s  \n" , i, hash_to_string(get_proof_sibling(proof, i)));
    }

    unsigned char hash[32];
    sha256_hash(query, strlen(query), hash);
    printf("Hash nume: %s\n", hash_to_string(hash));

    bool verificare=verify_proof(get_root_hash(tree) , query, proof);
    if(verificare == true)  
        printf("Proof is correct.\n");
    else
        printf("Proof is incorrect.\n");


    free_merkle_tree(tree);
    free_merkle_proof(proof);
    return 0;
}
