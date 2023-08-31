rm -rf target/

./mvnw clean package -Dnative -Dquarkus.profile=g1 -Dquarkus.package.output-name=quarkus-aot-sample-g1