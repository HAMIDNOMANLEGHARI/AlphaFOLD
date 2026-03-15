from colabfold.batch import run
import os

def predict_structure(sequence):
    output_dir = "results"

    run(
        queries=[("protein", sequence)],
        result_dir=output_dir,
        num_models=5,
        is_complex=False,
        use_templates=False
    )

    return output_dir + "/protein.pdb"
