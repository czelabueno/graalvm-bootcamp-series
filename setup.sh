#!/bin/bash
source "$HOME/.sdkman/bin/sdkman-init.sh"

# Setup Oracle GraalVM using SDKMAN!
sdk install java 17.0.8-graal
sdk use java 17.0.8-graal
java -version

# Setup http performance tool
TOOL_CHAIN_DIR=/workspace/hey
echo $TOOL_CHAIN_DIR

mkdir -p $TOOL_CHAIN_DIR
cd $TOOL_CHAIN_DIR
rm -rf hey*
wget -q https://hey-release.s3.us-east-2.amazonaws.com/hey_linux_amd64
mv hey_linux_amd64 hey
chmod +x hey
export PATH=`pwd`:$PATH

cd /workspace/graalvm-bootcamp-series
hey


