INPUT_DIR="./dataset/midi"
SEQUENCES_TFRECORD="./notesequences.tfrecord"
SEQUENCE_EXAMPLES="./sequence_examples"
CONFIG='performance_with_dynamics_compact'
SEQUENCE_EXAMPLE_TFRECORD="./sequence_examples/training_performances.tfrecord"
SEQUENCE_EVAL_TFRECORD="./sequence_examples/eval_performances.tfrecord"
HPARAMS="rnn_layer_sizes=[512,512,512]"
RUN_DIR="./run_dir"
OUTPUT_DIR="./output"