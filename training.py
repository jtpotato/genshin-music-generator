import os
import variables

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
os.system(f"performance_rnn_train --config={variables.CONFIG} --run_dir={variables.RUN_DIR} --hparams={variables.HPARAMS} --sequence_example_file={variables.SEQUENCE_EXAMPLE_TFRECORD} --num_training_steps=10000")