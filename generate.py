import os
import variables

os.system(f"polyphony_rnn_generate --run_dir={variables.RUN_DIR} --hparams=\"{variables.HPARAMS}\" --output_dir={variables.OUTPUT_DIR} --num_outputs=10 --num_steps=512 --primer_pitches=\"[64]\" --condition_on_primer=true --inject_primer_during_generation=false")
