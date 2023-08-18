# GraalVM Bootcamp Series

## Serie 1. Starting with GraalVM

- 📽️ [Watch the Video](https://www.youtube.com/live/63tdF5XBpag)

In this session, we'll provide an overview, ecosystem and architecture of GraalVM and its significance in the world of programming. You'll learn about the various languages and runtimes supported by GraalVM, along with its unique features like high-performance JIT and AOT compilation for native image generation.

### Clone this repo
```
git clone https://github.com/czelabueno/graalvm-bootcamp-series.git
cd ./Serie1-StartingWithGraalVM
```
### Just-In-Time (JIT)  
`graal` compiler in HotSpot JVM
- Optimized machine code.

### Ahead-Of-Time (AOT)
Native Image generation from:

 - `native-image Hello` (.class)
 - `native-image --module-path Hello.jar --module HelloModule` (java module)
 - `native-image -jar Hello.jar` (.jar)
### Build tool: Maven and Gradle
   - Use of maven profiles `mvn clean package -Pnative`
   - Use of Tracing Agent to generate config json files.
### Use of dynamic features of Java.
   - Resources
   - Reflections
### Generation of polyglot native image using `python`, `javascript` and `java` languages in the same executable. 

