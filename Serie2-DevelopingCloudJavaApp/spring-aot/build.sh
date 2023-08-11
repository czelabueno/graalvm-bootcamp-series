rm -rf target
./mvnw clean -Pnative native:compile
# ./gradlew nativeCompile

docker build -f Dockerfile.slim --build-arg APP_FILE=target/spring-aot-ni -t  local/spring-aot:slim .
