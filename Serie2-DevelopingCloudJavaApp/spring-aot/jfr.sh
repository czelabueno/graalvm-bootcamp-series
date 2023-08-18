rm -rf recording.jfr
./target/spring-aot-ni -XX:StartFlightRecording="filename=recording.jfr" -XX:FlightRecorderLogging=all=trace
