rm -rf target/

./mvnw clean package -Dnative -Dquarkus.profile=pgo -Dquarkus.package.output-name=quarkus-aot-sample-pgo