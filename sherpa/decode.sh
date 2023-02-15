#!/usr/bin/env bash

time ./sherpa-ncnn \
    ./tokens.txt \
    ./encoder_jit_trace-pnnx.ncnn.int8.param \
    ./encoder_jit_trace-pnnx.ncnn.int8.bin \
    ./decoder_jit_trace-pnnx.ncnn.param \
    ./decoder_jit_trace-pnnx.ncnn.bin \
    ./joiner_jit_trace-pnnx.ncnn.int8.param \
    ./joiner_jit_trace-pnnx.ncnn.int8.bin \
    ./test_wavs/multiple_keywords.wav \
    4 \
    greedy_search