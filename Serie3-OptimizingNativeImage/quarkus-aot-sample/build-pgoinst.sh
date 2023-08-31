rm -rf target/

./mvnw clean package -Dnative -Dquarkus.profile=pgoinst -Dquarkus.package.output-name=quarkus-aot-sample-pgoinst