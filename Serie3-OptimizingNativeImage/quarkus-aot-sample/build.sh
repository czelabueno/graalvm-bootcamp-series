rm -rf target/

./mvnw clean package -Dnative -Dquarkus.package.output-name=quarkus-aot-sample-ni
