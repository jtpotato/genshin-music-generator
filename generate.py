import os
import variables

os.system(f"performance_rnn_generate --config={variables.CONFIG} --run_dir={variables.RUN_DIR} --hparams={variables.HPARAMS} --output_dir={variables.OUTPUT_DIR} --num_outputs=10 --num_steps=6000 --primer_melody=[64]")