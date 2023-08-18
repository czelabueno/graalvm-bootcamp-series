rm -rf target/
./mvnw clean -Pnative native:compile && ./target/spring-aot-ni -XX:+DumpHeapAndExit -XX:HeapDumpPath=target/native-image/configurations/spring-ni-sample.hprof
