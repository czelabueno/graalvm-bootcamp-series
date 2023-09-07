# GraalVM Bootcamp Series

Welcome to the [GraalVM](https://www.graalvm.org/) Bootcamp! 🚀

![GraalVM Logo](images/img.png)

## About the Bootcamp

Are you ready to unlock the full potential of GraalVM? This is an immersive bootcamp experience where we dive deep into the world of GraalVM and explore its capabilities. This bootcamp consists of a serie of 3 talks that will equip you with the knowledge and skills to harness the power of GraalVM in your projects.

## Pre-requisites & Specs
- SDKMAN installed, here an installation [guide](https://sdkman.io/install)
- Execute this script
  ```
  $ ./setup.sh
  ```
  OR  you can download and install GraalVM directly. Use this [link](https://www.oracle.com/java/technologies/javase/graalvm-jdk17-archive-downloads.html).

## Series

### 1. Starting with GraalVM
- 📽️ [Watch the Video](https://www.youtube.com/live/63tdF5XBpag) (in spanish)

You'll learn about ecosystem and architecture of GraalVM and different languages and runtimes supported by GraalVM, along with its unique features like high-performance JIT and AOT compilation for native image generation. During the talk, we also demonstrated live examples to showcase the concepts in action of:

- Just-In-Time (JIT) -  `graal` compiler in HotSpot JVM
  - Optimized machine code in runtime.
- Ahead-Of-Time (AOT) - Native Image generation in buildtime. You can generate a native executable from:
  - `native-image Hello` (.class)
  - `native-image --module-path Hello.jar --module HelloModule` (java module)
  - `native-image -jar Hello.jar` (.jar)
- Build tool: Maven and Gradle
  - Use of maven profiles `mvn clean package -Pnative`
  - Use of Tracing Agent to generate config json files.
  - Use of `reflections` and `resources` as dynamic features of Java.
- Generation of polyglot native image using `python`, `javascript` and `java` languages in the same executable.

#### Reproduce demo following this [guideline](Serie1-StartingWithGraalVM/README.md)

### 2. Developing cloud native java applications 
- 📽️ [Watch the Video](https://www.youtube.com/live/s7iZX_7WQr4) (in spanish)

Building on the previous talks, this session will deep dive into developer experience to create native images in AOT mode using most popular java frameworks. Learn how to transform your Java applications into standalone, lightweight executables that start up in milliseconds and consume minimal resources. 

During the talk, we walked through step-by-step live demos of development, testing, debugging/diagnostic and deploy native executables containerized into [AWS ECS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html) and [Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/overview). During the talk, we also demonstrated live examples to showcase the concepts in action of:

- Native integration with most java frameworks:
  - `Springboot` (demo), `Micronaut` (demo), Quarkus, Helidon
    - Dynamic features: resource, reflection (with -agentlib)
    - Rest API Unit testing - Spring AOT & `JUnit 5`
    - Debugging GDB (Linux OS only), Diagnostic with Heap Dump, JFR snapshot with JVisualVM, use of `native-image-inspect` and Software Bill of Material (`sbom`).
- Container options for each native image executable type.
  - Dynamic libs executable - `docker` from linux `slim`
  - Mostly static executable - `docker` from `distroless`
  - Full static musl - `docker` from `scratch` or `alpine`
- CI/CD pipeline with [`Github Actions`](.github/workflows/scratchcontainer-deploy-cloud.yml)
- Deploy on cloud platform:
  - [x] Azure
  - [x] AWS
  - [ ] Oracle Cloud

#### Reproduce demo following this [guideline](Serie2-DevelopingCloudJavaApp/README.md)

### 3. Performance optimization of native image executable for high-scale environment
- 📽️ [Watch the Video](https://www.youtube.com/watch?v=2_XJcnkMg5k)

Building on the previous talks, this session will deep dive different optimization options in AOT mode. 

During the talk, we walked through a `quarkus` application and optimized it step by step to achieve maximum performance of:

- Peak throughput
  - G1GC: Use of G1 GC `--gc=G1`
  - Use of Profile Guided Optimization `--pgo`
- CPU max compatibility
  - Enable more CPU performance feature with `-march=native`
- Memory
  - HEAP: Set max heap for improved and more predictable memory ussage.
- Build time
  - Use de quick build mode for development time `-Ob`
- Executable size
  - Compression using Ultimate Packer for eXecutables `upx`
- Benchmarking of throughput and resource consumption.
  - `JIT` vs `PGO G1` vs `PGO G1 UPX`

#### Reproduce demo following this [guideline](Serie3-OptimizingNativeImage/README.md)

## Who Should Attend

Whether you're a seasoned developer or just starting your journey in programming, this bootcamp is designed for anyone interested in enhancing their understanding of GraalVM. If you're curious about boosting your application's performance, reducing resource usage, and exploring innovative programming languages, this bootcamp is for you.


---

## Share the GraalVM Bootcamp Experience!

💡 Please clone, fork, or share this repository with other developers to spread the word about GraalVM Bootcamp and train other developers in using GraalVM.

[czelabueno/graalvm-bootcamp-series](https://github.com/czelabueno/graalvm-bootcamp-series)

Thank you for being a part of the GraalVM Bootcamp journey! 🙌🚀

## Author
[`Carlos Zela`](https://sessionize.com/czelabueno)