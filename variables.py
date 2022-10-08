INPUT_DIR="./dataset/midi"
SEQUENCES_TFRECORD="./notesequences.tfrecord"
SEQUENCE_EXAMPLES="./sequence_examples"
CONFIG='performance_with_dynamics_compact'
SEQUENCE_EXAMPLE_TFRECORD="./sequence_examples/training_poly_tracks.tfrecord"
SEQUENCE_EVAL_TFRECORD="./sequence_examples/eval_poly_tracks.tfrecord"
HPARAMS="rnn_layer_sizes=[256,256],learning_rate=0.02"
# Use learning_rate 0.001 for finer tuning, learning_rate 0.01 for coarse tuning.
RUN_DIR="./run_dir"
OUTPUT_DIR="./output"