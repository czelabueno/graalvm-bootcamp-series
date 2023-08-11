TOOLCHAIN_DIR=`pwd`/x86_64-linux-musl-native
CC=${TOOLCHAIN_DIR}/bin/gcc
PATH=${TOOLCHAIN_DIR}/bin:${PATH}

rm -rf target
./mvnw clean -Pnative native:compile
# ./gradlew nativeCompile
docker build -f Dockerfile.scratch --build-arg APP_FILE=target/spring-aot-ni -t  local/spring-aot:scratch .
