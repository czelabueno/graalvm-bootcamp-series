#!/bin/bash
source "$HOME/.sdkman/bin/sdkman-init.sh"

# Setup Oracle GraalVM using SDKMAN!
echo "Installing Oracle GraalVM for JDK 17 from SDKMAN!..."
sdk install java 17.0.8-graal
sdk use java 17.0.8-graal
java -version

TOOL_CHAIN_DIR=/workspace/tool
mkdir -p $TOOL_CHAIN_DIR
echo $TOOL_CHAIN_DIR
cd $TOOL_CHAIN_DIR

# Setup http performance tool
echo "Installing hey HTTP load testing tool..."
rm -rf hey*
wget -q https://hey-release.s3.us-east-2.amazonaws.com/hey_linux_amd64
mv hey_linux_amd64 hey
chmod +x hey
export PATH=`pwd`:$PATH

# Setup UPX advances executable file compressor.
echo "Installing Ultimate Packer for eXecutables (UPX)..."
wget -q https://github.com/upx/upx/releases/download/v4.1.0/upx-4.1.0-amd64_linux.tar.xz
tar -xf upx-4.1.0-amd64_linux.tar.xz
rm upx-4.1.0-amd64_linux.tar.xz
cd upx-4.1.0-amd64_linux
export PATH=`pwd`:$PATH

cd /workspace/graalvm-bootcamp-series
hey
upx
