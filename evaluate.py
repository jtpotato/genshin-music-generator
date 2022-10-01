import os
import variables

os.system(f"polyphony_rnn_train --hparams={variables.HPARAMS} --run_dir={variables.RUN_DIR} --sequence_example_file={variables.SEQUENCE_EVAL_TFRECORD} --eval")
