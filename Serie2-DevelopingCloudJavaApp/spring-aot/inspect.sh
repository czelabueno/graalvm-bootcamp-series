# Inspect to list all methods included in the native executable
# JSON schema format is defined by default here: https://www.graalvm.org/docs/reference-manual/native-image/assets/native-image-inspect-schema-v0.2.0.json
echo "Generating inspect JSON file from native executable..."
native-image-inspect target/spring-aot-ni > spring-aot-ni-inspect.json
echo "Generating Software Bill of Materials of the native executable"
echo "Don't forget build native image using arg --enable-sbom"
native-image-inspect --sbom target/spring-aot-ni > spring-ni-sample-sbom.json
tree *.json
