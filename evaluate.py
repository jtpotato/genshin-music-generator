import os
import variables

os.system(f"performance_rnn_train --hparams={variables.HPARAMS} --config={variables.CONFIG} --run_dir={variables.RUN_DIR} --sequence_example_file={variables.SEQUENCE_EVAL_TFRECORD} --eval")