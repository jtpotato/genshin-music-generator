INPUT_DIR="./dataset/midi"
SEQUENCES_TFRECORD="./notesequences.tfrecord"
SEQUENCE_EXAMPLES="./sequence_examples"
CONFIG='performance_with_dynamics_compact'
SEQUENCE_EXAMPLE_TFRECORD="./sequence_examples/training_poly_tracks.tfrecord"
SEQUENCE_EVAL_TFRECORD="./sequence_examples/eval_poly_tracks.tfrecord"
HPARAMS="rnn_layer_sizes=[64,64]"
RUN_DIR="./run_dir"
OUTPUT_DIR="./output"