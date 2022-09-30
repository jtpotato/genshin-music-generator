import os
import variables

os.system(f"convert_dir_to_note_sequences --input_dir={variables.INPUT_DIR} --output_file={variables.SEQUENCES_TFRECORD} --recursive")

os.system(f"performance_rnn_create_dataset --config={variables.CONFIG} --input={variables.SEQUENCES_TFRECORD} --output_dir={variables.SEQUENCE_EXAMPLES} --eval_ratio=0.15")