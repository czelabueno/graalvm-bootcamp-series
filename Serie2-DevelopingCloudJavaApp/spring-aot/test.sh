#Generate AOT test sources
./mvnw clean test spring-boot:process-test-aot

#Run test in AOT mode on JVM
./mvnw -Dspring.aot.enabled=true test

#Generate Test Junit - Jupiter report
./mvnw clean -PnativeTest test
